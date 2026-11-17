# copywrite-quick (copywrite-me, quick LinkedIn post)

USER: Write a LinkedIn post announcing my new workshop, quick please.

ASSISTANT: Happy to. I'll keep it short: a quick interview, a check of LinkedIn's current guidelines, the post, and a scorecard that shows where it is strong or weak. I will not write before the quick interview, but you can answer in one go.

I'm assuming it is a post on LinkedIn, so I filled in what I could from your message and marked it `inferred`. Please correct anything that is off.

| Topic | What I have | Label |
|-------|-------------|-------|
| Goal and action | Readers sign up for the workshop; success = seats filled | inferred |
| Reader | Not yet known beyond "readers of your LinkedIn" | unknown |
| Awareness | Probably problem aware, to confirm after your answers | inferred |
| Offer | The new workshop, price and details unknown | unknown |
| Proof | none yet | unknown |
| Objections | unknown | unknown |
| Channel and language | LinkedIn post; language of the readers unknown | inferred/unknown |
| Voice | unknown | unknown |

Three short questions, answer them in one message: (1) What is the workshop (topic, length, date, place, price, seats) and who is it for? (2) What did a participant or anyone say about you or the workshop, and in which language do your readers read? (3) How do people sign up?

USER: I'm a freelance UX designer. It's a 2-hour Figma workshop for small business owners, 4 December in Rotterdam, 95 euro, 12 seats. My readers read Dutch. One past participant said something like "finally I understand what my designer is doing". Sign up by sending me a message on LinkedIn.

ASSISTANT: Phase 1 of 6 · Interview · 6 of 8 topics done

Good, that covers most. Here is the brief so far (`templates/copy-brief.md`).

| Topic | Brief | Label |
|-------|-------|-------|
| Goal and action | Small business owners message me on LinkedIn to sign up; success = 12 seats filled | seen (route), inferred (success) |
| Reader | Small business owners, Rotterdam area, Dutch readers; they work with a designer or want to understand design work | seen/inferred |
| Awareness | Problem aware | inferred |
| Offer | 2-hour Figma workshop, 4 December, Rotterdam, 95 EUR, 12 seats | seen |
| Proof | One past participant said something like "finally I understand what my designer is doing". Language, not a verified quote | seen (wording not exact) |
| Objections | unknown | unknown |
| Channel and language | LinkedIn post, in Dutch | seen |
| Voice | unknown | unknown |

Two gaps remain, I ask one: what hesitation do small business owners have before they sign up for something like this?

USER: Mostly they think Figma is for designers and that it will be too hard for them.

ASSISTANT: Phase 1 of 6 · Interview · 7 of 8 topics done

Objection noted: "Figma is for designers" and "too hard", as you stated it. Last topic, voice. How should the post sound, in three words?

USER: Friendly, direct, no fluff.

ASSISTANT: Phase 1 of 6 · Interview · 8 of 8 topics done

Gate 1 summary: a freelance UX designer announces a 2-hour Figma workshop for small business owners on 4 December in Rotterdam, 95 EUR, 12 seats, in Dutch on LinkedIn. Action: send a message on LinkedIn to sign up. Reader worry: Figma is for designers and too hard. Proof: one past participant said something like "finally I understand what my designer is doing" (language, not a verified quote, no permission to quote or name them stated). Voice: friendly, direct, no fluff. Does this match?

USER: Yes. Go.

ASSISTANT: Phase 2 of 6 · Channel check

