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

## v2 (2026-10-11, same day): "way too long", "you just copied what we already had"
Javier, verbatim: *"this is way too long... I love the hero section... You can keep the frequently asked questions. I would take out where it says check your 2027 plan before december... I want to keep what we're covered, but I don't want to show [the slides]... the webinar is not that long, right? This is b to c rather than b to b... let's just keep making this more premium."*

- Hero kept exactly. Everything between hero and FAQ rebuilt: 11,000px → 3,900px at 1440.
- Cut: 3-numbers strip, problem rows, reframe band, 6-step rail, agenda-with-slides, for/not-for, navy closing block.
- New: one navy "Inside the webinar" band. Problem + reframe compressed into its H2 ("Same plan name. Different plan.")
  and lede, with six topic teasers beside it. No slides, no answers: two teasers carry the real number blurred
  with a "Revealed live" tag so the reason to show up is visible.
- Host + reviews merged into one light section; reviews became a hairline strip of three short excerpts (cut, not reworded).
- FAQ kept, now carries the last CTA. Footer is a light logo + disclaimer plate.
- v1 kept locally as v1-archived.html / v1-src-archived.html.

## v3 hero copy (2026-10-11)
Javier supplied "Could You Be Paying More for Medicare in 2027 Without Realizing It?" + two supporting lines, but
wanted the headline "more of a call out" blended with what we had. Shipped: "On Medicare in Maine or New Hampshire? /
You could be paying more in 2027 / *without realizing it.*" Sub = his "find out what to check... before December 7"
line (em dash → comma); second line = his "join local Medicare advisor Brianna Henward..." as a ruled aside.
H1 down to 58px so the callout line fits one line at 1440 (it clipped the "?" at 64px). Page title uses his question.

## v4 (2026-10-11): state call-out rejected
Javier: *"This is the worst headline in the fucking world. Why are you calling out Maine or New Hampshire? Because we're doing more than [that]."*
Tindon serves beyond the states on its website. Removed every state reference: H1 line 1 is now "Already on Medicare?",
bio ends "families like yours", ME · NH fact → "Licensed / Health & life insurance", the Julee excerpt that said
"Maine plans" swapped for her "thoughtful, expert advice on all things Medicare" line, and the state dropdown is gone
from the form (name, email, phone only). The Wells, Maine office address stays (it's the real address).

## Thank-you page (2026-10-11)
`thanks.html` (source `thanks.src.html`, built by `build.py`). Same tokens and logo. Order: check seal → "Your seat is
saved" → "You're in, <Name>. / *We'll see you there.*" (name from `?first_name=` or the opt-in's localStorage) →
lede (link comes by text and email) → double-bezel navy event card (title, when, where, host) → "Before the webinar":
Annual Notice of Change, prescriptions, doctors (from the deck's checklist) → office phone 207-248-8411 → footer.
No CTA to sell; the phone link is the one deliberate exit. ~1,900px at 1440.
`EVENT_START` empty = card says the date is coming and calendar buttons stay hidden. Set it (same value as the opt-in)
and the card shows the date in ET, a countdown, Add To Calendar (.ics, verified: CRLF, 75-octet folding, 22:00Z for
6 PM EDT, 30-min alarm) and Google Calendar. For iPhones, host an .ics and set `ICS_URL` once the date exists.
Opt-in `THANKS` = 'thanks.html' and now appends `?first_name=` (first name only, never email/phone in the URL).
Still preview-only until `WEBHOOK` is set. In GHL, swap THANKS for the GHL thank-you URL.

## v5 (2026-10-25): webhook, GHL paste, real photos, what-you'll-learn
- WEBHOOK = hooks/HGSTYFasQVLLo1YnAvEJ/webhook-trigger/577686d2-... (test record accepted). THANKS = https://go.tindon.us/registered.
- Javier pastes `index.html` into GHL, so every asset now builds to an absolute GitHub Pages URL (`{{A}}` in src;
  `LOCAL=1 python3 build.py` for relative paths during local review). Relative `assets/` paths break on the GHL domain.
- Javier supplied Brianna's white-background headshot and a 7-person team photo (both ~1000px). Headshot → host
  slot (4:5 crop) and the hero webinar cam tile (initials gone). Team photo → new section.
- New light section between the navy "Inside the webinar" band and the host: "What you'll learn / Leave knowing
  exactly where you stand for 2027." Five outcomes (drugs covered, doctors in network, 2027 costs, which path, what
  to do before Dec 7) + the free one-on-one review as the bonus line + CTA. Outcomes, not topics, so it doesn't repeat
  the agenda. First layout (photo centred beside a tall list) left dead space; fixed by stacking heading + photo + CTA
  left, outcomes right. ~4,900px at 1440.

## Booking page (2026-10-30): post-webinar 2027 plan review
**Brief (Javier):** "make a booking page, this will be after a webinar to do the review or something, have a placeholder
for the calendar." Live registration page referenced: go.tindon.us/registration-page (it is our index.html pasted in GHL).

- Files: `book.src.html` → `book.html` (build.py now emits it too; same `{{A}}` absolute-asset rule for the GHL paste).
  Preview: https://javmartz04-ship-it.github.io/tindon-medicare-webinar/book.html
- Call = the "free one-on-one plan review" the webinar page already promises. H1 "Book Your 2027 / Plan Review /
  *With Brianna Henward.*" (RIG booking formula). Sub = who she checks it against (plan, doctors, prescriptions);
  no promise of what the call delivers, no length or format invented.
- Layout: logo only, no nav, 0 links. Desktop = headline + Brianna card (headshot, 5.0 Google, 2007, licensed) left,
  calendar shell right, top at 116px. Phone = headline → calendar (top 375px at 375x812) → Brianna card.
- Below: "What to have ready" 3 steps (ANOC, prescriptions, doctors), the same 3 real Google review excerpts, disclosure footer.
- Calendar: `CALENDAR_URL` in CONFIG (empty = labelled dashed placeholder). Javier sent the embed the same day:
  https://link.tindon.com/widget/booking/tXCEEx1ZAbS9NTAn243M ("2027 Plan Review with Brianna", 30 min), loaded with
  link.tindon.com/js/form_embed.js. GHL side: it opens on January 2027 with no slots that month and shows
  America/Chicago; both are calendar settings in GHL.
- Rework: v1 stacked headline over a person/calendar row, calendar top ~460px → moved calendar beside the headline.
  Emphasis line wrapped to 2 lines in a 470px column → 560px column, 56px H1, nowrap on desktop. Phone overflow came
  from the rail's nowrap time-zone label inside a `1fr` grid → `minmax(0,1fr)` and hide the label under 620px.
- **Booked thank-you (2026-10-30):** `booked.src.html` → `booked.html`, built from the webinar thanks page's shell.
  Seal + "You're all set, <first>. / *Brianna will see you soon.*", navy card (2027 Plan Review with Brianna, her
  headshot, When = "in your confirmation email", 30 minutes, With), reschedule = the link in their email, "Before your
  review" 3 items, office phone, disclosure. No CTA (conversion already happened). `?first_name=` personalises.
  Set the GHL calendar's redirect to this page after booking.
