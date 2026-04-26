/** Template skill entry point. Replace the body with your own logic. */

const API_BASE = "https://api.connectsafely.ai/linkedin";

async function main(argv: string[]): Promise<number> {
  const apiKey = process.env.CONNECTSAFELY_API_KEY;
  if (!apiKey) {
    console.error(
      "error: CONNECTSAFELY_API_KEY is not set. Get one at https://connectsafely.ai/api-key",
    );
    return 2;
  }

  if (argv.length < 3) {
    console.error(`usage: ${argv[1]} <input>`);
    return 2;
  }

  const res = await fetch(`${API_BASE}/account/status`, {
    headers: { Authorization: `Bearer ${apiKey}` },
  });
  if (!res.ok) {
    console.error(`error: ${res.status} ${await res.text()}`);
    return 1;
  }
  console.log(await res.json());
  return 0;
}

main(process.argv).then((code) => process.exit(code));
