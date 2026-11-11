# Photoshop & Design Coach

> A free graphic-design coach for beginners, students, SMM freelancers and junior designers. Step-by-step Photoshop how-tos with Windows and Mac shortcuts and the same steps in Photopea, GIMP or Canva, a fix-my-problem mode, social and print sizes (DPI, bleed, CMYK), design reviews with a contrast check, honest AI-feature help, junior designer job prep and licence basics. Answers in your language (Azerbaijani by default).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Skill](https://img.shields.io/badge/Claude-Skill-D97757.svg)](SKILL.md)
[![Price: Free](https://img.shields.io/badge/price-free-brightgreen.svg)](#license)

A free, text-only skill by Codelady Abroad. It runs anywhere a plain prompt runs: Claude Code, the Claude app, other agents or a simple website form. It doesn't control Photoshop and doesn't open your PSD files. It teaches you to do the work yourself, in your own program.

## Modes

| Mode | You say | You get |
|---|---|---|
| How-to | "How do I remove a background?" | 3–8 steps with menu paths, `Ctrl` / `Cmd` shortcuts, a check, one common mistake, and the free-tool way |
| Fix | "My export is blurry", "colours changed in print" | Most likely cause → one check → the fix, up to 3 causes |
| Size & print | "A5 flyer + Instagram story sizes?" | Pixels, bleed, safe zone, CMYK/PDF checklist; your print shop's rules win |
| Review | "Check my poster" | One strength, up to 5 prioritised fixes, WCAG contrast numbers |
| AI | "Generative Fill is greyed out" | Requirements, credits, prompt pattern, non-AI alternative, commercial-use notes |
| Job | "Junior designer test task" | Portfolio plan, test-task time plan, self-check, interview questions |
| Rights | "Free Photoshop?", "Can I use this font?" | Legal options (trial, Photopea, GIMP…), licence basics. Never cracks, never copied logos |

Captions, hashtags and posting plans are not here: use the sibling **Instagram Manager** skill.

## Optional Python helper

`scripts/design_calc.py` is a standalone, standard-library-only Python 3 script (no files, no network, no pip):

```
python scripts/design_calc.py px 90 50 --dpi 300 --bleed 3     # print size -> pixels (card with bleed)
python scripts/design_calc.py size 3000 2000 --dpi 300         # pixels -> max print size
python scripts/design_calc.py preset ig-portrait               # named sizes; `presets` lists all
python scripts/design_calc.py contrast "#777777" "#ffffff"     # WCAG contrast ratio
```

The skill never needs it: SKILL.md and `references/` give the same formulas for agents that can't run code.

## Safety and honesty

- No help with cracks, keygens, trial resets, unlocking Canva Pro or removing watermarks.
- No copying other brands' logos or living artists' styles for commercial work; it offers an original direction instead.
- Version facts carry the version, and anything not confirmed on an official page is marked in `references/` as unverified.
- Licence notes are basics, not legal advice.

## Example requests

> Photoshop-da şəklin fonunu necə silim? Məhsul şəklidir, ağ fon lazımdır.

> Я сделала визитку, в типографии цвета тусклые и текст у края обрезался. Что не так?

> I use Photopea. How do I make a YouTube thumbnail with my photo cut out and big text?

## Files

- `SKILL.md`: the skill
- `references/photoshop-howto.md`: menu paths and Win/Mac shortcuts
- `references/free-tools.md`: Photopea, GIMP 3, Krita, Inkscape, Canva; 15-task mapping table
- `references/troubleshooting.md`: 10 symptom cards
- `references/sizes-and-print.md`: social sizes, print sizes with bleed, formulas, print checklist
- `references/design-review.md`: review checklist and contrast by hand
- `references/ai-features.md`: generative AI requirements, credits, commercial use
- `references/rights.md`: software options, fonts, stock, AI images, logos
- `references/job-prep.md`: Baku job snapshot, portfolio, test task, interview
- `scripts/design_calc.py`: optional calculator; `tests/node-port/`: Node port used to verify its maths
- `evals/evals.json`: test prompts; `tests/`: blind eval results

## Install

- **Claude Code:** copy this folder to `~/.claude/skills/photoshop-design-coach/`.
- **Claude app:** zip the folder (with `SKILL.md` inside `photoshop-design-coach/`) and upload it under *Customize → Skills*.
- **Other agents:** use `SKILL.md` as the system prompt and attach `references/`.
- **Agensi package:** `pwsh ./scripts/build-agensi-zip.ps1` builds `dist/photoshop-design-coach.zip`.

## Sources

Written from scratch. Facts were checked on adobe.com plan and feature pages, photopea.com/learn, gimp.org and docs.gimp.org, krita.org, w3.org (WCAG 2.2), YouTube and LinkedIn help, the Meta ads guide, and the licence pages of Unsplash, Pexels, Adobe Stock, the SIL OFL and the US Copyright Office. helpx.adobe.com could not be opened during research, so shortcut and troubleshooting facts from it are marked unverified. Research notes: `../../research/photoshop-design-skill-research-2026-11-11.md`.

Adobe, Photoshop, Firefly and Creative Cloud are trademarks of Adobe. Canva, Photopea, GIMP, Krita and Inkscape belong to their owners. This project is not affiliated with or endorsed by any of them.

## License

[MIT](LICENSE) © 2026 Codelady Abroad
