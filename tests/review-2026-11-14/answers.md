# Blind answers, review 2026-11-14 (cases 9-11, verbatim)

ZIP: v1.1.0 before the footer fix. Answer agent: one fresh subagent, ZIP files only, no code, no web search.

## Case 9

**Harada:** Crop tool (`C`) ▸ kətanın kənarını şəkildən kənara çəkin ▸ Contextual Task Bar-da **Generate**. Prompt boş qala bilər. Onda Photoshop fonu uyğun şəkildə özü tamamlayır.

**Nə lazımdır:** internet, Adobe ID ilə giriş, Photoshop 25.0+ və generativ kreditlər (generative credits).

**Kredit:**
- Photoshop tək proqram planı ayda **25 generativ kredit** verir (ABŞ plan səhifəsi, 2026-11). Kreditlər hər ay sıfırlanır və növbəti aya keçmir.
- Bir Expand əməliyyatının neçə kredit apardığını dəqiq təsdiqləyə bilmirəm. Partnyor modelləri (Gemini, FLUX) daha çox kredit aparır. **Generate-ə basmazdan əvvəl düymədə göstərilən rəqəmə baxın.**
- Menyu yolu versiyaya görə dəyişə bilər. Öz versiyanız üçün Adobe Help-ə (helpx.adobe.com) baxın.

**Yoxlama:** Generate düyməsi görünmürsə, ya versiyanız köhnədir, ya da oflaynsınız.

**Kreditsiz yol:** Crop ilə kətanı böyüdün ▸ boş sahəni seçin ▸ `Edit ▸ Content-Aware Fill`. Sadə fonlarda yaxşı işləyir.

Nəticə həmişə mükəmməl çıxmır. 2–3 variant yaradın və kənarları maska ilə təmizləyin.

Versiya faktları Adobe Help-dən götürülüb (2026-11 yoxlanılıb). Planınızın səhifəsindəki rəqəm əsasdır.

## Case 10

1. `File ▸ New` (`Ctrl+N` / `Cmd+N`): Width **96 mm**, Height **56 mm**, **300 ppi**. Bu ölçü 90×50 mm + hər tərəfdən 3 mm bleed deməkdir (bleed = kəsim xəttindən kənara çıxan əlavə fon). Nəticə 1134 × 661 px olur.
2. Fon və şəkilləri kənara qədər uzadın. Mətni və loqonu kəsim xəttindən ən azı 3 mm (daha yaxşısı 5 mm) içəridə saxlayın.
3. Faylı `File ▸ Save As ▸ Photoshop PDF` kimi yadda saxlayın. CMYK-ni yalnız mətbəə istəsə və onun profili ilə edin.

Mətbəənin qaydaları əsasdır: başlamazdan əvvəl onlardan ölçünü, bleed-i və fayl formatını soruşun.

Detallar?

## Case 11

**Contrast: #888888 on white ≈ 3.54:1**
(L of #888888 ≈ 0.246 → (1 + 0.05) ÷ (0.246 + 0.05) ≈ 3.54)
- **Large text** (≥ 24 px regular or ≥ ~18.7 px bold) needs 3:1, so it passes. A big headline is OK.
- **Normal text** needs 4.5:1, so it fails. Don't use this grey for body text, dates or contact details.
- A safer option is a darker grey: #767676 gives 4.54:1, and near-black (#1A1A1A–#333333) makes the headline stand out more as the focal point.

**A5 poster + 3 mm bleed at 300 ppi**
- Size with bleed: 148 × 210 mm + 2 × 3 mm = **154 × 216 mm**
- Pixels: 154 ÷ 25.4 × 300 = **1819 px**; 216 ÷ 25.4 × 300 = **2551 px** → **1819 × 2551 px**
- Keep text at least 3 mm inside the cut line. The print shop's rules win, so ask them about bleed, colour profile and file format before you start.

Want the full print checklist for sending it to the shop?
