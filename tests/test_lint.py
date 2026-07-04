"""Tests for scripts/ai_pattern_lint.py and the repo's own examples."""

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures"
sys.path.insert(0, str(ROOT / "scripts"))

import ai_pattern_lint as lint  # noqa: E402


def density(text):
    hits, words = lint.lint_text(text)
    return len(hits) / words * 1000 if words else 0.0


def read(path):
    return path.read_text(encoding="utf-8")


# --- fixture-level behavior ------------------------------------------------

@pytest.mark.parametrize("name", ["ai_dense.txt", "ai_subtle.txt"])
def test_ai_text_is_flagged(name):
    assert density(read(FIXTURES / name)) >= lint.DEFAULT_THRESHOLD


@pytest.mark.parametrize("name", ["human_plain.txt", "human_formal.txt"])
def test_human_text_passes(name):
    assert density(read(FIXTURES / name)) < lint.DEFAULT_THRESHOLD


@pytest.mark.parametrize("n", ["01", "02", "03", "04"])
def test_before_fixtures_are_flagged(n):
    assert density(read(FIXTURES / "pairs" / f"{n}-before.txt")) >= lint.DEFAULT_THRESHOLD


@pytest.mark.parametrize("n", ["01", "02", "03", "04"])
def test_after_fixtures_lint_completely_clean(n):
    hits, _ = lint.lint_text(read(FIXTURES / "pairs" / f"{n}-after.txt"))
    assert hits == [], f"after-fixture {n} should have zero hits, got: {hits}"


# --- exit codes and JSON ----------------------------------------------------

def test_exit_code_fail_on_ai_text():
    assert lint.main([str(FIXTURES / "ai_dense.txt")]) == 1


def test_exit_code_pass_on_human_text():
    assert lint.main([str(FIXTURES / "human_plain.txt")]) == 0


def test_json_output_shape(capsys):
    lint.main(["--json", str(FIXTURES / "ai_dense.txt")])
    report = json.loads(capsys.readouterr().out)
    assert report["words"] > 0
    assert report["hit_count"] == len(report["hits"]) > 0
    assert report["pass"] is False
    first = report["hits"][0]
    assert {"file", "line", "pattern", "name", "match"} <= set(first)


# --- individual checks ------------------------------------------------------

def hit_patterns(text):
    hits, _ = lint.lint_text(text)
    return [h["pattern"] for h in hits]


def test_negative_parallelism():
    assert "P1" in hit_patterns("This isn't just a product. It's a movement.")


def test_not_only_but_also():
    assert "P2" in hit_patterns("The tool not only saves time but also cuts costs.")


def test_triplet_list():
    assert "P3" in hit_patterns("The platform is fast, simple, and secure.")


def test_trailing_significance_participle():
    text = "Revenue doubled in March, underscoring the team's momentum."
    assert "P5" in hit_patterns(text)


def test_hedging_stack():
    assert "P9" in hit_patterns("This could potentially improve results.")


def test_summary_opener_line_number():
    hits, _ = lint.lint_text("A first line.\n\nIn conclusion, that was it.")
    p13 = [h for h in hits if h["pattern"] == "P13"]
    assert p13 and p13[0]["line"] == 3


def test_em_dash_budget():
    text = "One — two — three — dashes in a short sentence."
    patterns = hit_patterns(text)
    assert patterns.count("P27") == 2  # 3 dashes, 1 allowed


def test_bold_term_bullet():
    assert "P29" in hit_patterns("- **Speed:** loads instantly")
    assert "P29" in hit_patterns("- **Speed**: loads instantly")


def test_emoji_heading():
    assert "P31" in hit_patterns("## 🚀 Launch plan")
    assert "P31" not in hit_patterns("## Launch plan")


def test_quote_mix():
    mixed = 'She said “yes” and he said "no".'
    consistent = "She said “yes” and he said “no”."
    assert "P34" in hit_patterns(mixed)
    assert "P34" not in hit_patterns(consistent)


def test_vocabulary_hit():
    assert "P35" in hit_patterns("We will delve into the tapestry of options.")


def test_code_blocks_are_ignored():
    text = "Plain sentence.\n```\ndelve leverage seamless — — — —\n```\nAnother plain sentence."
    hits, _ = lint.lint_text(text)
    assert hits == []


# --- docs consistency ---------------------------------------------------------

def test_linter_vocabulary_appears_in_vocabulary_reference():
    """Every stem the linter bans must be documented in references/vocabulary.md."""
    vocab_doc = read(ROOT / "references" / "vocabulary.md").lower()
    spot_checks = ["delve", "tapestry", "pivotal", "leverage", "seamless",
                   "synergy", "myriad", "plethora", "nestled", "renowned"]
    for word in spot_checks:
        assert word in vocab_doc, f"{word} missing from vocabulary.md"


def test_skill_frontmatter_limits():
    skill = read(ROOT / "SKILL.md")
    match = re.match(r"---\n(.*?)\n---\n", skill, re.S)
    assert match, "SKILL.md must start with YAML frontmatter"
    front = match.group(1)
    desc = re.search(r"^description:\s*(.+)$", front, re.M).group(1)
    assert len(desc) <= 1024, "frontmatter description exceeds 1024 characters"
    assert ": " not in desc, "unquoted colon-space inside description breaks YAML"
    body_lines = skill[match.end():].count("\n") + front.count("\n") + 3
    assert body_lines < 200, f"SKILL.md is {body_lines} lines; must stay under 200"


def test_readme_worked_example_lints_clean():
    """The credibility test: the README's humanized example must pass its own linter."""
    readme = read(ROOT / "README.md")
    block = re.search(
        r"<!-- lint:after-example:start -->\n(.*?)<!-- lint:after-example:end -->",
        readme, re.S)
    assert block, "README.md must mark its worked after-example with lint markers"
    hits, words = lint.lint_text(block.group(1))
    assert words > 150, "worked example should be roughly 200 words"
    assert hits == [], f"README worked example must lint clean, got: {hits}"
