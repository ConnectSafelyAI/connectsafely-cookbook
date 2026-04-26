# Contributing

Thanks for considering a contribution. This cookbook only ships things that actually run, so the quality bar is concrete. Read this before opening a PR.

## What belongs here

- **Skills** — A `SKILL.md` plus a runnable example that solves one specific job (research a prospect, score an inbound lead, draft a comment). Use [skills/_template/](skills/_template/) as the starting point.
- **MCP recipes** — Configs and prompts for using the ConnectSafely MCP server from Claude, Cursor, Continue, etc.
- **Workflow exports** — n8n JSON and Make.com blueprints that import cleanly and run with only an API key.
- **Snippets** — Single-purpose code in `snippets/<language>/` for one endpoint or one task.

What does *not* belong here: marketing pages, screenshots without code, anything that requires a paid third-party service beyond a ConnectSafely API key, or scraping workarounds that bypass the official API.

## Quality bar

Every contribution must:

1. **Run with only an API key.** No DB setup, no extra accounts, no manual steps beyond `cp .env.example .env`. If a skill needs more, document it loudly at the top of the README.
2. **Cite the endpoints it calls.** Link each ConnectSafely endpoint to its page on https://connectsafely.ai/docs. If the endpoint isn't documented, don't use it.
3. **Handle the obvious failure modes.** Missing API key, 401, 429, malformed input — print a clear message and exit non-zero. See [skills/prospect-researcher/example.py](skills/prospect-researcher/example.py) for the pattern.
4. **Include a sample output.** A `sample-output.md` (or `.json`) checked in next to the example so reviewers can see what success looks like without running anything.
5. **Pass CI.** [.github/workflows/test-skills.yml](.github/workflows/test-skills.yml) runs every example weekly. PRs that break it get blocked.

## SKILL.md format

The frontmatter is non-optional and consumed by Claude Skills tooling.

```yaml
---
name: prospect-researcher
description: One sentence. What it does + what it returns.
when_to_use: One sentence. The trigger condition for an agent to pick this skill.
---
```

The body should cover: required env vars, quickstart command, expected output shape, customization knobs, and a "Endpoints used" section that links each call back to the docs. See [skills/_template/SKILL.md](skills/_template/SKILL.md).

## PR process

1. Fork and branch from `main`.
2. Build inside `skills/<your-skill-name>/` (or the appropriate folder).
3. Run your example end-to-end against your own key. Save the output as `sample-output.md`.
4. Open a PR. Fill in [the template](.github/PULL_REQUEST_TEMPLATE.md) — endpoints used, env vars, sample output link.
5. A maintainer will review for the quality bar above. Expect comments; the goal is that your skill works for someone who has never seen it.

## Style

- Python: stdlib + `requests` or `httpx`. No frameworks. Type hints encouraged, not required.
- TypeScript: stdlib `fetch`. Avoid SDKs that pin dependencies.
- Comments only when *why* is non-obvious. Don't explain *what* the code does.
- Plain prose in user-facing copy. No emoji in CTAs.
