---
title: "Scrape LinkedIn Group Members to Google Sheets: Make.com Scenario"
description: "Stop manually copying LinkedIn group member profiles one by one. This Make.com scenario automatically extracts premium members from LinkedIn Groups and saves them to Google Sheets."
platform:
  - make
category: sales
difficulty: intermediate
featured: true
popular: true
thumbnail: "https://d2ehv4qhihc5sm.cloudfront.net/images/templates/scrape-linkedIn-group-members.jpg"
videoUrl: "https://www.youtube.com/watch?v=7WtmP--j5l4"
blueprintUrl: "https://us2.make.com/public/shared-scenario/3OMov0FbkOU/linked-in-group-premium-member-extractor"
date: "2026-03-06"
keywords: ["linkedin group members scraper", "make.com linkedin groups google sheets", "extract linkedin group members", "linkedin premium members list automation", "connectsafely make blueprint groups"]
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
  - "Make.com account"
  - "ConnectSafely.ai account with API key"
  - "LinkedIn account connected to ConnectSafely"
  - "Membership in the target LinkedIn Group"
  - "Google Sheets account"
useCases:
  - "Extract premium members from LinkedIn Groups into a spreadsheet"
  - "Build targeted prospect lists from niche LinkedIn communities"
  - "Identify high-value members (LinkedIn Premium = higher-intent buyers)"
  - "Populate outreach lists from groups in your industry or niche"
  - "Research group composition before advertising or content targeting"
howItWorks:
  - "ConnectSafely API fetches members from the target LinkedIn Group"
  - "Filters for premium members only (higher-intent prospects)"
  - "Extracts name, headline, company, and LinkedIn URL for each"
  - "Appends each member as a new row in Google Sheets"
relatedTemplates:
  - "make-linkedin-search-to-google-sheets"
  - "make-linkedin-ai-outreach-gemini"
  - "n8n-linkedin-group-members-sheets"
modules:
  - "Manual or Schedule Trigger"
  - "ConnectSafely.ai (Get Group Members)"
  - "Iterator"
  - "Filter (Premium Only)"
  - "Google Sheets (Search Existing Rows)"
  - "Router"
  - "Google Sheets (Append Row)"
---

# Scrape LinkedIn Group Members to Google Sheets: Make.com Scenario (2026)

Stop manually copying LinkedIn group member profiles one by one. This Make.com scenario automates the entire extraction process — pulling only premium members from any LinkedIn Group and saving them directly to Google Sheets as a ready-to-use prospect list.

## Video Tutorial

[](youtube:7WtmP--j5l4)


## Why Target LinkedIn Group Premium Members?

Not all LinkedIn group members are equal. Premium members are:

- **Higher intent** — they pay for LinkedIn tools, signaling professional investment
- **More active** — premium users engage more frequently with content and outreach
- **Better qualified** — LinkedIn Premium is most common among sales, marketing, and leadership roles
- **More responsive** — InMail and DM response rates are higher among premium users

LinkedIn groups in your niche are goldmines of pre-qualified, niche-relevant prospects that most competitors overlook.

## Scenario Overview

