# mirror (for Claude)

**Claude reads your messages, learns how you talk to each person, and every morning tells you who you owe a reply to. It drafts. You press send.**

Type `/mirror` and Claude does five things:

- **Reads your inbox:** Gmail, your calendar, and your chats (iMessage, Instagram, WhatsApp, LinkedIn, Slack and more) through Beeper.
- **Builds one file on every person:** who they are, the history, what is still open, and how you write to them (tone, length, emoji, greeting).
- **Builds one `my-voice.md` file** from the messages you sent, so drafts sound like you.
- **Gives a morning brief:** who you owe a reply to (oldest first), what you talked about last, and a suggested reply for each.
- **Never sends anything.** That is a hard rule in the skill. Gmail replies are saved as drafts. Chat replies are written in Claude's answer, and you copy them and send them yourself.

**[Download mirror-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/mirror-skill.md)**

## Install in Claude Code (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `mirror-skill.md` in and type **set this up**.
3. Type `/mirror` and follow the first run.

## The full setup

### 1. Connect Gmail and Google Calendar

In Claude, open the connectors list, connect **Gmail** and **Google Calendar**, and sign in. Claude can then read your email and your events.

### 2. Connect your chats with Beeper

[Beeper](https://www.beeper.com) puts your chat apps in one app. Its list of networks includes WhatsApp, Instagram, LinkedIn and Slack. Beeper's developer docs say iMessage works only on a Mac.

1. Install **Beeper Desktop** and add your chat accounts.
2. Keep Beeper Desktop open. Its built in server runs only while the app is open.
3. Connect it to Claude. Beeper's docs ([developers.beeper.com/desktop-api/mcp](https://developers.beeper.com/desktop-api/mcp/)) give these ways:
   - **Claude Code:** run `claude mcp add beeper http://localhost:23373/v0/mcp -t http -s user`
   - **Claude desktop app:** use the Claude Desktop install button on that page, or the `@beeper/mcp-remote` option listed there (needs Node.js).
4. Sign in when asked. If sign in fails, make an access token in Beeper Desktop: Settings, then Integrations, then the **+** next to Approved connections.

**What is confirmed and what is not**

| | |
|---|---|
| Confirmed in Beeper's own docs | Beeper Desktop has a local API and a built in MCP server on your computer. Claude Code and Claude Desktop can connect to it. It can search chats and read messages. It only works while Beeper Desktop is open. Beeper recommends it for personal use only. |
| Confirmed, with a warning | The same server also has tools that send, edit and delete messages as you. That is why this skill tells Claude to use only the read tools. |
| Not confirmed | How far back your history goes. Beeper says it builds history in the background, so older messages may be missing at first. I could not confirm which tokens are read only in the Beeper app. Their MCP page says a read only token can only search and read, so pick read only if you see the option. I also could not confirm the exact Claude Desktop menu steps, so follow Beeper's page. |

**Fallback if Beeper does not connect:** copy the chat text for one person at a time and paste it into Claude, or save chats as text files in a folder and tell Claude where it is. WhatsApp can export a chat as a text file. Claude then works only from what you give it.

### 3. The files Claude builds

Everything is saved on your own computer in `~/mirror/`:

```
~/mirror/
  my-voice.md          how you write, built from messages you sent
  people/
    sam-lee.md         one file per person
    ana-ruiz.md
```

Each person file has: who they are, where you talk, when you last talked, the history, the open loops, and **how you write to them**. Claude only writes what the messages show. If it is not sure, it says so.

Start with the 20 people you talk to most in the last 6 months. Claude shows you the list first, and you can remove anyone. Then open two or three files and fix anything wrong. Your fixes make every later draft better.

### 4. The switch: draft only, never send

Inside the skill, as a rule above everything else:

- Claude never sends, replies to, edits, deletes or reacts to any message.
- Gmail: it can save a **draft**. It never sends.
- Chat apps: it reads only. The reply is written in Claude's answer. You copy it and press send.
- Calendar: read only.

**Why:** these are real people, and a message that sounds like you but says the wrong thing cannot be unsent. You read every draft.

For extra safety, in Beeper choose a read only token if it is offered, and keep Claude's approval prompt on for any tool that sends. A rule in a skill is an instruction, not a lock. Read only access is the lock.

### 5. The morning brief

Type `/mirror` and then "morning brief", or paste this:

```
Run my Mirror morning brief. Read my chats, Gmail and calendar for the last 14 days.
Tell me who I owe a reply to, oldest first. For each person give me:
what we talked about last, what they said last, and a suggested reply in my voice.
Use my files in ~/mirror. Draft only. Never send anything.
```

You get a list like this:

```
You owe 4 replies.

1. Sam, waiting 6 days, on WhatsApp
   Last talked about: the Q3 proposal
   What they said last: "Can you send the new numbers?"
   Suggested reply (copy and send yourself):
   > Hey Sam, sorry for the wait. Numbers are attached [add file]. Want to go over them Thursday?
```

Claude also updates the person files with what is new.

**Run it every morning:** if your Claude has scheduled tasks (for example in the Claude desktop app with Claude Code), make one that runs every morning with the prompt above. It only works when your computer is on and Beeper Desktop is open. If you do not see scheduled tasks, open Claude each morning and run the prompt yourself.

### 6. Privacy

You are reading **other people's messages**, and they did not agree to it.

- Keep `~/mirror/` on your own computer. Do not upload it, share it, or put it in a team folder, a shared Project or a repo.
- When Claude reads a message, that text goes to Claude to be processed, like any other chat. Check your Claude privacy settings. Do not use this on messages you are not allowed to share, for example a client under a privacy agreement.
- Keep passwords, bank numbers, ID numbers and health details out of the files.
- Say "delete [name]'s file" or "delete everything" any time, and Claude does it.

### What it cannot do

- It does not learn while you are away. It knows what is in the files and what it can read today. The files get better each time they are updated and corrected.
- It cannot read chat apps Beeper does not support, or messages Beeper has not loaded.
- It does not promise that people will not notice. Read every draft and fix what does not sound like you.

The source is right here: [`SKILL.md`](SKILL.md).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
