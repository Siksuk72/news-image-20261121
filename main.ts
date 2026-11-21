// news-image-20261121: the entrypoint the grader runs (Node 22,
// standard library only).
//
// The front page is already painted and stored in this repository as
// entry.png (draw.py paints it with Pillow; hero.png is the AI-made
// dawn-scramble illustration it uses). This program only carries those
// finished bytes to the grader at /output/entry.png, so the result is
// identical every run.
//
// Local trial run, without the grader:
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, chmodSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const repoRoot = dirname(fileURLToPath(import.meta.url));
const source = join(repoRoot, "entry.png");
const targetDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(targetDir, "entry.png");

if (!existsSync(source)) {
  throw new Error(`entry.png missing next to main.ts: ${source}`);
}
mkdirSync(targetDir, { recursive: true });
copyFileSync(source, target);
chmodSync(target, 0o644);
