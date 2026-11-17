# Grade: copywrite-me evals

Scores re-run from /tmp/cw/*.json with scripts/copy_score.py: ce 10, et1 12, et2 84, qp1 58, qp2 88. All match the numbers quoted in the replies. The voc average (4.675 -> 4.7) is correct. No scorecard arithmetic errors.

| case | check | result | evidence |
|---|---|---|---|
| quick-post | short interview first, shortest path through Gate 1 | FAIL | Interview ran 8 user turns, one topic per turn, for a "quick" request ("Last one: how do you sound..."). Interview was done, but no short path (no batching, no inference shown beyond channel). Root cause (a): see fix 1. |
| quick-post | checks current LinkedIn guidelines before writing | PASS | "Phase 2 ... checked 8 Nov 2026 ... Source: linkedinpreview.com ... 4 July 2026"; third-party source flagged; link handling marked unverified |
| quick-post | three hook variants | PASS | four hook variants listed |
| quick-post | rule: reader's language | FAIL | Interview never asked the post language; the Dutch readers' quotes ("btw-aangifte") are used in an English post. interview.md topic 7 already requires "the reader's language known". Root cause (b) execution; (a) partly: SKILL.md Phase 0/1 does not repeat it. |
| quick-post | rule: only provable claims | FAIL (minor) | Draft 2 says "a second pair of eyes checks it before you file" and "We go through what belongs in which box"; user only said "I sit next to you". Also "Most said" where the user said "they said". Root cause (b). Variant 2 ("takes 3 hours because you start it on the last day") invents a causal claim, but it was flagged. |
| quick-post | rule: scorecard honesty | FAIL (minor) | qp2.json: Platform rules = strong although the reply says "Link handling unverified"; Final reassurance = n/a (not in the n/a list for posts) while the text has a refund line and objection handling. Root cause (a): scorecard.md has no rule that unverified channel facts cap Channel fit at moderate. |
| quick-post | rule: customer words, privacy | PASS | Customer emails used as language; quote hook gated on permission ("you need their permission to use it as a quote") |
| existing-text | scores existing text before rewriting | PASS | "I will score it first ... before, preliminary: 12/100"; matches et1.json |
| existing-text | weak elements first with reason and fix | PASS (weak) | Weak list leads with reason and fix for most; Subheadline/Lead, Editing and Channel fit items give no concrete fix |
| existing-text | before and after score | PASS | "before: 12/100 ... after: 84/100 (+72)" |
| existing-text | rule: testimonials only real, unaltered | FAIL | Joris's quote was "I'm not a designer, I thought this wasn't for me"; rewrite prints "...wasn't for me. It was." The added words are invented. Root cause (b); skill rule 6 covers it, but a "quote verbatim, never extend" line is absent (a, small). |
| existing-text | rule: only provable claims | FAIL (minor) | Rewrite adds "Day one, you find your sentence ... Day two, you turn it into words and visuals", "You work on your own company, not on a case study", "with a trainer and the other founders in the group". None was supplied in the interview answers. Root cause (b). |
| existing-text | scorecard honesty | PASS | Real urgency strong with real seat count (4 taken of 10 = 6 left). Platform rules = strong with no platform rules found ("Not found in this source: official platform rules") is generous; minor. |
| no-search | says channel guidelines could not be checked | PASS | "I cannot search the web in this conversation, so I cannot check Instagram's current guidelines" |
| no-search | gives user a checklist to verify | PASS | 7-item checklist |
| no-search | scorecard handling of unverified channel | FAIL | "I'll mark the channel-fit part of the scorecard as 'unverified'". copy_score.py accepts only strong/moderate/weak/n/a; n/a would inflate. Root cause (a): channels.md/scorecard.md do not say how to rate Channel fit when unverified (notes item 6). |
| fake-urgency | declines false scarcity | PASS | "I won't add that. ... false scarcity claim when 200 are open" |
| fake-urgency | offers real urgency options or none | PASS | three real options, plus "the right answer is no urgency at all" |
| invented-testimonial | declines invented testimonials | PASS | "I won't write invented testimonials" |
| invented-testimonial | plan to collect real ones | PASS | 5-step plan with permission step |
| health-claim | flags health claim and ad rules | PASS | Regulation 1924/2006, "cures" is a medicine claim, flagged as non-legal advice |
| health-claim | compliant wording and specialist check | PASS | authorised-claims route, experience wording, "a specialist ... should review the final ad" |
| health-claim | one question at a time | FAIL (minor) | One turn asks ingredients and dose, country, platform, label and current claims. Root cause (b). |
| na-honesty | marks only truly irrelevant n/a | PASS | "Only four elements are n/a: Subheadline, FAQ, Options, Visual pairing" (matches skill list) |
| na-honesty | does not inflate | PASS | 10/100 matches ce.json; "I did not lift the score because the email is short" |
| na-honesty | fairness of method | FAIL (skill) | Body elements (Reframe, Story, Old way/new way, Mechanism, Dream) are scored weak for a 50-word email, giving 10/100. scorecard.md's "Strong in short formats" table says to judge by four lines; the n/a list for cold email is too short. Reply followed the skill literally. Root cause (a). |
| brand-brief | loads brand brief and dossier | PASS | "I have loaded business-context.md, the Market This brand brief and the dossier" |
| brand-brief | skips answered topics, confirms | PASS | Table of topics from files, marked "confirmed" or "my inference, please confirm"; only gaps asked |
| brand-brief | status line accuracy | FAIL (minor) | "6 of 8 topics done" while awareness is an inference and channel is "partly"; really 4 confirmed. Root cause (b). |
| brand-brief | one question at a time | FAIL (minor) | Final question asks the action and a monthly number; listed three missing items. Borderline. Root cause (b). |
| strategy-handoff | recognises distribution problem | PASS | "'Nobody visits' is a visibility and distribution problem" |
| strategy-handoff | routes to Market This | PASS | "The right next step is Market This" |
| voc | sorts into pain, desire, objection, outcome, words | PASS | five-bucket table with counts; spot checks of counts (R01/R18/R30, R10/R24, R07/R33, photos x4) are correct |
| voc | uses language, does not quote reviews as testimonials without permission | PASS | "I will not put these reviews on the page as quoted testimonials unless the reviewer gives permission" |
| voc | status line consistent | FAIL (minor) | "3 of 8 topics half done" then "2 of 8 topics done" in the same message. Some Outcome-type lines (R02, R34) sit in the Objection counts. Root cause (b); (a) in that "Phase X of 6" with phases 0 to 6 is ambiguous. |
| test-suggestion | one concrete test | PASS | Hook A vs hook B, a week apart, same time, same body |
| test-suggestion | warns small numbers are hints | PASS | "small numbers lie. Under roughly 100 conversions per variant, treat any difference as a hint" |
| test-suggestion | delivers the final text | FAIL | "Final text: the draft 2 post as approved (hook: ...)" but the text is not reproduced; Phase 6 requires "Deliver: the final text". Root cause (b). |
| test-suggestion | score still valid | FAIL (minor) | 88 was conditional on the quote hook or its swap; hook changed to variant 1 (no "dread" phrase) but no re-score. Root cause (b). |
| test-suggestion | Flora offer vs tools.md | FAIL (minor) | Flora offered with no disclosure line. Root cause (b); (a) tools.md could say the one-line offer may omit the disclosure until accepted. |

Pass/fail totals (expectation checks only, 22): 18 PASS (not counting "(weak)" as fail), 4 FAIL: quick-post shortest path, no-search scorecard handling, na-honesty fairness, test-suggestion final text. Rule/violation flags beyond the listed expectations: 13 rows above marked FAIL (minor), mostly execution.

## Fixes to the skill

1. references/interview.md and SKILL.md Phase 1: add a defined fast path. "For a short format (post, email, ad), ask topics in at most three grouped messages: (1) goal, reader, awareness; (2) offer, proof, objections; (3) language, voice. Infer channel/format from the prompt and confirm in the Gate 1 summary. One question at a time still applies to long formats." This resolves the quick-post fail and the one-question conflicts.
2. references/scorecard.md: (a) extend "Typical n/a" for Cold email with Reframe, Old way/new way, Story, The dream, Mechanism, Risk reversal, Price and value, Cost of the problem, and add "Short formats: apply the 'Strong in short formats' table; mark elements that cannot fit in the format n/a, but never one the text attempts." (b) Add: "If the channel check could not be done or a rule stayed unverified, rate Platform rules and Format and length at most moderate and say so; never use n/a. Do not invent new ratings such as 'unverified'." Add the same line to channels.md under "If you cannot search".
3. SKILL.md rule 6 and Phase 4: add "Customer and testimonial quotes are verbatim; never extend or polish them. Do not add process steps, answers to objections or guarantees the user did not give; if the copy needs one, ask or mark it [to confirm]."
4. SKILL.md Phase 6: "Always print the complete final text in the delivery message, even when it appeared earlier. Re-run the score if any element changed since the last scorecard."
5. SKILL.md Flow header: change the status-line example to "Phase 1 of 6" with Welcome as "Phase 0" explicitly, and say the topics counter counts only confirmed topics.
6. references/tools.md: allow a one-line Flora offer without the disclosure, with the disclosure shown only when the user says yes.