![Workflow Screenshot](https://d2ehv4qhihc5sm.cloudfront.net/images/templates/scrape-linkedIn-group-members.jpg)

## What You'll Build

A Make.com scenario that:

1. **Fetches group members** from a target LinkedIn Group
2. **Filters** for premium members only
3. **Extracts** name, headline, company, LinkedIn URL for each
4. **Appends** rows to Google Sheets with deduplication
5. **Ready for outreach** immediately

```
Trigger → Fetch Group Members → Filter (Premium) → Iterator → Append to Sheets
```

## Setting Up the Blueprint


### Step 1: Prepare Your Google Sheet

Create a sheet with these columns:

| Column | Description |
|---|---|
| LinkedIn URL | Profile link |
| Name | Full name |
| Headline | Job title / description |
| Company | Current employer |
| Premium | Yes/No |
| Added Date | Filled by Make |
| Status | `Pending` (for outreach tracking) |

### Step 2: Connect Your API Key

1. Go to [ConnectSafely.ai](https://connectsafely.ai) → **Settings → API Key**
2. Add to Make's HTTP module:
   ```
   Authorization: Bearer YOUR_API_KEY
   ```

### Step 3: Configure the Modules

**Module 1: Manual or Schedule Trigger**
- Run manually when you want to extract a new group
- Or schedule weekly to catch new members

**Module 2: ConnectSafely — Get Group Members**
```
GET https://api.connectsafely.ai/v1/groups/members
Headers: Authorization: Bearer YOUR_API_KEY
Body: { "groupUrl": "YOUR_LINKEDIN_GROUP_URL" }
```

Returns list of members with profile data including premium status.

**Module 3: Iterator**
- Loop through each member

**Module 4: Filter — Premium Members Only**
- Condition: `member.isPremium = true`
- This is the core filter that qualifies your list

**Module 5: Google Sheets — Search Existing Rows**
- Check if LinkedIn URL already exists in sheet
- Prevents duplicate entries

**Module 6: Router**
- **Route A:** Already in sheet → Skip
- **Route B:** New member → Append row

**Module 7: Google Sheets — Append Row**
- Add all profile fields as a new row
- Set `Status = Pending` for outreach tracking
- Set `Added Date = {{now}}`

### Step 4: Find Target LinkedIn Groups

Best groups to target:

| Group Type | Why It Works |
|---|---|
| Industry-specific groups | Members share your niche |
| Role-specific groups (CMOs, VPs) | Self-selected by job function |
| Competitor customer groups | Pre-qualified by use case |
| Conference or event groups | High-intent professionals |
| Technology user groups (HubSpot, Salesforce, etc.) | Tool-qualified buyers |

Search LinkedIn Groups: `linkedin.com/groups/search/`

## Using the List for Outreach

Once your sheet is populated with premium members:

**Option 1: Direct connection requests**
→ Use the [AI-Powered Outreach Blueprint](/integrations/templates/make-linkedin-ai-outreach-gemini) to send personalized connection requests

**Option 2: LinkedIn follow campaign**
→ Use the [Auto-Follow from Sheets Blueprint](/integrations/templates/make-linkedin-auto-follow-from-sheets)

**Option 3: Export to CRM**
→ Push to HubSpot using the [Commenters to HubSpot Blueprint](/integrations/templates/make-linkedin-commenters-to-hubspot) (adaptable for sheet-based inputs)

## Best Practices

### Group Selection Strategy

- Join groups **before** running extraction — you must be a member
- Target groups with 1,000–50,000 members (sweet spot for quality + volume)
- Avoid spammy groups dominated by self-promotion posts
- Cross-reference: does this group's member profile match your ICP?

### Rate Limits for Extraction

- Extract in batches of 200–500 members per run
- Add a 2–5 second delay between member fetches
- Spread large extractions (5,000+ members) across multiple days

### List Hygiene

- Filter out profiles without a headline (often inactive accounts)
- Remove accounts with 0 connections (likely fake or abandoned)
- Prioritize recent joiners — more likely to be actively looking for connections

## Common Issues & Fixes

| Issue | Solution |
|---|---|
| No members returned | Confirm you're a member of the group first |
| Private group access denied | You must have accepted membership before extracting |
| Duplicates in sheet | Check Search Rows module before Append |
| Premium filter catches too few | Some groups have low premium ratios — remove filter for all members |

## Frequently Asked Questions

### How do I extract LinkedIn group members into Google Sheets?

Join the target LinkedIn group, then use this Make.com scenario with ConnectSafely's API. The scenario fetches group members, filters for premium status, and appends each profile as a new row in your Google Sheet automatically.

### Why focus on LinkedIn Premium members specifically?

Premium members pay for LinkedIn tools — they're demonstrably more professional and active on the platform. They have higher InMail response rates, accept connection requests more frequently, and are often in decision-making roles (Sales Navigator, Recruiter, and Business Premium are the most common).

### How many members can I extract from a LinkedIn Group?

Extraction limits depend on group size and pace. For groups under 5,000 members, a single run works fine. For larger groups, spread extraction across multiple runs over several days to avoid hitting rate limits.

## Related Workflows

- [Build LinkedIn Lead Lists from Search](/integrations/templates/make-linkedin-search-to-google-sheets) - Extract from LinkedIn search results instead of groups
- [Auto-Follow Profiles from Sheets](/integrations/templates/make-linkedin-auto-follow-from-sheets) - Follow every profile you extracted
- [n8n: Group Members to Sheets](/integrations/templates/n8n-linkedin-group-members-sheets) - Same workflow built on n8n

---

*Build your next prospect list in minutes, not days. [Start your ConnectSafely free trial](/pricing) and get started today.*
