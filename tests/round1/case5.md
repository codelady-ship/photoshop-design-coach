**Generative Fill greyed out (Photoshop 2025, Mac)**

Most likely: no active selection.
Check: do you see marching ants (the moving dashed outline)?
Fix: make a selection with Lasso (`L`) or Rectangular Marquee (`M`), then use Contextual Task Bar ▸ Generative Fill or `Edit ▸ Generative Fill`. Select a bit more than the area.

If not → unsupported file or layer.
Check: `Image ▸ Mode`. It must be RGB Color and 8 Bits/Channel. Also check that the active layer is a normal pixel layer. Text, shape, smart object, clipped, grayscale and 32-bit layers or files can block it.
Fix: set `Image ▸ Mode ▸ RGB Color` and `8 Bits/Channel`, rasterise the layer or pick a pixel layer, and unclip it. Files over 40 MB or bigger than 8000 x 8000 px are rejected.

If not → account or connection.
Check: are you signed in (Help ▸ Sign in)? Are you online? Do you have generative credits left? The single-app Photoshop plan has 25 per month, and they don't roll over. The Adobe ID also needs a valid birth date (18+). Education and Enterprise accounts can have it turned off by an admin, and it is not available in some regions, such as China.
Fix: sign in, connect, fix the birth date on your Adobe account page, or wait for the monthly credit reset. Also run Help ▸ Updates.

Not sure your version has it? Look under Edit. If there is no Generative Fill, your version is older (it needs Photoshop 25.0+) or you are offline.

No AI needed? Use Edit ▸ Content-Aware Fill, Spot Healing Brush (`J`) or Clone Stamp (`S`).
Free: Photopea has Spot Healing and Clone Stamp, and GIMP has Heal (`H`) and Clone (`C`).

**Can you use the result in a client's ad?**

Often yes, with care. Not legal advice.
- Adobe says output from its Firefly models is generally OK for commercial use. Beta features may be personal use only, so don't use beta features for client work.
- Partner models (for example Gemini or FLUX) inside Generative Fill are your responsibility to check. They also cost more credits, so check the number shown before you click.
- Adobe's own Generative Fill page words commercial use in a mixed way. Read Adobe's current terms for the exact feature you use.
- Purely AI-made images may have no copyright protection (US Copyright Office, Jan 2025). Your own edits and arrangement can be protected. Tell your client this.
- Don't prompt for other brands' logos, real people without their consent, or "in the style of" a living artist.
- AI output may need clean-up, so zoom to 100% and fix edges with a mask.

Next step: tell me what the Mode check says (`Image ▸ Mode`) and whether you see marching ants, and I'll narrow it down.

Version facts from Adobe Help (checked 2026-11); your client's rules win.
