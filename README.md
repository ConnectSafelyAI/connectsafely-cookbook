# ConnectSafely Cookbook — LinkedIn API Examples, Claude Skills & MCP Recipes

> Open-source recipes for the **[ConnectSafely.ai](https://connectsafely.ai) LinkedIn API**: ready-to-run Claude Skills, Model Context Protocol (MCP) examples, n8n workflows, and code snippets for LinkedIn automation, outreach, lead research, and AI agents.

[![test-skills](https://github.com/ConnectSafelyAI/connectsafely-cookbook/actions/workflows/test-skills.yml/badge.svg)](https://github.com/ConnectSafelyAI/connectsafely-cookbook/actions/workflows/test-skills.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Claude-Skills-7c3aed)](https://docs.claude.com/en/docs/agents/skills)
[![MCP Compatible](https://img.shields.io/badge/MCP-compatible-2563eb)](https://modelcontextprotocol.io/)

**Get a ConnectSafely API key:** [connectsafely.ai/api-key](https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=readme)

API access starts at **$10/month** (Ultimate Outreach plan). The free plan covers post-boosting only — see [pricing](docs/pricing.md) for the full breakdown.

---

## Table of contents

- [What is this cookbook?](#what-is-this-cookbook)
- [Quickstart](#quickstart)
- [Claude Skills](#claude-skills)
- [Other recipes](#other-recipes)
- [Use cases](#use-cases)
- [FAQ](#faq)
- [Contributing](#contributing)

---

## What is this cookbook?

A growing library of **runnable LinkedIn automation examples** built on the ConnectSafely LinkedIn API. Every recipe runs end-to-end with only a single API key — no databases, no extra services. Designed for:

- **AI agent builders** who need a LinkedIn tool surface for Claude, GPT, or open-source agent frameworks.
- **Growth and RevOps engineers** who automate prospecting, enrichment, and outreach.
- **Developers** integrating LinkedIn data into CRMs, lead-scoring pipelines, or recruiting workflows.

Code is plain Python or TypeScript with stdlib + `requests`/`fetch`. Skip the SDK churn.

---

## Quickstart

Run the reference skill against any public LinkedIn profile in under a minute:

```bash
git clone https://github.com/ConnectSafelyAI/connectsafely-cookbook.git
cd connectsafely-cookbook/skills/prospect-researcher
cp ../../.env.example .env       # then paste your CONNECTSAFELY_API_KEY
python3 -m pip install -r requirements.txt
python3 example.py https://www.linkedin.com/in/williamhgates/
```

You'll get a Markdown outreach brief on stdout. See the [full sample output](skills/prospect-researcher/sample-output.md).

---

## Claude Skills

Reusable [Claude Skills](https://docs.claude.com/en/docs/agents/skills) — drop-in agent capabilities you can use from Claude Desktop, Claude Code, or the Anthropic API.

| Skill | What it does | Endpoints |
| --- | --- | --- |
| [prospect-researcher](skills/prospect-researcher/) | Turn a LinkedIn profile URL into a structured outreach brief with conversation hooks and a draft DM | `/linkedin/profile`, `/linkedin/posts/latest` |
| [_template](skills/_template/) | Starting point for new skill contributions | — |

More skills are on the way. Vote on what's next or request your own under [issues labeled `skill-request`](https://github.com/ConnectSafelyAI/connectsafely-cookbook/issues?q=label%3Askill-request).

### Use a skill from Claude

```bash
mkdir -p ~/.claude/skills
cp -R skills/prospect-researcher ~/.claude/skills/
# In Claude: "Research https://www.linkedin.com/in/<id>/ for me"
```

Claude reads the frontmatter in `SKILL.md` and routes to the skill automatically.

---

## Other recipes

| Folder | What's there |
| --- | --- |
| [`mcp/`](mcp/) | **Model Context Protocol** server configs and prompts for Claude Desktop, Cursor, Continue, and other MCP-aware clients |
| [`n8n/`](n8n/) | **10 importable n8n workflows** for LinkedIn automation (AI connection requests, commenter→HubSpot, post rewriter, more) |
| [`make/`](make/) | **9 Make.com scenarios** with public blueprint URLs (AI outreach, profile-visitors→HubSpot, keyword→DM, more) |
| [`snippets/`](snippets/) | Single-purpose code samples in [Python](snippets/python/), [TypeScript](snippets/typescript/), and [curl](snippets/curl/) |
| [`docs/`](docs/) | Cookbook guides: [auth](docs/auth.md), [rate limits](docs/rate-limits.md), [errors](docs/errors.md), [pricing](docs/pricing.md) |

---

## Use cases

The ConnectSafely API powers workflows like:

- **AI sales prospecting agents** — give an AI agent the ability to research a prospect before drafting an email.
- **LinkedIn lead enrichment** — hydrate a CRM record with current title, company, headline, and recent activity.
- **Inbound lead scoring** — score signups by ICP fit using profile + company data.
- **Recruiter sourcing** — search candidates, check mutual connections, send InMail.
- **Auto-comment growth loops** — comment on creators in your niche from a managed LinkedIn account.
- **Personalized outreach at scale** — generate openers grounded in the prospect's recent posts.
- **Warm-intro discovery** — find first-degree connections at a target company.

Each is one or two API calls. The [`skills/`](skills/) folder turns them into copy-paste agent capabilities.

---

## FAQ

### What is the ConnectSafely API?

A managed LinkedIn API that wraps the most common automation actions — fetching profiles, sending messages, posting, commenting, searching — behind a single bearer-token endpoint. Your LinkedIn account stays connected through ConnectSafely's safety layer (rate-limit pacing, warmup, error recovery).

### Is there a free tier?

The product has a free plan, but it is **scoped to post-boosting only** and does not include API access. API access requires the **Ultimate Outreach** plan at **$10/month**. New accounts receive a trial. See [docs/pricing.md](docs/pricing.md).

### Which LinkedIn endpoints are supported?

Profiles, posts (read, comment, react, repost, search), messaging (DM and InMail), connection requests, follow/unfollow, people and company search, groups, jobs, account analytics, and Sales Navigator threads. Full reference at [connectsafely.ai/docs](https://connectsafely.ai/docs).

### Can I use this with Claude, ChatGPT, or LangChain?

Yes. The skills here ship as Claude Skills, but the underlying scripts are plain Python — wire them into LangChain tools, OpenAI function-calling, or any agent framework. The [`mcp/`](mcp/) folder shows the MCP integration path for Claude Desktop and Cursor.

### How do I avoid getting rate-limited?

Read [`docs/rate-limits.md`](docs/rate-limits.md). Every response includes `X-RateLimit-*` headers — pace off those rather than guessing. Hardest limits: 90 connection requests/week and 120 unique profile fetches/day per LinkedIn account.

### What if a recipe stops working?

Open a [broken-skill issue](.github/ISSUE_TEMPLATE/broken-skill.md). CI runs every skill weekly so we catch most drift early.

---

## Contributing

Built something useful? [Open a PR](CONTRIBUTING.md). The quality bar:

- Runs end-to-end with only an API key
- Has a committed sample output
- Links every endpoint it calls back to the [API docs](https://connectsafely.ai/docs)

Issue templates: [request a skill](.github/ISSUE_TEMPLATE/skill-request.md) · [report a broken skill](.github/ISSUE_TEMPLATE/broken-skill.md) · [share what you built](.github/ISSUE_TEMPLATE/share-skill.md)

---

## Related

- [ConnectSafely API docs](https://connectsafely.ai/docs)
- [ConnectSafely n8n community node](https://github.com/connectsafely/N8N_Package_ConnectSafely)
- [Claude Skills documentation](https://docs.claude.com/en/docs/agents/skills)
- [Model Context Protocol](https://modelcontextprotocol.io/)

---

## License

MIT — see [LICENSE](LICENSE). Use freely in commercial projects.
