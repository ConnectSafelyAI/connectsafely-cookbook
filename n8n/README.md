# n8n workflows

Importable n8n workflow exports that use the ConnectSafely API.

Get an API key: https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=n8n

There is also a community n8n node: https://github.com/connectsafely/N8N_Package_ConnectSafely

## Contributing

Each workflow lives in its own subfolder with:

- `workflow.json` — exported from n8n's UI (Settings → Download).
- `README.md` — what it does, what nodes it uses, env vars / credentials needed.
- `screenshot.png` (optional) — the canvas view.

Strip credentials before exporting. Use n8n environment variables or credentials, not hardcoded keys.
