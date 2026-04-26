# Authentication

ConnectSafely uses [bearer-token authentication](https://datatracker.ietf.org/doc/html/rfc6750). One header, one value.

## Get a key

https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=docs-auth

Keys belong to your account. They have access to whichever LinkedIn accounts you've connected in the dashboard.

## Use the key

Send it as the `Authorization` header on every request:

```
Authorization: Bearer <YOUR_API_KEY>
```

### curl

```bash
curl -X POST https://api.connectsafely.ai/linkedin/account/status \
  -H "Authorization: Bearer $CONNECTSAFELY_API_KEY"
```

### Python (requests)

```python
import os, requests
session = requests.Session()
session.headers["Authorization"] = f"Bearer {os.environ['CONNECTSAFELY_API_KEY']}"
session.headers["Content-Type"] = "application/json"
r = session.post("https://api.connectsafely.ai/linkedin/profile", json={"profileId": "williamhgates"})
r.raise_for_status()
print(r.json())
```

### TypeScript (fetch)

```ts
const res = await fetch("https://api.connectsafely.ai/linkedin/profile", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.CONNECTSAFELY_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ profileId: "williamhgates" }),
});
```

## Multiple LinkedIn accounts

If you've connected more than one LinkedIn account to your ConnectSafely workspace, each request may include an `accountId` in the body. If you omit it, the API uses your default account.

```json
{ "profileId": "williamhgates", "accountId": "<24-char-hex>" }
```

Fetch the list of accounts via [`GET /linkedin/account/status`](https://connectsafely.ai/docs).

## Don't commit your key

Use `.env` (this repo's `.gitignore` already excludes it) and load via `os.environ` / `process.env`. Rotate from the dashboard if exposed.
