---
name: Lead Heat Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Lead Heat Skill

Some leads are ready to buy, some are just looking. Paste your DM chats and Claude scores how warm and how good a fit each lead is, sorts them into hot, warm, cold or wrong fit, and writes the next message to send. Booked calls also get a 5-line brief for your closer.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /lead-heat a $3,000 12-week coaching program for new gym owners

Claude asks once for your price and your ideal client, then you paste your DM chats. It scores each lead, sorts them and writes the next message for each.

## What gets installed

- `~/.claude/skills/lead-heat/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/lead-heat/` (on Windows: `%USERPROFILE%\.claude\skills\lead-heat\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/lead-heat` and their offer, then paste their DM chats. If `/lead-heat` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/lead-heat/SKILL.md`

`````markdown
---
name: lead-heat
description: Reads DM chats or booked-call answers, scores each lead on how warm they are and how good a fit they are, sorts them into hot, warm, cold or wrong fit, and writes the next message to send. Hot leads get a booking message, warm leads get one question, cold leads get one helpful nudge, wrong-fit leads get a kind no. Booked leads also get a 5-line brief for the closer. Made for coaches, consultants and service owners who book sales calls from Instagram DMs. Use when someone types /lead-heat, or asks which leads are ready to buy, who to follow up with, what to reply to a lead, or how to prep a closer for a call.
---

# Lead Heat

Some leads are ready to buy and some are only looking. They need different messages. This skill reads each chat, says which kind of lead it is and why, and writes the next message to send.

Two things get scored separately, because they are not the same:

- **Heat:** how interested the person is right now.
- **Fit:** whether they can and should buy from you.

A short, quiet reply lowers Heat. It does not lower Fit. Never write off a good-fit person just because they type little.

## 1. Ask once

Ask for all of this in ONE message, then wait:

- **Your offer:** what you sell and the result it gets.
- **Price:** and how it is paid.
- **Your ideal client:** who gets the best result, and who you do not want. Ask for 2 or 3 "not a fit" signs.
- **How people book:** a booking link, or a call by hand.
- **A sample of how you write** (optional, 3 to 5 messages). If given, match it.

Never guess these. If the person skips the price or the ideal client, ask again, because Fit cannot be scored without them.

## 2. Get the leads

Ask the person to paste one or more DM chats, or a booked lead's form answers. Say they can paste many at once, with a name or label above each. Score only what is written. If something is not in the chat, write "not shown", never fill the gap.

## 3. The scoring table

Explain this table to the person in a few lines before the first lead.

**Heat (0 to 8)**

| Signal | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Pain, in their own words | none | vague ("I want more clients") | clear problem | clear problem plus what it costs them |
| Urgency | none or "someday" | "this year" | a near goal or deadline | a reason they must fix it now |
| Knows you (max 2) | no idea who you are | saw one post | watched or read a lot, or asked to work with you | not used |

Add one point only if they asked a buying question (price, how it works, next step). Heat is 8 at most.

**Fit (0 to 8)**

| Signal | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Budget signs | says they cannot pay | not shown | pays for similar things or hints at money | names a budget or invests already |
| Who decides | someone else, not in the chat | not shown | shares the choice | they decide |
| Match to your ideal client | clearly not | partly | mostly | exactly |

Budget and Match go up to 3, Who decides up to 2. Fit is 8 at most.

**Red flags** take 1 to 3 points off Fit. Examples: wants a result with no work, wants a free version of the whole thing, argues about every point, is rude, only asks about the lowest price, expects a result you cannot honestly promise, or hits one of your "not a fit" signs. A hard red flag (an "I do not want clients like this" sign from step 1) makes the lead wrong fit at any score.

If a signal is "not shown", score it 1 and say so. Do not score it 0.

## 4. Sort each lead

- **HOT:** Heat 6 or more and Fit 5 or more.
- **WARM:** Heat 3 to 5 and Fit 4 or more, or Heat 6 or more with Fit 4.
- **COLD:** Heat 0 to 2 and Fit 4 or more. Quiet, but could still be a good client.
- **WRONG FIT:** Fit 3 or less, or a hard red flag, at any Heat.

Show a table at the top: name, Heat, Fit, group, and the one line that decided it, quoting their own words.

## 5. Write the next message

One message per lead, in the person's voice. Never invent a result, number, client or deadline. Never use fake urgency or fake scarcity.

- **HOT, booking message:** answer their last question first. Say what the call is for in one line. Then ask a small yes: "Want me to send my calendar link?" Send the link only after they say yes. Add [your booking link] as the slot.
- **WARM, one question:** ask the one thing that moves them forward, and make it about helping them, not about checking if they can pay. For example, what is driving this right now, or what they already tried. Only one question.
- **COLD, one helpful nudge:** give something useful tied to what they said: a short tip, a post, a case you really have, or a free resource. Do not write "just following up" or "still interested?". End with an easy choice, never a push.
- **WRONG FIT, a kind no:** thank them, say honestly this is not the right match right now, and point to something that may help (a free resource, a cheaper option, or "come back when X"). No guilt, no door slam.

Rules for every message: short sentences, 6th grade words, no em dashes or en dashes, no hype words, no emojis unless the person uses them. Under 60 words.

## 6. Pre-call brief for booked leads

If a lead has booked, add exactly 5 lines for the closer:

1. **Who:** name, what they do, how they found you.
2. **Pain:** their problem, in their words.
3. **Why now:** what made them book today.
4. **Money and decider:** what is known, and what is "not shown".
5. **Watch for:** the biggest doubt or red flag, plus the first question to ask.

## What to do now

1. Send the hot leads their booking message today, before the others.
2. Send warm and cold messages within a day. Interest drops fast when no one answers.
3. Send the kind no to wrong-fit leads, so your calendar stays clear for good ones.
4. Give the closer the 5-line brief before each call.
5. Re-run this skill on any lead who replies.

**What to measure:** the show rate on booked calls, and how many hot leads you booked, before and after you use this for two weeks.

## Rules

- Score only what is on the page. Never invent facts about a lead or the offer.
- Heat and Fit stay separate. Quiet is not unqualified.
- Plain English. No dashes as punctuation, no hype, no promises about sales.
- Say plainly that scores are a careful AI reading, not a prediction. The person knows their market best and can overrule any call.
`````
