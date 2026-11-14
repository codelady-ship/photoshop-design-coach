# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [1.1.0] - 2026-11-14

### Added
- `SKILL.md`: **Plan compatibility (Free, Pro, Max, Team)** section. No web search: answers come from `references/` and version-specific Photoshop facts the references don't confirm are marked "check Adobe Help", never "checked". Free usage limits: lite path (one mode, top 3 steps, then "details?"), without cutting the refusal or "print shop's rules win" lines. No code execution: px, DPI, bleed and contrast by hand with the existing formulas. No scheduled tasks needed.
- README: matching "Plan compatibility" section.
- `evals/evals.json`: cases 9-11 (no web search, lite path, no code execution).

### Fixed
- `scripts/design_calc.py`: `--json` now works after the command too (`design_calc.py px 90 50 --json`), as the docstring says, via a shared parent parser; `--json` before the command still works.
- README: removed a link to research notes outside this repository.
- `SKILL.md` footer no longer says "Version facts from Adobe Help (checked 2026-11)": helpx.adobe.com could not be opened during research, and the blind eval showed the model repeating "checked" in a no-web-search answer. It now says the facts come from the skill's notes and to check Adobe Help for your version.

## [1.0.0] - 2026-11-11

### Added
- `SKILL.md`: Photoshop & Design Coach with seven modes (HOW-TO, FIX, SIZE & PRINT, REVIEW, AI, JOB, RIGHTS) and golden rules (user's language with Azerbaijani default, Win/Mac shortcuts, free-tool equivalent, no invented facts, legal software only, respect trademarks and living artists, honest AI, text only, Instagram strategy goes to the Instagram Manager skill).
- `references/photoshop-howto.md`: menu paths and Win/Mac shortcuts for documents, layers, masks, selections, retouch, text, export and print colour.
- `references/free-tools.md`: Photopea, GIMP 3, Krita, Inkscape, Canva, Adobe Express and remove.bg, with a 15-task command mapping table and V/U marks.
- `references/troubleshooting.md`: 10 symptom cards (blurry export, print colour shift, no bleed, Generative Fill greyed out, huge files, jagged cut-outs, missing fonts, locked layers, washed-out web colours, lost work).
- `references/sizes-and-print.md`: social sizes from official pages where available, print sizes with bleed and pixels, formulas, print-shop checklist.
- `references/design-review.md`: 11-point review checklist with WCAG contrast by hand and pre-computed pairs.
- `references/ai-features.md`: generative AI requirements, credits per plan, feature table, prompt pattern, non-AI alternatives, commercial-use notes.
- `references/rights.md`: legal software options, fonts, stock, AI images, logos and styles.
- `references/job-prep.md`: Baku job-ad snapshot, portfolio plan, test-task time plan and self-check, interview questions.
- `scripts/design_calc.py`: optional standalone Python (stdlib only, no files, no network) for pixels/print size, bleed, presets and WCAG contrast. SKILL.md gives the same maths as a text fallback.
- `evals/evals.json` (8 cases), `scripts/build-agensi-zip.ps1`, `LISTING.md`, README, MIT licence.

### Fixed (blind evals, before release)
- Round 1 (5/8): whole-answer length cap (~25 lines), exactly one closing line, translated format labels, no filler; Instagram Manager pointer only when asked; "Faster:" only when useful; stay in the user's free tool; text stroke/shadow for small screens; max 3 causes per answer; review must cover focal point and key info; salary data only if asked; commercial-use answer in 3 bullets; hedged guide-layout and Photopea mask paths.
- Round 2 (2/5): print problems always end with "the print shop's rules win"; fixed items in the review's format-fit line; portfolio always includes a print piece with bleed; removed an unverified "Help ▸ Sign in" path.
- Round 3: 3/3. Final 8/8. Details: `tests/results.md`. The Python helper was verified via a Node port (16/16) because Python isn't installed on the build PC.
