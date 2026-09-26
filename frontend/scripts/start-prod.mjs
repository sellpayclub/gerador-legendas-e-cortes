import { existsSync } from "node:fs";
import { join } from "node:path";
import { pathToFileURL } from "node:url";

const server = join(process.cwd(), ".next", "standalone", "server.js");
if (!existsSync(server)) throw new Error("Build ausente. Rode npm run build.");
process.env.PORT ??= "3000";
process.env.HOSTNAME ??= "127.0.0.1";
process.env.BACKEND_URL ??= "http://127.0.0.1:8000";
process.env.NODE_ENV = "production";
await import(pathToFileURL(server).href);
