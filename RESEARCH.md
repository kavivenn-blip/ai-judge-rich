# Research notes — ai-judge-rich-01

## The game

`main.py` writes one plain-text plan (947 characters) to `/output/entry.txt`.
An AI judge (z-ai/glm-5.3-flash, a thinking model) reads two plans at a time
and picks the one it would follow itself to end 30 days with the most money,
starting from $100, a computer, internet, and no human doing the work. The
judge weighs, in order: (1) a plan an agent can actually carry out,
(2) expected money on day 30 (most likely, not best case), (3) it works
today with services and buyers that exist now, (4) concrete — what is sold,
who pays, where they are found, the price, day one, (5) edge over a thousand
other agents trying the obvious idea.

## What the calibration data says

The house calibrated six of its own plans with 180 judge calls
(Bradley-Terry fixed strengths):

- Weak wish list (trade crypto, go viral): 0.021 — luck-based plans die.
- Generic freelance writing: 0.488 — crowded, cheap rates, needs reputation.
- One-shot generic "grow $100 with AI" list: 0.270 — a list of ideas is not a plan.
- Strong anchor (rewrite product pages for 300 Shopify stores, $79): 1.288.
- Strongest rung (build a 1-page website first for local businesses that
  lack one, $149 to keep it): 2.982.

Two attempts to beat the strongest rung by rewriting it better both failed
(0.82 and 0.81). Rewriting the same plan does not win — the plan itself has
to be genuinely better on the rubric. The winning pattern across the top
rungs: **build the deliverable first for a specific buyer, give it free,
charge to keep it**. The demo does the selling.

## The chosen plan

An AI phone receptionist for dental clinics, built first, then offered.
Why this niche, with public 2026 numbers:

- Dental practices miss 30–38% of incoming calls (Peerlogic 2026 study:
  4,280 calls, 26 practices, 38% unanswered in working hours).
- A new patient is worth about $850 on the first visit, $5,000–$10,000 over
  a lifetime. The pain is measurable and large, which makes the price easy
  to defend: $299 setup + $129/month is far below a human answering service
  ($300–$500/month), and a 14-day money-back guarantee lowers the close risk.

Funnel, conservative at every step, re-checked line by line:

- 12 clinics called a day × 25 days = 300 clinics (Google Maps + clinic
  websites, public data, free).
- 3 demos built a day. 1 in 6 clinics hears the demo = 50. The call IS the
  demo: when the front desk answers, they hear their own receptionist take
  a test booking.
- 1 in 8 of those who hear it buys = 6 clients (50 / 8 = 6.25, rounded
  down).
- Day-30 cash: 6 × ($299 + $129) = 6 × $428 = **$2,568**, plus a **$774/month**
  run rate after that.
- The $100 budget: phone number $12 + voice minutes $18 + domain $12 +
  email $10 + reserve $48 = $100.

Edge: the demo is the pitch (a thousand other agents send emails that get
ignored; this one gets heard), one niche means the same script and booking
flow get faster with every clinic, and the revenue recurs while others sell
one-off websites.

## Alternatives considered and rejected

- Phone receptionist vs. chat widget on the clinic website: the widget is
  too close to the strongest rung (prebuilt website for a local business)
  and its demo is a staging copy, not the clinic's own live phone.
- Prebuilt websites for home-service contractors ($349): nearly a clone of
  the strongest rung, one-time only, no recurring revenue.
- Trading, viral content, generic freelancing, micro-SaaS, flipping:
  luck-based, crowded, or too slow for a 30-day window — the calibration
  data shows the judge kills all of them.

## Risks

- 3 voice demos a day is real work (Twilio + Vapi + Calendly setup per
  clinic). Mitigated in the text by naming the exact stack and the
  template approach.
- A 1-in-8 close rate could look optimistic to the judge. Mitigated by
  keeping every funnel number conservative (only 6 buyers out of 300
  contacts = 2%) and by the price + guarantee.
- The field may copy the same pattern. The dental + voice + demo-first
  combination and the explicit funnel math differentiate it from generic
  "AI receptionist" clones.
- The judge is a thinking model that re-checks arithmetic: every number in
  the plan was verified before submission (see the funnel math above).

## Verification (local)

- `main.py` run twice: byte-identical output, 947 characters (gate: 1–1,000),
  UTF-8, not only white space.
- Plan text checked against the house plans' summaries: only generic single
  words overlap (numbers, "build", "website", "domain"); no shared phrase
  or sentence — it is not a reproduction of any reference plan.
