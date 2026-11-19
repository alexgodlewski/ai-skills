---
name: Presell Audit Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Presell Audit Skill

Find out why your content gets views but not buyers. Paste your last posts or scripts and `/presell-audit` scores each one on three things: one single desire, the frustrations your buyer already tried, and the beliefs that stop them buying. It quotes the weak lines, rewrites them, and gives you 5 post ideas that pre-sell. Made for coaches and service businesses.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /presell-audit

Then paste your last 5 to 20 posts, scripts or captions, plus a few lines about your offer.

## What gets installed

- `~/.claude/skills/presell-audit/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/presell-audit/` (on Windows: `%USERPROFILE%\.claude\skills\presell-audit\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/presell-audit` and paste in their posts. If `/presell-audit` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/presell-audit/SKILL.md`

`````markdown
---
name: presell-audit
description: Checks a person's content for pre-selling. Scores each post, script or caption on three things: one single desire (does the content make the offer the best option right now and show why other paths are worse), frustrations (does it name what the buyer already tried that failed), and beliefs (does it break the beliefs that stop them buying or acting). Quotes the weak lines, rewrites them, and suggests 5 new post ideas that pre-sell. Made for coaches and service businesses. Use when someone types /presell-audit, or wants to know why their content gets views but not buyers.
---

# Presell Audit

Pre-selling means the buyer is already mostly sold before they ever see the offer. Content does that job when it does three things. This skill checks your content for all three, shows you the weak lines, rewrites them, and gives you 5 post ideas that pre-sell.

The three checks:

- **A. One single desire.** Does the content make your offer the best option right now, and show why the other ways to get the result are worse?
- **B. Frustrations.** Does it name what the buyer has already tried that did not work?
- **C. Beliefs.** Does it break the beliefs that stop them from buying or acting?

## 0. Start

You need two things from the person. Ask for both in one message and wait:

1. **Their content.** Their last 5 to 20 posts, reel scripts or captions, pasted in, or as a file (a text file, a document, or an export of their profile or captions). If they give a profile link and you have a browser tool, try to read their recent posts, and say plainly if you cannot see them. Do not guess what a post said. With fewer than 5 pieces, still do the audit, but say the sample is small.
2. **Their offer,** in a few lines: what they sell, who it is for, the price level, the result it gets, and how someone buys (call, link, DM). If they sell more than one thing, ask which one this content should sell.

Then write down, in a short block, the offer, the buyer, and the **one desire** the buyer wants most (the result, in the buyer's own words). Ask the person to confirm it before scoring. Everything is scored against that one desire.

## 1. Score each piece

Give each post three scores from 0 to 5, then a total out of 15. Read the post closely and use these anchors:

**A. One single desire (0 to 5)**
- 0: no clear desire, or several different ones.
- 2: one desire is clear, but nothing says why this offer, or why now.
- 4: it makes the offer the clear way to the desire and says why now.
- 5: also shows why the other paths are worse (doing it alone, free content, a cheaper option, another type of provider, waiting), with a real reason.

**B. Frustrations (0 to 5)**
- 0: no mention of what the buyer already tried.
- 2: general ("you are tired of struggling") with no named attempt.
- 4: names a specific thing they tried (a method, a tool, a person, a plan) and that it failed.
- 5: also says why it failed, in a way that points to the offer as the fix.

**C. Beliefs (0 to 5)**
- 0: no belief is touched.
- 2: a belief is named but not answered.
- 4: it names a belief that stops buying and answers it with logic or a story.
- 5: also gives proof (a real client result, a number, a before and after, a demo).

Common beliefs that stop coaching and service buyers: "it will not work for me", "I am not the type", "I do not have time", "I cannot afford it", "I should be able to do this myself", "I need to learn more first", "I will start later", "nothing has worked so far, so this will not either", "it only works for people with a big audience or a big budget".

A post can be good content and still score low. That is the point: views and trust are not the same as pre-selling. Do not give points for being entertaining.

## 2. Show your work

For each piece, give:

- the three scores and the total;
- **the weak lines:** quote them exactly (the person's own words, in quotation marks) and say in one sentence why each is weak;
- **a rewrite** of those lines in the person's own voice, keeping their words and tone where you can. Rewrite only the weak lines, not the whole post.

In rewrites, never make up results, client names, numbers, quotes or testimonials. Where proof is needed, leave a bracket the person fills in with something real, for example `[your real client result here]`. Do not add claims the person cannot back up.

## 3. The big picture

After all the pieces, show:

- a short table: each piece, its A, B, C and total;
- the averages for A, B and C, and which of the three is weakest overall;
- the pattern in plain words (for example: "Your posts name the desire well but almost never say why other options fail");
- the 3 weakest pieces and the 3 strongest, and what the strong ones do that the weak ones do not.

Say plainly that scores are a careful reading by an AI against the rubric above. They are not sales data. The real test is whether people reply, book or buy after seeing the content.

## 4. Five post ideas that pre-sell

Write 5 new post ideas that fix the weakest areas first. For each one:

- **Aim:** which of A, B or C it works on;
- **Hook:** the first line, in the person's voice;
- **Outline:** 3 to 5 short points;
- **Proof to add:** what real thing the person should bring (a client story, a number, a screenshot), left as a bracket if you do not have it;
- **Why it pre-sells:** one sentence.

At least one idea must show why the other paths are worse (A), at least one must name a failed attempt (B), and at least one must break a belief (C). Do not use hype words. Do not promise results.

## 5. Hand over

End with the one change that would help most this week, in one sentence.

## Rules

- Quote the person's real words. Never invent a post, a line, a result or a testimonial.
- Score only what is written in the content, not what the person probably meant.
- Say plainly when the sample is small.
- Plain words at a 6th grade level. No jargon unless you explain it in the same sentence.
- No hype and no promises about sales.
`````
