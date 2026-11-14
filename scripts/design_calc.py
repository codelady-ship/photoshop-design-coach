#!/usr/bin/env python3
"""design_calc.py - optional helper for the photoshop-design-coach skill.

Standalone, Python 3.8+ standard library only. Reads no files, writes no
files, uses no network. Safe to run anywhere.

Commands
  px       print size -> pixels      design_calc.py px 210 297 --unit mm --dpi 300 --bleed 3
  size     pixels -> print size      design_calc.py size 3000 2000 --dpi 300
  preset   one named size            design_calc.py preset ig-portrait
  presets  list all named sizes      design_calc.py presets
  contrast WCAG 2.x contrast ratio   design_calc.py contrast "#777777" "#ffffff"

Add --json to any command for machine-readable output, before or after the
command: design_calc.py px 90 50 --json  or  design_calc.py --json px 90 50
"""

import argparse
import json
import sys

MM_PER_INCH = 25.4

# Named sizes. kind "px" = screen (pixels); kind "mm" = print trim size.
# Screen sizes: check the platform's own help page before an important job;
# platforms change them. Print sizes: ISO 216 and common local card sizes.
PRESETS = {
    # Instagram (Meta help pages; 4:5 portrait is the safe feed default)
    "ig-square":   {"kind": "px", "w": 1080, "h": 1080, "note": "Instagram feed 1:1"},
    "ig-portrait": {"kind": "px", "w": 1080, "h": 1350, "note": "Instagram feed 4:5 (most space in feed)"},
    "ig-34":       {"kind": "px", "w": 1080, "h": 1440, "note": "Instagram 3:4 (grid crop talked about since 2025; not confirmed officially - check in app)"},
    "ig-story":    {"kind": "px", "w": 1080, "h": 1920, "note": "Stories/Reels 9:16; Meta ads guide: keep text out of top 14%, bottom 35%, 6% each side"},
    "tiktok":      {"kind": "px", "w": 1080, "h": 1920, "note": "TikTok 9:16"},
    "fb-post":     {"kind": "px", "w": 1080, "h": 1350, "note": "Facebook feed 4:5 (Meta ads guide recommends 1440x1800; 1080x1350 is the same ratio)"},
    "yt-thumb":    {"kind": "px", "w": 1280, "h": 720,  "note": "YouTube thumbnail 16:9 classic size (min width 640); 2 MB limit on mobile, 50 MB desktop"},
    "yt-thumb-4k": {"kind": "px", "w": 3840, "h": 2160, "note": "YouTube now recommends 3840x2160 (16:9); keep under the upload limit"},
    "yt-banner":   {"kind": "px", "w": 2560, "h": 1440, "note": "YouTube banner (min 2048x1152, max 6 MB); text/logo safe area centre 1235x338 at min size, about 1546x423 at 2560"},
    "li-banner":   {"kind": "px", "w": 1584, "h": 396,  "note": "LinkedIn personal profile background 4:1 (unverified; company cover is 1512x256)"},
    "li-post":     {"kind": "px", "w": 1200, "h": 1200, "note": "LinkedIn square image post (1200x627 for link-style)"},
    "x-post":      {"kind": "px", "w": 1600, "h": 900,  "note": "X (Twitter) 16:9 image (unverified, check help page)"},
    # Print (trim size, mm). Add bleed with --bleed.
    "a3":          {"kind": "mm", "w": 297, "h": 420, "note": "ISO A3"},
    "a4":          {"kind": "mm", "w": 210, "h": 297, "note": "ISO A4"},
    "a5":          {"kind": "mm", "w": 148, "h": 210, "note": "ISO A5 (common flyer)"},
    "a6":          {"kind": "mm", "w": 105, "h": 148, "note": "ISO A6 (small flyer/postcard)"},
    "card-90x50":  {"kind": "mm", "w": 90,  "h": 50,  "note": "Business card common in AZ/CIS"},
    "card-85x55":  {"kind": "mm", "w": 85,  "h": 55,  "note": "Business card common in EU"},
    "card-us":     {"kind": "mm", "w": 88.9, "h": 50.8, "note": "Business card US 3.5x2 in"},
    "rollup":      {"kind": "mm", "w": 850, "h": 2000, "note": "Roll-up banner 85x200 cm; 100-150 ppi at full size is usual - ask the print shop"},
}


def to_mm(value, unit):
    if unit == "mm":
        return value
    if unit == "cm":
        return value * 10.0
    if unit == "in":
        return value * MM_PER_INCH
    raise ValueError("unit must be mm, cm or in")


def mm_to_px(mm, dpi):
    # Round half up so 0.5 px always rounds the same way on every system.
    return int(mm / MM_PER_INCH * dpi + 0.5)


def print_to_px(w, h, unit="mm", dpi=300, bleed_mm=0.0):
    if dpi <= 0:
        raise ValueError("dpi must be > 0")
    wmm, hmm = to_mm(w, unit), to_mm(h, unit)
    out = {
        "trim_mm": [round(wmm, 2), round(hmm, 2)],
        "dpi": dpi,
        "trim_px": [mm_to_px(wmm, dpi), mm_to_px(hmm, dpi)],
        "bleed_mm_each_side": bleed_mm,
    }
    if bleed_mm:
        bw, bh = wmm + 2 * bleed_mm, hmm + 2 * bleed_mm
        out["with_bleed_mm"] = [round(bw, 2), round(bh, 2)]
        out["with_bleed_px"] = [mm_to_px(bw, dpi), mm_to_px(bh, dpi)]
    return out


