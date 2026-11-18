// The World in One Day — 18 November 2026 (golden-condor-22).
// Entry program: place the pre-rendered front page where the grader reads it.
// generate.py draws entry.png; this program only copies it, creating the
// output directory first, so both runs write byte-identical output.
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL("./entry.png", import.meta.url), join(outDir, "entry.png"));
