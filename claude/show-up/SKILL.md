---
name: show-up
description: Builds the reminder sequence that goes out between a booked call and the call itself, so more people actually show up. Works out which message goes out when (right after booking, the day before, the morning of, 1 hour before, 5 minutes before) based on how far ahead the call was booked, then writes every message in full in the person's own voice, for email, Instagram DM and SMS (SMS only for people who opted in). Each message is short, does one job, gives a reason to show up and an easy way to reschedule. Ends with how to set it up in a calendar app or email tool. Use when someone types /show-up, or says people book calls and then do not come, or asks for call reminders, no-show messages or a way to raise their show rate.
---

# Show Up

Booking a call is a small yes. Between the booking and the call, life gets in the way and the person forgets why they booked. This skill fills that gap with a short sequence of messages. Each one is easy to read, has one job, and makes showing up the easy choice.

It covers the time from booking to the call only. It does not write the confirmation page, and it does not write messages for people who went quiet before booking.

## 1. Get the inputs

Ask for everything in ONE message, then wait:

- **The offer:** what the call is for, who it is for, and what the person gets out of the call itself (a plan, a review, an answer, a decision).
- **Who is on the call:** the name of the person who will talk to them.
- **Booking lead time:** how far ahead calls are usually booked (same day, next day, 3 or more days out, or a mix).
- **Call link or calendar link,** and the reschedule link if there is one. If there is none, ask what they want people to do (reply with a new time).
- **Call length** and how it happens (video call, phone, in person).
- **Channels they use:** email, Instagram DM, SMS. For SMS, ask: did these people clearly agree to get texts? If the answer is no or not sure, do not write SMS.
- **A sample of their writing:** 3 to 5 messages or captions they wrote. If they give none, ask for one. Without a sample, write plain and friendly and say so.
- **Proof they can share:** one real client result, review, FAQ page or short video that helps a nervous person. If none, leave it out. Do not make one up.

Never invent a result, a name, a number or a review. If a slot is empty, write it as `[your client's result here]` and tell them what to put there.

## 2. Build the matrix

Show the plan as a table before any copy. One row per message: when, channel, and its one job.

The five points in time:

1. **Right after booking:** confirm and remind them why they booked.
2. **The day before.**
3. **The morning of the call.**
4. **1 hour before.**
5. **5 minutes before.**

Use the lead time to pick the rows:

- **Same day (booked a few hours ahead):** send message 1 at once. Add the 1 hour message only if there is more than an hour left. Always send the 5 minute message.
- **Next day:** messages 1, 3, 4 and 5. The day before is the booking itself, so skip it.
- **3 or more days out:** all five. Add one extra message about 2 days after booking, built around a reason to show up (see section 3, message 1b).
- **Mixed lead times:** give all three plans in one table and say which one to use for which booking.

Rules for the table:

- Use the lead's time zone, not the sender's. Every message that names a time says the time zone.
- Mark which channel each message uses. Email carries the longer ones. DM and SMS carry the 1 hour and 5 minute ones.
- Two messages in one channel should never land within a few minutes of each other.
- Never put more than one message in a channel within 1 hour unless it is the 5 minute one.

## 3. Write every message in full

Write each message ready to paste, with slots like `[first name]`, `[time and time zone]`, `[call link]`. Email gets a subject line (under 8 words, lowercase, no tricks) and a body. DM and SMS get the body only.

Every message follows the same four rules:

- **One job.** Confirm, remind, give a reason, or send the link. Not all four.
- **A reason to show up.** Say what they will get on the call, in the person's words. Use only what the person gave you in section 1.
- **An easy way out that is not a ghost.** One line that gives the reschedule link, or says "reply with a better time." Make it as easy as showing up.
- **No pressure tricks.** No fake spots left, no fake deadlines, no guilt. A real fact is fine, such as "I hold this hour for you."

Write these messages:

- **1. Right after booking (email, plus DM if that is how they booked).** Confirm the time with the time zone. Remind them what they asked for and why they booked, using their own answers if you have them. Add the call link and the reschedule link.
- **1b. About 2 days after booking (only for 3 or more days out).** One reason to show up. Share the one real proof item from section 1, or one question to think about before the call. If no proof was given, send the question.
- **2. The day before (email).** Short. Say what the call will cover, what to have ready (one or two items), and the link.
- **3. The morning of (email or DM).** One line on the time, one line on what they leave with, the link.
- **4. 1 hour before (DM, or SMS if opted in).** Two short lines. Time and link.
- **5. 5 minutes before (DM, or SMS if opted in).** One line. The link and "I'm here."

If they use SMS, each text must say who it is from, and the first one must give a simple way to stop ("reply STOP to opt out"). Never write a text for a person who did not agree to texts. Never plan a call or voicemail to anyone who did not agree to it.

Also write two short extras:

- **If they reply "can't make it":** a reply that offers two new times or the reschedule link, with no guilt.
- **If they do not show:** one short message sent within 15 minutes after the start time. It says you saw they could not make it and offers to rebook. One message, no chasing. If they stay quiet, stop and hand them to the person's follow-up for quiet leads.

## 4. Check the voice

Before showing the person, go through every message:

- Short sentences, simple words, 6th grade reading level.
- No em dashes and no en dashes. Use a period or a comma.
- No hype words, no all caps, no stacked emojis.
- Matches their sample: same greeting, same sign-off, same level of casual.
- Read it as the lead would on a phone. If it needs scrolling, cut it.

## 5. How to set it up

Explain this in general terms. Tool menus change, so name the idea, not the exact setting, and tell them to check their tool's help page if a name differs.

- **Calendar app:** most booking tools can send a confirmation and timed reminders. Paste messages 1 and 4 into them and set the offsets (for example "1 hour before"). Turn their default reminder off if it duplicates yours.
- **Email tool or CRM:** build one automation that starts when a call is booked. Add a wait step before each message, counted back from the call time. Use the lead's time zone, a merge field for first name and the call link.
- **Stop rules:** the automation must stop when the person cancels, reschedules (restart it with the new time), or joins the call.
- **Instagram DM:** if a setter or an AI setter handles DMs, give them messages 3 to 5 as the script. If you do it by hand, put the times in your calendar. Only message people who have talked to you, and follow the platform's current messaging rules.
- **SMS:** only for people who agreed. Keep the opt-out line. Respect quiet hours in their time zone.
- **Test it:** book a call for yourself on a Friday and check that every message arrives at the right time with the right link.

## What to do now

1. Paste the messages into your booking tool or email tool, and set the timing from the matrix.
2. Fill every `[slot]`, especially the proof slot. Delete a slot you cannot fill with something real.
3. Book a test call and check each message and link on your own phone.
4. Turn on the stop rules so cancelled or rescheduled calls do not get the wrong reminders.
5. Run it for 2 weeks, then read the numbers.

**What to measure:** your show rate before and after (people who joined the call divided by people who booked), and how many people used the reschedule link instead of vanishing.
