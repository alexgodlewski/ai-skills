---
name: Revive Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Revive Skill

Don't send "just following up". Paste the chat where a lead went quiet, and Claude works out where they stopped and why. Then it writes 2 or 3 messages in your voice, tells you when to send each, and gives you a short follow-up plan with a clear point to stop.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /revive

Then paste the DM chat with the lead who went quiet, for example after you sent the price 4 days ago. You get the stage, the likely reason, 2 or 3 messages with send times, and a 3 to 5 touch plan.

## What gets installed

- `~/.claude/skills/revive/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/revive/` (on Windows: `%USERPROFILE%\.claude\skills\revive\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/revive` and paste the chat with the lead who went quiet. If `/revive` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/revive/SKILL.md`

`````markdown
---
name: revive
description: Writes the next message to a lead who went quiet. The person pastes the chat (or describes it). Claude works out the stage where the lead stopped (after the first DM, after a price or link, after booking but before the call, after a no-show, or after the call with "I need to think about it"), guesses why, writes 2 or 3 message options in the person's own voice, says when to send each, and gives a short follow-up plan with when to stop. Made for coaches, consultants and service businesses that sell through DMs and booked calls. Use when someone types /revive, or asks what to say to a lead who ghosted, how to follow up without being annoying, or how to stop "just following up" messages.
---

# Revive

A lead who goes quiet is rarely a "no". Most of the time, life got busy, the interest cooled, or one small doubt was never answered. A message like "just checking in" gives them nothing, so they ignore it. This skill finds out why the lead went quiet and writes the next message so that it is easy and worth answering.

## 0. Rules for every message

- Send it only in the channel where this lead already talks to the person (the same DM thread, the same email, the same text). Never find the lead on another app or number to chase them.
- Only follow up with people who asked for info, booked, applied or spoke to the person. Never message a cold list this way.
- No guilt, no pressure, no fake deadline, no "this is your last chance" unless it is true. Never make the lead feel bad for being quiet.
- Give the lead something: an answer, a useful asset, a simple question, or an easy way out.
- Always leave a polite way to say no. A clear "no" is a good result.

## 1. Get the facts

Ask for these in ONE message, then wait:

1. **The chat.** Paste it, or describe it: who spoke last, what was said, how many days ago.
2. **The offer:** what is sold, who it is for, the price level, and what the lead gets.
3. **Where the lead came from** (a Reel, a comment, an ad, a referral) and where they talk to the person (Instagram DM, text, email).
4. **How they book:** the calendar link or the way a call is set.
5. **The person's voice:** a few real messages they wrote, if they have them. Match their words, their length and their emoji habits.
6. **What they can send as help:** a short video, a guide, a case study, an FAQ, a result from a real client. If they have none, say so and do not make any up.

Never invent facts, results, client names or numbers. If the message needs proof the person did not give, leave a slot like `[your client's result here]` and tell them what to put there.

## 2. Find the stage and the reason

Pick ONE stage and say it in a line:

- **A. Quiet after the first DM.** They never answered, or gave a one word reply.
- **B. Quiet after a price or a link.** They saw it and said nothing.
- **C. Booked, quiet before the call.** Risk of a no-show.
- **D. No-show.** They booked and did not come.
- **E. After the call: "I need to think about it."**

Then give the most likely reason, as a guess, in one or two lines. Use the chat to support it. Common reasons:

- **Interest cooled.** They were curious, then life took over (A, C, D).
- **Unsure it is for them.** They doubt it will work for their case (B, E).
- **Price or risk.** They did not say it out loud (B, E).
- **Friction.** The link was hard, the time did not fit, the question was too big (B, C).
- **Wrong timing.** A real reason that may be true (all stages).
- **Not a fit.** They are not the right buyer (any stage).

Say plainly that this is a guess. If the chat does not give enough clues, ask one short question before writing.

## 3. Write 2 or 3 options

Write the options for that stage, each a different angle. Label each one, add a line on **when to send it**, and keep it short enough to read in one screen. Use this menu of angles:

- **A (after first DM):** a useful tip for their exact situation, then a small question; or two things you could send them to pick from; or ask permission to share how others get the result.
- **B (after price or link):** answer the most likely doubt in two lines, then ask if that was the missing piece; or offer a smaller first step; or ask if the timing is wrong and offer to check back on a date they choose.
- **C (before the call):** a short, personal note that says what the call is for and what to bring; or a quick question about their goal so the call is useful to them; or an easy way to reschedule.
- **D (after a no-show):** no blame. Say it happens, offer one new time, and make it easy to pick; or a short voice or video note; or a clear "if now is not good, tell me and I will close this out".
- **E (after the call):** name the one thing they said they were weighing, send something that answers it, and ask what would help them decide; or ask a simple "what is the main thing holding you back?"; or set a date to talk again.

Each message:

- uses short sentences and plain words (6th grade level);
- sounds like a person typing to a person, not a template;
- has one clear ask, and makes the next step tiny (a one word answer is fine);
- has no hype words and no dashes used as punctuation;
- uses the lead's first name and one detail from the chat so it cannot be copied to someone else.

Never write "just following up", "circling back", "touching base", "are you still interested" or "I have 15 minutes free". These are about the sender, not the lead.

## 4. The follow-up plan

Give a short plan in a small table: touch number, how many days after the last message, what it is (a different angle each time), and the channel.

- Use **3 to 5 touches** in total for one quiet lead, spaced about 2 to 4 days apart at first, then wider.
- Each touch must add something new: an answer, an asset, a question, a story the person can really back up. Never repeat the same message.
- If the lead answers at any point, stop the plan and reply to what they said.
- If the lead says no or not now, thank them, ask when to check back if they want, and do exactly that.
- **When to stop:** after the last touch, send one short closing message that leaves the door open, then stop. Do not message again unless they reply.

## 5. Check before sending

Run this list on each message and fix any fail:

1. Does it give the lead something, not just ask for something?
2. Could the lead answer in under 10 seconds?
3. Is it free of guilt, pressure and made up urgency?
4. Is it in the channel where they already talk?
5. Does it sound like the person wrote it?

## What to do now

1. Pick the message you like best and send it at the time Claude gave.
2. Put the next touches in your calendar or CRM, with the dates from the plan.
3. Save the lead's real reason (price, trust, timing) in your notes, and look for the pattern across leads.
4. Run `/revive` on every quiet chat from the last 30 days, oldest first.
5. When a lead replies, answer first and stop the plan.

**Measure:** the reply rate on your follow-ups, and the show rate on booked calls, for two weeks before and two weeks after.
`````
