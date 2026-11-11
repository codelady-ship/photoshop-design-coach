# Photoshop how-to cheatsheet

Shortcuts are the Photoshop defaults (Windows / Mac). Users can change them under Edit ▸ Keyboard Shortcuts, so if one does nothing, check there. Source to send users to: https://helpx.adobe.com/photoshop/using/default-keyboard-shortcuts.html. **Status:** the helpx page could not be opened when this file was written (403), so these are the long-standing defaults, not freshly checked. If a user reports a different shortcut, believe their screen.

Russian/other interface: menu names differ; shortcuts are the same.

## Document and size
| Task | Path | Win | Mac |
|---|---|---|---|
| New document | File ▸ New (set W, H, units, resolution, RGB/CMYK) | `Ctrl+N` | `Cmd+N` |
| Image size (resample) | Image ▸ Image Size | `Ctrl+Alt+I` | `Cmd+Option+I` |
| Canvas size (add space, no scaling) | Image ▸ Canvas Size | `Ctrl+Alt+C` | `Cmd+Option+C` |
| Crop to exact ratio | Crop tool `C` ▸ options bar: Ratio or W × H × Resolution | `C` | `C` |
| Colour mode | Image ▸ Mode ▸ RGB Color / CMYK Color | – | – |
| Rulers / guides | View ▸ Rulers; drag a guide from the ruler; View ▸ Guides ▸ New Guide Layout (margins, columns) | `Ctrl+R` | `Cmd+R` |

Image Size tip: untick **Resample** to change only the ppi number for print without changing pixels. Tick Resample (Preserve Details 2.0 / Bicubic) to really change pixels. Upscaling a small photo adds no real detail.

## Layers
| Task | Path | Win | Mac |
|---|---|---|---|
| Duplicate layer / copy selection to new layer | Layer ▸ New ▸ Layer via Copy | `Ctrl+J` | `Cmd+J` |
| New layer | Layer ▸ New ▸ Layer | `Ctrl+Shift+N` | `Cmd+Shift+N` |
| Group layers | Layer ▸ Group Layers | `Ctrl+G` | `Cmd+G` |
| Clipping mask (layer shows only inside the one below) | Layer ▸ Create Clipping Mask | `Ctrl+Alt+G` | `Cmd+Option+G` |
| Layer mask | Layer ▸ Layer Mask ▸ Reveal All / Reveal Selection, or the mask icon at the bottom of the Layers panel | – | – |
| Smart Object (scale without losing quality) | Layer ▸ Smart Objects ▸ Convert to Smart Object | – | – |
| Merge visible to new layer (keep originals) | – | `Ctrl+Shift+Alt+E` | `Cmd+Shift+Option+E` |

Mask painting: black hides, white shows (`D` resets colours, `X` swaps).

## Transform
- Free Transform: Edit ▸ Free Transform, `Ctrl+T` / `Cmd+T`. Since Photoshop CC 2019 (v20) dragging a corner keeps proportions by default; hold `Shift` to stretch freely. (Old behaviour: Preferences ▸ General ▸ Use Legacy Free Transform.)
- Hold `Alt` / `Option` to scale from the centre. Press `Enter` / `Return` to apply, `Esc` to cancel.

## Select and cut out
| Task | Path |
|---|---|
| Select Subject (AI, one click) | Select ▸ Subject, or the Object Selection tool's options bar |
| Remove background in one step | Properties panel (with the layer selected) ▸ Quick Actions ▸ Remove Background; also on the Contextual Task Bar. Creates a layer mask, so nothing is deleted |
| Refine hair/edges | Select ▸ Select and Mask (`Ctrl+Alt+R` / `Cmd+Option+R`) ▸ Refine Hair or Refine Edge Brush ▸ Output To: Layer Mask |
| Select a colour range (e.g. sky) | Select ▸ Color Range / Select ▸ Sky |
| Invert selection | Select ▸ Inverse, `Ctrl+Shift+I` / `Cmd+Shift+I` |
| Deselect | `Ctrl+D` / `Cmd+D` |

## Retouch
| Task | Tool / path | Key |
|---|---|---|
| Small spots, dust, pimples | Spot Healing Brush | `J` (`Shift+J` cycles healing tools) |
| Remove an object (brush over it) | Remove tool (in the healing tools group, Photoshop 2024+; see ai-features.md) | `J` group |
| Fill a selected area from surroundings | Edit ▸ Content-Aware Fill (non-AI, no credits) | – |
| Copy texture by hand | Clone Stamp | `S` |
| Brightness/contrast without damage | Layer ▸ New Adjustment Layer ▸ Curves / Levels / Hue/Saturation | `Ctrl+M` (Curves, destructive version) |

Work on a duplicate layer (`Ctrl+J`) or a new empty layer with "Sample All Layers" on.

## Text
- Type tool `T`. Click once for point text (headlines); drag a box for paragraph text.
- Window ▸ Character / Paragraph for size, leading, tracking.
- Missing font on open: Photoshop shows a warning; Type ▸ Resolve Missing Fonts (Adobe Fonts may auto-activate if available).
- Keep text as text (vector) until export; it stays sharp at any size.

## Save and export
| Goal | Path | Win | Mac |
|---|---|---|---|
| Keep layers for later | File ▸ Save As ▸ .PSD (or .PSB if over 2 GB) | `Ctrl+Shift+S` | `Cmd+Shift+S` |
| JPG/PNG copy (keeps your PSD open) | File ▸ Save a Copy | `Ctrl+Alt+S` | `Cmd+Option+S` |
| Web/social export with size and quality | File ▸ Export ▸ Export As (tick Convert to sRGB) | `Ctrl+Shift+Alt+W` | `Cmd+Shift+Option+W` |
| One-click PNG | File ▸ Export ▸ Quick Export as PNG | – | – |
| Print PDF | File ▸ Save As ▸ Photoshop PDF ▸ preset PDF/X-1a or PDF/X-4 (ask the print shop) | – | – |

Export rules: photos → JPG quality 80–90 %; text, logos, flat graphics, transparency → PNG. Always check at 100 % zoom (`Ctrl+1` / `Cmd+1`).

## Colour for print
- Edit ▸ Color Settings (`Ctrl+Shift+K` / `Cmd+Shift+K`).
- View ▸ Proof Setup ▸ Working CMYK (or the print shop's profile) then View ▸ Proof Colors (`Ctrl+Y` / `Cmd+Y`) to preview print colours.
- View ▸ Gamut Warning (`Ctrl+Shift+Y` / `Cmd+Shift+Y`) shows colours that can't print.
- Convert only when asked: Edit ▸ Convert to Profile ▸ the shop's CMYK profile. Keep an RGB master copy.
