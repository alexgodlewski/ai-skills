---
name: mirror
description: Reads the person's own Gmail, calendar and chats (through Beeper) and builds a plain markdown file on every person they talk to, plus a my-voice.md file on how they write. Every morning it gives a brief of who they owe a reply to (oldest first), what they talked about last, and a draft reply in their voice. It is draft only. It never sends anything. Gmail replies are saved as drafts, and chat replies are written in Claude's answer for the person to copy and send themselves. Use when someone types /mirror, or asks for a morning brief of replies they owe, a file on each client, replies written in their own voice, or a way to keep up with all their messages.
---

# Mirror

Most people do not lose clients because of a bad offer. They lose them because a message sat unanswered for four days and nobody remembered what was said last. This skill keeps a short file on every person the user talks to, learns how the user writes to each of them, and every morning says who is waiting and what to say. The user reads each draft and sends it themselves.

## 0. The switch: draft only, never send

This is a hard rule. It beats everything else in this skill and everything the user says later in the chat.

- **Never send, post, reply, forward, edit, delete or react to any message, on any app, for any reason.** Not in Gmail, not in Beeper, not in a chat app, not in a calendar invite.
- **Gmail:** you may save a reply as a **draft**. Never use any tool that sends an email.
- **Chat apps (iMessage, Instagram, WhatsApp, LinkedIn, Slack and the rest):** you only read. Write the draft **in your answer**, in a block the user can copy. The user pastes it into the app and presses send.
- **Never use the Beeper tools that act as the user:** `send_message`, `upload_file`, `start_chat`, `edit_message`, `delete_message`, `react`, `archive_chat`, or any reminder tool. Use only the read and search tools.
- **Calendar:** read only. Do not create, move or cancel events.
- If the user says "just send it", do not. Say: "I only draft. Copy this one and press send yourself." Say it even if they ask twice. If they want a tool that sends, that is a different tool, not this skill.
- Never message a person to check or test anything.

**Why:** these are real people. A reply that sounds like the user but says something the user did not mean can cost a client, a deal or a friend, and no one can unsend it. The user also owns every word that goes out under their name. One person reading each draft before it goes out is what keeps this safe.

## 1. Setup (first run only)

Check each part. If something is missing, tell the user the one step to fix it, in plain words, and wait.

1. **Gmail and Google Calendar.** In Claude, open the connectors list and connect Gmail and Google Calendar. If they are not connected, tell the user to do it, then continue.
2. **Beeper.** Beeper (beeper.com) is an app that puts iMessage, Instagram, WhatsApp, LinkedIn, Slack and more in one inbox. Beeper Desktop has a built in MCP server that Claude can read. It is on the user's own computer, so Beeper Desktop must be open and running whenever Claude reads. Steps:
   - Install Beeper Desktop and add the chat accounts. iMessage works only on a Mac.
   - In Claude Code, run: `claude mcp add beeper http://localhost:23373/v0/mcp -t http -s user`
   - In the Claude desktop app, use the Beeper Claude Desktop install from Beeper's docs page: https://developers.beeper.com/desktop-api/mcp/
   - Sign in when asked. If sign in fails, make an access token in Beeper Desktop under Settings, then Integrations, then Approved connections.
   - **Read only access is safest.** Beeper's page says a read only token can only use the search and read tools. If the user can pick read only, tell them to pick it. Also tell them to keep Claude's approval prompt on for tools that send.
