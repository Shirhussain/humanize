#!/usr/bin/env python3
"""Deterministic linter for AI-writing patterns.

Detects the mechanically checkable subset of the pattern catalog in
references/patterns.md and reports a density score (hits per 1000 words).

Usage:
    python3 scripts/ai_pattern_lint.py FILE [FILE ...]
    cat draft.txt | python3 scripts/ai_pattern_lint.py
    python3 scripts/ai_pattern_lint.py --json --threshold 5 draft.md

Exit code 0 if density is below the threshold, 1 otherwise (CI-friendly).
Python 3.8+, standard library only.
"""

import argparse
import json
import re
import sys
import unicodedata

EM_DASH_BUDGET_WORDS = 300  # one em dash allowed per this many words
DEFAULT_THRESHOLD = 5.0     # hits per 1000 words

# Verbs that editorialize when trailing a fact in a participle clause (P5).
# Stems only: "ing" is appended by the P5 regex ("underscor" + "ing").
SIGNIFICANCE_VERBS = (
    "highlight|underscor|cement|showcas|demonstrat|reflect|mark|solidify|"
    "reinforc|signal|signall|emphasiz|emphasis|illustrat|position|pav|usher|"
    "affirm|exemplify|bolster"
)

# High-confidence AI vocabulary (P35). A subset of references/vocabulary.md:
# ambiguous words that also appear in normal human prose (dynamic, notable,
# significant) are deliberately excluded to keep false positives low.
VOCABULARY = [
    r"delv(?:e|es|ed|ing)", r"tapestr(?:y|ies)", r"intricate(?:ly)?",
    r"pivotal", r"crucial(?:ly)?", r"underscor(?:e|es|ed|ing)",
    r"foster(?:s|ed|ing)?", r"testament", r"boast(?:s|ed|ing)?",
    r"meticulous(?:ly)?", r"realm", r"showcas(?:e|es|ed|ing)",
    r"leverag(?:e|es|ed|ing)", r"robust(?:ly|ness)?", r"seamless(?:ly)?",
    r"elevat(?:e|es|ing)", r"embark(?:s|ed|ing)?", r"harness(?:es|ed|ing)?",
    r"empower(?:s|ed|ing|ment)?", r"game[- ]chang(?:er|ing)",
    r"cutting[- ]edge", r"groundbreaking", r"transformative",
    r"holistic(?:ally)?", r"streamlin(?:e|es|ed|ing)", r"synerg(?:y|ies|istic)",
    r"paradigm", r"myriad", r"plethora", r"vibrant", r"ever[- ]evolving",
    r"state[- ]of[- ]the[- ]art", r"bespoke", r"garner(?:s|ed|ing)?",
    r"bolster(?:s|ed|ing)?", r"facilitat(?:e|es|ed|ing)",
    r"revolutioniz(?:e|es|ed|ing)", r"utiliz(?:e|es|ed|ing|ation)",
    r"comprehensive(?:ly)?", r"invaluable", r"unparalleled", r"renowned",
    r"esteemed", r"nestled", r"world[- ]class", r"deep[- ]dive",
]

PHRASES = {  # phrase -> pattern id
    "in today's fast-paced world": "P36",
    "in today's digital age": "P36",
    "at the end of the day": "P36",
    "when it comes to": "P10",
    "in order to": "P10",
    "due to the fact that": "P10",
    "last but not least": "P36",
    "first and foremost": "P36",
    "take it to the next level": "P36",
    "it's important to note": "P14",
    "it is important to note": "P14",
    "it's worth noting": "P14",
    "it is worth noting": "P14",
    "it's worth mentioning": "P14",
    "needless to say": "P14",
    "no discussion would be complete": "P14",
    "experts say": "P15",
    "experts agree": "P15",
    "studies show": "P15",
    "research shows": "P15",
    "studies have shown": "P15",
    "many believe": "P15",
    "widely regarded as": "P16",
    "industry reports": "P15",
    "great question": "P21",
    "i hope this helps": "P23",
    "hope this helps": "P23",
    "feel free to reach out": "P23",
    "happy to help": "P23",
    "would you like me to": "P24",
    "as of my last update": "P25",
    "as an ai": "P25",
    "i cannot browse": "P25",
    "serves as a": "P6",
    "stands as a": "P6",
}

REGEX_CHECKS = [
    # (pattern id, name, compiled regex)
    ("P1", "negative parallelism",
     re.compile(r"\b(?:it|this|that)(?:'s| is| was)?\s*n(?:o|')t\s+"
                r"(?:just|only|merely|simply|about)\b", re.I)),
    ("P1", "negative parallelism",
     re.compile(r"\bisn't\s+(?:just|only|merely|about)\b", re.I)),
    ("P1", "negative parallelism",
     re.compile(r"\bnot\s+(?:just|only|merely)\s+(?:a|an|the|about)\b"
                r"[^.!?\n]{0,80}\bbut\b", re.I)),
    ("P2", "correlative not-only-but-also",
     re.compile(r"\bnot\s+only\b[^.!?\n]{0,100}\bbut\s+(?:also\s+)?", re.I)),
    ("P3", "rule-of-three list",
     re.compile(r"\b[A-Za-z]+,\s+[A-Za-z]+,\s+and\s+[A-Za-z]+\b")),
    ("P5", "significance-laden trailing participle",
     re.compile(r",\s*(?:" + SIGNIFICANCE_VERBS + r")ing\s+"
                r"(?:its|his|her|their|the|a|an)\b", re.I)),
    ("P9", "hedging stack",
     re.compile(r"\b(?:could|may|might|can)\s+potentially\b"
                r"|\bpotentially\s+possibly\b"
                r"|\bcould\s+possibly\b", re.I)),
    ("P13", "summary opener",
     re.compile(r"^[ \t]*(?:in conclusion|in summary|to sum up|in essence|"
                r"overall|ultimately)\b[, ]", re.I | re.M)),
    ("P29", "bold-term bullet",
     re.compile(r"^[ \t]*(?:[-*+•]|\d+\.)[ \t]*\*\*[^*\n]+?(?::\*\*|\*\*[ \t]*[:—])",
                re.M)),
]

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002700-\U000027BF\U0001F000-\U0001F02F"
    "\U00002600-\U000026FF\U0001F900-\U0001F9FF⬀-⯿️]"
)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
WORD_RE = re.compile(r"[A-Za-z0-9']+")
CURLY_QUOTES = "“”"
STRAIGHT_QUOTE = '"'


