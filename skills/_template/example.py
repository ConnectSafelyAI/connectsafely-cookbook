"""Template skill entry point. Replace the body with your own logic."""
from __future__ import annotations

import os
import sys

import requests

API_BASE = "https://api.connectsafely.ai/linkedin"


def main(argv: list[str]) -> int:
    api_key = os.environ.get("CONNECTSAFELY_API_KEY")
    if not api_key:
        print("error: CONNECTSAFELY_API_KEY is not set. Get one at "
              "https://connectsafely.ai/api-key", file=sys.stderr)
        return 2

    if len(argv) < 2:
        print(f"usage: {argv[0]} <input>", file=sys.stderr)
        return 2

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Replace this with your endpoint and payload.
    response = requests.post(f"{API_BASE}/account/status", headers=headers, timeout=30)
    response.raise_for_status()
    print(response.json())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
