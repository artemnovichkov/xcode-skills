# Vietnamese (vi) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Vietnamese uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "Go to \u201CSoftware Update\u201D" → *Target:* "Đi tới \u201CCập nhật phần mềm\u201D"

## Tone And Voice

- **Smart-Casual, Leaning Formal**: The tone for Vietnamese is best described as smart-casual — more formal than informal, but never stiff or overly rigid. Avoid trendy slang or hip vocabulary. Use Vietnamese as much as possible and keep a neutral, descriptive style that works for all audiences regardless of age.

## Addressing Users

- **Always Address the User As 'Bạn'**: Translate the English second-person pronoun 'you' consistently as 'bạn'. This word is appropriate across all levels of formality and all demographic groups, making it the safe default for every context.
  - *Source:* "You sent a photo." → *Target:* "Bạn đã gửi một ảnh."

## Abbreviations

- **Avoid Abbreviations**: If the source spells a word out in full, keep it spelled out in the translation rather than shortening it. If the source itself uses an abbreviation, an abbreviated form in the translation is acceptable; use at most two per phrase. Never abbreviate action words, nouns, or CTA buttons, menus, commands, options, and toolbar buttons (UIs that call/trigger actions).
  - *Source:* "%ld-month avg" → *Target:* "TB %ld tháng"

## Acronyms

- **Keep Acronyms in English Unless a Standard Equivalent Exists**: Do not translate acronyms unless a widely-used Vietnamese equivalent already exists. When an expansion is provided in brackets and is well known in Vietnamese, the expansion may be translated.
  - *Source:* "CD-ROM" → *Target:* "CD-ROM"

## Date And Time

- **Follow Vietnamese Date and Time Conventions**: Follow standard Vietnamese date and time conventions.
  - *Source:* "March 3, 2026 at 5:30 PM" → *Target:* "Ngày 3 tháng 3 năm 2026 lúc 17:30"

## Measurements

- **Do Not Convert Measurement Units**: Never convert imperial measurements to metric or to any other local standard. Never use " as an abbreviation for inch.
  - *Source:* "10 inches" → *Target:* "10 inch"

## Names And Addresses

- **Vietnamese Address Format**: Format addresses following Vietnamese conventions: number, street, ward, city/province, country. Urban alley addresses follow a nested number format (e.g. 205/10/16). As of July 2025, Vietnam reorganized its administrative units, removing the district level; follow the current two-tier structure, with the ward (phường) or commune (xã) directly under the city/province. Example format: Số 1 Tràng Tiền, Phường Cửa Nam, Hà Nội, Việt Nam.

## Numerals

- **Vietnamese Number Separators**: Vietnamese uses a period as the thousands separator and a comma as the decimal separator. Apply this convention to numbers, currency, and measurement values.
  - *Source:* "1,000,000 songs" → *Target:* "1.000.000 bài hát"
  - *Source:* "10.5 cm" → *Target:* "10,5 cm"

## Special Characters

- **Spaces Around Punctuation**: Insert a space after a full stop, comma, colon, semicolon, or ellipsis when more text follows; a trailing full stop at the end of a string takes no space. Do not insert a space between parentheses and the text inside them. Double spaces are not allowed in Vietnamese.
  - *Source:* "Restart the app (Settings > General), then try again." → *Target:* "Khởi động lại ứng dụng (Cài đặt > Cài đặt chung), sau đó thử lại."

- **Use En Dash Instead of Em Dash**: Em dashes are not used in Vietnamese. When the source uses an em dash to connect two phrases, replace it with an en dash surrounded by spaces on both sides.
  - *Source:* "Smart Replies—suggests responses before you even finish reading the message." → *Target:* "Trả lời thông minh – gợi ý câu trả lời trước cả khi bạn đọc xong tin nhắn."

## Trademarks And Product Names

- **Do Not Translate Trademarks and Product Names**: Keep trademarks, trademarked terms, and product names in the source language — do not translate or transliterate them unless the source does. Other company names likewise remain untranslated, or use their established Vietnamese name where one exists.

## Grammar

- **Capitalization of Multi-Syllable Vietnamese UI Terms**: When one English word maps to a multi-syllable Vietnamese phrase separated by spaces, capitalize only the first letter of the first syllable. If a UI element name appears within a sentence, capitalize its first letter. Do not capitalize every syllable.
  - *Source:* "Software Update" → *Target:* "Cập nhật phần mềm"
  - *Source:* "Go to Settings > General > Software Update" → *Target:* "Đi tới Cài đặt > Cài đặt chung > Cập nhật phần mềm"

