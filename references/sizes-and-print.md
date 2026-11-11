# Sizes, DPI, bleed and print (checked 2026-11-11)

V = official/primary page opened; U = not confirmed. Platforms change sizes; for important jobs say "check the platform's help page".

## Screen vs print in one line each
- **Screen** (Instagram, web, YouTube): only **pixels** and the **aspect ratio** matter. The ppi number (72/96/300) changes nothing on screen. Work in RGB, export sRGB.
- **Print**: final size in **mm** + **300 ppi at that size** for flyers, cards, posters you hold close. Large banners seen from far: often 100–150 ppi at full size (U); **ask the print shop**.

## Social sizes (pixels)
| Use | Size | Ratio | Mark / note |
|---|---|---|---|
| Instagram feed portrait (best default) | 1080 × 1350 | 4:5 | Common size (U). Meta ads guide recommends 1440 × 1800, same 4:5 (V) |
| Instagram square | 1080 × 1080 | 1:1 | U |
| Instagram 3:4 grid look | 1080 × 1440 | 3:4 | U: grid crop discussed since 2025, no official confirmation found |
| Stories / Reels cover / TikTok | 1080 × 1920 | 9:16 | Meta ads guide: 1440 × 2560 (V). Keep text out of the top 14 %, bottom 35 % and 6 % each side (V, ads guide; good rule for organic too) |
| Facebook feed | 1080 × 1350 or 1440 × 1800 | 4:5 | V (ads guide 1440 × 1800, min 600 × 750) |
| YouTube thumbnail | 1280 × 720 classic; YouTube now recommends 3840 × 2160 | 16:9 | V: support.google.com/youtube/answer/72431 — min width 640, JPG/PNG, max 2 MB on mobile / 50 MB desktop; Shorts 9:16 |
| YouTube banner | 2560 × 1440 (min 2048 × 1152, ≤ 6 MB) | 16:9 | V: answer/10456525 — text/logo safe area 1235 × 338 at min size (about 1546 × 423 at 2560, derived) |
| LinkedIn company cover | 1512 × 256; logo 400 × 400 | – | V: linkedin.com/help answer a563309, PNG/JPG ≤ 3 MB |
| LinkedIn personal banner | 1584 × 396 | 4:1 | U |
| LinkedIn link-post image | 1200 × 627 | 1.91:1 | V (same page) |
| X (Twitter) image | 1600 × 900 or 1200 × 1200 | 16:9 / 1:1 | U |

Captions, hashtags, posting plans: not here; point to the Instagram Manager skill.

## Print sizes (trim, mm)
| Item | Trim | + 3 mm bleed | Pixels at 300 ppi (with bleed) |
|---|---|---|---|
| A3 poster | 297 × 420 | 303 × 426 | 3579 × 5031 |
| A4 | 210 × 297 | 216 × 303 | 2551 × 3579 |
| A5 flyer | 148 × 210 | 154 × 216 | 1819 × 2551 |
| A6 flyer/postcard | 105 × 148 | 111 × 154 | 1311 × 1819 |
| Business card AZ/CIS | 90 × 50 | 96 × 56 | 1134 × 661 |
| Business card EU/Turkey | 85 × 55 | 91 × 61 | 1075 × 720 |
| Business card US 3.5 × 2 in | 88.9 × 50.8 | + 0.125 in → 3.75 × 2.25 in | 1125 × 675 |
| Roll-up banner | 850 × 2000 | ask the shop (often 0 or larger) | at 150 ppi: 5020 × 11811 (no bleed) |

ISO A sizes V (Wikipedia, ISO 216). Card sizes: 85 × 55 (W. Europe, Turkey), 90 × 50 (Russia and others), 3.5 × 2 in (US) V (Wikipedia); 90 × 50 "common in Azerbaijan" U — ask the shop.

## Formulas (text fallback; no code needed)
- pixels = mm ÷ 25.4 × ppi  (round to the nearest whole pixel)
- mm = pixels ÷ ppi × 25.4
- size with bleed = trim + 2 × bleed (each direction)
- Max print size of a photo at 300 ppi: width px ÷ 300 × 25.4 mm. Example 3000 × 2000 px → 254 × 169 mm.
- Example: 90 × 50 mm card + 3 mm bleed → 96 × 56 mm → 96 ÷ 25.4 × 300 = 1134 px, 56 ÷ 25.4 × 300 = 661 px.
- Optional: `python scripts/design_calc.py px 90 50 --dpi 300 --bleed 3` gives the same numbers. `preset a5`, `preset yt-banner`, `presets` lists all.

## Print checklist (send to the print shop)
1. Ask first: size, bleed, safe zone, file type (PDF?), colour mode/profile, paper, quantity, deadline. **Their rules win.**
2. Document at final size + bleed, 300 ppi. Background and photos run to the bleed edge.
3. Safe zone: text and logos at least 3 mm inside the trim (5 mm is safer on cards).
4. Bleed: 3 mm per side (metric, AZ/CIS/EU); 0.125 in (US). A Baku print shop (print.az) asks for "PDF, CMYK, 3 mm on each side, text and logo at least 3 mm inside the cut line" (V: print.az/korporativ-cap-mehsullari/vizit-kartlar/).
5. Colour: CMYK if they ask, with their profile (Edit ▸ Convert to Profile); soft-proof first (View ▸ Proof Colors). Keep an RGB master.
6. Black: small text in pure black (K 100 only). Big black areas: rich black (e.g. C50 M50 Y50 K100) only if the shop agrees; total ink ≤ ~240–300 % (V: rich black, Wikipedia; ask the shop).
7. Fonts: embedded in the PDF (PDF/X-1a needs all fonts embedded and only CMYK/spot colours; PDF/X-4 keeps transparency and allows colour-managed RGB) (V: PDF/X, Wikipedia). Or convert text to shapes on a copy.
8. Export: File ▸ Save As ▸ Photoshop PDF ▸ PDF/X preset the shop names. Name it `client_item_size_v1.pdf`.
9. Check at 100 % zoom and on a printed home test if possible. Spelling, phone numbers, Azerbaijani letters (ə, ı, ş, ğ).

Photoshop is a raster editor. For multi-page or text-heavy print (brochures, menus), InDesign/Affinity/Scribus or Canva PDF Print are easier; Photoshop is fine for a single flyer, poster or card.
