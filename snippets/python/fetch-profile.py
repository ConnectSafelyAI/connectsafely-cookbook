"""Fetch a single LinkedIn profile by public id.

Endpoint: POST /linkedin/profile — https://connectsafely.ai/docs
Get a key: https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=snippet
"""
import os
import sys

import requests


def main(profile_id: str) -> int:
    api_key = os.environ["CONNECTSAFELY_API_KEY"]
    r = requests.post(
        "https://api.connectsafely.ai/linkedin/profile",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"profileId": profile_id, "includeExperience": True},
        timeout=30,
    )
    r.raise_for_status()
    print(r.json())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "williamhgates"))
