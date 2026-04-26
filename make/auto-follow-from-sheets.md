---
title: "Automate LinkedIn Follows from Google Sheets: Make.com Scenario"
description: "Stop clicking the follow button one by one. This Make.com scenario reads your target list from Google Sheets and automatically follows each LinkedIn profile using ConnectSafely."
platform:
  - make
category: ai-powered
difficulty: beginner
featured: true
popular: true
thumbnail: "https://d2ehv4qhihc5sm.cloudfront.net/images/templates/automate-linkedIn-follows-from-google-sheets.jpg"
videoUrl: "https://www.youtube.com/watch?v=Ik5Oa0bltA8"
blueprintUrl: "https://us2.make.com/public/shared-scenario/RBnabVLpvzW/linked-in-auto-follow-from-sheets"
date: "2026-03-06"
keywords: ["linkedin auto follow automation", "make.com linkedin follow sheets", "bulk follow linkedin profiles", "connectsafely make blueprint", "linkedin follow list automation"]
integrations:
  - name: "Make.com"
    icon: "/images/integrations/make.svg"
  - name: "ConnectSafely"
    icon: "/images/logo-icon.png"
  - name: "LinkedIn"
    icon: "/images/linkedin.png"
  - name: "Google Sheets"
    icon: "https://cdn.simpleicons.org/googlesheets/0F9D58"
prerequisites:
  - "Make.com account (free tier works for testing)"
  - "ConnectSafely.ai account with API key"
  - "LinkedIn account connected to ConnectSafely"
  - "Google Sheets list of LinkedIn profile URLs to follow"
useCases:
  - "Follow hundreds of target prospects without clicking one by one"
  - "Build visibility with key accounts before outreach"
  - "Follow industry thought leaders and influencers at scale"
  - "Warm up prospects by following them before sending a connection request"
  - "Automate LinkedIn audience building from any prospect list"
howItWorks:
  - "Google Sheets trigger picks up new rows of LinkedIn URLs"
  - "Make.com iterates through each profile with rate limiting"
  - "ConnectSafely API follows each LinkedIn profile"
  - "Sheet row updated with status and timestamp"
relatedTemplates:
  - "make-linkedin-ai-outreach-gemini"
  - "make-linkedin-commenters-to-connections"
  - "n8n-linkedin-follow-automation"
modules:
  - "Google Sheets (Watch Rows)"
  - "Iterator"
  - "ConnectSafely.ai (Follow Profile)"
  - "Sleep"
  - "Google Sheets (Update Row)"
---

# Automate LinkedIn Follows from Google Sheets: Make.com Scenario (2026)

Stop clicking the follow button one by one on LinkedIn. This Make.com scenario reads your target list directly from Google Sheets and automatically follows each profile using ConnectSafely — no manual work, no browser extensions, no limits headaches.

## Video Tutorial

[](youtube:Ik5Oa0bltA8)


## Why Automate LinkedIn Follows?

Following is a low-friction, high-impact LinkedIn growth strategy:

- **No approval needed** — unlike connection requests, follows are instant
- **Warms up prospects** — they see your name before you ever reach out
- **Algorithm signal** — following creators boosts their content in your feed
- **Scales safely** — LinkedIn is far more lenient on follows than connections
- **Sequencing play** — follow → engage with content → connect → message

Many top sales teams use "follow → comment → connect" as their warm outreach sequence. This blueprint handles step one at scale.

## Scenario Overview

