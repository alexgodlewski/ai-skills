# outbound

**Type `/outbound` and your website. Claude builds an assembly line of agents that finds leads, finds their emails, writes the emails and gets them ready to send.**

It reads your website and writes your ideal customer profile: who buys, where they are and what problems they have. Then four teams of agents work in waves:

1. **Finders** search the web for businesses that match (and use Apify Google Maps if you have a token).
2. **Email finders** look on each contact, about and team page for the real email. If they can only guess from a pattern, they mark it as a guess.
3. **Writers** write one personal email per lead in your voice, with a humanizer pass.
4. **The sender** makes Gmail drafts if the Gmail connector is on, and always writes a CSV you can import.

You choose the size of each team: `/outbound yourwebsite.com 5/5/5/2`, or just say "build me 100 agents" and it splits them 30/30/30/10. The default is small: 3/3/3/1.

Everything is saved in an `outbound/` folder (leads with a score, the emails, a run log), so a big run can stop and pick up again.

**It never sends.** "Ready to send" means drafts and a CSV. Mail providers punish new senders who blast cold email, and the law (CAN-SPAM in the US, GDPR in Europe) needs a real sender address and an easy way to opt out. Every email has both. This is not legal advice.

**[Download outbound-skill.md](https://github.com/alexgodlewski/ai-skills/releases/latest/download/outbound-skill.md)**

## Install (30 seconds)

1. Open the Claude desktop app and click the **Code** tab.
2. Drag `outbound-skill.md` in and type **set this up**.
3. Type `/outbound yourwebsite.com`.

For the best emails, also install [`leads`](../leads) (it has the cold email writer and the humanizer). Outbound works without it, with plainer emails.

## What to know first

- Big teams use a lot of Claude usage. Test with the default size first.
- Claude Code runs agents in waves, so a big team takes time.
- Each finder returns up to 20 leads by default. 100 agents is a lot of leads, but it is not a promise of thousands. For thousands, run more rounds.
- Emails come from public pages only, so expect gaps. Guesses are marked and are not drafted.
- Claude does not read or answer replies here. That part is yours.

The source is right here: [`SKILL.md`](SKILL.md). Made by [Alex Godlewski](https://www.instagram.com/alexgodlewsky/). More skills: [ai-skills](https://github.com/alexgodlewski/ai-skills).
