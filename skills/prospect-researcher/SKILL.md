---
name: prospect-researcher
description: Research a LinkedIn prospect from their profile URL. Returns a structured Markdown brief with their current role, recent posts, conversation hooks, and a draft outreach DM. Use when the user provides a LinkedIn profile URL and asks for context, talking points, or a personalized opener for cold outreach, sales prospecting, or recruiting.
---

# prospect-researcher

Turn any LinkedIn URL into a one-page outreach brief in two API calls. Pulls the profile (name, headline, current role, location, experience) and the last five posts, then formats them into Markdown sections with three conversation hooks and a 280-character DM draft.

## Required env vars

| Variable | Purpose |
| --- | --- |
| `CONNECTSAFELY_API_KEY` | Your ConnectSafely API key. [Get one](https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=skill-prospect-researcher). |
| `CONNECTSAFELY_ACCOUNT_ID` | Optional. Defaults to the default account on your key. |

## Quickstart

```bash
cp ../../.env.example ../../.env       # then paste your CONNECTSAFELY_API_KEY
python3 -m pip install -r requirements.txt
python3 example.py https://www.linkedin.com/in/williamhgates/
```

The script auto-loads `.env` from this folder or any parent (so a single `.env` at the repo root covers every skill). You can also `export CONNECTSAFELY_API_KEY=…` directly in your shell — real environment variables always win over `.env`.

Pass `--json` to emit machine-readable output instead of Markdown:

```bash
python3 example.py https://www.linkedin.com/in/williamhgates/ --json
```

## Expected output

A Markdown brief with these sections:

- **Snapshot** — name, headline, location, current company, connection degree, follower count.
- **Background** — top three roles from experience.
- **Recent activity** — last five posts with engagement counts and links.
- **Conversation hooks** — three openers grounded in their posts and role.
- **Suggested DM** — a 280-char outreach draft you can edit and send.

See [sample-output.md](sample-output.md) for a real run.

## Customization

- `--posts N` — number of recent posts to fetch (1–20, default 5).
- `--json` — emit JSON instead of Markdown.
- `--include-skills` / `--include-education` — pull additional sections from the profile (no extra rate-limit cost; same call).

## Endpoints used

- [`POST /linkedin/profile`](https://connectsafely.ai/docs) — fetch name, headline, experience, location. Limited to 120 unique profiles/day per LinkedIn account; cached responses do not count.
- [`POST /linkedin/posts/latest`](https://connectsafely.ai/docs) — fetch the last N posts (max 20).

Both endpoints accept a `profileId` (the URL slug, e.g. `williamhgates` from `linkedin.com/in/williamhgates/`). The script extracts this from the URL automatically.

## Tier notes

API access requires a paid plan ($10/month Ultimate Outreach is the entry tier). New accounts get a trial. There is no free API tier — the "free" plan on the pricing page is for the post-boosting product only. See [docs/pricing.md](../../docs/pricing.md).

## Failure modes handled

- Missing `CONNECTSAFELY_API_KEY` → exit 2 with a link to get one.
- Malformed LinkedIn URL → exit 2 with the expected format.
- 401 (bad key) → exit 1 with "your API key was rejected".
- 429 (rate limited) → exit 1 with the reset time from `X-RateLimit-Reset`.
- 403 (trial expired / no subscription) → exit 1 with the upgrade link.
- Any other non-2xx → exit 1 with the response body.
