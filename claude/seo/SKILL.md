---
name: seo
description: Three SEO tools in one skill. The SEO Audit crawls a website, checks every page, shows the searches it shows up for and the searches competitors win, and ranks every fix with the biggest wins first. The Keyword Finder groups real search terms into pages. The Page Writer writes new titles, descriptions and missing pages, and edits the site files when it has access. Use when someone types /seo with their website, or asks why Google does not send them customers, or wants better rankings.
---

# SEO

Three tools in one skill: the **SEO Audit**, the **Keyword Finder** and the **Page Writer**. Start with the website. Run the audit first, then offer the other two.

For Google's AI answers (AI Overviews), use the `/search` skill. This skill is about the normal results.

Be honest with the person: nobody can promise a ranking, and SEO takes weeks to show. This finds what holds the site back and fixes it.

## 0. Start

The website is what the person typed after `/seo`. If there is none, ask for it in one line and wait.

Open the site. Write down in one short block: what they sell, the main services, the town or area they serve (if any), and who buys. Ask one short question only if something important is missing, usually the area.

Then ask in one line, and do not wait on the answer if they skip it:

- "Do you have Google Search Console? If yes, export Performance (Queries and Pages, last 3 months) as CSV and drop it here, or connect it. If not, I will say which parts are estimated."
- "Are the website files in this folder, or can I reach your site's admin? If yes, I can make the fixes."

## 1. SEO Audit

### 1a. Crawl the site

1. Fetch `/robots.txt` and `/sitemap.xml` (also `/sitemap_index.xml`, and any Sitemap line in robots.txt). Read every URL in the sitemap.
2. If there is no sitemap, start at the home page and follow internal links (same domain only).
3. Page cap: 100 pages. If the site is bigger, take the home page, every page in the main menu, then a sample of the rest, and say plainly that you sampled and how many pages the site has.
4. Fetch pages with the tools you have (a web fetch tool, or `curl`). If a page comes back nearly empty because the site builds its text with JavaScript, say so and use a browser tool if you have one. Never guess what a page says.
5. Skip images, files, login pages and URLs with tracking parameters.

### 1b. Check every page

For each page record:

| Check | What to write down |
|---|---|
| Status | The HTTP code. Note redirects and 404s. |
| Title | The text, and its length in characters |
| Meta description | The text, and its length (missing is a problem) |
| H1 | The text. Missing or more than one is a problem |
| Word count | Words of real page text, not menus or footers |
| Indexable? | Yes or No, and why: robots.txt block, `noindex`, or a canonical tag pointing to another page |
| Images | How many have no alt text |

Flag: titles over 60 characters or under 30; descriptions over 155 or under 70; two pages with the same title or description; pages under 300 words that are meant to rank; pages in the sitemap that are not indexable; pages no other page links to.

### 1c. Check the whole site

- Uses https, and http redirects to https; one version only (with or without www).
- sitemap.xml exists, is listed in robots.txt, and holds only pages that return 200 and are indexable.
- robots.txt does not block pages that should rank.
- Broken internal links and redirect chains.
- Missing pages: for each main service, is there its own page? If there is an area, is there a page for each service in that area?
- Contact details (name, address, phone) match on every page.
- Schema markup: look for LocalBusiness or Organization on the home page, and FAQPage where there are FAQs.
- Page speed: only if you can run a real test (for example Google PageSpeed Insights). Otherwise say "not tested". Never guess a score.

### 1d. The searches they show up for

**With Google Search Console data** (CSV export or a connection): use the real numbers. List the top queries by clicks, then these groups:

- **Almost there:** average position 8 to 20 with real impressions. These are the quick wins.
- **Seen but not clicked:** many impressions, low click rate. The title or description needs work.
- **Pages with no clicks at all.**

Quote the numbers exactly as they are in the file. Do not round them up or fill gaps.

**Without it**, say this in plain words at the top of this section: "This part is estimated. Without Search Console I cannot see the real searches or numbers." Then give only what you can show: search the web for the brand name and the main services plus the area, and report which of the site's pages appear and where. Mark each result "seen in a search, not a measured rank". Tell them how to get the real data: Search Console is free, they verify the site once, and data starts to fill in within a few days.

### 1e. The searches competitors win

1. For each main service (up to 5), search the web for the service alone and for the service plus the area. Use two or three phrasings a customer would type.
2. For each search write down who is in the top results: the business, the exact page that ranks, its title, and what kind of page it is (service page, blog post, directory, map listing).
3. Mark the searches where this site is missing and a competitor wins. For each, say what the winning page has that this site does not (a page for that exact service, a page for that town, an FAQ, more detail, reviews on the page).
4. Directories and big sites (Yelp, Angi, Wikipedia and the like) are not competitors to copy. Note them as "directory" and look at the real businesses.
5. If you cannot search the web from here, say so. Never invent results or rankings.

