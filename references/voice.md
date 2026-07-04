# Voice calibration

Stripping AI patterns produces clean, neutral prose. That's the floor, not the goal — clean-neutral is still nobody's voice. If the user gives you samples of their real writing, extract a profile and write in *their* voice instead.

## When to calibrate

- The user offers 2–3 paragraphs of their own writing (emails they've sent, posts they've published).
- A `voice-profile.md` file exists in the project — read it and apply it. Check for it before defaulting to the generic clean voice.
- The user says output "doesn't sound like me".

Two or three paragraphs (150+ words) is enough. One sentence is not; ask for more or skip calibration.

## What to extract

Read the samples and fill in each dimension with observed evidence, not guesses:

1. **Sentence length distribution.** Count roughly: what share of sentences are short (under 10 words), medium (10–25), long (25+)? Does the writer ever use fragments?
2. **Punctuation habits.** Do they use em dashes, semicolons, parentheses, ellipses? How often? (Someone who never uses semicolons should not get semicolons.)
3. **Favorite transitions.** How do they connect ideas — "But", "So", "And yet", "Anyway", numbered points, or no connectives at all?
4. **Formality and contractions.** Do they write "don't" or "do not"? Slang? Profanity? How do they open and sign off?
5. **Characteristic quirks.** Anything recurring: starting sentences with "Look,", one-sentence paragraphs, rhetorical questions, specific pet words, lowercase styling.

## The profile file

Save the result as `voice-profile.md` in the user's project so it persists across sessions. Tell the user you've saved it and that future sessions will pick it up automatically. Template:

```markdown
# Voice profile: <name>

Extracted from <n> samples (<context: e.g. two sales emails, one blog post>) on <date>.

- Sentence mix: ~40% short, ~50% medium, ~10% long; occasional fragments for emphasis
- Punctuation: frequent parentheses, no semicolons, one em dash per ~500 words
- Transitions: starts sentences with "But" and "So"; rarely uses "however"
- Formality: always contractions; first names; signs emails "— S"
- Quirks: one-sentence paragraphs to land a point; asks a rhetorical question
  about once per piece; pet word "shipped"

## Sample sentences (verbatim, for rhythm reference)
> <one or two representative sentences copied from their samples>
```

## Applying a profile

- The profile controls *rhythm and register*. The pattern rules in SKILL.md still apply — a voice profile is never a license to write "delve" or "It's not X, it's Y", unless the user's own samples genuinely contain that habit, in which case their voice wins.
- Match their sentence-length mix, not your default. If they write short, write short.
- Use their transitions and their sign-offs verbatim where appropriate.
- When the profile and the requested register conflict (their samples are casual emails but they ask for a formal report), keep their structural habits (sentence mix, directness) and drop the casual markers.

## Updating

If the user corrects your output ("I'd never say that"), update `voice-profile.md` with the correction. The profile is theirs; edit it in place rather than accumulating contradictory notes.
