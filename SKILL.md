---
name: humanize-writing
description: Use when writing or editing prose an audience will read — emails, blog posts, articles, marketing and website copy, LinkedIn or social posts, cover letters, newsletters, product descriptions, reports, essays — and when the user asks to humanize text, make it sound natural or less robotic, remove AI patterns, or clean up an AI-generated draft. Applies by default to any audience-facing writing task. Do not use for code, commit messages, config files, or legal documents where formulaic precision is required.
---

# Humanize Writing

Removes the statistical fingerprints of LLM-generated text, as catalogued by Wikipedia's WikiProject AI Cleanup ("Signs of AI writing") and confirmed by corpus studies of 15M+ PubMed abstracts (Kobak et al. 2024, arXiv:2406.07016).

The core principle: no single pattern matters much in isolation. What exposes AI text is the *density* of patterns appearing together. Write so the cluster never forms.

## Two modes

**Generation mode (default).** You are writing new prose. Apply the rules while drafting so the text comes out human the first time.

**Rewrite mode.** The user pastes existing text and asks you to clean it. Strip AI patterns while preserving everything else:

- Never alter direct quotes. Quoted third-party text stays verbatim, even if it contains banned patterns.
- Never change citations, numbers, statistics, dates, URLs, or proper nouns.
- Preserve the author's meaning, facts, and claims exactly. If removing a pattern would change what the text asserts, keep the assertion and only change the phrasing.
- Don't "improve" content they didn't ask you to change. Strip patterns; don't editorialize.

Enter rewrite mode when the user provides text to fix; otherwise stay in generation mode.

## Detect the register first

A cold email, a LinkedIn post, a blog article, and a formal report should not be humanized identically. Before applying any rule, infer the register from the user's request and context:

| Register | Contractions | Fragments | Em dashes | Example contexts |
|----------|--------------|-----------|-----------|------------------|
| Social | yes | yes | rare | LinkedIn, X/Twitter, Slack, chat |
| Email | yes | sparingly | rare | cold email, follow-ups, newsletters |
| Editorial | yes | rarely | max 1/300 words | blog posts, articles, essays |
| Formal | no | no | avoid | reports, proposals, formal docs, academic |

All other rules apply in every register. When the register is ambiguous, ask yourself who receives the text and default to the closest row.

## Workflow

1. Detect mode (generation vs rewrite) and register.
2. If a `voice-profile.md` exists in the project, or the user offers samples of their own writing, read `references/voice.md` and apply their profile instead of the generic clean voice.
3. Draft (or rewrite) with the core rules below in mind.
4. Run the self-audit checklist against the draft.
5. Fix every violation, then deliver.

Read the reference files when you need depth:

- `references/patterns.md` — the full numbered catalog (36 patterns, each with a before/after pair). Read it in rewrite mode, or whenever the self-audit flags something and you need the precise fix.
- `references/vocabulary.md` — the banned-word list with plain replacements, grouped by category. Read it when substituting words.
- `references/voice.md` — voice calibration: extracting a profile from user samples and persisting it.

## Core rules

The most damaging patterns, always in effect. Numbers refer to `references/patterns.md`.

**Structure (P1–P12).** Never write negative parallelism ("It's not X, it's Y" / "This isn't about speed. It's about trust.") — state the positive claim directly. Break the rule of three: one strong word or two, not "innovative, efficient, and scalable". No false ranges ("from startups to enterprises"). No trailing participles that editorialize ("...cementing its status as a leader") — state the fact and stop. Use plain "is/are" instead of "serves as", "stands as", "boasts". Call a thing the same name twice instead of cycling synonyms. No staccato drama fragments ("One goal. Zero excuses."). Collapse hedging stacks ("could potentially help" → "may help" or commit). Cut filler ("in order to" → "to").

**Framing (P13–P20).** No summary closers ("In conclusion", "Overall", a final paragraph restating the piece) — end on your last substantive point. Cut "It's important to note", "Notably", "Interestingly". Name your sources or cut the claim — no "experts say", "studies show", "widely regarded as". No significance inflation ("pivotal moment", "enduring legacy"). No "Despite challenges... the future looks bright" scaffolds. Don't open with a definition or a restatement of the prompt — open with the most interesting true thing.

**Conversational artifacts (P21–P26).** Strip anything a chatbot says to its user: "Great question!", "Honestly?", "I hope this helps!", "Would you like me to...", "As of my last update...", and unfilled placeholders like "[Insert name]". These must never appear inside a deliverable.

**Formatting (P27–P34).** At most one em dash per ~300 words, and only where a comma or parentheses genuinely wouldn't work. No bold mid-sentence for emphasis. No "**Term:** definition" bullets. Default to prose — bullets only when the user asks or the content is truly enumerable. No emoji in headings, ever. No headings at all under ~400 words. Sentence case for headings. Keep quotation marks consistent (don't mix curly and straight).

**Vocabulary (P35–P36).** Avoid the AI word list — delve, tapestry, intricate, pivotal, crucial, underscore, landscape (metaphorical), foster, testament, boast, meticulous, realm, showcase, leverage (verb), robust, seamless, elevate, embark, journey (metaphorical), navigate (metaphorical), unlock, harness, empower, game-changer, cutting-edge, groundbreaking, transformative, comprehensive, holistic, streamline, synergy, paradigm, myriad, plethora, vibrant, ever-evolving, "in today's fast-paced world", "at the end of the day", deep dive — unless the user's own text uses them or no plain alternative exists. Full list and replacements in `references/vocabulary.md`.

**Rhythm.** Vary sentence length deliberately; follow a long sentence with a short one. Prefer concrete specifics ("replies within two hours") over abstractions ("prompt communication"). Commit to claims at the scale they're actually true. Say each idea once — cut the echoes.

## Self-audit checklist

Before delivering any prose, scan the draft for:

1. Any "not X, but Y" / "isn't just X — it's Y" construction (P1–P2) → rewrite as a direct claim
2. Em dashes — more than 1 per 300 words (P27)? → replace with commas or parentheses
3. Any banned-vocabulary word (P35) → replace with the plain alternative
4. Triplet lists (P3) → cut to one or two, or expand honestly
5. Final paragraph (P13) → does it summarize instead of end? Replace with a specific closing point
6. Trailing "-ing" significance clauses (P5) → delete
7. "It's important to note" and cousins (P14), chatbot phrases (P21–P26) → delete
8. Bold mid-prose, "Term: definition" bullets, emoji headings (P28–P31) → strip
9. Unnamed "experts/studies" (P15) → name them or cut
10. Read three consecutive sentences aloud — same length and rhythm? → break one up

Optional mechanical check: run `scripts/ai_pattern_lint.py` on the draft; it reports pattern hits per 1000 words.

## False-positive guard

These patterns are statistical signals, not proof of anything. Apply them with judgment:

- **The user wins.** If they explicitly ask for bullets, em dashes, bold terms, or any banned element, their instruction overrides this skill. It sets defaults, not handcuffs.
- **Quotes are untouchable.** Never "fix" quoted third-party text, in either mode.
- **Precision beats style.** Never sacrifice factual accuracy, a necessary technical term, or a legally required phrase to dodge a pattern. If "comprehensive" is the accurate word, keep it.
- **Humans use these too.** An em dash or a three-item list is not a crime; the density of many patterns together is the tell. Fix the cluster, not every isolated instance.
