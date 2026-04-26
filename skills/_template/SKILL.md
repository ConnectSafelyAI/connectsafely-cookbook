---
name: skill-name-here
description: One or two sentences describing what this skill does, what it returns, and the trigger condition under which Claude should pick it. The description is the only signal Claude uses to decide whether to load this skill, so be specific. Example pattern - "Do X from Y. Returns Z. Use when the user provides <input> and asks for <outcome>."
---

# skill-name-here

What this skill does, in one paragraph. Mention the inputs, the output, and the endpoints it calls.

## Required env vars

| Variable | Purpose |
| --- | --- |
| `CONNECTSAFELY_API_KEY` | Your ConnectSafely API key. Get one at https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=skill |
| `CONNECTSAFELY_ACCOUNT_ID` | (Optional) Specific LinkedIn account on your key. Defaults to your default account. |

## Quickstart

```bash
cp ../../.env.example .env       # then paste your CONNECTSAFELY_API_KEY
pip install -r requirements.txt
python example.py <input-here>
```

## Expected output

Describe the output shape. Reference [sample-output.md](sample-output.md) for a real run.

## Customization

- Knob 1: what it does, how to set it.
- Knob 2: same.

## Endpoints used

- [`POST /linkedin/<endpoint>`](https://connectsafely.ai/docs) — what we use it for.

## Tier notes

Calls out which endpoints require a paid plan vs trial. API access begins at $10/month (Ultimate Outreach).
