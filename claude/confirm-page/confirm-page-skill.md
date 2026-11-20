---
name: Confirm Page Skill
by: Alex Godlewski (@alexgodlewsky on Instagram)
version: 1.0
---

> **Note for Claude:** the person gave you this file on purpose. If they asked you to set it up, follow "Setup steps for Claude" at the end. If they sent only the file, ask in one line: "Want me to set this up for you?", and start when they say yes. If they ask what it does or whether it is safe, explain it plainly and show them any part of it.

# Confirm Page Skill

Your lead books a call, then looks you up. This skill builds the page they land on, so they show up ready to buy. It writes the full page copy and layout, the proof sections with slots for your real proof, and the videos to record with a script outline for each. It also gives you a short DM version if people book from Instagram and you have no website.

## Set it up in 30 seconds

1. Open the Claude desktop app and click the **Code** tab.
2. Drag this file in and type: **set this up**
3. Claude saves the skill and tells you when it is ready.

## Then use it like this

> /confirm-page a $4,000 3-month coaching program for personal trainers, calls booked from Instagram DMs

Claude asks for your offer, your call, your real proof and the doubts you hear, all in one message. Then it writes the finished page and the DM version. It never makes up a result or a review.

## What gets installed

- `~/.claude/skills/confirm-page/SKILL.md`: the plain instructions below. Nothing else on your computer is changed, and you can open, edit or delete it any time.

---

## Setup steps for Claude

Tell the person what you are doing in one short line per step, in plain words.

