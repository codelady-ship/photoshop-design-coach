# Free tools and command mapping (checked 2026-11-11)

V = checked in the tool's own docs; U = not confirmed (page blocked or from memory). For U items tell the user "check the menu; it may be named slightly differently".

## Which free tool when
| Tool | Best for | Can't / weak | Notes |
|---|---|---|---|
| **Photopea** (photopea.com) | Closest to Photoshop, in the browser, opens and saves PSD | Big files are slow; ads on free plan; CMYK is only a preview (SWOP v2), not real prepress | Free with ads, paid ad-free Premium (price: check site). Runs in Chrome/Firefox/Edge/Safari (V: Wikipedia, photopea.com/learn) |
| **GIMP 3** (gimp.org) | Photo editing, retouch, offline, Win/Mac/Linux | No full CMYK editing yet; exports CMYK JPEG/TIFF/PSD and soft-proofs (V: GIMP 3.0 notes). Different shortcuts from Photoshop | 3.0 added non-destructive filters (V); 3.2 adds link/vector layers (V) |
| **Krita** (krita.org) | Drawing, illustration, painting | Not a layout/print tool | Free, open source, supports CMYK colour model (V) |
| **Inkscape** (inkscape.org) | Logos, icons, vector print files (SVG/PDF) | Not for photos | Free, open source (U) |
| **Canva Free** (canva.com) | Fast social posts from templates, team work | Background Remover, Magic Resize, Brand Kit, CMYK PDF are Pro (U); Canva elements can't be used in logos (U) | Good for SMM speed; weak for learning real skills |
| **Adobe Express Free** | Templates, quick social graphics, some AI | Premium features locked; remove-background free with daily limit (V, wording changes) | 250 generative credits/month free (V) |
| **remove.bg** | One-off cut-outs | Free preview only 0.25 MP (~625 × 400) (V) | Full res is paid |

## Photopea differences that trip people up
- **Free Transform is `Alt+Ctrl+T`** (Edit ▸ Free Transform), not `Ctrl+T`, because `Ctrl+T` opens a new browser tab (V: photopea.com/learn/free-transform). On Mac try `Option+Cmd+T`.
- Layer mask: Layer ▸ Raster Mask ▸ Add (or Vector Mask) per photopea.com/learn/masks (V); the submenu may show Reveal All / Hide All; the mask icon at the bottom of the Layers panel always works.
- Text stroke/shadow: Layer ▸ Layer Style ▸ Stroke / Drop Shadow, or double-click the layer (U: check the menu).
- One-click background removal: Select ▸ Remove BG, then File ▸ Export As ▸ PNG (V). Select ▸ Magic Cut also exists (U).
- Save with layers: File ▸ Save as PSD (V). Export: File ▸ Export As ▸ JPG/PNG/PDF/SVG with size and quality (V).
- Image ▸ Mode ▸ CMYK only previews print colours with a generic profile (V: Photopea 5.2 blog). For real print, send RGB PDF/PNG to the shop and ask them, or use a tool with real CMYK output.

## Mapping table
| Task | Photoshop | Photopea | GIMP 3 | Canva |
|---|---|---|---|---|
| New document | File ▸ New (`Ctrl+N`) | File ▸ New (U) | File ▸ New (`Ctrl+N`) (U) | Create a design ▸ Custom size |
| Resize image | Image ▸ Image Size (`Ctrl+Alt+I`) | Image ▸ Image Size (V) | Image ▸ Scale Image (V) | Resize (Pro) (U) |
| Canvas size | Image ▸ Canvas Size (`Ctrl+Alt+C`) | Image ▸ Canvas Size (V) | Image ▸ Canvas Size (V) | Custom size / Resize (U) |
| Crop | Crop tool `C` | Crop tool `C` (V) | Crop tool `Shift+C` (U) | Double-click image ▸ Crop |
| Free transform | `Ctrl+T` | **`Alt+Ctrl+T`** (V) | Unified Transform `Shift+T` (V) | Drag the handles |
| Cut out / remove BG | Select ▸ Subject; Quick Actions ▸ Remove Background | Select ▸ Remove BG (V) | Foreground Select tool (no default key) (V) | Edit ▸ BG Remover (Pro) (U) |
| Layer mask | Layer ▸ Layer Mask ▸ Reveal All | Layer ▸ Raster Mask ▸ Add (V) | Layer ▸ Mask ▸ Add Layer Mask (V) | Use Frames (U) |
| Clipping mask | `Ctrl+Alt+G` | `Alt+Ctrl+G` (U) | No direct one; use a layer mask from selection (U) | Frames (U) |
| Spot heal / remove | Spot Healing `J`, Remove tool | Spot Healing Brush (V) | Heal `H`, Ctrl+click sets source (V) | Magic Eraser (Pro) (U) |
| Clone | Clone Stamp `S` | Clone Stamp `S` (U) | Clone `C` (U) | – |
| Text | Type tool `T` | `T` (U) | Text tool `T` (U) | Text ▸ Add a heading |
| Curves / Levels | Layer ▸ New Adjustment Layer | Layer ▸ New Adjustment Layer (U) | Colors ▸ Curves / Levels, editable afterwards in 3.x (V) | Edit ▸ Adjust (U) |
| Export PNG/JPG | File ▸ Export ▸ Export As | File ▸ Export As (V) | File ▸ Export As (`Shift+Ctrl+E`) (V) | Share ▸ Download |
| Save layered | .PSD | File ▸ Save as PSD (V) | .XCF (`Ctrl+S`) (U) | Stays in Canva |
| CMYK | Image ▸ Mode ▸ CMYK / Convert to Profile | Image ▸ Mode ▸ CMYK (preview only) (V) | Export CMYK JPEG/TIFF/PSD + soft-proof (V) | PDF Print ▸ CMYK (Pro) (U) |
| Rulers/guides | View ▸ Rulers (`Ctrl+R`) | View ▸ Rulers; drag guides with Move tool (V) | View ▸ Show Rulers (U) | File ▸ Settings ▸ Show rulers and guides (U) |

On Mac, `Ctrl` → `Cmd`, `Alt` → `Option` in Photoshop and GIMP. Photopea follows the browser: test the key once.

## Recommended free path for a beginner
1. Learn layers, masks, selections and export in **Photopea** (same ideas as Photoshop, so skills transfer to a job).
2. Use **Canva** for speed later, not as the only tool (job ads ask for Photoshop/Illustrator).
3. Logos in **Inkscape** (vector), never as a raster PNG only.
4. Before a job test that requires Photoshop, use the official 7-day trial in the final week.