![Workflow Screenshot](https://d2ehv4qhihc5sm.cloudfront.net/images/templates/automate-linkedIn-follows-from-google-sheets.jpg)

## What You'll Build

A Make.com scenario that:

1. **Reads LinkedIn URLs** from your Google Sheet
2. **Iterates** through each profile with safe delays
3. **Follows each profile** via ConnectSafely API
4. **Updates** the sheet row with status and timestamp

```
Google Sheets (New Rows) → Iterator → ConnectSafely (Follow) → Update Row
```

## Setting Up the Blueprint


### Step 1: Prepare Your Google Sheet

Create a sheet with these columns:

| Column | Description |
|---|---|
| LinkedIn URL | Full profile URL (required) |
| Name | For reference |
| Status | `Pending` / `Done` / `Error` |
| Followed Date | Filled by Make automatically |

### Step 2: Connect Your API Key

1. Go to [ConnectSafely.ai](https://connectsafely.ai) → **Settings → API Key**
2. Add to Make's HTTP module:
   ```
   Authorization: Bearer YOUR_API_KEY
   ```

### Step 3: Configure the Modules

**Module 1: Google Sheets — Watch Rows**
- Trigger: New rows where `Status = Pending`
- Limit: 50–100 rows per run

**Module 2: Iterator**
- Loop through each row returned

**Module 3: ConnectSafely — Follow Profile**
```
POST https://api.connectsafely.ai/v1/follows/send
Headers: Authorization: Bearer YOUR_API_KEY
Body: { "linkedinUrl": "{{row.LinkedInURL}}" }
```

**Module 4: Sleep**
- 10–30 second delay between follows
- Follows are lower-risk than connections but still worth spacing out

**Module 5: Google Sheets — Update Row**
- Set `Status` = `Done`
- Set `Followed Date` = `{{now}}`

### Step 4: Build Your Target List

**Best sources for your follow list:**
- LinkedIn search results (use the [LinkedIn Search to Sheets Blueprint](/integrations/templates/make-linkedin-search-to-google-sheets))
- Event attendee lists
- Industry conference speakers
- Competitor follower lists
- Podcast guest lists in your niche

## Best Practices

### Safe Daily Follow Limits

| Account Type | Max Follows/Day |
|---|---|
| New account | 50–80/day |
| Established account | 100–150/day |
| Premium account | 150–200/day |

Follows are much safer than connection requests — LinkedIn allows significantly more.

### Sequencing Strategy

Use follows as step one of a multi-touch warm outreach sequence:

1. **Day 1:** Follow profile (this blueprint)
2. **Day 3–5:** Like or comment on their recent post
3. **Day 7:** Send connection request with context
4. **Day 10:** Send DM after connection accepted

This sequence achieves 50–70% connection acceptance vs. 25–35% for cold requests.

### Target the Right People

Follow people who:
- Match your ICP (ideal customer profile)
- Are active posters (check if they post regularly)
- Work at target accounts you want to sell to
- Are thought leaders whose followers are your audience

## Common Issues & Fixes

| Issue | Solution |
|---|---|
| Follow fails (404) | LinkedIn profile URL may be incorrect or profile deleted |
| Rate limit error (429) | Increase Sleep module delay |
| Sheet not updating | Check Google Sheets module permissions in Make |
| Only some rows processed | Check "Limit" setting in Watch Rows module |

## Frequently Asked Questions

### How do I bulk follow LinkedIn profiles automatically?

Use this Make.com scenario with ConnectSafely's API. Paste your target LinkedIn URLs into Google Sheets, connect your API key, and the scenario reads each row and follows every profile automatically with safe rate limiting.

### How many LinkedIn profiles can I follow per day?

LinkedIn allows roughly 100–200 follows per day for established accounts. Unlike connection requests (limited to ~100/week), follows are much more permissive. Start at 50/day and increase gradually. ConnectSafely handles safe sending patterns automatically.

### Will people know I followed them?

Yes — LinkedIn notifies users when someone follows them (unless they've disabled notifications). This is a feature, not a bug — it creates passive visibility before you ever reach out directly.

## Related Workflows

- [AI-Powered Outreach with Make.com + Gemini](/integrations/templates/make-linkedin-ai-outreach-gemini) - Follow-up with connection requests after following
- [Turn Commenters into Connections](/integrations/templates/make-linkedin-commenters-to-connections) - Convert engaged followers into connections
- [n8n: LinkedIn Follow Automation](/integrations/templates/n8n-linkedin-follow-automation) - Same workflow built on n8n

---

*Start building your LinkedIn presence at scale. [Start your ConnectSafely free trial](/pricing) to go live today.*
