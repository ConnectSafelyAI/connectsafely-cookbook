# Errors

## Status codes you'll see

| Code | What it means | What to do |
| --- | --- | --- |
| 200 | Success | — |
| 400 | Bad request — usually a Zod validation error on the body | Read `error.issues` for the offending fields |
| 401 | Missing or invalid API key | Check `CONNECTSAFELY_API_KEY`. Get a new one if needed. |
| 403 | Trial expired or no active subscription | Upgrade or restart trial at https://connectsafely.ai/api-key |
| 404 | Resource not found (profile/post/company doesn't exist or isn't visible) | Confirm the URL/id is correct |
| 429 | Rate limit exceeded | See [rate-limits.md](rate-limits.md) — don't retry until reset |
| 500 | Server error | Retry once with backoff; report if persistent |

## Standard error body

```json
{ "success": false, "error": "human-readable message" }
```

## Validation errors (400)

Zod returns structured issues:

```json
{
  "success": false,
  "error": {
    "name": "ZodError",
    "issues": [
      {
        "code": "invalid_type",
        "expected": "string",
        "received": "undefined",
        "path": ["profileId"],
        "message": "Required"
      }
    ]
  }
}
```

When this happens, look at `path` first — it tells you which field your code missed.

## A reusable error helper (Python)

```python
def call(session, path, payload):
    r = session.post(f"https://api.connectsafely.ai/linkedin{path}", json=payload, timeout=60)
    if r.status_code == 401:
        raise RuntimeError("API key rejected — check CONNECTSAFELY_API_KEY")
    if r.status_code == 403:
        raise RuntimeError("subscription required — see https://connectsafely.ai/api-key")
    if r.status_code == 429:
        reset = r.headers.get("X-RateLimit-Reset", "unknown")
        raise RuntimeError(f"rate limited; resets at {reset}")
    if not r.ok:
        body = r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text
        raise RuntimeError(f"{path} {r.status_code}: {body}")
    return r.json()
```

## Account status errors

If `GET /linkedin/account/status` returns `status: "ERROR"`, the LinkedIn account itself needs attention (re-auth, captcha, etc.). API calls against that account will fail until it's healthy. Surface this to your users early — see [skills/prospect-researcher/example.py](../skills/prospect-researcher/example.py) for the pattern.
