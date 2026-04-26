# n8n Workflows for the ConnectSafely LinkedIn API

Importable n8n workflow JSON exports for **LinkedIn automation** with the [ConnectSafely.ai](https://connectsafely.ai) API. Each file is a complete workflow you can drop into n8n via **Workflows → Import from File**.

**Get a ConnectSafely API key:** [connectsafely.ai/api-key](https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=n8n)

There is also a community n8n node: [ConnectSafelyAI/N8N_Package_ConnectSafely](https://github.com/ConnectSafelyAI/N8N_Package_ConnectSafely). The workflows below use the generic **HTTP Request** node, so they work without installing the community node.

---

## Available workflows

| Workflow | What it does |
| --- | --- |
| [ai-connection-requests-gemini.json](ai-connection-requests-gemini.json) | Send AI-personalized LinkedIn connection requests from a Google Sheet using Google Gemini. Targets 40–60% acceptance via per-prospect personalization. |
| [follow-automation.json](follow-automation.json) | 4-node workflow: read profile URLs from a Google Sheet, follow each one via ConnectSafely, mark the row done. |
| [commenters-hubspot-crm.json](commenters-hubspot-crm.json) | Capture LinkedIn post commenters and sync them to HubSpot CRM, enriched with email + company data via Apify. |
| [connection-requests-commenters.json](connection-requests-commenters.json) | Send connection requests to people who commented on a chosen post. 3–5× higher acceptance vs cold outreach. |
| [dm-profile-visitors.json](dm-profile-visitors.json) | Auto-DM LinkedIn profile visitors. Splits the flow: DM existing connections, send connection request to non-connections. |
| [group-members-sheets.json](group-members-sheets.json) | Extract LinkedIn group members to Google Sheets. Optional filter for premium members. |
| [keyword-dm-automation.json](keyword-dm-automation.json) | Detect specific keywords in comments on your post and auto-DM the commenter (the "comment X to get Y" pattern). |
| [search-results-sheets.json](search-results-sheets.json) | Run a LinkedIn search and dump results to Google Sheets. 3-node prospecting workflow. |
| [viral-post-rewriter-gemini.json](viral-post-rewriter-gemini.json) | Find a viral post, rewrite it in your voice with Gemini, send to Telegram for approval, then auto-publish. |
| [visitors-hubspot-crm.json](visitors-hubspot-crm.json) | Auto-sync LinkedIn profile visitors to HubSpot CRM with email + company enrichment via Apify. |

---

## How to use

1. **Get an API key** at [connectsafely.ai/api-key](https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=n8n).
2. In n8n, go to **Workflows → Import from File** and pick a JSON file from this folder.
3. **Set credentials** on the HTTP Request nodes:
   - **Authentication:** Generic Credential Type → **Header Auth**
   - **Name:** `Authorization`
   - **Value:** `Bearer YOUR_CONNECTSAFELY_API_KEY`
4. **Connect any other accounts** the workflow needs (Google Sheets, Gemini, HubSpot, Telegram, Apify) using n8n's built-in credential UI.
5. Open each Sticky Note in the workflow — they explain that node's purpose and what to customize.
6. **Activate** the workflow.

---

## Common requirements

| Workflow uses | What you need |
| --- | --- |
| Google Sheets | Google account + a sheet with the columns the workflow expects (each workflow's sticky note lists them) |
| Gemini AI | Google AI Studio API key |
| HubSpot | HubSpot Private App token |
| Apify | Apify token (for the email/company enrichment workflows) |
| Telegram | Bot token + your chat ID |

ConnectSafely is the only required credential — the rest are optional depending on which workflow you import.

---

## Tier

ConnectSafely API access starts at **$10/month** (Ultimate Outreach). New keys get a trial. See [../docs/pricing.md](../docs/pricing.md).

---

## Contributing

To add a new workflow:

1. Build and test it in n8n with your own credentials.
2. **Strip credentials** before exporting — n8n's "Download" leaves credential references but not secrets, which is what we want.
3. Add a sticky note at top-left explaining: who it's for, what it does, requirements, setup, customization.
4. Save the JSON to this folder with a short kebab-case name.
5. Add a row to the table above.
6. Open a PR per [../CONTRIBUTING.md](../CONTRIBUTING.md).
