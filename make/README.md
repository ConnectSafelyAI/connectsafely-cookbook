# Make.com Scenarios for the ConnectSafely LinkedIn API

Pre-built **Make.com (Integromat) scenarios** for LinkedIn automation with the [ConnectSafely.ai](https://connectsafely.ai) API. Each template links to a public, importable Make scenario blueprint plus full setup instructions.

**Get a ConnectSafely API key:** [connectsafely.ai/api-key](https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=make)

---

## How Make templates work

Make doesn't ship scenario JSON the way n8n does — instead, each scenario has a **public shared-scenario URL**. Click the URL, sign into Make, click **"Create scenario"**, and Make clones the entire flow into your account. Then connect your credentials and run.

Each `.md` file in this folder has:

- **What the scenario does** and use cases
- **Prerequisites** (accounts, API keys, sheet schemas)
- **The blueprint URL** to clone the scenario into your Make account
- **Module-by-module breakdown** of the flow
- **Customization tips**

---

## Available scenarios

| Scenario | What it does |
| --- | --- |
| [ai-outreach-gemini.md](ai-outreach-gemini.md) | AI-personalized LinkedIn outreach using Google Sheets, Gemini, and ConnectSafely. The flagship Make recipe. |
| [auto-follow-from-sheets.md](auto-follow-from-sheets.md) | Read a target list from Google Sheets and auto-follow each profile via ConnectSafely. |
| [commenters-to-connections.md](commenters-to-connections.md) | Detect commenters on a LinkedIn post and send them automated connection requests. |
| [commenters-to-hubspot.md](commenters-to-hubspot.md) | Pipe LinkedIn post commenters into HubSpot CRM as new leads. |
| [group-members-to-sheets.md](group-members-to-sheets.md) | Extract premium LinkedIn group members into Google Sheets. |
| [keyword-comment-to-dm.md](keyword-comment-to-dm.md) | "Comment X to get Y" — detect a keyword in comments and auto-DM the lead magnet. |
| [profile-visitor-messaging.md](profile-visitor-messaging.md) | Auto-message LinkedIn profile visitors so warm signals don't go cold. |
| [profile-visitors-to-hubspot.md](profile-visitors-to-hubspot.md) | Pipe LinkedIn profile visitors into HubSpot CRM as new leads. |
| [search-to-google-sheets.md](search-to-google-sheets.md) | Run a LinkedIn search and dump structured results to Google Sheets for prospecting. |

---

## How to use

1. **Get a ConnectSafely API key** at [connectsafely.ai/api-key](https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=make).
2. Open the scenario `.md` you want.
3. Click the **blueprint URL** in the file. Make will prompt you to sign in and clone the scenario.
4. **Add your ConnectSafely connection** in Make:
   - Type: **HTTP / Custom**
   - Authorization header: `Bearer YOUR_API_KEY`
5. **Connect any other apps** the scenario uses (Google Sheets, Gemini, HubSpot, etc.).
6. Configure the trigger schedule and run.

---

## Tier

ConnectSafely API access starts at **$10/month** (Ultimate Outreach). New keys get a trial. See [../docs/pricing.md](../docs/pricing.md). Make.com has a generous free tier that's enough to test these scenarios.

---

## Contributing

To add a new scenario:

1. Build it in Make, test against your own ConnectSafely key.
2. In Make, open the scenario → **⋯ menu → Create blueprint → Make public** to get a shared-scenario URL.
3. Add a new `.md` file to this folder following the format of the existing ones (frontmatter with `title`, `description`, `prerequisites`, `useCases`, `howItWorks`, `blueprintUrl`, `modules`).
4. Add a row to the table above.
5. Open a PR per [../CONTRIBUTING.md](../CONTRIBUTING.md).
