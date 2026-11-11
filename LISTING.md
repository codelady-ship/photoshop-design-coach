# Agensi listing texts: Photoshop & Design Coach

DRAFT. Nothing has been submitted. The owner pastes these fields into agensi.io/dashboard/submit herself. Upload `dist/photoshop-design-coach.zip` (built by `scripts/build-agensi-zip.ps1`). Any demo screenshots come from @codelady.abroad or a fictional account, never @cahanacademy.

| | |
|---|---|
| ZIP to upload | `photoshop-design-coach\dist\photoshop-design-coach.zip` |
| ZIP contents | SKILL.md, references/ (8), scripts/design_calc.py, CHANGELOG.md. No README, LICENSE, LISTING, evals or tests |
| Version | 1.0.0 |
| Price | **Free** |
| Brand | Codelady Abroad |
| Docs link | **Leave empty.** No public repo exists yet. Add `https://github.com/codelady-ship/photoshop-design-coach` only after the owner makes the repo public (and then uncomment `docs_url` in SKILL.md) |

## Name (≤ 60) — 49 characters
```text
Photoshop & Design Coach: Free Tools, Print, Jobs
```

## Summary (≤ 300) — 294 characters
```text
Free Photoshop and graphic-design coach. Step-by-step how-tos with Win/Mac shortcuts and Photopea/GIMP/Canva equivalents, a fix-my-problem mode, social and print sizes (DPI, bleed, CMYK), design reviews with a contrast check, honest AI-feature help, junior designer job prep and licence basics.
```

## Description (Markdown) — 1494 characters (Agensi documents no cap for this field; the 1,024 cap applies only to the SKILL.md frontmatter description, which is 986)
```markdown
Photoshop & Design Coach teaches you to do the work yourself, in Photoshop or a free tool (Photopea, GIMP, Krita, Canva). It answers in your language (Azerbaijani by default), phone-short.

- **How-to:** numbered steps with exact menu paths and Windows and Mac shortcuts, then the same task in a free tool.
- **Fix:** blurry export, colours change in print, text cut at the edge, Generative Fill greyed out, huge file, jagged cut-out, missing fonts → likely cause, one check, the fix.
- **Size & print:** pixel sizes for posts, stories, thumbnails and banners; DPI, 3 mm bleed, safe zone, CMYK and PDF checklist for the print shop. Includes an optional standard-library Python calculator; without code it does the maths in text.
- **Review:** one strength and up to 5 prioritised fixes, with WCAG contrast numbers.
- **AI:** what Generative Fill, Remove tool and credits need, a prompt pattern, a non-AI way, commercial-use notes.
- **Job:** portfolio plan, test-task time plan and self-check, interview questions.
- **Rights:** legal software options, font, stock and AI-image licence basics.

Where it stops: it can't see your screen or open PSD files (it reviews images only if your agent shows them). It doesn't control Photoshop. It never helps with cracks, copying other brands' logos or imitating living artists' styles for commercial work. Licence notes are basics, not legal advice. Your print shop's and client's rules win. Captions and posting plans: see our Instagram Manager skill.
```

## "See it in action" demo (700+ characters)
Use the passing blind-eval answer for case 2 (Russian business card print problem) or case 3 (A5 flyer + story sizes) from `tests/` (request + full answer).

## Categories (up to 3)
1. Education & Learning
2. Branding & Design
3. Career & Jobs

## Tags (10)
photoshop, graphic-design, photopea, gimp, canva, print-design, social-media-design, portfolio, students, free

## Use cases (8)
- Learn a Photoshop task step by step with Windows and Mac shortcuts
- Do the same task in Photopea, GIMP or Canva for free
- Fix a blurry export, a colour shift in print or a greyed-out AI tool
- Get exact pixel sizes for posts, stories, thumbnails and banners
- Prepare a flyer or business card for the print shop (bleed, CMYK, PDF)
- Get a design review with a colour-contrast check
- Build a junior designer portfolio and prepare for a test task
- Check whether fonts, stock photos and AI images are safe to use

## Needs access to
Nothing required. Text only. Optional: running `scripts/design_calc.py` (Python 3, standard library, no files, no network) if the agent can run code. Expect the scan to show "scripts present"; there are no network calls, file writes, shell calls or env reads.

## Compatibility note
Works on any agent. The Python calculator is optional; agents without code execution use the formulas in SKILL.md. Image review needs an agent that accepts images; otherwise the user describes the design.

## Limitations / FAQ
- **Does it open my PSD?** No. Paste the numbers (Image ▸ Image Size, Image ▸ Mode) or a screenshot if your agent supports images.
- **Are shortcuts exact?** They are Photoshop's defaults; custom shortcuts and other languages may differ. Facts not confirmed on an official page are marked in the references.
- **Prices and AI credits?** Taken from Adobe's US pages on 2026-11-11; they change and differ by country.
- **Is it legal advice?** No. Licence notes are basics; read the licence of the exact item.
- **Not affiliated with Adobe, Canva or Photopea.** Photoshop is a trademark of Adobe.

## Price suggestion: **Free**
- **Competitors are free:** the closest Agensi listing (Visual Design, Brand and Presentations pack) is free with 5 uses; Photoshop GPTs are free; skills.sh Photoshop skills are free automation tools.
- **Audience:** beginners and SMM freelancers in Azerbaijan/CIS (SMM pay seen 300–700 AZN/month). Under $5 they can only pay from an Agensi balance, which most don't have.
- **Low demand signal:** design skills on Agensi mostly have under 100 uses; a paid newcomer with no reviews would get none.
- **Strategy:** free coaches build uses and reviews for Codelady Abroad's paid skills. No payout setup is needed.
- **Later:** if it passes 50+ uses with good reviews, a separate paid "Design Coach Pro" (one-time $5): 30 graded daily briefs with feedback rubrics, local print-shop templates and a portfolio review checklist. It must be a different package, not this ZIP.
