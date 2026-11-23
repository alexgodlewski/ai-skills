# Real research: make Claude read the page

Why Claude makes things up about your market, and how to stop it. A free guide by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/).

<img src="cover.png" width="420" alt="Real research: make Claude read the page">

**PDF for your phone:** [real-research.pdf](real-research.pdf)

## Most people think Claude reads

When Claude searches, it does not always read what it finds.

Three things can go wrong. A search is not the same as opening a page. Some pages load in a way Claude's page reader does not handle. And some sites do not want to be read by AI companies.

This guide shows each one with the source, then the fix and a prompt you can paste.

## Reason 1 search is not reading

1. **What you get.** Anthropic's documents for the search tool say each result has a web address, a title, the age of the page, and a block of content for Claude. A quote Claude shows you is up to 150 letters.
2. **Opening is a second step.** Reading a whole page is done by a different tool, web fetch. The documents say Claude uses it when you point to a page. They say it does not use it for open questions.
3. **So.** For an open question like what do buyers think of this, Claude can answer from search results and never open a page. These are the documents for developers. The Claude app can work in another way, and I could not check that.

## Reason 2 half empty pages

1. **What the documents say.** Anthropic's page for web fetch says it currently does not support sites that are built with JavaScript.
2. **What that means.** Many sites load an empty frame first and fill it in later, with code. A reader that does not run that code sees the frame, not the page.
3. **The fix.** Use a tool that runs a real browser. Context.dev says JavaScript pages are part of the base price of one page.

## Reason 3 locked doors

1. **Reddit sells its data.** Reddit has licence deals with Google and OpenAI, say news reports on its court case. In June 2025 Reddit sued Anthropic over its bots. Anthropic said it disagrees.
2. **Doors close.** On 23 November 2026 a plain request from my computer to reddit.com got a page that says Blocked. Anthropic says Claude's fetch tool skips URLs that robots.txt blocks.
3. **LinkedIn too.** LinkedIn's robots.txt says automated access without permission is not allowed.
4. **Test it yourself.** Ask Claude to open a Reddit thread and say exactly what it got.

## The fix open the page

1. **For normal pages.** Context.dev. It loads the whole page and gives Claude the text. Setup is in the free guide Claude setup.
2. **For Reddit.** Apify, actor trudax/reddit-scraper-lite. About $3.40 for 1,000 results.
3. **For X.** Apify, actor apidojo/tweet-scraper. $0.40 for 1,000 tweets. Its page says free accounts get 5 runs a month, 10 results each, and no use through the API. So it may not work through Claude on the free plan.
4. **For LinkedIn.** Apify, actor harvestapi/linkedin-post-search. No cookies needed. About $2 for 1,000 posts.

## Setup in one minute each

1. **Context.dev.** Customize, Connectors, Add custom connector, https://mcp.context.dev/mcp
2. **Apify.** Customize, Connectors, Add custom connector, https://mcp.apify.com
3. **Claude Code.** claude mcp add --transport http --scope user context https://mcp.context.dev/mcp   and   claude mcp add apify "https://mcp.apify.com" -t http
4. **Then say.** Use the Apify actor [name] for this. Name the actor in your message so Claude does not pick another one.

## The prompt market research

Fill in the two brackets and paste it.

```text
I need research on [my market, in one sentence, for example: coaches who sell online programs].

My question: [what I want to know, for example: what do these people complain about when they buy ads?]

Rules, no exceptions:
1. Do not use search snippets as proof. For every page you use, OPEN the page with the context.dev tool (scrape) and read it. If you cannot open it, do not use it.
2. For Reddit, X and LinkedIn use my Apify connector. Reddit: trudax/reddit-scraper-lite. X: apidojo/tweet-scraper. LinkedIn posts: harvestapi/linkedin-post-search. If an actor fails or I have no credits, say so. Do not fill the gap from memory.
3. After the page loads, check it. If the page looks empty, short or cut off (only menus, "loading", a login box), say "this page did not load" and try again once or drop it.
4. Write the answer as claims. Under EVERY claim list the pages you read for it, with the full web address, and one short quote (under 15 words) from each page.
5. If a claim comes from your own knowledge and not from a page you opened, mark it "from memory, not checked". Better: leave it out.
6. If only one page backs a claim, say "one source".
7. At the end give me three lists: pages you opened and used, pages you could not open, and what you could not find out.

Start by telling me your plan: which pages and tools you will use. Then do it.
```

## Check the answer

1. **Open three links.** Pick three claims. Open the links under them. Does the page say it?
2. **Look for the words.** from memory, not checked and one source. Those claims are weak.
3. **Pages that did not load.** If the list is long, the answer is thin. Try again with other pages.
4. **Be fair to the sites.** Scraping can break a site's terms. Reddit sued over it. Keep it small, for your own research, and read the actor's page.

## Where this comes from

- [Anthropic: web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)
- [Anthropic: web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- [The Register: Reddit sues Anthropic](https://www.theregister.com/2025/06/05/reddit_sues_anthropic_over_ai/)
- [Fortune: Reddit sues Anthropic](https://fortune.com/2025/06/04/reddit-sues-anthropic-user-comments-train-ai-claude/)
- [Context.dev prices](https://www.context.dev/pricing)
- [Apify Reddit Scraper Lite](https://apify.com/trudax/reddit-scraper-lite)
- [Apify Tweet Scraper V2](https://apify.com/apidojo/tweet-scraper)
- [Apify LinkedIn Post Search](https://apify.com/harvestapi/linkedin-post-search)

---

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/), founder of [Setor](https://setor.ai). We book sales calls in the DMs.
