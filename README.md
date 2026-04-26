# ConnectSafely Cookbook

Working examples for the [ConnectSafely.ai](https://connectsafely.ai) LinkedIn automation API — Claude Skills, MCP recipes, and integration snippets that you can run with one API key.

[![test-skills](https://github.com/connectsafely/cookbook/actions/workflows/test-skills.yml/badge.svg)](https://github.com/connectsafely/cookbook/actions/workflows/test-skills.yml)

**Get an API key:** https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=readme

API access starts at $10/month (Ultimate Outreach plan). Free tier is limited to scheduled post-boosting and does not include API access — see [docs/pricing.md](docs/pricing.md) for the full breakdown.

## Quickstart

```bash
git clone https://github.com/connectsafely/cookbook.git
cd cookbook/skills/prospect-researcher
cp ../../.env.example .env && $EDITOR .env   # paste your CONNECTSAFELY_API_KEY
pip install -r requirements.txt
python example.py https://www.linkedin.com/in/williamhgates/
```

## Skills

Reusable [Claude Skills](https://docs.claude.com/en/docs/agents/skills) you can drop into any agent.

| Skill | What it does |
| --- | --- |
| [prospect-researcher](skills/prospect-researcher/) | Profile + recent activity → structured outreach brief with conversation hooks |
| [_template](skills/_template/) | Starting point for new skills |

More coming. See [issues labeled `skill-request`](https://github.com/connectsafely/cookbook/issues?q=label%3Askill-request) for what the community is asking for.

## Other recipes

| Folder | What's there |
| --- | --- |
| [mcp/](mcp/) | Using the ConnectSafely MCP server with Claude, Cursor, and other clients |
| [n8n/](n8n/) | n8n workflow JSON exports |
| [make/](make/) | Make.com blueprint exports |
| [snippets/](snippets/) | Single-purpose code snippets by language (Python, TypeScript, curl) |
| [docs/](docs/) | Cookbook guides — [auth](docs/auth.md), [rate limits](docs/rate-limits.md), [errors](docs/errors.md) |

## Contributing

Built something useful? [Open a PR](CONTRIBUTING.md). The bar is: runs end-to-end with only an API key, has a sample output, and links the endpoints used back to [the API docs](https://connectsafely.ai/docs).

- [Request a skill](.github/ISSUE_TEMPLATE/skill-request.md)
- [Report a broken skill](.github/ISSUE_TEMPLATE/broken-skill.md)
- [Share a skill you built](.github/ISSUE_TEMPLATE/share-skill.md)

## License

MIT — see [LICENSE](LICENSE).