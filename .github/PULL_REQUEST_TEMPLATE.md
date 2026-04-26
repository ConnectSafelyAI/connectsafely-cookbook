<!-- Thanks for contributing. Fill in the sections below before requesting review. -->

## What this PR adds

<!-- One sentence: new skill, new MCP recipe, new snippet, fix, etc. -->

## Endpoints used

<!-- List every ConnectSafely endpoint your code calls, linked to the docs page. -->

- [ ] `POST /linkedin/...` — https://connectsafely.ai/docs

## Env vars required

<!-- Beyond CONNECTSAFELY_API_KEY, list anything new and update .env.example. -->

- `CONNECTSAFELY_API_KEY` (always)

## Sample output

<!-- Link to the sample-output.md in your skill folder, or paste a trimmed run here. -->

## Quality checklist

- [ ] Runs end-to-end with only an API key (no DB, no extra services).
- [ ] Handles 401 / 403 / 429 / missing input with clear messages and non-zero exit.
- [ ] `sample-output.md` (or `.json`) is committed.
- [ ] All endpoints I call are linked to https://connectsafely.ai/docs in `SKILL.md`.
- [ ] Signup links in user-facing READMEs use the UTM pattern `?utm_source=github&utm_medium=cookbook&utm_campaign=<context>`.
- [ ] CI passes (or I've explained why it can't run locally).
