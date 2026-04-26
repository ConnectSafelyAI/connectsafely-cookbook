# prospect-researcher

Get an API key: https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=skill-prospect-researcher

Turns a LinkedIn profile URL into a one-page outreach brief. Two API calls, no other setup.

```bash
cp ../../.env.example .env && $EDITOR .env
pip install -r requirements.txt
python example.py https://www.linkedin.com/in/williamhgates/
```

See [SKILL.md](SKILL.md) for the full reference and [sample-output.md](sample-output.md) for what a real run produces.

## Use it from Claude

Drop this whole folder into your Claude Skills directory (`~/.claude/skills/` or your project's `.claude/skills/`). Claude will pick it up via the frontmatter in `SKILL.md`. From there:

> Research https://www.linkedin.com/in/williamhgates/ for me — I want to send a connection request.

Claude will run `example.py`, parse the brief, and use it to draft your outreach.

## Use it from the shell

The script prints Markdown to stdout, so you can pipe it:

```bash
python example.py https://www.linkedin.com/in/williamhgates/ > brief.md
python example.py https://www.linkedin.com/in/williamhgates/ --json | jq '.suggested_dm'
```

## Tier

Paid only. $10/month entry tier. New keys get a trial. See [../../docs/pricing.md](../../docs/pricing.md).