### 1f. The ranked fix list

Turn everything into one list. For each fix give: what to change, the exact pages, **why it matters** in one plain sentence, **impact** (High, Medium, Low), **effort** (Low, Medium, High), and the evidence (a number, a quote, or a link).

Order by impact first, then lowest effort. A fix that blocks pages from Google (noindex by mistake, a robots.txt block) always goes first. Number them. Show the top 10 in full and the rest in a short list.

Impact rules, so the order is not a guess:

- **High:** pages that should bring customers are blocked, missing or have no page at all for a service or town; a searched term where competitors win and this site has no page; real Search Console terms at position 8 to 20.
- **Medium:** weak titles and descriptions on pages that already get impressions; thin pages; duplicate titles.
- **Low:** missing alt text, small length problems, tidy-ups.

Finish the audit with one screen: the three biggest wins, then say "Want me to find keywords and write the fixes?"

## 2. Keyword Finder

1. **Seed terms.** Take them from the site: service names, product names, the town and nearby places, words from the headings. Add the terms from the competitor pages you found in 1e.
2. **Ask Google.** Search the web for each seed. Write down the Google autocomplete suggestions you can see and the "People also ask" questions. If you cannot see them, say so and skip them. Never write suggestions from memory as if you saw them.
3. **Competitor titles.** List the title of each competitor page that ranks, and the words in common.
4. **Search intent.** Label each term: *buy or hire now* ("emergency plumber [town]"), *compare* ("best plumber in [town]"), *price* ("how much does [service] cost"), *learn* ("why is my boiler leaking"). Match each term to the right kind of page: a service page for buy and hire, a comparison or guide for compare, an FAQ or blog post for learn.
5. **Group into pages.** One main term per page, with 3 to 8 close terms that the same page can answer. Mark each group: **exists** (a page already covers it, improve it), **weak** (a page exists but misses the term), or **missing** (a new page is needed). Never put two pages on the same main term.
6. **Volumes.** Do not invent search volumes, difficulty scores or "traffic" numbers. Show a number only if it comes from the person's Search Console file or from a tool they have connected or pasted (for example Keyword Planner, Semrush, Ahrefs). Otherwise show "no volume data". You can still rank groups by intent and by how many competitors show up for them, and say that is how you ranked them.

Output a table: page, main term, close terms, intent, status (exists, weak, missing), and the reason.

## 3. Page Writer

Write only what the audit and the keyword groups show is needed.

### 3a. Titles and descriptions

For each page to fix, write a new title and meta description:

- Title: 30 to 60 characters, main term near the front, the town if it is a local term, the brand name last if it fits.
- Description: 70 to 155 characters, says what the page offers, why choose them, and a clear next step. Only claims the business can back up.
- **Count the characters of every title and description** and show the count next to it. Rewrite any that are over or under.
- Show old and new side by side.

### 3b. Missing pages

For each **missing** group, write the whole page: the title, the description, one H1, an opening paragraph with the service and the town, what is included, who it is for, the area served, how it works, a price guide only if the person gave one, a clear call to action, and an FAQ of 4 to 8 real questions (use the "People also ask" questions you found) with plain answers. Use real details from the site: names, services, years, reviews that exist. Where you do not know something, write [fill in]. Never make up reviews, prices, licences, awards or staff.

Do not write near-copies of the same page for many towns. Each page needs details that are true for that place, or do not write it. Say this plainly if the person asks for 50 town pages.

### 3c. Make the changes

**If the website's files are here** (a code folder, an exported site, or a CMS you can reach with a connection): list the files you will change in a few lines, show the diff of every change, and ask "Make these changes? (yes / no)". Only on yes, edit the files. Then show what changed. Never publish, deploy or push without asking first. Add each new page to the sitemap if the site has one built by hand.

**If not** (Wix, Squarespace, a WordPress you cannot reach): give every fix ready to paste, grouped by page, and say exactly where it goes (for example "Page title field in the SEO settings of the Services page").

## 4. Hand over

Finish with: what you changed, what they still do themselves (in order), and when to run `/seo` again (about 4 to 6 weeks after the changes go live, with a fresh Search Console export, to see what moved).

## Rules

- Never invent data: no made-up rankings, search volumes, traffic, scores, reviews or prices. If you did not see it, say you did not see it.
- Say clearly which numbers are real (from Search Console or a tool the person has) and which are not measured.
- Never promise a ranking, a date or more customers.
- Never change, publish or deploy without showing the diff and getting a yes.
- Plain words. No jargon unless you explain it in the same sentence.
