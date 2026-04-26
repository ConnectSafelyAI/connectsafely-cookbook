# ConnectSafely Cookbook

Working examples for the [ConnectSafely.ai](https://connectsafely.ai) LinkedIn automation API — Claude Skills, MCP recipes, and integration snippets that you can run with one API key.

[![test-skills](https://github.com/ConnectSafelyAI/connectsafely-cookbook-/actions/workflows/test-skills.yml/badge.svg)](https://github.com/ConnectSafelyAI/connectsafely-cookbook-/actions/workflows/test-skills.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Get an API key:** [connectsafely.ai/api-key](https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=readme)

API access starts at $10/month (Ultimate Outreach plan). The free tier is limited to scheduled post-boosting and does not include API access — see [docs/pricing.md](docs/pricing.md) for the breakdown.

---

## Quickstart

```bash
git clone https://github.com/ConnectSafelyAI/connectsafely-cookbook-.git
cd connectsafely-cookbook-/skills/prospect-researcher
cp ../../.env.example .env       # then paste your CONNECTSAFELY_API_KEY
pip install -r requirements.txt
python example.py https://www.linkedin.com/in/williamhgates/
```

---

## Skills

Reusable [Claude Skills](https://docs.claude.com/en/docs/agents/skills) you can drop into any agent.

| Skill | What it does |
| --- | --- |
| [prospect-researcher](skills/prospect-researcher/) | Turns a LinkedIn URL into a structured outreach brief with conversation hooks |
| [_template](skills/_template/) | Starting point for new skills |

More coming. See [issues labeled `skill-request`](https://github.com/ConnectSafelyAI/connectsafely-cookbook-/issues?q=label%3Askill-request) for what the community is asking for.

---

## Other recipes

| Folder | What's there |
| --- | --- |
| [mcp/](mcp/) | Using the ConnectSafely MCP server with Claude, Cursor, and other clients |
| [n8n/](n8n/) | n8n workflow JSON exports |
| [make/](make/) | Make.com blueprint exports |
| [snippets/](snippets/) | Single-purpose code snippets (Python, TypeScript, curl) |
| [docs/](docs/) | Cookbook guides: [auth](docs/auth.md), [rate limits](docs/rate-limits.md), [errors](docs/errors.md), [pricing](docs/pricing.md) |

---

## Contributing

Built something useful? [Open a PR](CONTRIBUTING.md). The bar is:

- Runs end-to-end with only an API key
- Has a committed sample output
- Links every endpoint it calls back to the [API docs](https://connectsafely.ai/docs)

Issue templates: [request a skill](.github/ISSUE_TEMPLATE/skill-request.md) · [report a broken skill](.github/ISSUE_TEMPLATE/broken-skill.md) · [share what you built](.github/ISSUE_TEMPLATE/share-skill.md)

---

## License

MIT — see [LICENSE](LICENSE).
