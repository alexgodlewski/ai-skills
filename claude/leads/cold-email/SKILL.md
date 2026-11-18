---
name: cold-email
description: Write cold emails in the person's own voice. Learns the voice from 2 or 3 emails or messages they wrote, then writes short first emails and follow-ups for a lead using real facts about that lead. Use when the person asks for a cold email, an outreach email, a follow-up, or when the leads skill needs emails written.
---

# Cold Email

You write the first email to a stranger so that it sounds like the person wrote it, and so that the reader can answer in one line.

## 1. Learn the voice (once)

Ask for 2 or 3 samples: emails, DMs or posts the person wrote themselves. Real ones, not polished ones. If they have none, ask them to write 3 sentences about what they do as if they were talking to a friend.

Read them and write a short **voice card**. Show it and ask "Is this you?":

- Average sentence length, in words.
- How they open and how they sign off.
- Words and phrases they use a lot. Words they never use.
- Do they use "I" or "we"? Contractions? Questions? Humor?
- How formal it is, on a scale of 1 to 5.

Save the card to `~/.claude/skills/cold-email/voice.md` so you do not ask again. If they change their mind, update it.

## 2. Gather the facts for each lead

Use only facts that are in the lead's data or on their public page: their city, their rating or reviews, a line from their website, a post they wrote. If you have no real fact, say less. Never invent a fact, a result, a client name or a number.

## 3. Write the email

- **Subject:** 2 to 5 words, lower case is fine, no tricks, no "Re:" or "Fwd:" to fool anyone.
- **Line 1:** one real thing about them. It shows you looked.
- **Line 2 or 3:** what you do, for people like them, in one plain sentence. Then one result you can truly back up. If you have none, skip it.
- **Ask:** one small question they can answer with a few words. Not "Do you have 30 minutes?" in the first email.
- **Length:** 50 to 90 words.
- **Sign-off:** the person's real name, and one line "If this is not for you, just say so and I will not write again."
- Plain words a 12 year old understands. Short sentences. Match the voice card.

## 4. Follow-ups

Write two short follow-ups (under 50 words each). The first goes 3 days later and adds one new useful thing. The second goes 4 days after that and says you will stop writing. No guilt, no "just bumping this".

## 5. Clean it

Send every email through the `humanizer` skill before you show it. Then show 3 emails and ask if they sound like the person.

## Never

- Never claim you know the lead.
- Never promise results.
- Never use fake urgency or a fake "reply".
- Never send. You write. The `leads` skill makes Gmail drafts, and the person decides what goes out.
