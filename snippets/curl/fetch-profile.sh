#!/usr/bin/env bash
# Fetch a single LinkedIn profile by public id.
# Endpoint: POST /linkedin/profile — https://connectsafely.ai/docs
set -euo pipefail

: "${CONNECTSAFELY_API_KEY:?set CONNECTSAFELY_API_KEY (https://connectsafely.ai/api-key)}"

PROFILE_ID="${1:-williamhgates}"

curl -sS -X POST https://api.connectsafely.ai/linkedin/profile \
  -H "Authorization: Bearer $CONNECTSAFELY_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"profileId\": \"$PROFILE_ID\", \"includeExperience\": true}" \
  | python3 -m json.tool