def px_to_print(wpx, hpx, dpi=300):
    if dpi <= 0:
        raise ValueError("dpi must be > 0")
    w_in, h_in = wpx / dpi, hpx / dpi
    return {
        "px": [wpx, hpx],
        "dpi": dpi,
        "size_mm": [round(w_in * MM_PER_INCH, 1), round(h_in * MM_PER_INCH, 1)],
        "size_cm": [round(w_in * 2.54, 2), round(h_in * 2.54, 2)],
        "size_in": [round(w_in, 2), round(h_in, 2)],
        "megapixels": round(wpx * hpx / 1e6, 2),
    }


def parse_hex(color):
    c = color.strip().lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    if len(c) != 6:
        raise ValueError("colour must be #RGB or #RRGGBB, got %r" % color)
    try:
        return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        raise ValueError("colour must be hex, got %r" % color)


def channel(v8):
    s = v8 / 255.0
    # WCAG 2.x sRGB linearisation (0.04045 per IEC 61966-2-1; WCAG text says
    # 0.03928 - no 8-bit value lies between, so results are identical).
    return s / 12.92 if s <= 0.04045 else ((s + 0.055) / 1.055) ** 2.4


def luminance(rgb):
    r, g, b = (channel(v) for v in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(fg, bg):
    l1, l2 = luminance(parse_hex(fg)), luminance(parse_hex(bg))
    hi, lo = max(l1, l2), min(l1, l2)
    ratio = (hi + 0.05) / (lo + 0.05)
    # Compare the ratio rounded down to 2 decimals so 4.499 never shows as a pass.
    r2 = int(ratio * 100) / 100.0
    return {
        "fg": fg, "bg": bg,
        "ratio": r2,
        "AA_normal_text_4.5": r2 >= 4.5,
        "AA_large_text_3": r2 >= 3.0,
        "AAA_normal_text_7": r2 >= 7.0,
        "AAA_large_text_4.5": r2 >= 4.5,
        "UI_graphics_3": r2 >= 3.0,
        "large_text_means": "at least 18 pt (24 px) regular or 14 pt (about 18.7 px) bold",
    }


def preset(name, dpi=300, bleed_mm=3.0):
    key = name.lower()
    if key not in PRESETS:
        raise ValueError("unknown preset %r; run 'presets' to list them" % name)
    p = PRESETS[key]
    if p["kind"] == "px":
        return {"preset": key, "kind": "screen", "px": [p["w"], p["h"]], "note": p["note"],
                "export": "sRGB, PNG for text/graphics, JPG quality 80-90 for photos"}
    out = print_to_px(p["w"], p["h"], "mm", dpi, bleed_mm)
    out.update({"preset": key, "kind": "print", "note": p["note"],
                "export": "CMYK only if the print shop asks; PDF/X with bleed; ask for their profile"})
    return out


def show(data, as_json):
    if as_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
        return
    if isinstance(data, list):
        for row in data:
            print(row)
        return
    for k, v in data.items():
        if isinstance(v, list):
            v = " x ".join(str(x) for x in v)
        print("%-22s %s" % (k, v))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Print/screen size, DPI, bleed and WCAG contrast calculator.")
    ap.add_argument("--json", action="store_true", help="JSON output")
    # Shared parent so --json also works after the command ("px 90 50 --json").
    # SUPPRESS keeps a subcommand from resetting a --json given before the command.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--json", action="store_true", default=argparse.SUPPRESS, help="JSON output")
    sub = ap.add_subparsers(dest="cmd")

    a = sub.add_parser("px", parents=[common], help="print size -> pixels")
    a.add_argument("w", type=float)
    a.add_argument("h", type=float)
    a.add_argument("--unit", default="mm", choices=["mm", "cm", "in"])
    a.add_argument("--dpi", type=float, default=300)
    a.add_argument("--bleed", type=float, default=0.0, help="bleed per side, in mm")

    b = sub.add_parser("size", parents=[common], help="pixels -> print size")
    b.add_argument("w", type=int)
    b.add_argument("h", type=int)
    b.add_argument("--dpi", type=float, default=300)

    c = sub.add_parser("preset", parents=[common], help="one named size")
    c.add_argument("name")
    c.add_argument("--dpi", type=float, default=300)
    c.add_argument("--bleed", type=float, default=3.0, help="bleed per side in mm (print presets)")

    sub.add_parser("presets", parents=[common], help="list named sizes")

    d = sub.add_parser("contrast", parents=[common], help="WCAG contrast of two hex colours")
    d.add_argument("fg")
    d.add_argument("bg")

    args = ap.parse_args(argv)
    try:
        if args.cmd == "px":
            data = print_to_px(args.w, args.h, args.unit, args.dpi, args.bleed)
        elif args.cmd == "size":
            data = px_to_print(args.w, args.h, args.dpi)
        elif args.cmd == "preset":
            data = preset(args.name, args.dpi, args.bleed)
        elif args.cmd == "presets":
            data = ["%-12s %-6s %s x %s  %s" % (k, p["kind"], p["w"], p["h"], p["note"])
                    for k, p in PRESETS.items()]
        elif args.cmd == "contrast":
            data = contrast(args.fg, args.bg)
        else:
            ap.print_help()
            return 1
    except ValueError as e:
        print("error: %s" % e, file=sys.stderr)
        return 2
    show(data, args.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
