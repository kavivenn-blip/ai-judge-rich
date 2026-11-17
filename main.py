"""ai-judge-rich-01 entry (Python 3.13, standard library only).

Writes one fixed plan to /output/entry.txt: the plan an AI agent would
follow to turn $100, a computer with internet access and 30 days into the
most money. Deterministic: every run writes the same bytes, no network,
no randomness, no clock. The grader runs `python3 -P -s /bot/main.py`
twice; MAKEFUN_OUTPUT_DIR stands in for /output outside the grader.
"""

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

PLAN = "\n".join(
    [
        "Sell an AI phone receptionist to dental clinics: it answers calls 24/7 and books appointments in their calendar. $299 setup, $129 a month.",
        "Clinics miss 30-38% of calls; a new patient is worth about $850 on the first visit.",
        "Build one per clinic from its website: services, hours, address. Twilio takes calls, Vapi talks, Calendly books.",
        "Day 1: domain, Twilio, Vapi, Stripe payment link, template, then a first demo for a real clinic.",
        "Daily: build 3 demos, call 12 clinics. The front desk hears its own receptionist take a test booking. The demo is the pitch.",
        "Offer $299 setup plus $129 a month, 14-day money-back guarantee. A human answering service costs $300-500 a month.",
        "Math: 300 clinics, 50 hear the demo, 6 buy. 6 x $428 = $2,568 on day 30, plus $774 a month after.",
        "Budget: number $12, voice $18, domain $12, email $10, reserve $48. Edge: one niche, so the template gets faster each time, and recurring income while others sell one-off sites.",
    ]
)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "wb") as f:
        f.write(PLAN.encode("utf-8"))


if __name__ == "__main__":
    main()
