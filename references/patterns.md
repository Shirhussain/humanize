# Pattern catalog

The 36 AI-writing patterns this skill removes, numbered for reference. Each entry: what it is, why it reads as machine output, and one before/after pair. Sources: Wikipedia's "Signs of AI writing" (WikiProject AI Cleanup) and corpus studies of LLM excess vocabulary (arXiv:2406.07016, arXiv:2502.09606).

Density is what matters. One pattern in a page of text is noise; five in a paragraph is a signature.

## A. Sentence structure

### P1. Negative parallelism

"It's not X, it's Y" and its two-sentence cousin. The single most recognizable AI tell. State the positive claim and let it stand.

- Before: *This isn't just another CRM. It's a complete rethink of how sales teams work.*
- After: *The CRM tracks every deal stage without manual data entry.*

### P2. Correlative "not only... but also"

Same reflex in formal dress. Almost always deletable without losing meaning.

- Before: *The update not only improves load times but also reduces server costs.*
- After: *The update cuts load times by half and trims server costs.*

### P3. Rule of three

Triplet adjectives, triplet benefits, triplet examples, everywhere. Use one strong word or two; if a list honestly has four items, keep four. Break the rhythm.

- Before: *Our platform is fast, reliable, and secure.*
- After: *Our platform stays up. Last year: 99.99% uptime, zero breaches.*

### P4. False ranges

"From X to Y" implying a spectrum that doesn't exist. Name the actual things or cut the phrase.

- Before: *We serve everyone from scrappy startups to global enterprises.*
- After: *Our customers include four-person agencies and two Fortune 500 retailers.*

### P5. Significance-laden trailing participles

A sentence ends, then a participle clause editorializes about its impact. State the fact and stop; readers can judge significance.

- Before: *The team shipped the feature in six weeks, underscoring its commitment to rapid iteration.*
- After: *The team shipped the feature in six weeks.*

### P6. Copula avoidance

"Serves as", "stands as", "boasts", "features", "represents", "marks" — anything to dodge plain "is/has". The plain verb is almost always better.

- Before: *The library serves as the foundation of the rendering pipeline and boasts extensive documentation.*
- After: *The library is the foundation of the rendering pipeline and has thorough documentation.*

### P7. Synonym cycling

Rotating through "the company / the firm / the organization / the business" to avoid repeating a word. Humans repeat names; forced elegant variation reads as machine output.

- Before: *Marlow raised a seed round in March. The startup hired five engineers in April. The young company expects to ship in Q3. The firm targets logistics teams.*
- After: *Marlow raised a seed round in March and hired five engineers in April. Marlow expects to ship in Q3, targeting logistics teams.*

### P8. Staccato manufactured-drama fragments

Chains of punchy fragments engineered for gravitas. One deliberate fragment lands; three in a row is a formula.

- Before: *One warehouse. Two weeks. Zero errors. That's the promise.*
- After: *We ran the pilot in one warehouse for two weeks and logged zero picking errors.*

### P9. Hedging stacks

Two or more hedges guarding one claim. Pick a confidence level and commit.

- Before: *This approach could potentially help reduce onboarding time in some cases.*
- After: *In our last three rollouts, this cut onboarding from two weeks to four days.*

### P10. Filler phrases

"In order to", "due to the fact that", "the process of", "it should be noted that", "when it comes to". Each has a one-word equivalent or none.

- Before: *In order to streamline the process of invoicing, we automated it due to the fact that it was error-prone.*
- After: *Invoicing was error-prone, so we automated it.*

### P11. Uniform sentence rhythm

Three or more consecutive sentences of the same length and shape. Human prose varies; follow a long sentence with a short one.

- Before: *The app syncs your files across devices. The dashboard shows your usage in real time. The API lets you build custom integrations.*
- After: *The app syncs your files across devices and shows usage on a real-time dashboard. Need something custom? There's an API.*

### P12. Echo restatement

