# Symptom cards

Format: likely causes in order → a check the user can do → the fix. Max 3 causes in an answer.

## 1. Export looks blurry / pixelated after upload
1. **Document too small or upscaled.** Check: Image ▸ Image Size, pixel numbers. Fix: start at the target size or bigger (e.g. 1080 × 1350 for an Instagram portrait post). Upscaling a small image adds no detail; reshoot or find a bigger source.
2. **Wrong aspect ratio, so the platform crops/rescales.** Check: ratio vs the platform (see sizes-and-print.md). Fix: crop to the exact ratio before export.
3. **Heavy JPG compression or the platform's own compression.** Check: Export As quality. Fix: JPG 80–90 % for photos, PNG for text/graphics; upload over Wi-Fi; in the Instagram app turn on high-quality uploads if available (check in app).
Also: text rasterised then scaled → keep text as a type layer; scaled raster logos → use a Smart Object or a vector (SVG/AI/PDF) logo.

## 2. Colours look different after printing (dull, blue turns purple)
1. **File was RGB with very bright colours outside the CMYK gamut.** Check: Image ▸ Mode; View ▸ Gamut Warning (`Ctrl+Shift+Y` / `Cmd+Shift+Y`). Fix: ask the print shop for its CMYK profile, soft-proof with View ▸ Proof Colors (`Ctrl+Y` / `Cmd+Y`), adjust, then Edit ▸ Convert to Profile only if they ask for CMYK. Bright RGB blues, greens and oranges can never print exactly.
2. **Screen too bright / not calibrated.** Check: phone vs monitor look different too. Fix: ask for a test print or a proof; judge colour on paper.
3. **Paper and process.** Uncoated paper prints duller than coated. Fix: ask which paper; for brand colours ask about Pantone/spot colours.
Never promise screen = print.

## 3. Text or logo cut off at the edge / white line at the edge after cutting
1. **No bleed.** Fix: extend the background 3 mm past each trim edge (0.125 in in the US). A 90 × 50 mm card becomes 96 × 56 mm.
2. **Important things too close to the edge.** Fix: keep text and logos inside a safe zone 3–5 mm inside the trim line (use guides: View ▸ Guides ▸ New Guide Layout ▸ Margin in recent versions; older versions: View ▸ New Guide Layout — check your View menu).
3. **Wrong document size** (e.g. made at 1000 × 600 px without mm). Fix: rebuild at the mm size + bleed at 300 ppi.

## 4. Generative Fill / Generate Image is greyed out or fails
Adobe's own list (helpx "Common generative AI issues in Photoshop", seen in search, not opened):
1. **No active selection** (Generative Fill needs one; Expand needs the Crop tool). Check: marching ants visible? Fix: make a selection.
2. **Unsupported file or layer.** Needs an RGB, 8-bit document and a normal pixel layer; text layers, shapes, smart objects, clipped layers, grayscale or 32-bit files can block it. Check: Image ▸ Mode. Fix: Image ▸ Mode ▸ RGB Color and 8 Bits/Channel, rasterise or pick a pixel layer, unclip.
3. **Account or connection.** Not signed in, offline/firewall, no generative credits left, Adobe ID without a valid birth date (18+ rule) or an Education/Enterprise account with gen-AI turned off, or a region where it is not offered. Check: signed in? (profile icon at the top right of Photoshop, or the Creative Cloud app); credits on the Adobe account page. Fix: sign in, connect, wait for the monthly reset or use Content-Aware Fill / Remove tool (non-AI).
Also update Photoshop (Help ▸ Updates) if the version is old.

## 5. File is huge / Photoshop slow
1. Many full-size layers and Smart Objects. Fix: merge finished layers into a copy, delete hidden unused layers, crop away off-canvas pixels (Crop tool ▸ Delete Cropped Pixels).
2. Document far bigger than needed (e.g. 8000 px for an Instagram post). Fix: Image ▸ Image Size with Resample, on a copy.
3. Scratch disk/RAM. Fix: Edit/Photoshop ▸ Preferences ▸ Performance (RAM %), Scratch Disks (a drive with free space). Close other apps.
For export size: the final JPG is small even if the PSD is big; that's normal.

## 6. Jagged or haloed cut-out edges
1. Hard selection. Fix: Select ▸ Select and Mask ▸ Refine Hair / Refine Edge Brush, Smooth 1–3, Feather 0.5–1 px, Decontaminate Colors for colour fringes, Output To: Layer Mask.
2. Low-resolution photo. Fix: use a bigger source.
3. Eraser was used. Fix: next time use a layer mask (paint black/white) so edges can be fixed later.

## 7. Font missing / text changed when opened on another computer or at the print shop
1. Font not installed there. Fix: send fonts only if the licence allows it (Adobe Fonts: never send font files); otherwise send a PDF with fonts embedded, or rasterise/convert text to shapes on a copy (Type ▸ Convert to Shape) for print.
2. Free font from a random site without Azerbaijani letters (ə, ğ, ı, ş). Fix: pick a font that supports the language (Google Fonts has a language filter).

## 8. Can't move / edit / paint
1. Layer locked (lock icon) or the Background layer. Fix: click the lock / double-click Background ▸ OK.
2. An active selection elsewhere. Fix: `Ctrl+D` / `Cmd+D`.
3. Wrong layer selected or painting on a mask. Fix: click the layer thumbnail (not the mask thumbnail).
4. Image in Indexed Color mode (GIFs). Fix: Image ▸ Mode ▸ RGB Color.

## 9. Colours look washed out on the web / Instagram after export
1. Exported without sRGB. Fix: Export As ▸ tick Convert to sRGB and embed the colour profile.
2. File was CMYK. Fix: make web versions from the RGB master.

## 10. Photoshop crashed / file lost
Work on a copy. Check File ▸ Open Recent; Photoshop's auto-recovery (Preferences ▸ File Handling ▸ Automatically Save Recovery Information) may reopen it after restart. Cloud documents have version history. Save often (`Ctrl+S` / `Cmd+S`).

## Free tools quick fixes
- Photopea blurry export: File ▸ Export as ▸ check the width/height and quality fields.
- GIMP "Save As" only saves .xcf: use File ▸ Export As (`Shift+Ctrl+E`) for PNG/JPG.
- Canva "print" blurry: download as PDF Print; Canva's crop marks and bleed option is in the download panel (check in app).
