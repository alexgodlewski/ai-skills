# The Reel Machine: How Claude Made 10 Reels in a Day

A free guide by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). This is the real setup I use, in simple steps, with the prompts you can paste into Claude Code. In one day, Claude made ten reels and scheduled them one every 90 minutes through [Setor](https://setor.ai).

Be honest with yourself before you start: this is a build-it-yourself setup, not a one-click button. It is for people who are happy to work in a terminal with Claude Code and who will watch every reel before it goes out.

## The idea in one line

Find reels that already worked, copy the script almost 1 to 1 and change one thing, give it your voice and your face with AI, let Claude edit and caption it, then schedule it.

## What you need

| Tool | What it does | Cost |
|---|---|---|
| [Claude Code](https://claude.com/product/claude-code) | The brain. Writes the scripts, edits the video, runs every step | A paid Claude plan |
| [HyperFrames](https://github.com/heygen-com/hyperframes) | Turns HTML into video, so Claude can "edit" by writing code | Free, open source |
| [ElevenLabs](https://elevenlabs.io) | Clones your voice | Paid plan needed for a voice clone. Check their pricing page |
| [HeyGen](https://www.heygen.com) | AI avatar video of you, from your voice | Paid plan. Check their pricing page |
| [Setor](https://setor.ai) | Schedules the reels, and runs the comment to DM flow. It connects to Claude through MCP and posts to Instagram and Facebook | Setor plan |
| A way to see creators' reels | To find outliers. A scraping API or just a spreadsheet and your own eyes | Varies |

Costs change, so look at each pricing page today. Voice credits and avatar minutes are what you use up most. A computer with enough memory for rendering also helps. Rendering is the slow part, and the machine runs a few jobs at a time on purpose.

Use your own voice and your own face, with their consent steps. Do not clone other people.

## The 8 steps

### Step 1. Find outlier reels

An **outlier** is a reel that did much better than that creator normally does:

`outlier score = views of the reel / the creator's median views`

If a creator usually gets 10,000 views and one reel got 200,000, that reel scores 20. A high score means the idea or the hook was the reason, not just the audience size. Pick creators in your topic, list their last 30 to 50 reels, and keep the ones with the highest score.

Prompt for Claude Code:

```
Here is a list of reels from creators in my niche (handle, link, views, date).
Work out each creator's median views, then give every reel an outlier score
(views divided by that creator's median). Show the top 15 as a table.
For each, write one line on why it probably worked: the hook, the topic, or the format.
```

### Step 2. Copy the script almost 1 to 1, and change one thing

Get the transcript of the best outlier (any transcription tool, or Whisper). Keep the structure, the pacing and the order. Change exactly ONE thing: the number, the topic angle, the tool, or the example. Mark that one change so you know what you are testing.

Prompt:

```
This is the transcript of a reel that got a high outlier score:
[paste transcript]

Write my version. Rules:
- Keep the same structure, same order of ideas, same length (within 10 percent).
- Change exactly ONE thing: [the thing, for example "use my 10,000 hours with Claude instead of their number"].
- Write in plain English at a 6th grade level. No idioms. No em dashes.
- Do not invent facts or numbers. Only use what is true about me: [facts].
- End with one call to action: "Comment WORD and I'll send you X". Pick one real word.
Show the script, then a list of what I changed against the original.
```

Why copy so closely: the structure already proved itself. You are not copying the creator's words, you are using a proven shape for your own idea and your own facts. Always make it true to you.

### Step 3. Clone your voice (ElevenLabs)

Record a clean sample of your voice, upload it to ElevenLabs, and make a voice clone of yourself. Then ask Claude Code to turn each script into audio with it. You need an API key from your ElevenLabs account. Keep the key in a `.env` file. Never paste it into a chat or a public repo.

Prompt:

```
Read script.txt. Write a small Python script that sends it to the ElevenLabs
text-to-speech API with my voice id (in .env as ELEVEN_VOICE_ID, key as ELEVEN_API_KEY)
and saves voice.mp3. Read the official ElevenLabs docs first so the endpoint and
parameters are right. Then run it and tell me how long the audio is.
```

### Step 4. Make the AI avatar video (HeyGen)

Make a digital twin or avatar of yourself in HeyGen (follow their consent steps). Then create a vertical 9:16 video where your avatar speaks your voice file. If you use the HeyGen connector in Claude, Claude can start the video for you. Otherwise, make it in HeyGen and download it.

Prompt (with the HeyGen connector on):

```
Create a 9:16 video with my avatar speaking the audio in voice.mp3.
Use my avatar look called "[your look name]". When it is ready, give me the link
to the finished file and wait for me to check it.
```

Always watch the result. If the lips or hands look wrong, remake it.

### Step 5. Edit with Claude Code and HyperFrames

[HyperFrames](https://github.com/heygen-com/hyperframes) renders a web page (HTML) as a video. So Claude edits the reel by writing HTML: the avatar video as the base, then titles, cards, logos, zooms and sound effects, each placed on the exact spoken word.

First get word timings from the audio (Whisper or similar), so every animation lands on the right word, not on a guessed second.

Prompt:

```
Use the hyperframes skill. Make a new 9:16 project for this reel.
Base video: aroll.mp4. Script and word timings: words.json.
Edit it like a pro short-form editor:
- a big hook title on a solid box in the first frame, gone after the hook
- a card or real logo each time I name a tool or a number
- a small zoom on the key sentence
- every animation starts on a spoken word, not on a time in seconds
- keep my face clear of every graphic
Use real logos and real screenshots where you can. No em dashes in any text.
Then run the HyperFrames check and fix every problem it finds. Do not render yet.
```

### Step 6. Captions

Captions are on screen for the whole reel. Keep them 4 to 5 words, on one line, and never end a caption on a small word like "of", "the" or "to". Break at the end of every sentence.

Prompt:

```
Add captions from words.json. Rules: 4 to 5 words per caption, one line, never end on
of / the / to / a / if / I, never cross a sentence end. Style: lime (#C6FF3D) pill,
black bold text, popping in with a quick scale. Place them where they do not cover
my face or a key graphic.
```

(Use your own colors and style. The point is the rules.)

### Step 7. Check and render

Open the preview and watch the whole reel yourself. Then render.

Prompt:

```
Take a frame every second and check each one: is any text cut off, is my face covered,
is any caption wrong, does any dash show up on screen? List every problem with the
time it happens. Fix them. Then render the final 9:16 video at 1080 by 1920.
```

Then you decide. Nothing goes out until you say yes.

### Step 8. Schedule through Setor

[Setor](https://setor.ai) is my AI DM tool. It connects to Claude through MCP, and it can publish and schedule posts to Instagram and Facebook. Connect it to Claude from your Setor account, then Claude can schedule all ten reels in one go.

The order that works:

1. Upload each finished video to a public file link Setor can read.
2. Write the caption (short is fine, and it works for Threads too).
3. Set up the comment to DM flow for the keyword, so people who comment get your free resource.
4. Schedule the reels one every 90 minutes.
5. Post to Instagram and Facebook.

Prompt:

```
I have 10 finished reels (file links and captions in plan.md). With the Setor connector:
1. Make one comment-to-DM flow per reel for its keyword, and send the lead magnet.
2. Schedule the 10 reels, one every 90 minutes, starting [date and time, my time zone],
   to Instagram and Facebook.
Show me the full table (slot, reel, caption, keyword) first. Do not publish anything
until I say yes.
```

Why one every 90 minutes: ten reels at once look like spam to people and may hurt your reach. Spreading them out gives each one its own time.

## Rules I follow

- I watch every reel before it goes out. Claude never publishes without my yes.
- One idea, one keyword, one free resource per reel.
- No invented numbers or facts.
- Real logos and real screenshots, not fake ones.
- I clean up the big video files after each reel, so the disk does not fill up.

## What can go wrong

- **The avatar looks fake:** use a better source photo or video, and shorter reels.
- **Scripts feel the same:** always change one thing, and add something new each time.
- **A reel does not take off:** that is normal. Make more, look at which ones worked, and find the next outlier.
- **Platform limits:** publishing tools have limits on how fast and how many posts you can send. Spread them out.

## More free stuff

My free Claude skills: [github.com/alexgodlewski/ai-skills](https://github.com/alexgodlewski/ai-skills)