- **Plural Articles — 'các' vs 'những'**: Vietnamese uses pre-noun articles to express plurality. Use 'các' for an indefinite plural (unspecified members of a group) and 'những' for a definite plural (a known, specific set). Choose based on whether the referent is determinate in context.
  - *Source:* "View Passes" → *Target:* "Xem các thẻ"
  - *Source:* "For things to be done before selling your devices…" → *Target:* "Để biết những bước cần thực hiện trước khi bán thiết bị của bạn…"

- **Tense Expressed via Time Adverbs**: Vietnamese does not inflect verbs for tense. Place the appropriate time adverb before the verb to indicate tense: đã for past, đang for present continuous, and sẽ for future. Context usually clarifies tense without these markers, so use them only when clarity requires it.
  - *Source:* "Mark as Read" → *Target:* "Đánh dấu là đã đọc"
  - *Source:* "Syncing your files…" → *Target:* "Đang đồng bộ hóa các tệp của bạn…"

- **Polite Imperatives with 'vui lòng' / 'hãy'**: When translating imperative sentences, insert 'vui lòng' or 'hãy' to convey politeness rather than a blunt command. Use 'vui lòng' for polite requests and 'hãy' for more direct but still courteous instructions. Always translate tooltips in the imperative form.
  - *Source:* "Please sign in again to continue." → *Target:* "Vui lòng đăng nhập lại để tiếp tục."
  - *Source:* "Enter a description." → *Target:* "Hãy nhập mô tả."

- **Full Stop Position with Parentheses**: When a full stop appears inside parentheses in the source, move it to outside the closing parenthesis in the Vietnamese translation.
  - *Source:* "(Check section 5.)" → *Target:* "(Kiểm tra phần 5)."

- **Compounds and Hyphens**: Hyphens are rarely used in Vietnamese compound words; prefer a space between elements. Hyphens may appear in certain transliterated loanwords (e.g. vi-rút, lô-gic) but even these are acceptable without a hyphen in many modern contexts.
  - *Source:* "Easy-to-use" → *Target:* "Dễ sử dụng"

## Terminology

- **Loan Words — Prefer the Most Accepted Localized Form**: When using loan words, always choose the most widely accepted localized form over a transliteration or the original foreign spelling. Reserve transliterations for forms already firmly established in Vietnamese (e.g. "sô cô la" for chocolate); don't coin new transliterations for common terms or proper names.
  - *Source:* "chocolate" → *Target:* "sô cô la" (not sô-cô-la, si cu la, or chocolate)
  - *Source:* "Alexander" → *Target:* "Alexander" (a personal name — kept as-is)

## Variables

- **Preserve Variables and Reorder When Needed**: Keep all variables exactly as they appear in the source. When Vietnamese grammar requires a different word order, number the variables using the n$@ notation (e.g. %1$@, %2$@). Never change a period to a comma inside a numeric format variable such as %.1f.
  - *Source:* "%@ %@" → *Target:* "%2$@ %1$@" (source is ordinal then day name; reordered to day name first)

## General Advice

- **Prioritize Vietnamese Terminology**: Use Vietnamese terminology first to make the language feel fully localized. English or other foreign terms are acceptable only when they provide a meaningful UI advantage, are widely recognized, or convey the meaning more clearly than any Vietnamese equivalent.

## Diversity And Inclusion

- **Avoid Offensive Slang and Culturally Harmful Terms**: Do not use internet or social-media slang that could be misunderstood or offensive to a general audience. Avoid derogatory terms for ethnic groups (e.g. thổ, mọi, tông dật) and disrespectful slang for LGBTQ+ identities. When in doubt, choose a neutral term or research the word's current connotations.
  - *Source:* "selfie" → *Target:* "ảnh tự chụp / ảnh selfie" (not "ảnh tự sướng", which carries a vulgar connotation)

- **Gender-Neutral Language**: Avoid binary gender representations where gender-neutral alternatives exist. Do not use gender-specific pronouns for people of unspecified gender; prefer neutral constructions or the plural form. Use people-first language when referring to disability.
  - *Source:* "The blind" → *Target:* "Người khiếm thị / Người bị mất thị lực / Người mù" (not "Người bị mù")

## Phone Number

- **Use Vietnamese Convention for Phone Numbers**: Use the Vietnamese convention when writing phone numbers. Landline numbers contain 11 digits; mobile numbers contain 10 digits (e.g. a landline written as (024) 1111 5555).

## Spacing

- **Space Between a Number and Its Unit**: Insert a space between a number and its unit of measurement. However, there must be no space between the number and a percentage (%) or degree (°) symbol.
  - *Source:* "2GB" → *Target:* "2 GB"