The same point re-said in slightly different words within a paragraph. Say it once.

- Before: *Manual data entry wastes hours. Teams lose significant time keying in records by hand. This repetitive typing eats into the workday.*
- After: *Manual data entry wastes hours — our pilot customers averaged 90 minutes a day keying in records.*

## B. Framing and claims

### P13. Compulsive summaries

"In conclusion", "Overall", "In summary", "Ultimately", or a final paragraph that restates the piece. End on your last substantive point — a specific detail or a direct statement.

- Before: *In conclusion, choosing the right vendor requires balancing cost, features, and support, as discussed above.*
- After: *If support response time matters more to you than price, Vendor B is the safer pick.*

### P14. Editorializing filler

"It's important to note that", "It's worth mentioning", "Notably", "Interestingly", "No discussion would be complete without". If the thing is important, saying it is enough.

- Before: *It's worth noting that the migration requires downtime.*
- After: *The migration requires about 40 minutes of downtime.*

### P15. Vague attribution

"Experts say", "studies show", "many believe", "industry reports suggest" with no named source. Name the expert, study, or outlet — or cut the claim.

- Before: *Studies show that most SaaS trials never convert.*
- After: *OpenView's 2023 benchmark put average free-trial conversion at 17%.*

### P16. Overgeneralization

One or two sources presented as consensus; "widely regarded as", "commonly considered". Claim exactly what your sources support.

- Before: *The framework is widely regarded as the industry standard for data pipelines.*
- After: *Airbnb and Shopify both moved their pipelines to the framework in 2023.*

### P17. Undue significance and legacy framing

"Pivotal moment", "enduring legacy", "broader trends", "cementing its place in history" — importance asserted rather than shown.

- Before: *The product launch marked a pivotal moment in the company's journey and reflected broader trends in remote work.*
- After: *The launch doubled monthly signups within a quarter.*

### P18. Promotional puffery

"Vibrant", "nestled", "renowned", "rich heritage", "state-of-the-art" — brochure language. Describe what the thing does, not how impressive it is.

- Before: *Nestled in the heart of Austin, our renowned studio delivers state-of-the-art design solutions.*
- After: *We're a six-person design studio in Austin. Recent clients: two YC startups and the city's transit authority.*

### P19. Formulaic challenges-and-outlook sections

"Despite these challenges, X continues to..." followed by a speculative bright future. An essay-outline reflex; real analysis names specific obstacles and specific plans.

- Before: *Despite these challenges, the company remains well-positioned for growth as the market continues to evolve.*
- After: *The open question is churn: if the team can hold monthly churn under 3%, the unit economics work.*

### P20. Definition and restatement openers

Opening by defining the topic or restating the prompt: "X is a process by which...", "When it comes to X...". Open with the most interesting true thing instead.

- Before: *Email marketing is a powerful strategy by which businesses reach customers directly in their inboxes.*
- After: *The average welcome email gets four times the open rate of a campaign blast.*

## C. Conversational artifacts

Chatbot-to-user language that leaks into deliverables. All of these must be stripped from any text meant to stand alone.

### P21. Sycophantic openers

- Before: *Great question! Choosing a database is one of the most exciting decisions you'll make.*
- After: *Postgres is the safe default here; the case for anything else has to be argued.*

### P22. Fake-candid openers

"Honestly?", "Let's be real:", "Here's the thing:" — manufactured intimacy before an ordinary claim.

- Before: *Honestly? Most onboarding flows lose users on the second screen.*
- After: *Most onboarding flows lose users on the second screen.*

### P23. Chatbot closers

"I hope this helps!", "Feel free to reach out!", "Happy writing!" — assistant sign-offs inside a document.

- Before: *...and that covers the quarterly results. I hope this overview helps!*
- After: *...and that covers the quarterly results.*

### P24. Collaborative offers

"Would you like me to also draft the follow-up email?" left inside the deliverable text.

