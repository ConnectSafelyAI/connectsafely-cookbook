"""Template skill entry point. Replace the body with your own logic."""
from __future__ import annotations

import os
import pathlib
import sys

import requests


def _load_dotenv() -> None:
    """Load KEY=VALUE from the nearest .env. Real env vars always win."""
    here = pathlib.Path(__file__).resolve().parent
    for directory in [here, *here.parents]:
        env_file = directory / ".env"
        if env_file.is_file():
            for raw in env_file.read_text().splitlines():
                line = raw.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip().lstrip("export ").strip()
                value = value.strip().strip('"').strip("'")
                if key and key not in os.environ:
                    os.environ[key] = value
            return


_load_dotenv()

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
