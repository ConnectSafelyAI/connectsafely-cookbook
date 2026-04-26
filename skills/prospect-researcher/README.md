# prospect-researcher — LinkedIn Prospect Research as a Claude Skill

Turn any LinkedIn profile URL into a structured outreach brief in two API calls. Designed for **sales prospecting**, **AI sales agents**, and **personalized cold outreach** workflows.

**Get a ConnectSafely API key:** [connectsafely.ai/api-key](https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=skill-prospect-researcher)

---

## What it does

Given a LinkedIn URL like `https://www.linkedin.com/in/williamhgates/`, this skill:

1. Fetches the profile (name, headline, current role, location, follower count, experience).
2. Fetches the last five posts (likes, comments, content, links).
3. Generates three **conversation hooks** grounded in the prospect's recent activity.
4. Drafts a 280-character **outreach DM** you can edit and send.

Output is a clean Markdown brief — easy to read, easy to pipe into other tools.

---

## Quickstart

```bash
cp ../../.env.example ../../.env       # then paste your CONNECTSAFELY_API_KEY
python3 -m pip install -r requirements.txt
python3 example.py https://www.linkedin.com/in/williamhgates/
```

`.env` is auto-loaded from this folder or any parent — one `.env` at the repo root works for every skill.

See [SKILL.md](SKILL.md) for the full reference and [sample-output.md](sample-output.md) for a real run.

---

## Use it from Claude

Drop this whole folder into your Claude Skills directory (`~/.claude/skills/` or your project's `.claude/skills/`). Claude picks it up automatically via the frontmatter in `SKILL.md`.

> "Research https://www.linkedin.com/in/williamhgates/ for me — I want to send a connection request."

Claude runs `example.py`, parses the brief, and uses it to draft your outreach.

---

## Use it from the shell

The script prints Markdown to stdout, so you can pipe it:

```bash
# Save the brief
python3 example.py https://www.linkedin.com/in/williamhgates/ > brief.md

# Extract the suggested DM as JSON
python3 example.py https://www.linkedin.com/in/williamhgates/ --json | jq -r '.suggested_dm'

# Pull more posts (1-20)
python3 example.py https://www.linkedin.com/in/williamhgates/ --posts 10

# AI-draft the DM with Claude (needs ANTHROPIC_API_KEY in env or .env)
python3 example.py https://www.linkedin.com/in/williamhgates/ --ai claude

# Or with OpenAI (needs OPENAI_API_KEY)
python3 example.py https://www.linkedin.com/in/williamhgates/ --ai openai
```

Without `--ai` the suggested DM is a deterministic template. With `--ai claude` or `--ai openai` it's drafted by `claude-haiku-4-5` or `gpt-4o-mini` over plain HTTP — no extra dependencies. Missing key or failed call → falls back to the template and warns on stderr.

---

## Endpoints used

| Endpoint | Purpose | Limit |
| --- | --- | --- |
| [`POST /linkedin/profile`](https://connectsafely.ai/docs) | Profile + experience + location | 120 unique profiles/day per account (cached fetches don't count) |
| [`POST /linkedin/posts/latest`](https://connectsafely.ai/docs) | Last N posts | 20 max per call |

Both calls use the LinkedIn URL slug as `profileId`. The script extracts it for you.

---

## Tier

Paid only. **$10/month entry tier** (Ultimate Outreach). New keys receive a trial. See [../../docs/pricing.md](../../docs/pricing.md).

---

## Related skills

- [_template](../_template/) — start your own skill from this format.