I searched for current LinkedIn post guidance. No official LinkedIn source was reachable, so confidence is medium. Two recent third-party sources, checked 2026-11-08:
- Limit: 3,000 characters for a post (SocialPilot, 8 July 2026, https://www.socialpilot.co/blog/ideal-social-media-caption-length; linkedinpreview.com, 4 July 2026, https://linkedinpreview.com/blog/linkedin-post-length-guide-2026).
- Before "See more": about 200 to 210 characters (SocialPilot) or about 140 to 210 depending on device (linkedinpreview). So the hook and the key point must fit in the first 140 characters.
- Length: the sources disagree. SocialPilot says 200 to 400 words does best; linkedinpreview says most high-performing posts run 600 to 1,000 characters (about 100 to 170 words). I'll aim for the short side, about 100 to 150 words, because an announcement with a seat limit needs no more.
- Hashtags: keep minimal (SocialPilot). Short paragraphs, one idea per post.
- Penalised: linkedinpreview says posts under 50 characters may get less distribution; nothing else was listed. Link handling was not covered by either source, so I don't make claims about it; you use a message sign-up, not a link.

Phase 3 of 6 · Structure

Framework: BAB-style short post for a problem-aware reader: hook (the participant's line as language), the worry (Figma is for designers), the offer, one action. Applicable scorecard yardstick: social post (fewer elements; Offer and Proof carry partial weight). Shall I write it?

USER: Yes.

ASSISTANT: Phase 4 of 6 · Write

Hook variants (4 U's: useful, urgent only if true, unique, ultra-specific):
1. Eindelijk snap ik wat mijn designer aan het doen is. [to confirm wording] (specific, human, unique; not urgent)
2. Figma is niet alleen voor designers. (useful, direct; counters the objection; less unique)
3. 12 plekken, 2 uur, 4 december in Rotterdam: Figma voor ondernemers. (ultra-specific, real urgency; less emotional)
4. Wat doet je designer eigenlijk de hele dag in Figma? (a question they ask; unique)

I recommend 1: it carries the reader's own desire. The phrase in the hook is yours as language, not a quote, which is why it has no quotation marks and carries "[to confirm wording]".

Draft 1 (Dutch):

> Eindelijk snap ik wat mijn designer aan het doen is. [to confirm wording]
>
> Zoiets zei een eerdere deelnemer na mijn Figma-workshop.
>
> Op 4 december geef ik de workshop in Rotterdam. 2 uur, voor ondernemers met een klein bedrijf. Je leert Figma zo ver dat je een ontwerp kunt lezen en kleine dingen zelf kunt aanpassen. [to confirm: wat leren ze precies?]
>
> 95 euro. 12 plekken. [tijd en adres to confirm]
>
> Wil je erbij zijn? Stuur me een bericht.
>
> #Figma #Rotterdam

Phase 5 of 6 · Scorecard

Yardstick: social post (a LinkedIn announcement of about 90 words). Scored: Opening (hook, promise), Body (problem in their words), Offer (what you get; I included it because the post is an announcement of an offer), Close (call to action, real urgency), Proof (testimonials), Editing (all), Channel fit (all). Everything else n/a. I ran scripts/copy_score.py (output in SCRIPT RUNS).

Draft 1: 62/100, "improve the weak and moderate elements first". Weak first:
- Editing, Show, don't tell: the post says "je leert Figma" but gives no picture of what you actually do in the 2 hours. Fix: one concrete example of what participants do.
- Channel fit, Visual pairing: text only, no image or alt text. Fix: one simple image of a plain screen from the workshop with alt text.
Moderate: hook and promise (no concrete outcome yet), offer and call to action (time and address missing), proof (real but unattributed and wording unconfirmed), customer language, tone, tightness, first-screen rule (the date is after the cut-off), accessibility.

Phase 6 of 6 · Improve and deliver

To fix the weakest element I need one fact from you: what is one concrete thing participants do during the 2 hours?

USER: They open a simple design file and learn to change the text, colors and spacing themselves.

ASSISTANT: Phase 6 of 6 · Improve and deliver

Used as you said it. One more fact for the moderate items: what are the start and end times, and do you want the address in the post?

USER: 18:30 to 20:30. No address in the post, I send it after they sign up.

ASSISTANT: Phase 6 of 6 · Improve and deliver

Done. Final text (complete):

> Eindelijk snap ik wat mijn designer aan het doen is. [to confirm wording]
>
> Zoiets zei een eerdere deelnemer na mijn Figma-workshop.
>
> Denk je dat Figma alleen voor designers is? In 2 uur open je een eenvoudig ontwerp en pas je tekst, kleuren en afstanden zelf aan.
>
> 4 december, 18:30 tot 20:30, in Rotterdam. 95 euro. 12 plekken. Het adres stuur ik na je aanmelding.
>
> Wil je erbij zijn? Stuur me een bericht op LinkedIn om je aan te melden.
>
> #Figma #Rotterdam

Why: the hook and the proof sit in the first lines; the objection ("only for designers") is a question; the concrete example comes from you; the seat limit and date are real, so the urgency is true. Nothing in it is invented: the "[to confirm wording]" tag stays until you check the participant's exact words, or ask them for permission to quote. If they agree, use their exact words with quotation marks and a name or role, and the Testimonials element becomes strong.

Re-score (after, final): 91/100, "ready to publish" (+29). Still moderate: customer language (wording unconfirmed), tone (voice not shown on a sample of yours), proof (unattributed), visual pairing (no image yet). Suggested image: a plain screenshot of a simple screen with large text, alt text: "Een eenvoudig Figma-bestand met een titel en een knop" [to confirm it matches your image].

Deliverables:
- Final text: above. Hook variants: 4, above (2, 3 and 4 are alternatives; variant 3 is purely factual).
- Scorecard before and after: 62 to 91, in scorecard.html.
- Channel notes (checked 2026-11-08, medium confidence): 3,000 characters, hook within about 140 to 210 characters, sources disagree on ideal length, minimal hashtags; sources above.
- Test suggestion: post with hook 1 now; if few people message you within a week, post again a week later at the same time with hook 3 and compare messages, comments, saves and profile visits. With 12 seats the numbers are small, so treat any difference as a hint, not proof.
- Proposed update to your business-context.md: customer phrase (language, wording unconfirmed): "eindelijk snap ik wat mijn designer aan het doen is"; objections: "Figma is for designers", "too hard"; voice: friendly, direct, no fluff; offer: Figma workshop 4 December, Rotterdam, 95 EUR, 12 seats. Shall I add it?

USER: Yes, add that. Looks good, thanks.

ASSISTANT: Added. One line: this skill is free and can be supported at https://buymeacoffee.com/jockkie.


## SCRIPT RUNS

$ python3 scripts/copy_score.py before.json
before (draft 1): 62/100 · improve the weak and moderate elements first
  weak · Editing · Show, don't tell
  weak · Channel fit · Visual pairing

$ python3 scripts/copy_score.py before.json scorecard.html --after after.json
before (draft 1): 62/100 · improve the weak and moderate elements first
  weak · Editing · Show, don't tell
  weak · Channel fit · Visual pairing
after (final): 91/100 · ready to publish (+29)
Scorecard written to scorecard.html