- Before: *[end of blog post] Would you like me to expand any section or adjust the tone?*
- After: *[end of blog post — nothing after the final substantive sentence]*

### P25. Knowledge-cutoff disclaimers

"As of my last update...", "As of [year], available information suggests..." — training-data language.

- Before: *As of my last update, the company had around 200 employees.*
- After: *The company reported 214 employees in its March filing.*

### P26. Placeholder text

"[Insert company name]", "[Your product here]", unfilled template slots shipped as finished text.

- Before: *At [Company], we believe in putting customers first.*
- After: *At Fernway, we answer every support ticket within two hours.*

## D. Formatting

### P27. Em dash overuse

Humans use em dashes; AI overuses them and puts them where commas, parentheses, or colons belong. Hard limit: one per ~300 words, and only where a comma genuinely wouldn't work.

- Before: *The tool — built for speed — handles imports — even large ones — without blocking.*
- After: *The tool is built for speed and handles imports, even large ones, without blocking.*

### P28. Bold mid-sentence emphasis

Bolding key terms mid-prose as decoration. Bold is for structure the reader navigates by, not emphasis.

- Before: *Our approach focuses on **speed**, giving teams **real-time visibility** into every **deployment**.*
- After: *Our approach focuses on speed: teams see every deployment in real time.*

### P29. "Term: definition" bullets

The bolded-label-colon-description list, AI's favorite way to fake structure.

- Before: *- **Scalability:** grows with your team. - **Security:** SOC 2 compliant.*
- After: *It scales with your team and passed its SOC 2 audit in January.*

### P30. List compulsion

Bullets or numbered lists where a sentence would do. Default to prose; use a list only when the user asks or the content is truly enumerable (steps, specs, options).

- Before: *Benefits include: - Saving time - Reducing errors - Improving morale*
- After: *Teams save time, make fewer errors, and by their own account are happier for it.*

### P31. Emoji as formatting

Emoji in headings or as bullet markers. Never in headings; in body text only where the register genuinely calls for it (a casual social post, at most).

- Before: *## 🚀 Getting Started*
- After: *## Getting started*

### P32. Title-case headings

Capitalizing Every Main Word in Headings. Use sentence case unless the user's style guide requires otherwise.

- Before: *## Five Ways To Improve Your Onboarding Flow*
- After: *## Five ways to improve your onboarding flow*

### P33. Section-skeleton overkill

Headings on short content, or a rigid Introduction / Challenges / Future Outlook / Conclusion scaffold imposed regardless of content. No headings under ~400 words; let the material dictate structure. Related tells: horizontal rules before headings, skipped heading levels (H2 → H4).

- Before: *[300-word email broken into "Introduction", "Key Points", "Next Steps", "Conclusion"]*
- After: *[the same 300 words as three plain paragraphs]*

### P34. Curly and straight quote mix

Both `"smart"` and `"straight"` quotation marks in one document — the fingerprint of AI text pasted into hand-typed text. Pick one and be consistent.

- Before: *She called it "a solid quarter" — the report says "growth exceeded plan".*
- After: *She called it "a solid quarter" — the report says "growth exceeded plan".*

## E. Vocabulary

### P35. AI-vocabulary hits

Words that spiked measurably in published text after ChatGPT's release (arXiv:2406.07016 measured the excess across 15M+ PubMed abstracts). Full list with replacements in `vocabulary.md`.

- Before: *We leverage cutting-edge technology to deliver a seamless, transformative experience across the entire customer journey.*
- After: *We use current browser APIs, so pages load in under a second and checkout takes two taps.*

### P36. Stock idiom crutches

"At the end of the day", "in today's fast-paced world", "a testament to", "when it comes to" — prefab phrases that fill space without adding meaning.

- Before: *In today's fast-paced world, staying organized is a testament to strong leadership.*
- After: *Managers who keep a written decision log spend less time re-litigating old choices.*
