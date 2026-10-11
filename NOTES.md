# Tindon Health & Wealth: Medicare 2027 webinar registration (2026-10-11)

**Brief (Javier):** a webinar funnel for Brianna (Tindon Health & Wealth). No photos of her; use a
labelled photo placeholder in the about section. Brand = the logo he pasted (navy shield/column,
orange HEALTH ⚡ WEALTH). Webinar content = the claude.ai slide deck "Medicare 2027: What's Changing
& What It Means for You" (it was written for Johnny Brock / RIG; same deck, Brianna presents).
Also research the company.

**Preview:** https://javmartz04-ship-it.github.io/tindon-medicare-webinar/ (repo of the same name; push to update).

## What the research found (tindon.com, BBB)
- Brianna **Henward** (not "Tindon"). Owner, Health Insurance Advisor, licensed health + life,
  Medicare + ACA. Office 655 Post Rd, Wells ME 04090. Serves ME + NH (their GHL webinar page also offers MA).
- "Tindon" = her parents Tina and Don Gross, started 2007. Sister Bridgette (CP, epilepsy, autism);
  Brianna enrolled her in Medicare at 20 and still manages her plan. Husband Andrew = financial advisor.
- Site palette: navy #0B294F, orange #FF914D, blue #153369, #F4F4F4. Roboto + Times.
- 10 Google reviews on tindon.com (5.0). Used verbatim: Julee Johnson, Colombe Cote, Anthony Imperato.
- Their own Medicare disclosure is quoted verbatim in the footer.
- A real headshot exists: tindon.com/wp-content/uploads/sites/150/2026/05/THW-Brianna-Henward-Headshot-2.jpg.
  Not used, because Javier asked for a placeholder. Offered as a swap.
- Existing GHL webinar page: go.tindon.com/landing ("Health Coverage For Retirement Webinar").

## Direction
Institutional trust for an older audience. Lit paper ground, navy ink, one orange accent (CTA fill,
eyebrow tick, emphasis line in #D9621A for 3.5:1 on paper). Playfair Display 600 + Inter. 6px radius
everywhere (shield register). Senior type scale: body 19px, sub 22px, 66px CTA, 62px inputs, labels above fields.
Logo traced to SVG (vtracer on a 3-colour quantize), inlined once as `<g id="lg">`, colours on custom
properties so `.inv` flips it white on navy.

## Structure (~11,000px at 1440, 0 anchors, one CTA label "Reserve My Free Seat" x5 + dock + form)
hero (no nav, H1 3 lines, emphasis "before December 7.", webinar window rotating 4 HTML slides, BH cam tile)
→ 3 numbers that change Jan 1 ($9,850 / $2,400 / $274, CMS) → problem 01-03 → reframe band
("They overpay because they never checked again.") → mechanism "The 2027 Plan Check", 6 steps on a rail
(navy band) → agenda 01-06, each with a real deck slide rebuilt in HTML → host (placeholder photo,
first-person bio from tindon.com) → 3 Google reviews → for / not for → FAQ → navy close with footer folded in.
Countdown: no webinar date given, so it counts to the end of AEP (Dec 7, 11:59pm ET). Set `EVENT_START`
and it switches to the webinar time everywhere.

## Form
Dialog: full name, email, phone, state (ME/NH/MA, from their own GHL page), all required. `WEBHOOK` and
`THANKS` empty = preview mode (success state, nothing sent). `?preview=1` forces preview later.
Prefill `?full_name=&email=&phone=`. Remembers the registration only after a confirmed send.

## Open items
- Webinar date/time, the GHL webhook and thank-you URL.
- Brianna's photo (or OK to use the headshot from tindon.com).
- TPMO counts ("we represent X organizations / Y products") if their compliance wants the full version.
- SMS consent line under the form is our default wording; confirm with their A2P copy.
- Part A/B 2027 numbers are projections until CMS publishes mid-November; update the deductibles slide then.

## Rework during the build
- H1 wrapped to 4 lines at 1440 → 64px + nowrap per line on desktop only.
- Playfair rendered "$0" as "$o" (old-style figures) → `font-variant-numeric:lining-nums` on body.
- Hero copy column overflowed at 390 (grid `1fr` + max-content countdown) → `minmax(0,1fr)`.
- Eyebrows cut from 9 to 4 (pre-flight max).
