/**
 * Fetch a single LinkedIn profile by public id.
 * Endpoint: POST /linkedin/profile — https://connectsafely.ai/docs
 * Get a key: https://connectsafely.ai/api-key?utm_source=github&utm_medium=cookbook&utm_campaign=snippet
 */

const profileId = process.argv[2] ?? "williamhgates";
const apiKey = process.env.CONNECTSAFELY_API_KEY;
if (!apiKey) throw new Error("set CONNECTSAFELY_API_KEY");

const res = await fetch("https://api.connectsafely.ai/linkedin/profile", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({ profileId, includeExperience: true }),
});

if (!res.ok) {
  console.error(`HTTP ${res.status}`, await res.text());
  process.exit(1);
}

console.log(JSON.stringify(await res.json(), null, 2));
