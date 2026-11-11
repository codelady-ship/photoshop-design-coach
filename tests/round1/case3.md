Yes, I worked it out by hand with the formula `pixels = mm ÷ 25.4 × ppi`.

**1. A5 flyer (print)**

Bleed = extra 3 mm of background past the cut line, so nothing white shows after cutting.

- A5 trim: 148 × 210 mm
- Add 3 mm bleed on each side: 148 + 6 = 154 mm, 210 + 6 = 216 mm
- At 300 ppi: 154 ÷ 25.4 × 300 = **1819 px**, 216 ÷ 25.4 × 300 = **2551 px**

Document: **1819 × 2551 px, 300 ppi** (`File ▸ New` or `Cmd+N` / `Ctrl+N`). Keep text and logo at least 3 mm inside the cut line (5 mm is safer). That is about 35 px at 300 ppi, or 59 px for 5 mm.

**2. Instagram story (screen)**

- **1080 × 1920 px**, ratio 9:16, RGB (sRGB). PPI does not matter on screen.
- Meta's ads guide recommends 1440 × 2560 for the same ratio if you want it sharper.
- Safe zone: keep text out of the top 14 % (about 270 px), the bottom 35 % (about 670 px) and 6 % on each side (about 65 px). The app puts buttons and the reply bar there.

**Important:** the story is much taller and narrower than A5, and the safe zone is big. Do not just stretch the flyer. Duplicate the file, make a new 1080 × 1920 canvas and rearrange the elements: headline, offer, phone number or address in the middle zone.

**Before you start:** ask the print shop for their rules (PDF? CMYK? bleed?). Their rules win. Many Baku shops ask for PDF, CMYK, 3 mm bleed on each side.

Free: in Photopea use `File ▸ New` and type the pixel sizes. Canva Free lets you set custom sizes in px or mm.

Next step: tell me which program you use (Photoshop, Photopea, Canva) and I will give you the steps to set up both documents.
