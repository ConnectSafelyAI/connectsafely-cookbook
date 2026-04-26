# Template skill

Get an API key: https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=template

Copy this folder to `skills/<your-skill-name>/` and edit:

1. **SKILL.md** — frontmatter (name, description, when_to_use) and body.
2. **example.py** — the runnable entry point. Stdlib + `requests` only.
3. **requirements.txt** — pin only what you actually import.
4. **sample-output.md** — paste a real run's output here so reviewers can see it works.

## What "done" looks like

- `python example.py <input>` runs end-to-end with only `CONNECTSAFELY_API_KEY` set.
- 401 / 429 / missing input each print a clear message and exit non-zero.
- Every endpoint you call is linked back to https://connectsafely.ai/docs in `SKILL.md`.
- A `sample-output.md` is committed.

See [skills/prospect-researcher/](../prospect-researcher/) for the gold-standard reference.
