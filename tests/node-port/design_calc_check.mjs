// Node port of the math in scripts/design_calc.py, used to verify the logic
// on a PC without Python. Same formulas, same rounding. Run: node design_calc_check.mjs
// Expected values come from independent sources (ISO A4 at 300 ppi = 2480 x 3508,
// WebAIM: #777777 on white = 4.47-4.48:1, #767676 on white = 4.54:1, black/white = 21:1).

const MM_PER_INCH = 25.4;
const toMm = (v, u) => (u === 'mm' ? v : u === 'cm' ? v * 10 : u === 'in' ? v * MM_PER_INCH : NaN);
const mmToPx = (mm, dpi) => Math.floor(mm / MM_PER_INCH * dpi + 0.5); // int(x + 0.5) for x >= 0
const round = (x, n) => Math.round(x * 10 ** n) / 10 ** n; // close enough to Python round for the checks below

function printToPx(w, h, unit = 'mm', dpi = 300, bleed = 0) {
  const wmm = toMm(w, unit), hmm = toMm(h, unit);
  const out = { trim_px: [mmToPx(wmm, dpi), mmToPx(hmm, dpi)] };
  if (bleed) out.with_bleed_px = [mmToPx(wmm + 2 * bleed, dpi), mmToPx(hmm + 2 * bleed, dpi)];
  return out;
}
function pxToPrint(w, h, dpi = 300) {
  return { size_mm: [round(w / dpi * MM_PER_INCH, 1), round(h / dpi * MM_PER_INCH, 1)], megapixels: round(w * h / 1e6, 2) };
}
function parseHex(c) {
  c = c.trim().replace(/^#/, '');
  if (c.length === 3) c = [...c].map(x => x + x).join('');
  if (!/^[0-9a-fA-F]{6}$/.test(c)) throw new Error('bad colour ' + c);
  return [0, 2, 4].map(i => parseInt(c.slice(i, i + 2), 16));
}
const ch = v => { const s = v / 255; return s <= 0.04045 ? s / 12.92 : ((s + 0.055) / 1.055) ** 2.4; };
const lum = ([r, g, b]) => 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b);
function contrast(fg, bg) {
  const a = lum(parseHex(fg)), b = lum(parseHex(bg));
  const ratio = (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
  const r2 = Math.floor(ratio * 100) / 100;
  return { ratio: r2, aaNormal: r2 >= 4.5, aaLarge: r2 >= 3 };
}

const checks = [];
const eq = (name, got, want) => checks.push([name, JSON.stringify(got) === JSON.stringify(want), got, want]);

eq('A4 300ppi trim', printToPx(210, 297).trim_px, [2480, 3508]);
eq('A4 300ppi +3mm bleed (216x303)', printToPx(210, 297, 'mm', 300, 3).with_bleed_px, [2551, 3579]);
eq('card 90x50 300ppi', printToPx(90, 50).trim_px, [1063, 591]);
eq('card 90x50 +3mm bleed (96x56)', printToPx(90, 50, 'mm', 300, 3).with_bleed_px, [1134, 661]);
eq('US card 3.5x2 in 300ppi', printToPx(3.5, 2, 'in').trim_px, [1050, 600]);
eq('US card +0.125in bleed (3.175mm)', printToPx(3.5, 2, 'in', 300, 3.175).with_bleed_px, [1125, 675]);
eq('A5 300ppi', printToPx(148, 210).trim_px, [1748, 2480]);
eq('rollup 85x200cm at 150ppi', printToPx(85, 200, 'cm', 150).trim_px, [5020, 11811]);
eq('3000x2000px at 300ppi -> mm', pxToPrint(3000, 2000).size_mm, [254, 169.3]);
eq('1080x1350 megapixels', pxToPrint(1080, 1350).megapixels, 1.46);
eq('black on white', contrast('#000', '#fff').ratio, 21);
eq('#777777 on white (fails AA by a hair)', contrast('#777777', '#ffffff'), { ratio: 4.47, aaNormal: false, aaLarge: true });
eq('#767676 on white (passes AA)', contrast('#767676', '#ffffff'), { ratio: 4.54, aaNormal: true, aaLarge: true });
eq('order does not matter', contrast('#ffffff', '#767676').ratio, 4.54);
eq('white on #E30613 red', contrast('#ffffff', '#E30613').aaNormal, true);
eq('yellow #FFD400 on white', contrast('#FFD400', '#ffffff').aaLarge, false);

let fail = 0;
for (const [name, ok, got, want] of checks) {
  if (!ok) fail++;
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${name}  got=${JSON.stringify(got)}${ok ? '' : '  want=' + JSON.stringify(want)}`);
}
console.log(`\n${checks.length - fail}/${checks.length} passed`);
process.exit(fail ? 1 : 0);