def visible_lines(text):
    """Yield (lineno, line) pairs, skipping fenced code blocks and inline code."""
    in_fence = False
    for i, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        yield i, re.sub(r"`[^`\n]*`", " ", line)


def lint_text(text, name="<stdin>"):
    """Return (hits, word_count) for one document."""
    lines = list(visible_lines(text))
    prose = "\n".join(line for _, line in lines)
    words = len(WORD_RE.findall(prose))
    hits = []

    def add(lineno, pid, pname, excerpt):
        hits.append({
            "file": name, "line": lineno, "pattern": pid,
            "name": pname, "match": excerpt.strip()[:80],
        })

    vocab_re = re.compile(r"\b(?:" + "|".join(VOCABULARY) + r")\b", re.I)
    phrase_res = [(re.compile(re.escape(p).replace("'", "['’]"), re.I), p, pid)
                  for p, pid in PHRASES.items()]

    em_dash_lines = []
    has_curly = has_straight = None  # (lineno) of first sighting

    for lineno, line in lines:
        for m in vocab_re.finditer(line):
            add(lineno, "P35", "ai-vocabulary", m.group(0))
        for rx, phrase, pid in phrase_res:
            for m in rx.finditer(line):
                add(lineno, pid, "stock phrase", m.group(0))
        for pid, pname, rx in REGEX_CHECKS:
            if rx.flags & re.M:
                continue  # handled on full text below
            for m in rx.finditer(line):
                add(lineno, pid, pname, m.group(0))
        for _ in re.finditer("—", line):
            em_dash_lines.append(lineno)
        if HEADING_RE.match(line) and EMOJI_RE.search(line):
            add(lineno, "P31", "emoji in heading", line)
        if has_curly is None and any(q in line for q in CURLY_QUOTES):
            has_curly = lineno
        if has_straight is None and STRAIGHT_QUOTE in line:
            has_straight = lineno

    # Multiline / line-anchored checks run against the joined prose.
    offsets, pos = [], 0
    for lineno, line in lines:
        offsets.append((pos, lineno))
        pos += len(line) + 1

    def line_of(char_index):
        result = 1
        for start, lineno in offsets:
            if start <= char_index:
                result = lineno
            else:
                break
        return result

    for pid, pname, rx in REGEX_CHECKS:
        if not rx.flags & re.M:
            continue
        for m in rx.finditer(prose):
            add(line_of(m.start()), pid, pname, m.group(0))

    # P27: em dashes beyond the budget of one per EM_DASH_BUDGET_WORDS.
    allowed = max(1, words // EM_DASH_BUDGET_WORDS)
    for lineno in em_dash_lines[allowed:]:
        add(lineno, "P27", "em dash over budget",
            f"em dash #{allowed + 1}+ (allowed {allowed} per {words} words)")

    # P34: curly and straight double quotes mixed in one document.
    if has_curly is not None and has_straight is not None:
        add(max(has_curly, has_straight), "P34", "curly/straight quote mix",
            "document mixes “curly” and \"straight\" quotes")

    hits.sort(key=lambda h: (h["file"], h["line"], h["pattern"]))
    return hits, words


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="*", help="text files (default: stdin)")
    ap.add_argument("--threshold", type=float, default=DEFAULT_THRESHOLD,
                    help="max hits per 1000 words (default %(default)s)")
    ap.add_argument("--json", action="store_true", dest="as_json",
                    help="emit a JSON report")
    args = ap.parse_args(argv)

    all_hits, total_words = [], 0
    if args.files:
        for path in args.files:
            with open(path, encoding="utf-8") as fh:
                hits, words = lint_text(fh.read(), name=path)
            all_hits.extend(hits)
            total_words += words
    else:
        hits, words = lint_text(sys.stdin.read())
        all_hits.extend(hits)
        total_words += words

    density = (len(all_hits) / total_words * 1000) if total_words else 0.0
    passed = density < args.threshold

    if args.as_json:
        print(json.dumps({
            "words": total_words, "hits": all_hits,
            "hit_count": len(all_hits), "density_per_1000_words": round(density, 2),
            "threshold": args.threshold, "pass": passed,
        }, indent=2))
    else:
        for h in all_hits:
            print(f"{h['file']}:{h['line']}: {h['pattern']} {h['name']}: "
                  f"“{h['match']}”")
        verdict = "PASS" if passed else "FAIL"
        print(f"\n{total_words} words, {len(all_hits)} hits, "
              f"density {density:.1f}/1000 words "
              f"(threshold {args.threshold:g}) → {verdict}")

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
