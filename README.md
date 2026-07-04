# humanize-writing

A skill that makes AI-assisted text read like a person wrote it — while writing, not just after the fact — plus a deterministic linter that scores any text for AI-pattern density.

Most tools in this space rewrite finished text. This one works in both directions: it shapes prose *as it's generated* so the patterns never appear, and it cleans existing text when you paste some in. It knows a cold email shouldn't be humanized like a formal report, it can learn *your* voice from a few paragraphs of your writing, and it ships with a stdlib-only Python linter you can run in CI.

It is not tied to any one assistant. The skill is plain Markdown in the open [Agent Skills](https://agentskills.io) format, so it works in Claude Code, Cursor, GitHub Copilot, Codex CLI, Amp, and any other harness that reads a `SKILL.md` — and the linter is a standalone script that needs nothing but Python.

Grounded in primary sources: Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup) and corpus studies of LLM excess vocabulary across 15M+ PubMed abstracts ([arXiv:2406.07016](https://arxiv.org/abs/2406.07016), [arXiv:2502.09606](https://arxiv.org/abs/2502.09606)).

## Install

**Any agent, via the skills CLI** (installs into Claude Code, Cursor, Copilot, Codex, and others — it detects what you use):

```
npx skills add Shirhussain/humanize
```

**Manual, for any harness that reads SKILL.md** — clone it into wherever your tool looks for skills:

```
git clone https://github.com/Shirhussain/humanize.git
# e.g. ~/.claude/skills/humanize-writing, ~/.cursor/skills/humanize-writing, ...
```

**Claude Code specifically**, as a plugin:

```
/plugin marketplace add Shirhussain/humanize
/plugin install humanize-writing@humanize
```

Whatever the harness, the skill is the same three Markdown files; `AGENTS.md` at the repo root tells any agent how to load and apply it.

## Usage

**Generation mode (default).** Once installed, the skill applies automatically to audience-facing writing tasks — emails, posts, articles, marketing copy, reports. Just ask for the writing; it comes out without the patterns.

> Write a launch announcement for our new invoicing feature.

**Rewrite mode.** Paste existing text and ask for it to be cleaned. Quotes, citations, numbers, and proper nouns are preserved verbatim; only the patterns go.

> Humanize this — keep the quotes and stats exactly as they are: [pasted draft]

**Register awareness.** The skill detects whether it's writing a LinkedIn post, an email, an article, or a formal report, and adjusts what "human" means for each (contractions and fragments in social posts, neither in formal documents). You can also state the register explicitly.

## The pattern catalog

36 patterns, each documented with a full before/after pair in [references/patterns.md](references/patterns.md). The one-line versions:

| # | Pattern | Before | After |
|---|---------|--------|-------|
| P1 | Negative parallelism | This isn't just a CRM. It's a rethink of sales. | The CRM tracks every deal stage without manual entry. |
| P2 | Not only... but also | Not only faster, but also cheaper. | Faster, and it cut our server bill in half. |
| P3 | Rule of three | Fast, reliable, and secure. | It stayed up all year. 99.99% uptime. |
| P4 | False ranges | From startups to global enterprises. | Our customers include four-person agencies and two Fortune 500 retailers. |
| P5 | Significance participles | ...shipped in six weeks, underscoring its commitment. | ...shipped in six weeks. |
| P6 | Copula avoidance | The library serves as the foundation. | The library is the foundation. |
| P7 | Synonym cycling | The company... the firm... the organization... | Marlow... Marlow... it... |
| P8 | Staccato drama | One warehouse. Two weeks. Zero errors. | The two-week pilot logged zero picking errors. |
| P9 | Hedging stacks | Could potentially help reduce onboarding time. | Cut onboarding from two weeks to four days. |
| P10 | Filler phrases | In order to streamline the process of invoicing... | Invoicing was error-prone, so we automated it. |
| P11 | Uniform rhythm | Three same-shape sentences in a row. | Long sentence, then a short one. Like this. |
| P12 | Echo restatement | Wastes hours. Loses time. Eats the workday. | Costs our pilot customers 90 minutes a day. |
| P13 | Compulsive summaries | In conclusion, choosing a vendor requires balance. | If support matters more than price, pick Vendor B. |
| P14 | Editorializing filler | It's worth noting the migration needs downtime. | The migration needs about 40 minutes of downtime. |
| P15 | Vague attribution | Studies show most trials never convert. | OpenView's 2023 benchmark: 17% trial conversion. |
| P16 | Overgeneralization | Widely regarded as the industry standard. | Airbnb and Shopify both adopted it in 2023. |
| P17 | Significance inflation | A pivotal moment in the company's journey. | The launch doubled monthly signups in a quarter. |
| P18 | Promotional puffery | Nestled in Austin, our renowned studio... | We're a six-person design studio in Austin. |
| P19 | Challenges-and-outlook | Despite challenges, well-positioned for growth. | If churn stays under 3%, the unit economics work. |
| P20 | Definition openers | Email marketing is a strategy by which... | Welcome emails get four times the open rate of blasts. |
| P21 | Sycophantic openers | Great question! Choosing a database is exciting! | Postgres is the safe default here. |
| P22 | Fake-candid openers | Honestly? Most onboarding flows lose users. | Most onboarding flows lose users on screen two. |
| P23 | Chatbot closers | ...covers the results. I hope this overview helps! | ...covers the results. |
| P24 | Collaborative offers | Would you like me to expand any section? | (nothing — the piece just ends) |
| P25 | Cutoff disclaimers | As of my last update, around 200 employees. | The March filing reported 214 employees. |
| P26 | Placeholder text | At [Company], we put customers first. | At Fernway, we answer every ticket within two hours. |
| P27 | Em dash overuse | The tool — built for speed — handles imports — fast. | The tool is built for speed and handles imports quickly. |
| P28 | Bold mid-sentence | We focus on **speed** and **visibility**. | We focus on speed: every deploy is visible live. |
| P29 | Term-colon bullets | **Scalability:** grows with your team. | It scales; the SOC 2 audit passed in January. |
| P30 | List compulsion | Benefits: • saves time • fewer errors | Teams save time and make fewer errors. |
| P31 | Emoji formatting | ## 🚀 Getting Started | ## Getting started |
| P32 | Title-case headings | ## Five Ways To Improve Onboarding | ## Five ways to improve onboarding |
| P33 | Skeleton overkill | A 300-word email with four headed sections. | The same 300 words as three paragraphs. |
| P34 | Quote mixing | Both “curly” and "straight" in one document. | One style, used consistently. |
| P35 | AI vocabulary | We leverage cutting-edge, seamless technology. | We use current browser APIs; pages load in under a second. |
| P36 | Stock idioms | In today's fast-paced world, at the end of the day... | (cut — they carry no information) |

The full banned-word list with plain replacements is in [references/vocabulary.md](references/vocabulary.md).

## A complete example

**Before** — a startup "about us" draft with the patterns left in:

> In today's fast-paced world, expense management isn't just an administrative task — it's a strategic imperative. Meet Relay, the game-changing platform that leverages cutting-edge automation to deliver a seamless, transformative experience for finance teams everywhere.
>
> Relay's comprehensive dashboard boasts real-time visibility, robust policy controls, and meticulous audit trails — empowering organizations to navigate the ever-evolving landscape of corporate spend. From scrappy startups to global enterprises, teams are embarking on a journey toward financial clarity, underscoring the pivotal role of intelligent automation.
>
> It's important to note that studies show most finance teams waste countless hours on manual reconciliation. That's where Relay comes in — it's not just software, it's a partner. Ultimately, Relay represents a paradigm shift in how modern businesses manage spend. I hope this helps you understand our vision!

**After** — the same company, humanized (this exact text is extracted and linted in CI):

<!-- lint:after-example:start -->
We started Relay after our last company failed an audit over $30,000 in receipts nobody could find.

Relay is expense software for companies with 20 to 200 employees. Every card swipe creates a draft expense with the receipt attached, pulled from the card feed within about a minute. Your accountant gets a live ledger instead of a shoebox of PDFs in March.

Two decisions shaped the product. First, approval works by exception: an expense that sits under its policy limit with a receipt attached closes itself, so managers only see the 5% that need a human. Second, we write to your ledger continuously rather than at month-end. Our earliest customer, a 60-person logistics firm in Rotterdam, closed their February books in four days instead of eleven.

We don't do corporate cards, travel booking, or invoicing. Plenty of good products do. Relay does receipts and approvals and keeps your ledger in sync, and we'd rather stay narrow and be the thing your accountant stops complaining about.

Pricing is $8 per active user per month, with a 30-day trial. Setup is a QuickBooks or Xero connection and takes most teams under an hour. If it takes you longer, email us and a founder will get on a call.
<!-- lint:after-example:end -->

Same company, same claims. The first version tells you it's transformative; the second tells you what it does, what it costs, and what it refuses to do.

## The linter

`scripts/ai_pattern_lint.py` is a deterministic checker for the mechanically detectable patterns. Python 3.9+, standard library only, no installation.

```
python3 scripts/ai_pattern_lint.py draft.md          # lint a file
cat draft.txt | python3 scripts/ai_pattern_lint.py    # or stdin
python3 scripts/ai_pattern_lint.py --json draft.md    # machine-readable
python3 scripts/ai_pattern_lint.py --threshold 3 *.md # stricter gate
```

Output (run against the "before" cold email in `tests/fixtures/pairs/01-before.txt`):

```
tests/fixtures/pairs/01-before.txt:5: P1 negative parallelism: “isn't just”
tests/fixtures/pairs/01-before.txt:5: P35 ai-vocabulary: “leverage”
tests/fixtures/pairs/01-before.txt:5: P36 stock phrase: “In today's fast-paced world”
tests/fixtures/pairs/01-before.txt:7: P14 stock phrase: “It's important to note”
tests/fixtures/pairs/01-before.txt:7: P27 em dash over budget: “em dash #2+ (allowed 1 per 121 words)”
...
121 words, 19 hits, density 157.0/1000 words (threshold 5) → FAIL
```

It exits 0 when density (hits per 1000 words) is under the threshold and 1 otherwise, so it drops straight into CI. This repo runs it on its own documentation: the worked example above and every `*-after.txt` fixture must lint clean or the build fails.

What it checks: banned vocabulary, negative parallelism, "not only... but also", rule-of-three lists, trailing significance participles, hedging stacks, editorializing and vague-attribution phrases, summary openers, chatbot closers, em-dash frequency, `**Term:**` bullets, emoji in headings, and curly/straight quote mixing. Markdown code blocks are skipped.

What it can't check: false ranges, synonym cycling, echo restatement, register mismatches — the judgment calls. The skill handles those; the linter is the smoke detector, not the fire department.

## Voice calibration

Cleaned text is neutral text, and neutral is nobody's voice. Give the skill 2–3 paragraphs of your real writing and it extracts a profile — sentence-length mix, punctuation habits, favorite transitions, formality — and writes with that instead:

> Here are two emails I sent last week. Match my voice from now on: [samples]

The profile is saved to `voice-profile.md` in your project, so it persists across sessions; any future session that finds the file applies it automatically. Details in [references/voice.md](references/voice.md).

## False positives

These patterns are statistical signals, not proof. Humans write em dashes and three-item lists too — the tell is density, not existence. The skill never edits quoted third-party text, never trades factual precision for style, and if you explicitly ask for bullets or em dashes, you win. The same caution applies to the linter: a score above threshold means "look closer," not "written by AI."

## References

- Wikipedia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — the WikiProject AI Cleanup catalog this skill's patterns are drawn from.
- Kobak, D., González-Márquez, R., Horvát, E.-Á., & Lause, J. (2024). [Delving into LLM-assisted writing in biomedical publications through excess vocabulary](https://arxiv.org/abs/2406.07016). The 15M-abstract corpus study behind the vocabulary list.
- [The rise and fall of LLM fingerprints](https://arxiv.org/abs/2502.09606) (arXiv:2502.09606) — follow-up work showing vocabulary fingerprints shift between model generations, which is why the word list is versioned.

## Changelog

**v2.0.0** (2026-07)
- Rewrite mode with hard preservation rules for quotes, citations, numbers, and proper nouns
- Register detection (social / email / editorial / formal)
- Pattern catalog restructured into `references/` with 36 numbered patterns, each with an original before/after pair
- Voice calibration with a persistent `voice-profile.md`
- `scripts/ai_pattern_lint.py`: deterministic linter with density scoring, JSON output, and CI exit codes
- Test suite and GitHub Actions workflow; the README's own examples are linted in CI
- Claude Code plugin + marketplace manifests; `npx skills add` compatibility

**v1** (unreleased)
- Single-file SKILL.md: generation-time rules, banned vocabulary, formatting rules, 10-point self-audit

## License

MIT
