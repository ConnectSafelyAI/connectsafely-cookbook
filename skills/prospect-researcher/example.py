"""Turn a LinkedIn profile URL into a structured outreach brief.

Usage:
    python example.py <linkedin-url> [--posts N] [--json] [--include-skills] [--include-education]

Endpoints:
    POST /linkedin/profile       — https://connectsafely.ai/docs
    POST /linkedin/posts/latest  — https://connectsafely.ai/docs
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from typing import Any

import requests

API_BASE = "https://api.connectsafely.ai/linkedin"
SIGNUP_URL = (
    "https://connectsafely.ai/api-key"
    "?utm_source=github&utm_medium=cookbook&utm_campaign=skill-prospect-researcher"
)
PROFILE_URL_RE = re.compile(r"linkedin\.com/in/([^/?#]+)", re.IGNORECASE)


class ApiError(Exception):
    def __init__(self, message: str, exit_code: int = 1) -> None:
        super().__init__(message)
        self.exit_code = exit_code


def extract_profile_id(url_or_id: str) -> str:
    """Accept a full LinkedIn URL or a bare profileId; return the slug."""
    match = PROFILE_URL_RE.search(url_or_id)
    if match:
        return match.group(1).rstrip("/")
    if "/" in url_or_id or " " in url_or_id:
        raise ApiError(
            f"could not parse a profile id from: {url_or_id!r}\n"
            "expected something like https://www.linkedin.com/in/williamhgates/",
            exit_code=2,
        )
    return url_or_id


def request(session: requests.Session, path: str, payload: dict[str, Any]) -> dict[str, Any]:
    """POST to a ConnectSafely endpoint and translate errors into ApiError."""
    try:
        response = session.post(f"{API_BASE}{path}", json=payload, timeout=60)
    except requests.RequestException as exc:
        raise ApiError(f"network error calling {path}: {exc}") from exc

    if response.status_code == 401:
        raise ApiError(
            "your API key was rejected (401). check CONNECTSAFELY_API_KEY, or get a new key at "
            + SIGNUP_URL
        )
    if response.status_code == 403:
        body = _safe_json(response)
        raise ApiError(
            "access denied (403): "
            + body.get("error", "trial expired or subscription required")
            + f"\nupgrade or restart your trial at {SIGNUP_URL}"
        )
    if response.status_code == 429:
        reset = response.headers.get("X-RateLimit-Reset", "unknown")
        action = response.headers.get("X-RateLimit-Action", "this action")
        raise ApiError(f"rate limit hit for {action}. resets at {reset}.")
    if not response.ok:
        body = _safe_json(response)
        raise ApiError(
            f"{path} returned {response.status_code}: "
            + (body.get("error") if isinstance(body.get("error"), str) else json.dumps(body))
        )
    return response.json()


def _safe_json(response: requests.Response) -> dict[str, Any]:
    try:
        return response.json()
    except ValueError:
        return {"error": response.text[:500]}


def fetch_profile(
    session: requests.Session,
    profile_id: str,
    include_skills: bool,
    include_education: bool,
) -> dict[str, Any]:
    payload = {
        "profileId": profile_id,
        "includeExperience": True,
        "includeGeoLocation": True,
        "includeSkills": include_skills,
        "includeEducation": include_education,
    }
    account_id = os.environ.get("CONNECTSAFELY_ACCOUNT_ID")
    if account_id:
        payload["accountId"] = account_id
    return request(session, "/profile", payload)


def fetch_latest_posts(
    session: requests.Session, profile_id: str, count: int
) -> dict[str, Any]:
    payload: dict[str, Any] = {"profileId": profile_id, "count": count, "includeReposts": True}
    account_id = os.environ.get("CONNECTSAFELY_ACCOUNT_ID")
    if account_id:
        payload["accountId"] = account_id
    return request(session, "/posts/latest", payload)


def build_brief(profile_payload: dict[str, Any], posts_payload: dict[str, Any]) -> dict[str, Any]:
    """Reduce raw API responses to the shape we render in Markdown / JSON."""
    profile = profile_payload.get("profile") or {}
    experience = profile.get("experience") or []
    posts = posts_payload.get("posts") or []

    current_role = experience[0] if experience else {}
    background = experience[:3]

    hooks = _conversation_hooks(profile, posts)
    return {
        "snapshot": {
            "name": _full_name(profile),
            "headline": profile.get("headline"),
            "location": _location(profile),
            "current_role": _role_summary(current_role),
            "connection_degree": profile.get("connectionDegree"),
            "is_premium": profile.get("isPremium", False),
            "follower_count": profile.get("followerCount"),
            "linkedin_url": f"https://www.linkedin.com/in/{profile.get('publicIdentifier', '')}/",
        },
        "background": [_role_summary(role) for role in background if role],
        "recent_posts": [
            {
                "url": p.get("url"),
                "content": (p.get("content") or "").strip(),
                "likes": p.get("numLikes", 0),
                "comments": p.get("numComments", 0),
                "shares": p.get("numShares", 0),
                "is_repost": p.get("isRepost", False),
                "timestamp": p.get("timestamp"),
            }
            for p in posts
        ],
        "conversation_hooks": hooks,
        "suggested_dm": _suggest_dm(profile, hooks),
    }


def _full_name(profile: dict[str, Any]) -> str:
    parts = [profile.get("firstName") or "", profile.get("lastName") or ""]
    return " ".join(p for p in parts if p).strip() or "Unknown"


def _location(profile: dict[str, Any]) -> str | None:
    geo = profile.get("geoLocation") or {}
    if isinstance(geo, dict):
        return geo.get("city") or geo.get("country")
    loc = profile.get("location")
    if isinstance(loc, dict):
        return loc.get("name") or loc.get("city")
    return None


def _role_summary(role: dict[str, Any]) -> str | None:
    if not role:
        return None
    title = role.get("title") or role.get("position")
    company = role.get("companyName") or role.get("company")
    if title and company:
        return f"{title} at {company}"
    return title or company


def _conversation_hooks(profile: dict[str, Any], posts: list[dict[str, Any]]) -> list[str]:
    hooks: list[str] = []

    for post in posts[:3]:
        content = (post.get("content") or "").strip()
        if not content:
            continue
        snippet = content[:140].rsplit(" ", 1)[0]
        if post.get("isRepost"):
            hooks.append(f"They reshared: \"{snippet}…\" — ask what resonated.")
        else:
            hooks.append(f"Reference their post: \"{snippet}…\"")

    headline = profile.get("headline")
    if headline and len(hooks) < 3:
        hooks.append(f"Their headline ({headline}) — ask what's changed in their role recently.")

    experience = profile.get("experience") or []
    if len(experience) >= 2 and len(hooks) < 3:
        prior = _role_summary(experience[1])
        if prior:
            hooks.append(f"Mention their move from {prior} — ask what motivated the change.")

    return hooks[:3] or ["No recent activity to anchor on. Lead with a specific, honest reason for reaching out."]


def _suggest_dm(profile: dict[str, Any], hooks: list[str]) -> str:
    name = profile.get("firstName") or "there"
    if hooks and not hooks[0].startswith("No recent"):
        anchor = hooks[0].split("—")[0].strip().rstrip(".")
        opener = f"Hi {name}, {anchor.lower()}"
    else:
        opener = f"Hi {name}, "
    closer = " — would love to swap notes if you're open to it."
    draft = (opener + closer).strip()
    return draft[:280]


def render_markdown(brief: dict[str, Any]) -> str:
    s = brief["snapshot"]
    lines: list[str] = []
    lines.append(f"# {s['name']}")
    lines.append("")
    lines.append("## Snapshot")
    lines.append(f"- **Headline:** {s.get('headline') or '—'}")
    lines.append(f"- **Current role:** {s.get('current_role') or '—'}")
    lines.append(f"- **Location:** {s.get('location') or '—'}")
    lines.append(f"- **Connection degree:** {s.get('connection_degree') or '—'}")
    if s.get("follower_count") is not None:
        lines.append(f"- **Followers:** {s['follower_count']:,}")
    lines.append(f"- **Profile:** {s['linkedin_url']}")
    lines.append("")

    if brief["background"]:
        lines.append("## Background")
        for role in brief["background"]:
            if role:
                lines.append(f"- {role}")
        lines.append("")

    if brief["recent_posts"]:
        lines.append("## Recent activity")
        for i, post in enumerate(brief["recent_posts"], 1):
            kind = "Repost" if post["is_repost"] else "Post"
            content = post["content"][:240]
            if len(post["content"]) > 240:
                content += "…"
            lines.append(
                f"{i}. **{kind}** ({post['likes']} likes, {post['comments']} comments) — {post['url']}"
            )
            if content:
                lines.append(f"   > {content}")
        lines.append("")

    lines.append("## Conversation hooks")
    for hook in brief["conversation_hooks"]:
        lines.append(f"- {hook}")
    lines.append("")

    lines.append("## Suggested DM")
    lines.append("")
    lines.append("> " + brief["suggested_dm"])
    lines.append("")
    return "\n".join(lines)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build an outreach brief from a LinkedIn URL.")
    parser.add_argument("profile", help="LinkedIn profile URL or public id")
    parser.add_argument("--posts", type=int, default=5, help="number of recent posts (1-20, default 5)")
    parser.add_argument("--json", dest="as_json", action="store_true", help="emit JSON instead of Markdown")
    parser.add_argument("--include-skills", action="store_true")
    parser.add_argument("--include-education", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    api_key = os.environ.get("CONNECTSAFELY_API_KEY")
    if not api_key:
        print(f"error: CONNECTSAFELY_API_KEY is not set. Get one at {SIGNUP_URL}", file=sys.stderr)
        return 2

    args = parse_args(argv[1:])
    if args.posts < 1 or args.posts > 20:
        print("error: --posts must be between 1 and 20 (API max).", file=sys.stderr)
        return 2

    try:
        profile_id = extract_profile_id(args.profile)
    except ApiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return exc.exit_code

    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "User-Agent": "connectsafely-cookbook/prospect-researcher",
    })

    try:
        profile_payload = fetch_profile(
            session, profile_id, args.include_skills, args.include_education
        )
        posts_payload = fetch_latest_posts(session, profile_id, args.posts)
    except ApiError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return exc.exit_code

    brief = build_brief(profile_payload, posts_payload)

    if args.as_json:
        print(json.dumps(brief, indent=2))
    else:
        print(render_markdown(brief))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
