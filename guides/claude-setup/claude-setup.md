# The Claude setup: 3 things to do in the first 10 minutes

A real search tool, your own files, and an interview. A free guide by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/).

<img src="cover.png" width="420" alt="The Claude setup: 3 things to do in the first 10 minutes">

**PDF for your phone:** [claude-setup.pdf](claude-setup.pdf)

## Three things before anything

Do these three things on a new Claude account before you ask it for real work.

One: give it a tool that really opens web pages. Two: let it read your last 30 days of email, files and calendar. Three: let it interview you and write down what it learns.

Everything below was checked in the official pages of each tool on 23 November 2026. Menu names change, so a button may have a different name on your screen.

## Step 1 open the web

1. **Why.** Claude's own search can answer from a list of search results and never open a page. That is where many made up answers start. Read more in the free guide Real research.
2. **Context.dev.** A service that opens a page the way a browser does and gives Claude the text. It was called Brand.dev before.
3. **Free plan.** 1,000 credits a month, no card. Reading one page costs 1 credit. The first paid plan is $20 a month for 10,000 credits. Check the price page before you pay.

## Step 1a connect context.dev

1. **In the Claude app.** Customize, Connectors, plus, Add custom connector. Paste https://mcp.context.dev/mcp and press Connect. Sign in in your browser.
2. **In Claude Code.** claude mcp add --transport http --scope user context https://mcp.context.dev/mcp   then /mcp, pick context, sign in.
3. **Test it.** Ask: List the tools you got from context. Then: Open [a page] and tell me its first heading.
4. **Good to know.** Signing in makes an API key in your account. You can turn it off in the dashboard.

## Step 1b Apify for Reddit

1. **What it is.** Apify runs ready made scrapers, called actors. Its Claude connector lets Claude start them.
2. **In the Claude app.** Customize, Connectors, Add custom connector. Paste https://mcp.apify.com and sign in. Or find Apify in the connector list.
3. **In Claude Code.** Type: claude mcp add apify "https://mcp.apify.com" -t http   Your browser opens to sign in.
4. **The Reddit actor.** trudax/reddit-scraper-lite. About $3.40 for 1,000 results. The free plan has $5 a month, about 1,000 results.

## About the Reddit actor

1. **Links work without more.** Give it a subreddit or a post link and it reads the page.
2. **Search needs a cookie.** To search Reddit for words, the actor asks for the reddit_session cookie of a Reddit account. Use a spare account for this, never your main one. Or skip search and give links.
3. **It stops near 1,000.** Reddit lists end around 1,000 posts.
4. **Test it.** Ask: Use the Apify Reddit actor trudax/reddit-scraper-lite to read this thread and give me the top 5 complaints: [link]

## Step 2 your last 30 days

Connect Gmail, Google Drive and Google Calendar in Settings, then Connectors. Claude sends you to Google to sign in. On a Team or Enterprise plan the owner turns them on first. Then paste this.

```text
Read only. Do not send, delete or change anything.

Use my Gmail, Google Drive and Google Calendar connectors. For each one, look only at the last 30 days.

1. Gmail: who do I write to most, what do I answer fast, what do I leave sitting, what do I keep sending again and again.
2. Google Drive: which files did I open or change, what are they about.
3. Google Calendar: what meetings do I have, who with, and how much of my week is calls.

Then tell me, in plain words:
- How do I work? Five short points.
- What does my business seem to be, from this alone?
- Where are the gaps? Things I do by hand again and again, things that wait too long, things you could not find.

First say what you could read and what you could not, for example "I found 41 emails". Do not guess. If you are not sure, say "not sure".
```

## About step 2 read this first

1. **It reads real mail.** Do this on your own account. Look at what Claude says before you save anything.
2. **Reading, not sending.** The prompt says read only. Claude's help page says it asks before it sends or changes things, unless you turn on Auto mode. Leave Auto mode off.
3. **It may not read everything.** Claude searches your mail and files. It does not open every one. That is why the prompt makes it say what it found.
4. **Blocked by Google?** On a work Google account the admin may have to allow Claude first.

## Step 3 the interview

This is reverse prompting. You do not write the prompt about your business. Claude asks you, one question at a time, and writes the file. Paste this.

```text
I want you to learn my business by interviewing me. This is called reverse prompting.

Rules:
- Ask ONE question at a time. Wait for my answer.
- Start from what you already know about me (my email, files and calendar, and anything you read about me). Do not ask what you can already see. Say what you think is true and ask me to fix it.
- Ask about what you still do not know: what I sell and to whom, my price, how a customer finds me, how a sale happens step by step, what I do every week, what I hate doing, who helps me, my tools, my goals for this year, what I never want you to do, how I like you to write (long or short, formal or not).
- If an answer is thin, ask a follow up. If it is clear, move on.
- Use simple words.
- Stop after 25 questions, or sooner if I say "done".

When we are done:
1. Write a short file called about-me.md with these headings: Me, My business, My customers, How a sale happens, My week, My tools, My goals, What to never do, How to write for me, Still unknown.
2. Under 600 words. Only things I told you or you read. No guesses. Mark anything unsure with "(unsure)".
3. Show it to me. Ask what is wrong. Fix it.
4. Then save it: if you can create files, save it as about-me.md in my current folder. If you cannot, tell me to copy it into my Claude Project instructions.

Start now with question 1.
```

## Then keep the file

1. **Claude Code.** The file about-me.md stays in your folder. Add one line to your CLAUDE.md file: Read about-me.md first.
2. **The Claude app.** Copy the text into the instructions of a Claude Project, so every chat in that project starts with it.
3. **Fix it every month.** Say: Read about-me.md and interview me about what changed. Only ask about what changed.
4. **Do not put in.** Passwords, card numbers, or private details of your clients.

## Where this comes from

- [Context.dev MCP setup](https://docs.context.dev/install-mcp.md)
- [Context.dev credits](https://docs.context.dev/account/credits.md)
- [Context.dev prices](https://www.context.dev/pricing)
- [Apify MCP server](https://docs.apify.com/platform/integrations/mcp)
- [Apify Reddit Scraper Lite](https://apify.com/trudax/reddit-scraper-lite)
- [Claude Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)

---

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/), founder of [Setor](https://setor.ai). We book sales calls in the DMs.