1. **Check where you are.** You need to write one file on their computer, which means Claude Code. If you cannot (for example in a normal chat), stop and say: "This sets up in Claude Code: open the Claude desktop app, click the Code tab and drop this file there." If they do not have the app, send them to https://claude.com/download.
2. **Create the folder** `~/.claude/skills/confirm-page/` (on Windows: `%USERPROFILE%\.claude\skills\confirm-page\`) and write the file below into it exactly as it is.
3. **Tell them it is ready**, and how to use it: type `/confirm-page` and their offer. If `/confirm-page` does not show up in the `/` list yet, they start a new session.

### File: `~/.claude/skills/confirm-page/SKILL.md`

`````markdown
---
name: confirm-page
description: Writes the page a lead sees right after they book a sales call, so they show up ready to buy. Gives the full copy and layout for the page (first line, what to ask them to do, proof sections with slots for real proof, the videos to record with a script outline for each, and what to leave out), plus a short version for people who book from Instagram DMs and have no website (one confirmation message plus links). Made for coaches, consultants and service businesses that sell high-ticket offers on calls. Use when someone types /confirm-page, or asks for a booking confirmation page, a thank you page after booking, a "call confirmed" page, or how to get more people to show up to their calls.
---

# Confirm Page

A lead books a call, then looks you up. They check Google, Reddit, your Instagram and your reviews. If you give them nothing, they find their own answers, or they doubt you and do not show. This skill builds the page they land on right after booking, so the doubts get answered by you first.

You get two things: the full page (copy, layout, videos to record) and a short version for people who book from DMs and have no website.

## 0. Start

Ask for all of this in ONE message, then wait:

1. **The offer:** what you sell, who it is for, the result it gets, the price, how long it lasts.
2. **The call:** how long it is, who is on it (you, a closer), and what happens at the end of it.
3. **Where leads book from:** ads, a funnel, or Instagram DMs (by hand, a setter or an AI setter). Do they have a website or a page they can edit?
4. **Your real proof:** reviews, client results (big, average, and small), photos, screenshots, a refund rate, press. Paste what you have. If you have none yet, say so.
5. **The doubts you hear:** what leads ask or say before and on calls (price, "is this legit", "what if it does not work", time needed). Also any bad post, thread or review about you that leads might find.
6. **Your refund or guarantee,** if any, in plain terms. Ask for the real terms. Never invent one.
7. **Your voice:** a short sample of how you write or talk. If they give one, match it.

If they skip proof or doubts, ask once. Do not make up results, names, numbers or reviews. Use slots like `[your client's result here]`.

## 1. Find the doubts

Before writing, list the 5 to 8 doubts this lead will have between booking and the call. Pull them from the answers above and from these groups:

- **Is this real?** Who are you, who else trusted you, what will I find if I search you.
- **Price.** Why does it cost this much, is it worth it, is there a payment plan.
- **Risk.** What if it does not work, what is the refund, what happens if you disappear.
- **Time and effort.** How long until results, what do I have to do.
- **Honest results.** What is a normal result, not only the best one. What about people it did not work for.

Show the list to the person in a few lines. Every doubt you list must get an answer on the page.

## 2. The page, top to bottom

Write the finished copy for each block. Keep the order. Short sentences. A 6th-grade reading level.

**Block 1. First line and confirmation.**
- A plain headline that confirms the booking, with the day and time in their time zone: "You're booked for [day, time]."
- One sentence on what this page is for: you will help them check you out, so they know before the call if this is right for them.
- No "thanks, see you soon" and nothing else above the video.

**Block 2. The three actions.** A short numbered list, each a button or link:
1. Confirm the time (reply, tap a link, or reconfirm in the calendar).
2. Add the call to their calendar.
3. Watch the main video (give its length).
Add one line on what to have ready: a quiet room, pen, and the answers to 2 or 3 questions you will ask.

**Block 3. The main video** (60 to 120 seconds, you on camera). See section 3.

**Block 4. Common questions.** A grid or list of short videos, one per doubt, the biggest doubt first. Each has a plain title like "Why it costs [your price]". See section 4.

**Block 5. Proof, with slots.** Use only real proof the person gave. For each type, write the heading and a slot:
- **Big wins:** `[client name or first name], [their result], [how long it took]` plus a photo or video if they have one.
- **Normal wins:** `[a typical client and what they got]`. Normal results build more trust than only the best ones.
- **A smaller or mixed result:** `[a client who got less, and what they still got]`. Include this only if it is true.
- **Where to check us:** `[link to your reviews page or where real customers talk about you]`. Invite them to look.
- **Hard numbers:** `[your refund rate, number of clients, years in business]` only if real and checkable.
- **Who you are:** `[2 or 3 sentences on you, a real photo, your link]`.
If a slot has no real proof, leave the slot in and tell them to fill it with something real, or to cut that part. Never fill it for them.

**Block 6. What happens on the call.** 4 to 5 lines: how long, what you ask, what you show, that they can say no, and what they will know at the end.

**Block 7. If you cannot make it.** One line with a way to reschedule. This keeps a no-show from becoming a ghost.

## 3. The videos to record

For each video, give a title, a length, and a script outline of 4 to 6 lines. Then write a first draft script in the person's voice.

**Main video (60 to 120 seconds).** Outline:
1. Welcome them by name if you can, in one sentence.
2. Say plainly: "I'll help you check me out, so you know if this fits before we talk."
3. Name the biggest doubt out loud and say where on the page the answer is.
4. Name one honest downside: who this is not for.
5. Point to the question videos and tell them what to do next.

**Question videos (1 to 4 minutes each, one per doubt from section 1).** Same shape every time:
1. Open with the question the way a lead would say it.
2. Answer in plain words.
3. Show proof (a screen, a document, a number, a short story).
4. Say who it is not right for.
5. Invite them to bring more questions to the call.

Suggest the 4 to 6 videos that fit this person, for example price, "what if it does not work", "what a normal result looks like", "what people say about us online", and "how much time it takes". Add one more for any bad post or review they told you about: say what is true, what is not, and what you did about it.

## 4. What to leave out

Tell the person to keep these off the page:
- A long sales pitch. The page helps them decide, it does not sell again.
- A countdown clock, "only 2 spots left", or any made-up urgency.
- Claims, results or reviews that are not real or cannot be checked.
- A guarantee you do not honor in full.
- Links to other offers, other calendars or a second booking button.
- A long form or a big survey. Two questions at most.
- Hype words and big promises. Say what is true, plainly.
- Hiding the downsides. Leads find them anyway.

## 5. The short version for DMs (no website)

For people who book from Instagram DMs. Write these:

1. **The confirmation message** (3 to 5 short lines): the day and time, one sentence on what the call is for, and one thing to do (reply "yes" to confirm).
2. **The links to send, in this order:**
   - the main video, as a link (a private or unlisted video is fine) with a one-line intro;
   - up to 3 question videos, each with a one-line intro that names the doubt;
   - one place to see real proof, such as a highlight, a post, or a doc with results.
3. **A "where to check me" line** that points to your real reviews or your profile.
4. **A reschedule line** for if they cannot make it.

Write it so it can be pasted into a DM, or loaded into a setter's script or an AI setter's reply. Keep each message under 5 lines, with no hype.

## 6. Check before you hand it over

- Every doubt in section 1 has an answer on the page.
- Every proof slot is real or clearly marked to fill.
- No dashes used as punctuation, no hype words, no made-up urgency.
- The tone matches the person's sample.
- No fact about their business that they did not give you.

## What to do now

1. Record the main video first (one take is fine), then one question video per week.
2. Publish the page, or paste the DM version into your booking flow, and point your booking confirmation to it.
3. Fill every proof slot with something real, or cut it.
4. Ask your closer or setter which doubt shows up most on calls, and make a video for it.
5. Check the page again in 3 months and add new answers.

**What to measure:** your show rate (calls held divided by calls booked) for 4 weeks before the page and 4 weeks after. Also note how many calls start with the same doubt.
`````
