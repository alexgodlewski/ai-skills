---
name: Buyer Panel Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Buyer Panel Skill

Test your idea on 20 simulated buyers before you spend a dollar. Type `/buyer-panel` and your offer. A Board of 3 advisors pokes holes in the plan, a CFO works out your real margin and break-even from your numbers, and 20 simulated buyers each say buy or not buy and why. The buyers are simulated, so you test the winner on real people next.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /buyer-panel a $500 website audit for dentists

It asks for any number it is missing, such as your costs, and never makes one up.

## What gets installed

- `~/.claude/skills/buyer-panel/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/buyer-panel/` (on Windows: `%USERPROFILE%\.claude\skills\buyer-panel\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/buyer-panel` and their offer. If `/buyer-panel` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/buyer-panel/SKILL.md`

`````markdown
---
name: buyer-panel
description: Test a business idea, offer or price on 20 simulated buyers before spending any money. A Board of 3 advisors pokes holes in the plan, a CFO works out the real margin and break-even from your numbers, and a Buyer Panel of 20 made-up customers each says buy or not buy and why. Use when someone types /buyer-panel with an offer, or asks if an idea will sell, if a price is right, or whether to launch something.
---

# Buyer Panel

Most people find out an offer does not sell after they pay for it. This skill finds out first. It has three parts: a Board that pokes holes in the plan, a CFO that checks the math, and a Panel of 20 simulated buyers that react to the offer.

Be honest with the person from the start: the buyers are made up by an AI. They show you likely objections and weak spots. They do not prove anyone will pay. The last step is always to test with real people.

## 1. Get the offer

The offer is what the person typed after `/buyer-panel`. Write it down in this short block, and ask for anything missing in one message:

- **What is sold** and what the customer gets
- **Price** (and how it is paid: once, monthly, in parts)
- **Who it is for** (the target customer, as exactly as they can say it)
- **How it is delivered** and how long it takes
- **Costs per sale**: time, tools, materials, fees, ads. This is for the CFO.

Never invent a number. If a price, a cost or a goal is missing, ask. If the person does not know a cost, write "not given" and let the CFO show the result for a range, labeled as a range.

## 2. The Board (3 advisors)

Three advisors read the plan. Each one speaks in first person, in two to four short sentences, and must name one specific hole in this exact plan, not general advice.

- **The Skeptic:** Why would this not work? What does the customer already believe that goes against it?
- **The Competitor:** Who already sells this, or something close, and why would a buyer pick them?
- **The Operator:** What breaks when you try to deliver it? Time, tools, results you cannot control.

End with one line: **The biggest risk:** (one sentence).

## 3. The CFO

Use only the numbers the person gave. Show the work in a small table.

- Price per sale
- Cost per sale (each item, then the total)
- **Margin per sale** in money and in percent
- **Break-even:** how many sales cover any fixed or upfront cost the person gave (if none was given, say so and show only the margin)
- What is **not counted** (taxes, refunds, ads, the person's own time if it was not given)

State every assumption in a line that starts with "Assumed:". Check the math twice. Then give a one-line verdict that says whether the numbers work, for example "The numbers work: 80% margin, 1 sale covers the tools."

## 4. The Buyer Panel (20 buyers)

Make 20 simulated buyers who fit the target customer. They must differ from each other, and they must not all like the offer. Real buyers are mixed, so include people who are ready, people who are unsure, and people who are clearly the wrong fit.

Each buyer has:

- **A first name and last initial**
- **Age and income** (a realistic range for the target customer)
- **Habits:** how they spend money and time, and how they usually decide
- **Current situation:** what is going on in their life or business right now
- **Doubts:** what worries them about this offer
- **Verdict:** **BUY** or **NOT BUY**, plus one sentence on why, in their own voice

Rules for the panel:

- Decide each verdict from the person's situation and the offer as written. Do not aim for a result. Do not round the vote up to make the offer look good or down to make it look bad.
- Do not use the same reason twice. If two buyers say the same thing, change one of them to fit a different situation.
- A buyer who has the budget but no trust says NOT BUY. A buyer who likes it but cannot pay says NOT BUY.
- Show the 20 as a numbered list, one buyer per entry, short.

After the 20, give:

- **Tally:** X of 20 would buy.
- **Top 3 objections,** each with how many buyers raised it.
- **Who bought:** one line on what the buyers had in common.

## 5. The verdict

Finish with a short summary:

1. The Board's biggest risk
2. The CFO's verdict
3. The Panel's tally and top objection
4. **One change to test first:** the one edit to the offer that would answer the top objection.

Then say this, in these words or close to them: "These buyers are simulated. They are good for finding weak spots, not for proving demand. Test the winner on real people next: show the offer to 10 real buyers, or ask for a small deposit, before you spend money."

## Rules

- Plain words, short sentences, written for a smart 12 year old.
- No dashes used as punctuation, no hype words.
- Never invent the person's numbers. Ask.
- Never promise a result. The panel is a test, not a forecast.
- Save the full run in a file if the person asks.
`````
