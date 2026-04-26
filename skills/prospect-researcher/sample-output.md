# Sample output

Real captured output of:

```bash
python3 example.py https://www.linkedin.com/in/williamhgates/
```

Trimmed slightly for length. Engagement counts and post content will change between runs.

---

# Bill Gates

## Snapshot
- **Headline:** Chair, Gates Foundation and Founder, Breakthrough Energy
- **Current role:** Co-chair at Gates Foundation
- **Location:** Seattle
- **Connection degree:** 3rd
- **Followers:** 40,252,287
- **Profile:** https://www.linkedin.com/in/williamhgates/

## Background
- Co-chair at Gates Foundation
- Breakthrough Energy
- Microsoft

## Recent activity
1. **Post** (332 likes, 50 comments) — https://www.linkedin.com/feed/update/urn:li:activity:7454016180836802560
   > Dr. Damaris Matoke-Muhia lost her younger brother to malaria as a child. Today, she's one of the scientists leading the fight to end it—researching how mosquitoes develop resistance, driving the development of new innovations, and helping m…
2. **Post** (950 likes, 127 comments) — https://www.linkedin.com/feed/update/urn:li:activity:7453877655780712448
   > Malaria still kills hundreds of thousands of children every year, mostly in Africa. But the good news is that science is delivering a new generation of tools: treatments for newborns, innovations that fight drug resistance, better protectio…
3. **Post** (3107 likes, 316 comments) — https://www.linkedin.com/feed/update/urn:li:activity:7453658782334730241
   > Malaria transmission is stubborn. Ending it for good will require better prevention tools, stronger health systems, and sustained commitment. The progress we've already made shows what's possible—and why continuing this work is so important…
4. **Post** (1412 likes, 221 comments) — https://www.linkedin.com/feed/update/urn:li:activity:7453291761340391424
   > This World Immunization Week, it's worth reflecting on just how far we've come. Over the last 25 years, under-five deaths have fallen faster than any other time in history…
5. **Post** (1567 likes, 340 comments) — https://www.linkedin.com/feed/update/urn:li:activity:7452185905571790848
   > Really interesting listen on food fortification. Adding essential vitamins and minerals to everyday foods is an incredible (and surprisingly simple) way to prevent malnutrition in kids.

## Conversation hooks
- Reference their post: "Dr. Damaris Matoke-Muhia lost her younger brother to malaria as a child. Today, she's one of the scientists leading the fight to end…"
- Reference their post: "Malaria still kills hundreds of thousands of children every year, mostly in Africa. But the good news is that science is delivering a new…"
- Reference their post: "Malaria transmission is stubborn. Ending it for good will require better prevention tools, stronger health systems, and sustained…"

---

_Use the hooks above to draft your outreach. Reference one specific post or role detail; keep the message under 280 characters._

---

## How the calling agent uses this

When Claude invokes the skill, the brief lands in Claude's context. Claude then writes the DM grounded in the hooks and recent posts, with knowledge of *your* product/tone/goal that this script doesn't have. Example follow-up from Claude after running the skill:

> Based on his recent malaria-eradication posts, here's a draft you could send:
>
> "Hi Bill — your post on Damaris Matoke-Muhia's work on mosquito resistance landed at the right time for me; we're looking at how to surface scientist-led narratives in our donor materials. Open to a 15-min chat?"

The skill provides the signal; the agent provides the writing.

## JSON mode

`python3 example.py <url> --json` returns the same data as a JSON object with keys: `snapshot`, `background`, `recent_posts`, `conversation_hooks`. Useful for piping into agents or downstream tooling.
