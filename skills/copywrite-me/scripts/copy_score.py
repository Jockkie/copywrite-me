#!/usr/bin/env python3
"""Score a Copywrite Me scorecard and optionally render it as HTML.

Usage:
    python3 copy_score.py scorecard.json              # print score and weak elements
    python3 copy_score.py scorecard.json out.html     # also write a visual scorecard
    python3 copy_score.py before.json out.html --after after.json   # before and after

Ratings per element: strong, moderate, weak or n/a.
Standard library only.
"""
import html
import json
import signal
import sys

if hasattr(signal, "SIGPIPE"):
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

WEIGHTS = {"Opening": 20, "Body": 15, "Offer": 15, "Close": 10,
           "Proof": 15, "Editing": 15, "Channel fit": 10}
VALUE = {"strong": 1.0, "moderate": 0.5, "unverified": 0.5, "weak": 0.0}
KNOWN = {
    "Opening": ["Headline or hook", "Subheadline", "Lead", "Promise"],
    "Body": ["Problem in their words", "Cost of the problem", "The dream", "Reframe", "Mechanism", "Old way, new way", "Story", "Who it is for and not for"],
    "Offer": ["What you get", "How it works", "Outcome focus", "Price and value", "Risk reversal", "Objections handled", "FAQ", "Options"],
    "Close": ["Call to action", "Real urgency", "Final reassurance"],
    "Proof": ["Testimonials", "Results and numbers", "Case or before and after", "Authority", "Proof placement"],
    "Editing": ["Clarity", "Customer language", "Tone of voice", "Show, don't tell", "Flow", "Tightness", "Readability"],
    "Channel fit": ["Format and length", "First-screen rule", "Platform rules", "Visual pairing", "Accessibility"],
}


def validate(card):
    problems = []
    for sec, els in card.get("sections", {}).items():
        if sec not in KNOWN:
            problems.append(f"unknown section: {sec}")
            continue
        for el, r in els.items():
            if el not in KNOWN[sec]:
                problems.append(f"unknown element in {sec}: {el}")
            if r not in VALUE and r != "n/a":
                problems.append(f"unknown rating for {el}: {r}")
    return problems


def score(card):
    sections = card.get("sections", {})
    parts, weight_sum = [], 0
    for name, weight in WEIGHTS.items():
        vals = [VALUE[r] for r in sections.get(name, {}).values() if r in VALUE]
        if vals:
            w = weight * min(len(vals), 3) / 3  # sections with 1 or 2 elements weigh less
            parts.append((sum(vals) / len(vals)) * w)
            weight_sum += w
    total = round(100 * sum(parts) / weight_sum) if weight_sum else 0
    weak = [(s, e) for s, els in sections.items() for e, r in els.items() if r == "weak"]
    return total, weak


def verdict(total):
    if total >= 80:
        return "ready to publish"
    if total >= 60:
        return "improve the weak and moderate elements first"
    return "rethink the structure"


def esc(v):
    return html.escape(str(v))


def card_html(card, total, compare=None):
    rows = []
    for name in WEIGHTS:
        els = card.get("sections", {}).get(name, {})
        if not els:
            continue
        pills = []
        for el, r in els.items():
            prev = compare.get("sections", {}).get(name, {}).get(el) if compare else None
            up = prev is not None and VALUE.get(r, -1) > VALUE.get(prev, -1)
            pills.append(f'<span class="pill {esc(r).replace("/", "")}{" up" if up else ""}"><i></i>{esc(el)}</span>')
        rows.append(f'<div class="row"><div class="sec">{esc(name)}</div><div class="pills">{"".join(pills)}</div></div>')
    label = esc(card.get("version", ""))
    return f'''<section class="card">
<div class="head"><h2>Copy score <span class="score">{total}<small>/100</small></span></h2>
<div class="legend"><span><i class="d strong"></i>Strong</span><span><i class="d moderate"></i>Moderate</span><span><i class="d weak"></i>Weak</span></div></div>
<div class="sub">{label} · {esc(verdict(total))}</div>
{"".join(rows)}
</section>'''


