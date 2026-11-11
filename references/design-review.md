# Design review checklist

Use for "check my design". Start with one real strength, then max 5 fixes, most important first, each with the reason and the exact change. Kind and specific.

## If you can't see the design, ask for
1. Where it will be used and the size (Instagram post, A5 flyer…).
2. The headline and the key info (date, place, price, contact).
3. Colours as hex codes (in Photoshop: double-click the colour ▸ the `#` field).
4. Fonts and sizes.

## The checks, in order
1. **Purpose and focal point.** In 3 seconds, does the viewer see one main thing (the headline or the product)? One focal point, not three.
2. **Hierarchy.** Headline clearly bigger than the subhead, subhead bigger than body (about 1.5–2× steps). Key info (date/place/price) easy to find.
3. **Contrast (WCAG 2.2, V: w3.org).** Normal text ≥ 4.5:1, large text (≥ 24 px regular or ≥ ~18.7 px bold) ≥ 3:1, icons/graphics ≥ 3:1. Logos are exempt. If you have hex codes, compute it (formula below or `python scripts/design_calc.py contrast "#777777" "#ffffff"`).
4. **Fonts.** Max 2 families (one for headlines, one for text). Readable at phone size; body for social at least ~28–32 px on a 1080-px-wide post (rule of thumb). The font supports Azerbaijani/Cyrillic letters needed.
5. **Alignment and margins.** Everything aligns to something (left edge, centre, grid). Even outer margins (e.g. 60–80 px on a 1080 post; 3–5 mm safe zone in print).
6. **Spacing.** Related things close, unrelated things apart. Enough empty space; don't fill every corner.
7. **Colour.** 1 main + 1 accent + neutrals is enough. Brand colours if the client has them.
8. **Images.** Sharp at 100 %, not stretched, same light/style, cut-outs clean.
9. **Format fit.** Right size and ratio for the place; text inside safe zones (stories: not top 14 % / bottom 35 %); print: bleed + 300 ppi.
10. **Text quality.** Spelling, numbers, phone, Azerbaijani letters (ə ı ş ğ ç ö ü), no widows (one word alone on a line).
11. **Rights.** Fonts, photos, icons licensed; no copied logos or other brands' assets.

## Contrast by hand (text fallback)
1. Each channel c = value/255; linear = c/12.92 if c ≤ 0.04045 else ((c+0.055)/1.055)^2.4.
2. L = 0.2126 R + 0.7152 G + 0.0722 B (linear values).
3. ratio = (L_lighter + 0.05) / (L_darker + 0.05).
Known values (pre-computed): black/white 21:1; #767676 on white 4.54:1 (passes AA); #777777 on white 4.47:1 (fails AA, passes large); white on #FFD400 yellow ≈ 1.43:1 (fails everything); #777777 on #FFD400 ≈ 3.13:1 (large text only); black on #FFD400 ≈ 14.7:1; #1A1A1A on #FFD400 ≈ 12.2:1. If you can't compute and the pair isn't listed, say "estimate" and point to a free checker (webaim.org/resources/contrastchecker).

## Answer format
```
Works: <one line>
Fix first:
1. <problem> → <change> (why)
…
Next: <one step or offer>
```
