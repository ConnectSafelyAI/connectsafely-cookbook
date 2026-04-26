# Rate limits

LinkedIn is the underlying network, so most limits exist to keep your account safe — not to throttle the API itself. Each LinkedIn account has its own quota.

## Per-action limits

| Action | Limit | Window | Scope |
| --- | --- | --- | --- |
| Profile fetch | 120 unique profiles | rolling 24h | per LinkedIn account (cached fetches do not count) |
| Connection requests | 90 | week (resets Mon 00:00 UTC) | per LinkedIn account |
| Direct messages | 100 | day | per LinkedIn account |
| Comments | 100 | day | per LinkedIn account |
| Follows / unfollows | 100 | day | per LinkedIn account |
| Group members | 1,000 | day | per LinkedIn account |

These are pulled from the public docs — check https://connectsafely.ai/docs for the canonical numbers before relying on them in production.

## Response headers

Every response includes:

| Header | Meaning |
| --- | --- |
| `X-RateLimit-Action` | Which action category this counts against (FOLLOW, CONNECT, COMMENT, MESSAGE, …) |
| `X-RateLimit-Limit` | Max actions in the current window |
| `X-RateLimit-Used` | How many you've consumed |
| `X-RateLimit-Remaining` | What's left |
| `X-RateLimit-Reset` | When the window resets (ISO-8601) |

Read these on success too — not just on 429s — so you can pace yourself.

## Handling 429

A 429 response looks like:

```json
{
  "success": false,
  "error": "Rate limit exceeded for CONNECT: 90/90 used. Resets at 2026-04-28T00:00:00Z",
  "holdUntil": "2026-04-27T15:42:11Z"
}
```

`holdUntil` shows up on connection-request 429s when LinkedIn has put the account on a temporary hold. **Do not retry until that timestamp.** Hammering through a hold can extend it.

### Pattern

```python
if r.status_code == 429:
    reset = r.headers.get("X-RateLimit-Reset")
    raise RuntimeError(f"rate limited; resets at {reset}")
```

For long-running scripts, sleep until the reset rather than retrying with backoff:

```python
from datetime import datetime, timezone
import time

reset = datetime.fromisoformat(r.headers["X-RateLimit-Reset"].replace("Z", "+00:00"))
time.sleep(max(0, (reset - datetime.now(timezone.utc)).total_seconds()) + 5)
```

## Pagination

`POST` endpoints that return lists accept `start`, `count`, and `paginationToken` in the body. Responses include:

```json
{
  "pagination": {
    "start": 0,
    "count": 25,
    "total": 412,
    "hasNextPage": true,
    "nextPaginationToken": "…"
  }
}
```

Pass `nextPaginationToken` back in the next request body to walk the cursor.
