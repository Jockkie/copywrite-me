# Scorecard

Rate each applicable element **strong**, **moderate** or **weak** (or **unverified** for Channel fit when the channel check was impossible). Mark elements that do not belong in this format as **n/a**. Never mark an element n/a just to raise the score.

## Scoring method

- strong = 1.0, moderate = 0.5, unverified = 0.5, weak = 0
- Section score = average of its applicable elements
- A section with fewer than three applicable elements counts with part of its weight: weight × (applicable elements ÷ 3). One element cannot decide a whole section in a short format.
- Total = weighted average of applicable sections × 100, rounded
- Weights: Opening 20, Body 15, Offer 15, Close 10, Proof 15, Editing 15, Channel fit 10. Weights of sections that are fully n/a are redistributed proportionally.
- 80 or higher: ready to publish. If the score stays below 80 only because Channel fit ratings are capped by medium-confidence sources, say so plainly: the text itself may be ready; the cap reflects how sure we are about the platform, not the writing. 60 to 79: improve the weak and moderate elements first. Below 60: rethink the structure.

`scripts/copy_score.py` does this and renders the visual scorecard.

## Elements

### Opening
| Element | Strong when |
|---------|-------------|
| Headline or hook | Specific, about the reader, makes them want the next line; passes the 4 U's |
| Subheadline | Adds the promise or the mechanism the headline left out |
| Lead | The first lines pull the reader in with their situation, story or a sharp fact |
| Promise | One clear outcome the reader gets |

### Body
| Element | Strong when |
|---------|-------------|
| Problem in their words | The reader recognises their own situation and wording |
| Cost of the problem | What it costs to leave it unsolved, concretely |
| The dream | A vivid, believable picture of life after |
| Reframe | A new way to see the problem that makes the old solutions look weak |
| Mechanism | Why this works when other things did not, in plain words |
| Old way, new way | Clear contrast between alternatives and this |
| Story | A real origin or customer story that carries the message |
| Who it is for and not for | The reader can qualify themselves |

### Offer
| Element | Strong when |
|---------|-------------|
| What you get | Concrete contents, format and timing |
| How it works | Simple steps from buying to result |
| Outcome focus | Features are translated into results for the reader |
| Price and value | The price is shown with a reason it is worth it, compared to the real alternative |
| Risk reversal | Guarantee, trial, small first step or clear exit |
| Objections handled | The top three objections are answered in the text |
| FAQ | Practical questions answered (only for long formats) |
| Options | Tiers or payment options are clear, not confusing |

### Close
| Element | Strong when |
|---------|-------------|
| Call to action | One clear next step, repeated where it helps, low friction |
| Real urgency | A true reason to act now (deadline, limited capacity, season), or none at all |
| Final reassurance | The last doubt is addressed right before the action |

### Proof
| Element | Strong when |
|---------|-------------|
| Testimonials | Real, specific, with name or role (with permission) |
| Results and numbers | Measured results, with context |
| Case or before and after | One worked example the reader can relate to |
| Authority | Credentials, experience, media, partners, relevant only |
| Proof placement | Proof sits where doubt arises (near claims, price and call to action) |

### Editing
| Element | Strong when |
|---------|-------------|
| Clarity | One idea per sentence, no jargon, no ambiguity |
| Customer language | Uses the reader's own words and phrases |
| Tone of voice | Matches the brand and the reader |
| Show, don't tell | Examples and specifics instead of adjectives |
| Flow | Each part leads to the next; skimmable with subheads where long |
| Tightness | Nothing to cut without losing meaning |
| Readability | Short paragraphs, plain words, suits reading level and device |

### Channel fit
| Element | Strong when |
|---------|-------------|
| Format and length | Matches the current platform guidelines found in Phase 2 |
| First-screen rule | The key message lands before truncation or the fold |
| Platform rules | Nothing the platform currently penalises; ad policies respected |
| Visual pairing | Text and visual support each other; alt text present |
| Accessibility | Meets the checks in `channels.md` |

## Which elements count per format

Short formats are judged on fewer elements. Mark the rest n/a; that is not inflation, it is the right yardstick.

| Format | Score these | n/a |
|--------|-------------|-----|
| Social post, carousel, cold email, ad, email subject, product description | Opening: headline or hook, promise · Body: problem in their words · Offer: call to action moved to Close, plus "what you get" for product descriptions and ads · Close: call to action, real urgency only if used · Proof: the one proof element used (or "results and numbers" as weak if none) · Editing: all · Channel fit: all | Everything else |
| Newsletter, blog post, short landing page | Opening, Body except Reframe and Story unless used, Offer: what you get, outcome focus, call to action, Close, Proof, Editing, Channel fit | FAQ, Options, Price and value unless a price is shown |
| Sales page, long landing page | Everything | Only what truly does not apply, with a reason |

Pick the row by the text's actual length and job, not by the name the user gives (a page under about 300 words is a short landing page), and name the yardstick you used in the reply. In short formats a missing price is a fix to suggest, not a weak element.

Strict ratings: Accessibility is `strong` only when alt text is written or confirmed; First-screen rule is `strong` only when the offer and the key detail (date, price or action) fit before the truncation point found in the channel check; any Channel fit element that rests on medium-confidence sources is at most `moderate`.

Rate `unverified` (counted as moderate) for Channel fit elements when the channel guidelines could not be checked.

## Output

Show the scorecard as a compact table per section with a coloured dot or label per element, the total out of 100, then the weak elements first with reason and fix.
