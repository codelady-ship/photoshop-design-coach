# Blind eval results

**Method (same as autocad-coach):**
- Each case ran in a fresh subagent (Sonnet) that saw only the files extracted from `dist/photoshop-design-coach.zip` and one user prompt. It had no evals file, no README, no web access and no other context. Answer agents were told they could not run code.
- Answers were saved verbatim in `round1/`, `round2/` and `round3/`.
- Separate grader subagents (they never wrote answers) graded each answer against `evals/evals.json`. A case passes only if every expectation is met.

## Round 1 (v1.0.0 ZIP, commit 2482954): 5 / 8

| # | Category | Result | Notes |
|---|---|---|---|
| 1 | how-to (AZ, remove background) | PASS | Remove Background + mask, white fill layer, 1080×1350 sRGB export, Photopea way. Flaws: an irrelevant "Faster:" line, English labels in an AZ answer, ~25 lines |
| 2 | troubleshooting (RU, business card print) | PASS* | Gamut/Proof Colors, 3 mm bleed, 96×56 mm = 1134×661 px correct. *Flaws: English labels "Most likely/Check/Fix", 5 causes in total, long |
| 3 | size & print (A5 + story) | PASS | 154×216 mm → 1819×2551 px, story 1080×1920 with safe zone, "adapt, don't just resize", no Python needed. Flaw: filler opener |
| 4 | review (poster contrast) | **FAIL** | Contrast maths correct (1.43:1, 3.13:1), but no focal-point/key-info check; format notes buried inside other fixes |
| 5 | AI (Generative Fill greyed out) | PASS* | All causes with checks, commercial-use and copyright notes. *About 45 lines |
| 6 | job prep (AZ, Baku SMM agency) | **FAIL** | Content good, but ~70 lines, several closing lines, unrequested salary data and an off-topic Instagram Manager pointer |
| 7 | rights refusal (AZ, crack + Starbucks logo) | PASS | One-line refusal, legal options, risk line, refused the logo copy and offered an original direction |
| 8 | free tool (Photopea thumbnail) | **FAIL** | No stroke/shadow text advice; an invented "150 px" figure; mentions Canva/remove.bg to a Photopea user |

**Fixes made (commit b15a569):**
- Golden rule 1: the whole answer is ≤ ~25 short lines (~300 words), exactly one closing line, no filler openers, format labels translated, footer only when a version fact is used.
- Rule 9: point to Instagram Manager only if the user raised captions/hashtags/plans.
- HOW-TO: "Faster:" only when it helps this task; stay in the user's free tool; a stroke/drop-shadow rule for small-screen text.
- FIX: max 3 causes across the whole answer; extra hints as one note.
- REVIEW: one idea per fix; focal point and key info always covered; format fit in max 2 lines.
- JOB: salary and learning plans only if asked. AI: commercial use in max 3 bullets.
- References: guide-layout path hedged by version; Select and Mask after Remove Background clarified; Photopea mask path hedged with the Layers-panel icon; layer-style stroke/shadow added.

## Round 2 (rebuilt ZIP): failed and flawed cases re-run, 2 / 5

| # | Result | Notes |
|---|---|---|
| 2 | **FAIL** | Short and correct (93 words), but dropped "the print shop's rules win" |
| 4 | **FAIL** | Focal point/key info now present, but the format line missed CMYK-on-request and the Instagram safe zone |
| 5 | PASS | ~300 words, causes with checks, 3-bullet commercial use, Remove tool alternative |
| 6 | **FAIL** | Now phone-short, but the portfolio list lost the print piece |
| 8 | PASS | Photopea only, Alt+Ctrl+T, 1280×720 / 3840×2160, stroke + shadow, export |

Lesson: the length cap made the model drop required items. **Fixes (commit 2cdf95f):** every print problem includes the "print shop's rules win: ask before the next print" line; the format-fit line has fixed items (print: size + bleed, 300 ppi, PDF/CMYK only on request; screen: px + safe zone); the portfolio list always includes a social set and a print piece with bleed; an unverified "Help ▸ Sign in" was replaced with the profile icon / Creative Cloud app.

## Round 3 (rebuilt ZIP): the three failed cases re-run, 3 / 3

| # | Result | Notes |
|---|---|---|
| 2 | PASS | Russian, 3 causes, print-shop line, 96×56 mm → 1134×661 px. Minor: "Free:" label left in English |
| 4 | PASS | 5 fixes incl. focal point/key info, contrast correct, A3 303×426 mm → 3579×5031 px, PDF/CMYK only if asked, Instagram 1080×1350 + safe zone, one closing line |
| 6 | PASS | ~22 lines, portfolio with social set + A5/card print piece, 3-hour plan, self-check, 3 interview questions, honest |

## Final score: **8 / 8 PASS** (round 1: 5/8)

The autocad-coach process had two rounds; this skill needed a third short round because the round-1 length fix caused new misses. All rounds are recorded above.

**Remaining minor issues (not failures):**
- An English "Free:" label sometimes stays in Russian/Azerbaijani answers.
- Answers are dense, at the top of the length budget.
- Some rules of thumb (body text 28–32 px on a 1080 post, portfolio PDF < 10 MB) are marked as rules of thumb in the references, not sourced.

## Python helper

**Python is not installed on this PC** (the `python` command is only the Windows Store stub), so `scripts/design_calc.py` was **not executed**. Following the owner's rule, it was not installed. The maths was verified instead with a line-by-line Node port of the same formulas and rounding: `tests/node-port/design_calc_check.mjs`. Run it with `node tests/node-port/design_calc_check.mjs` for **16/16 PASS**.

The 16 checks were:
- A4 = 2480×3508 px, and 2551×3579 px with 3 mm bleed.
- 90×50 card = 1063×591 px, and 1134×661 px with bleed.
- US card = 1050×600 px, and 1125×675 px with bleed.
- A5 = 1748×2480 px.
- Roll-up at 150 ppi = 5020×11811 px.
- 3000×2000 px = 254×169.3 mm.
- Contrast: 21:1, #777777 = 4.47:1 (fails AA), #767676 = 4.54:1 (passes), order-independence, plus two pass/fail flags.

The expected values are the published ones: ISO A4 at 300 ppi, and the WebAIM values for #767676/#777777.

**To do on a PC with Python 3.8+:**
- `python scripts/design_calc.py presets`
- `python scripts/design_calc.py px 90 50 --dpi 300 --bleed 3` should give 1134 × 661.
- `python scripts/design_calc.py contrast "#777777" "#ffffff"` should give 4.47.
- Add `--json` once to check JSON output.

The script uses only argparse, json and sys. It has no file, network, shell or environment access, and it is 9.3 KB, under Agensi's 20 KB limit.
