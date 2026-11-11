# Photoshop AI features (checked 2026-11-11)

Marks: **V** = official Adobe page opened. **U** = Adobe page blocked (helpx returned 403) or third-party/search only. Tell the user "check Adobe's page for your version" for anything U. Features and credit costs change often; never quote a number not in this file.

## What every generative feature needs
- Internet, signing in with an Adobe ID, and **generative credits**. (V: adobe.com/products/photoshop/generative-fill.html says Photoshop 25.0+, a membership or trial with generative credits, and not available in China.)
- Size limits for Generative Fill on that page: files over 40 MB or bigger than 8000 × 8000 px are rejected. (V)
- Age 18+ on the Adobe ID (a missing birth date can grey the tool out), not on Education/Enterprise accounts where an admin turned it off, and not in some regions. (U: helpx "Common generative AI issues in Photoshop" via search; community posts.)
- RGB, 8-bit document, a normal pixel layer and (for Fill) an active selection. Text layers, shapes, smart objects, clipped layers, grayscale and 32-bit can block it. (U: same helpx page via search.)

## Credits (US plan pages, V on adobe.com, 2026-11-11)
- Photoshop single-app plan: **25 generative credits per month**. Creative Cloud Pro: 4,000. Photography plan: 1,000. (adobe.com/products/photoshop/plans.html)
- Credits reset monthly and don't roll over; you can wait, upgrade or buy an add-on. (adobe.com/products/firefly/plans.html)
- Adobe's Firefly models cost fewer credits than partner models (e.g. Gemini "Nano Banana", FLUX) inside Generative Fill/Expand, which are "premium" and cost more per generation (U: CG Channel, Adobe community posts). Say "partner models use more credits; check the number shown before you click".
- With 25 credits a beginner can run out fast. Teach the non-AI tools too.

## Features (where to find them)
| Feature | What it does | Where | Credits | Mark |
|---|---|---|---|---|
| Generative Fill | Adds, removes or replaces content inside a selection from a text prompt (or empty prompt to remove) | Make a selection ▸ Contextual Task Bar ▸ Generative Fill, or Edit ▸ Generative Fill | Yes | V (page), path U |
| Generative Expand | Extends the canvas with matching content | Crop tool `C` ▸ drag past the edge ▸ Generate | Yes | U |
| Remove tool | Brush over an object to remove it | Healing tools group (`J`), Photoshop 25.0+ (2024) | Basic use: no credits; newer "remove related elements" options may use credits | U |
| Generate Image / Generate Background | Creates an image or a new background from a prompt | Contextual Task Bar / Edit menu (2024+) | Yes | U |
| Remove Background | One-click cut-out with a layer mask | Properties ▸ Quick Actions ▸ Remove Background | No (on-device for the basic action) | U |
| Harmonize | Matches light/colour of a placed object to the background | Layer/Contextual Task Bar (Photoshop 27, 2025) | Yes | U |
| Generative Upscale | Enlarges with AI | Image menu (27.0+) | Yes | U |
| AI Assistant (beta) | Chat-style help/edits | Photoshop web and mobile beta (2025–2026) | Varies | U |

Newest desktop release seen: Photoshop 28.0 (November 2026, needs Windows 10+ / macOS 15+) with Relight, Generative Recompose and more (U: cgchannel.com). If a user names a feature not listed here, say you can't confirm it and point to Help ▸ What's New in their Photoshop.

## Prompt pattern (Generative Fill)
- Select a bit more than the area (include the shadow). Describe **what should be there**, not commands: "wooden table surface, soft daylight" (not "remove the cup"). Empty prompt = remove and fill with surroundings.
- Generate 2–3 times, pick a variation in the Properties panel, then clean up edges with a mask.
- Match light, perspective and grain; zoom to 100 % before you say it's done.

## Non-AI alternatives (no internet, no credits, also in free tools)
- Edit ▸ Content-Aware Fill (selection first), Spot Healing Brush (`J`), Clone Stamp (`S`).
- Photopea: Spot Healing, Clone Stamp, Edit ▸ Content-Aware Fill style "Fill" (check the menu); GIMP: Heal tool (`H`), Clone (`C`), Filters ▸ Enhance ▸ Heal Selection (if the Resynthesizer plug-in is installed).

## Commercial use and rights (short; not legal advice)
- Adobe says outputs of its generative AI features can **generally be used commercially**, but **beta features may be limited to personal use** (V: adobe.com/express/pricing FAQ; adobe.com/products/firefly/plans.html "Outputs from Adobe Firefly AI models are safe for commercial use"). Partner-model output (Gemini, FLUX…) is the user's responsibility to check (V: Firefly plans page).
- Adobe's own Generative Fill page has mixed wording on commercial use (V, noted 2026-11-11), so tell users: "check Adobe's current terms for the feature you use; avoid beta features for client work".
- Adobe Gen AI User Guidelines forbid prompts made to generate copyrighted or trademarked content, impersonation, sexual content involving minors, hate and violence (V: adobe.com/legal/licenses-terms/adobe-gen-ai-user-guidelines.html).
- US Copyright Office (Part 2 report, 29 Jan 2025): purely AI-generated material and prompts alone are not copyrightable; human selection, arrangement and edits can be (V: copyright.gov/ai). Other countries may differ.
- Content Credentials may be attached to files edited with generative AI (U). Don't promise anything about them.
- Never generate real people for ads without consent, other brands' logos, or "in the style of <living artist>" for commercial work.
