# Competitor spy: see how any company gets its customers

The open source tool from the SPY reel, and my prompt that turns their best ads into ideas for yours. A free guide by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/).

## The tool

**REM (Reverse Engineer Marketing)**: https://github.com/dansugc/reverse-engineer-marketing

You give it one link. It collects what is public about that company: the ads in the ad libraries (and how long each one has run), the tracking pixels on the site, the SEO pages, the funnel, the founders and Reddit. Then it writes a report, and every claim links to the proof it came from. It is open source (MIT license) and runs on your own computer. It was made by DansUGC, not by me. Read its page before you run it.

## Step 1 run it with no keys

1. **Install Node.js 22** from nodejs.org if you do not have it.
2. **Open a terminal** and type: `npx reverse-engineer-marketing competitor.com` (use your competitor's website).
3. **What you get without keys:** the website, tracking pixels (also inside Google Tag Manager), SEO and sitemaps, the Wayback history of their homepage, App Store and Hacker News. The report lands in a folder called `rem-reports`.
4. **Try the demo first** if you want to see it with no setup: `npx reverse-engineer-marketing demo`.

## Step 2 use your Claude plan

Type `npx reverse-engineer-marketing web`. A local page opens. Paste a link and pick Claude Code as the report writer. It uses the Claude subscription you already pay for, not an API key.

## Step 3 add the ads (optional, paid)

The ad libraries (Meta, Google, LinkedIn), social stats, founders and Reddit need a Scrape Creators key. The README says a run costs about 25 to 50 of their credits. Check their price before you buy.

## Step 4 run it on your 3 biggest competitors

Run it once for each. Then open Claude, attach the three `report.md` files and paste this prompt.

```text
You are my ad strategist. I attached marketing reports of my 3 biggest competitors.

My business: [what you sell, who it is for, the price].

1. List the ads that ran the longest in each report. Long running ads are usually the ones that make money.
2. For each of those ads, write what it promises, who it talks to, and the first line.
3. Find what the winners have in common.
4. Write 10 ad ideas for MY business that use the same angle, in my words. Do not copy their text.
5. Tell me which 3 ideas to test first, and why.

Quote the report for every claim. If something is not in the reports, say so.
```

## Good to know

1. **It only reads public data.** Paused ads, pixels and sitemaps are things anyone can see. It does not log in anywhere.
2. **Unknowns are listed.** What REM could not see is marked as unknown, with a link to check it yourself.
3. **Copy angles, not words.** Use what works as an idea, then write your own ad.

Questions? Reply to my DM.