def page(title, body):
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Copywrite Me · {esc(title)}</title>
<style>
:root {{ --bg:#F5F5DC; --fg:#212121; --muted:#5D4037; --line:rgba(33,33,33,.12); --card:#FBFBEE; --strong:#388E3C; --moderate:#FFCA28; --weak:#F57C00; }}
@media (prefers-color-scheme: dark) {{ :root {{ --bg:#212121; --fg:#F5F5DC; --muted:rgba(245,245,220,.62); --line:rgba(245,245,220,.14); --card:#292929; --strong:#81C784; }} }}
* {{ box-sizing:border-box; }}
body {{ margin:0; background:var(--bg); color:var(--fg); font:15px/1.5 Inter, system-ui, -apple-system, sans-serif; }}
main {{ max-width:900px; margin:0 auto; padding:40px 20px 64px; }}
.eyebrow {{ font-size:11px; font-weight:600; letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }}
.eyebrow::before {{ content:""; display:inline-block; width:22px; height:2px; background:var(--weak); vertical-align:middle; margin-right:10px; }}
h1 {{ font-family:Spectral, Georgia, serif; font-weight:600; font-size:32px; letter-spacing:-0.02em; margin:12px 0 28px; }}
.card {{ background:var(--card); border:1px solid var(--line); border-radius:14px; padding:22px 24px; margin-bottom:22px; }}
.head {{ display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px; border-bottom:2px solid var(--fg); padding-bottom:12px; }}
h2 {{ margin:0; font-size:24px; letter-spacing:-0.03em; }}
.score {{ background:rgba(245,124,0,.12); border-radius:8px; padding:2px 10px; margin-left:8px; }}
.score small {{ font-size:13px; color:var(--muted); }}
.legend {{ display:flex; gap:14px; font-size:13px; }}
.sub {{ color:var(--muted); font-size:13px; margin:8px 0 4px; }}
.row {{ display:grid; grid-template-columns:120px 1fr; gap:12px; padding:12px 0; border-bottom:1px solid var(--line); }}
.row:last-child {{ border-bottom:0; }}
.sec {{ font-weight:700; font-size:14px; }}
.pills {{ display:flex; flex-wrap:wrap; gap:6px; }}
.pill {{ display:inline-flex; align-items:center; gap:6px; border:1px solid var(--line); border-radius:999px; padding:4px 11px; font-size:13px; }}
.pill i, .d {{ width:8px; height:8px; border-radius:50%; display:inline-block; }}
.d {{ margin-right:6px; }}
.strong i, .d.strong {{ background:var(--strong); }} .moderate i, .d.moderate {{ background:var(--moderate); }} .weak i, .d.weak {{ background:var(--weak); }}
.weak {{ border-color:var(--weak); }} .unverified {{ border-style:dashed; }} .unverified i {{ background:var(--moderate); }} .na {{ opacity:.35; }} .na i {{ background:var(--muted); }}
.up {{ box-shadow:0 0 0 2px rgba(56,142,60,.35); }}
footer {{ color:var(--muted); font-size:12px; margin-top:30px; }}
@media (max-width:560px) {{ .row {{ grid-template-columns:1fr; }} }}
</style></head><body><main>
<div class="eyebrow">Copywrite Me · by Jockkie Studio</div>
<h1>{esc(title)}</h1>
{body}
<footer>Strong = 1, moderate = 0.5, weak = 0, n/a left out. Weighted per section. A green ring marks an element that improved. jockkie.com</footer>
</main></body></html>'''


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    with open(argv[1], encoding="utf-8") as f:
        card = json.load(f)
    after = None
    if "--after" in argv:
        with open(argv[argv.index("--after") + 1], encoding="utf-8") as f:
            after = json.load(f)
    for prob in validate(card):
        print("warning: " + prob)
    total, weak = score(card)
    print(f"{card.get('version', 'score')}: {total}/100 · {verdict(total)}")
    for s, e in weak:
        fix = card.get("fixes", {}).get(e, "")
        print(f"  weak · {s} · {e}" + (f" → {fix}" if fix else ""))
    body = card_html(card, total)
    if after:
        a_total, a_weak = score(after)
        print(f"{after.get('version', 'after')}: {a_total}/100 · {verdict(a_total)} ({a_total - total:+d})")
        body = card_html(after, a_total, compare=card) + body
    out = [a for a in argv[2:] if a.endswith(".html")]
    if out:
        with open(out[0], "w", encoding="utf-8") as f:
            f.write(page(card.get("title", "Scorecard"), body))
        print(f"Scorecard written to {out[0]}")


if __name__ == "__main__":
    main(sys.argv)