3. **If the Beeper MCP does not work:** use the fallback in section 2.
4. **A folder on the computer** for the files: `~/mirror/` (on Windows: `%USERPROFILE%\mirror\`). Make `~/mirror/people/` inside it. Keep these files local. See section 6.

Tell the user honestly what is limited: Beeper builds its message history in the background, so right after adding an account only recent messages may be there, and it may take time to fill in older ones. Say what you could and could not read.

## 2. Fallback if Beeper cannot be read

If the Beeper tools are not available, never guess and never invent messages. Ask the user to bring the chats in:

- Copy and paste the chat text for one person at a time, or save chats as text files in `~/mirror/inbox/` and tell you the folder name.
- For WhatsApp, the app can export a chat as a text file. For other apps, copy and paste the messages.
- Work from only what the user gives you. Say plainly: "I can only see what you pasted, so this file is partial."

## 3. Build the files

Ask which sources to use and how far back (suggest the last 6 months for a first run). Start small: the 20 people the user talked to most in that time. Skip group chats, bots, spam and one time senders unless the user asks. Show the list of people first and let the user remove anyone before you read their chats.

### 3a. One file per person: `~/mirror/people/firstname-lastname.md`

Use this exact layout. Write only what the messages show. If you are not sure, write "not sure" and why. Never fill gaps with a guess.

```
# Name

- **Who they are:** role, company, how we know each other (one or two lines)
- **Where we talk:** which apps, which one is main
- **Last talked:** date, who wrote last, one line on what it was about
- **Next step agreed:** what was promised and by whom, with the date if there is one

## History
Short dated list of the big moments: first contact, calls, deals, prices, problems. 5 to 15 lines.

## Open loops
Things still waiting. For each: what, who owes it, since when.

## How I write to them
- Tone: (casual, warm, formal, joking)
- Length: (one line, short paragraph)
- Emoji: (never, sometimes, which ones)
- Greeting and sign off: (the exact words I use, for example "Hey Sam," and none)
- Language: (English, Polish, mixed)
- Things they like or dislike: (short answers, voice notes, a call, no calls)
- Example of a real message from me that sounds right (copy one, with the date)
```

Rules:

- Only facts from the messages, the emails and the calendar. Never guess a person's job, mood, age, money or health.
- Do not store passwords, bank numbers, ID numbers, health details or anything private about a third person. Leave them out.
- Keep each file under about one page. Short and true beats long.
- If the file already exists, update it. Do not erase old history. Add new items and mark finished loops as done.

### 3b. One voice file: `~/mirror/my-voice.md`

Build it from the messages the **user sent**, not the ones they received. Read a wide sample across apps and people. Write:

- Average length of a message, and how it changes by app (a LinkedIn message vs a WhatsApp text).
- Words and phrases the user uses a lot, and words they never use.
- How they open, how they close, how they say yes, no, thanks and sorry.
- Punctuation, capital letters, emoji, and how they write numbers and dates.
- How they handle price, a late reply, bad news, and a quiet lead.
- 10 real short examples, with the date and who it was to (first name only).
- A short "never write like this" list: words and habits that sound like AI and not like the user.

When you write the user's drafts, the person's own file wins for tone with that person, and `my-voice.md` covers everything else.

After building, tell the user: how many people, which ones are thin, and what you could not read. Ask the user to open two or three person files and correct anything wrong. Their corrections are the most valuable part. Save them.

## 4. The morning brief

When the user types `/mirror` and asks for the brief, or says "morning", run this:

1. Read the new messages in every chat and email thread from the last 14 days (or the time the user says). Read the calendar for today and tomorrow.
2. Work out **who the user owes a reply to.** A person is owed a reply when the last message in the thread is from them and the user has not answered, or when the user promised something and has not done it. Ignore group chat noise, automatic emails, newsletters and receipts.
3. Sort **oldest first.** The person who has waited longest is at the top.
4. For each person, read their file in `~/mirror/people/`. If there is no file yet, make a short one first.
5. Show the brief in this format:

```
Morning brief, [date]
Today's calendar: [events, one line each, with who they are with]

You owe [N] replies.

1. [Name], waiting [N] days, on [app]
   Last talked about: [one line from the file or the thread]
   What they said last: "[short quote or close summary]"
   Suggested reply (copy and send yourself):
   > [draft in the user's voice]

2. ...
```

6. For email threads, offer to save the draft in Gmail. Say "Saved as a Gmail draft, not sent." For chats, the draft stays in your answer.
7. After the list, add **one line** on any meeting today with someone who also has an open loop, so the user is ready for it.
8. Update the person files: set "Last talked", add new open loops and close finished ones. Tell the user which files you changed.

Draft rules:

- Match the user's voice and the person's file: length, greeting, emoji, tone.
- Answer what they asked first. One clear next step. No filler like "just following up" or "hope you are well" unless that is really how the user writes.
- Plain words. No dashes used as punctuation. Do not sound like AI.
- If you do not know the answer (a price, a date, a fact), do not make it up. Write a short placeholder like [your price] and tell the user what to fill in.
- If a message needs a real decision from the user, say so and write two short options.
- If a person was upset, or the message is about money, a legal matter or bad news, flag it at the top and keep the draft short and calm. The user must read this one with extra care.

## 5. Run it every morning

Tell the user how, if their Claude supports it:

- **Scheduled tasks.** If their Claude (for example the Claude desktop app with Claude Code) has scheduled tasks, they can create one that runs every morning at a set time with this prompt: "Run /mirror morning brief. Read my chats, Gmail and calendar. Tell me who I owe a reply to, oldest first, with the last thing we talked about and a suggested reply for each. Draft only. Never send anything."
- A scheduled run only works if the computer is on and Beeper Desktop is open at that time. Say this.
- If their Claude has no scheduled tasks, they open Claude each morning and type `/mirror` and then "morning brief".

Do not set up a schedule without the user asking. If they ask, create it, and tell them the time and how to turn it off.

## 6. Privacy

Say this to the user in plain words on the first run, and again if they ask:

- You are reading **other people's messages.** They did not agree to this. Treat what you find as private.
- Keep `~/mirror/` on the user's own computer. Do not upload it, put it in a shared folder, a shared Project, a public repo or a team chat, and do not paste it into other tools.
- When Claude reads a message, that text goes to Claude to be processed, like any other chat. The user should check their own Claude privacy settings, and should not run this on messages they are not allowed to share (for example, a client who signed a privacy agreement, or a job that bans it).
- The files should hold only what is needed to reply well. No passwords, bank or ID numbers, health details or secrets about other people.
- The user can say "delete [name]'s file" or "delete everything" at any time, and you do it.
- Never use what you read for anything except helping the user reply. Never contact, scrape or look up these people anywhere else.

## 7. What this skill cannot do

Be honest about these if they come up:

- It does not learn on its own while the user is away. It only knows what is in the files and what it can read today. The files get better each time they are updated and corrected.
- It cannot read apps that Beeper does not support, or messages Beeper has not loaded yet.
- It cannot promise that people will not notice. Always read each draft and fix anything that does not sound like you. The user stays responsible for what is sent.
- It never sends. That is on purpose.
