# podcast-skill

**Claude can listen to any episode and learn from it.**

Give Claude a YouTube link, an Apple Podcasts or Spotify episode, a podcast feed or an audio file link, or a whole list of them. It gets the words, reads all of it, learns the method the episode teaches, and saves it as a skill you keep.

- Drop in a sales podcast and ask: *Check my sales call against what this episode teaches.*
- Drop in an episode on offers and ask: *Rewrite my offer the way this episode teaches.*

**[Download podcast-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/podcast-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Paste this link and type **install this skill**: `https://github.com/alexgodlewski/ai-skills/releases/latest/download/podcast-skill.md`
   (Or download `podcast-skill.md`, drag it in and type **set this up**.)
3. Paste a podcast link and say: *Listen to this, learn what it teaches, and turn it into a skill I can use forever.*

## How it gets the words

- **YouTube with captions:** uses the captions. Free and fast.
- **No captions, and podcasts:** it downloads the audio and turns it into text. You choose: free on your own computer (faster-whisper, about 150 MB, slower), or with your own OpenAI key (about 0.3 to 0.6 cents a minute, so about 18 to 36 cents for an hour, and the audio is sent to OpenAI).
- **Spotify:** Spotify audio is protected. It finds the same show's public feed and matches the episode. Shows that are only on Spotify cannot be read. Use the YouTube link or the feed instead.

## Limits

- It learns what is said, not what is shown on screen.
- Machine text can get names and numbers wrong. Check the key numbers.
- A podcast is one person's method. It does not prove the method works for your business.
- Each skill is a file you can open, edit or delete. Many skills at once make Claude's list long, so merge episodes on one topic.

The source is right here: [`SKILL.md`](SKILL.md) and [`transcript.py`](transcript.py). It builds on [youtube-skill](../youtube-skill).

Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
