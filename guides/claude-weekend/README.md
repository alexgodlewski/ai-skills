# The Claude Weekend: Set Up Claude in One Weekend

A free plan by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). Five steps, two days. At the end, Claude knows you, remembers your work, can reach your apps, and has real skills installed.

**Short PDF version:** [claude-weekend.pdf](claude-weekend.pdf)

You need: a Claude account (a paid plan is needed for Projects and most connectors) and about six hours spread over the weekend. Features and menu names change from time to time. If a button has moved, search the [Claude help center](https://support.claude.com).

## The plan

| When | Step | Result |
|---|---|---|
| Saturday morning | 1. The About Me doc | One document that tells Claude who you are |
| Saturday afternoon | 2. Your second brain | One home for all your context |
| Saturday evening or Sunday start | 3. Move real work into Projects | One Project for each area of your life or business |
| Sunday morning | 4. Connect your apps | Claude can read your mail, calendar and files |
| Sunday afternoon | 5. Install skills and build one real thing | A first useful result, saved so you can repeat it |

---

## Step 1. Saturday morning: the About Me doc (about 90 minutes)

Claude knows nothing about you until you tell it. So let Claude interview you. It asks 50 questions, one at a time. You answer in plain words, a sentence or two each. Voice dictation works great here. At the end Claude writes everything into one clean document.

**How:** open a new chat (or the Claude app), paste the prompt below, and answer.

### Copy and paste this prompt

```
I want you to build an "About Me" document about me, so that every future chat with you starts with real context.

Interview me with 50 questions. Rules:
- Ask ONE question at a time. Wait for my answer before the next one.
- Go through these 7 groups in order: Work, Business and offer, Customers, Voice and style, Goals, Tools, Preferences.
- Number each question (for example "Question 12 of 50") and tell me the group name when we move to a new group.
- If an answer is short or unclear, ask one quick follow up before moving on. That follow up does not count as a new question.
- Do not give advice yet. Only ask.
- If I say "skip", move on.

When all 50 are done, write the About Me document:
- Plain English, no hype.
- One section for each of the 7 groups.
- At the top, a 5 line summary of who I am.
- At the end, a list of "things Claude should always do" and "things Claude should never do" when it works with me.
- Keep my own words and phrases where you can, so my voice stays in it.

Start with Question 1.
```

### The 50 questions

You do not have to write these yourself. The prompt above makes Claude ask them in its own way. This list is what the interview should cover. Use it to check that nothing is missing, or to ask them yourself.

**Work (7)**

1. What is your name, and what do you do for work?
2. What is your job title, or how do you describe what you do to a stranger?
3. How long have you done this?
4. What does a normal week look like for you?
5. Which tasks take most of your time?
6. Which tasks do you dislike or keep putting off?
7. Who do you work with often (team, partners, clients)?

**Business and offer (8)**

8. What do you sell or provide? Describe it in one simple sentence.
9. What is the price, or the price range?
10. What problem does it solve for people?
11. What result do people get after they buy?
12. What makes you different from others who do the same thing?
13. What is your best selling product or service?
14. How do people find you today?
15. What does the buying process look like, from first contact to payment?

**Customers (8)**

16. Who is your ideal customer? Describe one real person.
17. What is their job, age range and situation?
18. What problem keeps them up at night?
19. What have they already tried that did not work?
20. What words do they use to describe their problem?
21. What are their top three objections before buying?
22. What questions do they ask you again and again?
23. Which customers do you not want to work with, and why?

**Voice and style (7)**

24. How would you describe your tone (friendly, direct, funny, calm)?
25. Which words or phrases do you use a lot?
26. Which words or phrases do you hate?
27. Do you write short or long? Casual or formal?
28. Name two or three people or brands whose writing you like.
29. Paste or describe one thing you wrote that you are proud of.
30. What should your writing never sound like?

**Goals (7)**

31. What is your main goal for the next 90 days?
32. What is your goal for the next 12 months?
33. What number would tell you that you are winning (money, clients, followers, hours saved)?
34. What is the biggest thing blocking you right now?
35. What would you do with 10 extra hours a week?
36. What have you tried before to reach this goal?
37. What is one thing you want AI to take off your plate first?

**Tools (7)**

38. Which email do you use (Gmail, Outlook, other)?
39. Which calendar do you use?
40. Where do you keep files (Google Drive, Dropbox, your computer)?
41. Which notes or task tools do you use (Notion, Apple Notes, Todoist, other)?
42. Which chat tools do you use (Slack, WhatsApp, Teams)?
43. Which tools run your business (CRM, payments, website, email marketing)?
44. Which AI tools do you use now, and what for?

**Preferences (6)**

45. Do you want short answers or detailed ones?
46. Should Claude ask questions first, or just give its best try?
47. How should Claude handle things it is not sure about (say so, or guess)?
48. What is your time zone, and when do you work?
49. Are there topics or things Claude should avoid?
50. Anything else Claude should know about you that we did not cover?

**When it is done:** read the document, fix anything wrong, and save it as `about-me.md` (or a Google Doc). You will use it in Step 2.

---

## Step 2. Saturday afternoon: your second brain (about 90 minutes)

A second brain is one home for everything Claude should know. Two good options. Pick one to start.

**Option A: a Claude Project (easiest)**

1. In Claude, open **Projects** and click **New project**. Name it "Me".
2. Add your About Me doc under the project's files (knowledge).
3. In the project instructions, write: "Read my About Me doc first. Use my voice. Ask a question if something is unclear."

**Option B: a folder that Claude Code reads (most powerful)**

1. Make a folder on your computer called `brain`.
2. Inside, make a file called `CLAUDE.md`. Claude Code reads this file at the start of every session. Put a short summary of you in it, and a line that points to the other files.
3. Add the files below, then open the folder in Claude Code.

### What goes in it

| File or section | What to put in it |
|---|---|
| `about-me.md` | Your About Me doc from Step 1 |
| `offer.md` | What you sell, price, results, how it works, how to buy |
| `customers.md` | Who you help, their problems, their words, their objections |
| `voice.md` | Your tone, words you like, words you hate, 3 to 5 samples of your best writing |
| `examples/` | Your best past work: emails, posts, proposals, replies |
| `facts.md` | Names, links, prices, dates, numbers Claude must get right |
| `rules.md` | Things Claude must always do and never do |

Two rules for a good second brain: real examples beat descriptions, and short beats long. Update it when something changes.

---

## Step 3. Move real work into Projects (about 60 to 90 minutes)

Do not start with test chats. Take work you really have this week and do it inside a Project.

1. Make one Project for each area of your life or business. For example: Sales, Content, Clients, Finance, Learning, Personal.
2. In each Project, add the files that area needs.
3. Write that Project's instructions. A good set of instructions has five parts:
   - **Role:** "You are my sales assistant."
   - **Context:** what this area is, who is involved.
   - **How to answer:** format, length, tone ("short, plain, no hype").
   - **Rules:** what to always do and never do.
   - **Questions first:** "If anything is unclear, ask me before you start."
4. Move one real task into each Project this weekend. Then keep using that Project for that area, so its chat history and files stack up.

Example instructions for a Sales Project:

```
You are my sales assistant. Read the About Me and Offer files first.
Help me write replies to leads, follow ups and call prep.
Write in my voice (see the Voice file). Keep messages under 80 words.
Never promise results I have not promised. Never invent numbers.
If something is unclear, ask me before you write.
```

---

## Step 4. Sunday morning: connect your apps through MCP (about 60 minutes)

MCP (Model Context Protocol) is a standard way to let Claude connect to your apps. In Claude these are called **connectors**. Once connected, Claude can look things up in your real data, instead of you copying and pasting.

**Good first connectors:** Gmail, Google Calendar, Google Drive, Notion, Slack. Connect only what you need. Start with read access where you can.

### In claude.ai (the website or desktop app)

1. Click your name, then **Settings**.
2. Open **Connectors**.
3. Find the app (for example Gmail) and click **Connect**.
4. Sign in with that app and approve the permissions.
5. In a chat, turn the connector on from the tools menu, then try it: "What is on my calendar tomorrow?" or "Find the last email from my biggest client."

Official help: search "connectors" in the [Claude help center](https://support.claude.com).

### In Claude Code

Add a remote MCP server from the terminal:

```
claude mcp add --transport http <name> <server-url>
```

Then inside Claude Code, type `/mcp` to check the list and sign in to any server that needs it. The server URL comes from the app's own docs. Official help: [Claude Code MCP](https://docs.claude.com/en/docs/claude-code/mcp)

Safety: Claude acts with the same access you give it. Approve each connection on purpose, ask Claude to show you drafts before it sends or changes anything, and remove connectors you no longer use.

---

## Step 5. Sunday afternoon: install a few skills and build one real thing (about 2 hours)

A skill is a saved set of instructions that Claude follows the same way every time. These are free and open. Pick two or three.

| Skill | What it does | Link |
|---|---|---|
| search | Checks how Google's AI sees your business, finds what is missing, and fixes it | [search](https://github.com/alexgodlewski/ai-skills/tree/main/claude/search) |
| outcome-first | Asks about the finished result before Claude builds anything, then builds it in one go | [outcome-first](https://github.com/alexgodlewski/ai-skills/tree/main/claude/outcome-first) |
| google-ads | Finds competitor ads, writes yours, and suggests where to move budget | [google-ads](https://github.com/alexgodlewski/ai-skills/tree/main/claude/google-ads) |
| youtube-skill | Watches a YouTube video or podcast and turns what it teaches into a skill | [youtube-skill](https://github.com/alexgodlewski/ai-skills/tree/main/claude/youtube-skill) |
| humanizer | Rewrites text so it does not sound like AI, in your own voice | [humanizer](https://github.com/alexgodlewski/ai-skills/tree/main/claude/humanizer) |

How to install: each skill's page has the download link and the steps. Short version: download the skill file, drag it into the Claude desktop app (Code tab), and type "set this up".

### Build one real thing

Pick one small job you repeat every week. Then:

1. Use **outcome-first**: describe the finished result and let Claude ask you questions.
2. Run it on real work.
3. When the result is good, ask: "Save what we just did as a skill so I can run it again."

Good first things: a weekly report, a reply template for leads, a content calendar, an ad draft, a check of your own website.

You are done when you can run the same job again next week in one line.

---

## Your Sunday night checklist

- [ ] About Me doc saved
- [ ] Second brain made (Project or folder)
- [ ] At least three real Projects with instructions
- [ ] Two or more connectors working
- [ ] Two or three skills installed
- [ ] One real job built and saved

## More free stuff

All my free Claude skills: [github.com/alexgodlewski/ai-skills](https://github.com/alexgodlewski/ai-skills). If this helped, star the repo.
