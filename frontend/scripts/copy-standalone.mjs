import { cpSync, existsSync, mkdirSync, rmSync } from "node:fs";
import { join } from "node:path";

const root = process.cwd();
const standalone = join(root, ".next", "standalone");
if (!existsSync(join(standalone, "server.js"))) {
  throw new Error("Build standalone ausente. Rode npm run build novamente.");
}
const staticTarget = join(standalone, ".next", "static");
mkdirSync(join(standalone, ".next"), { recursive: true });
rmSync(staticTarget, { recursive: true, force: true });
cpSync(join(root, ".next", "static"), staticTarget, { recursive: true });
const publicSource = join(root, "public");
const publicTarget = join(standalone, "public");
rmSync(publicTarget, { recursive: true, force: true });
if (existsSync(publicSource)) cpSync(publicSource, publicTarget, { recursive: true });
