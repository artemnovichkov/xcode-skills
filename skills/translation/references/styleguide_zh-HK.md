# Traditional Chinese (Hong Kong) (zh-HK) — Software String Localization Style Guide

## Tone And Voice

- **Smart Yet Casual, Traditional Chinese First**: Write in a tone that is direct, friendly, and moderately formal without being stiff. Use Traditional Chinese as the default, though common English terms are acceptable in everyday speech. Capture the essence of the message rather than translating word-for-word. When context is ambiguous, check the string's comment, key IDs, other translations, and surrounding context before translating.
  - *Source:* "Smart Backup keeps your photos and documents safe in the cloud, so you never lose a thing." → *Target:* "「智能備份」會將你的相片和文件安全備份到雲端，讓你不會遺失任何重要資料。"

## Addressing Users

- **Use Informal 你 for All Software**: Address users as 你 in all software. The formal form 您 is not used for Hong Kong. This maintains a consistent, friendly tone across the product.
  - *Source:* "You can change your password in Settings > Account > Security." → *Target:* "你可以在「設定」>「帳戶」>「保安」中更改你的密碼。"

## Abbreviations

- **Translate an Abbreviation When a Common Local Equivalent Exists**: Everyday abbreviations such as e.g., i.e., info, and CC have standard Traditional Chinese equivalents, so translate them to their meaning. Keep an abbreviation in English only when it has no common local equivalent — most often a technical acronym such as SIM or CD-ROM.
  - *Source:* "e.g." → *Target:* "例如"
  - *Source:* "CC" → *Target:* "副本"
  - *Source:* "i.e." → *Target:* "即是"

## Acronyms

- **Retain English Acronyms When Meaning Is Apparent**: Keep technical acronyms in English when users would understand them (e.g., SIM, CD-ROM, RAM). Do not translate unless a common localized equivalent exists.
  - *Source:* "CD-ROM drive" → *Target:* "CD-ROM 光碟機"
  - *Source:* "SIM card" → *Target:* "SIM 卡"

## Date And Time

- **Follow Traditional Chinese (HK) Date and Time Conventions**: Follow the Traditional Chinese (HK) date and time conventions. Use 至 to connect the start and end of date ranges, following the CLDR value for Traditional Chinese (HK).
  - *Source:* "On %1$@, at %2$@, %3$@ wrote:" → *Target:* "%3$@於%1$@ %2$@寫道："
  - *Source:* "Aug 1 – Aug 5" → *Target:* "8月1日至8月5日"

## Measurements

- **Do Not Convert Measurements; Keep Digital Units in English Singular**: Do not convert imperial measurements to metric. Storage and data-rate units (bit, byte, kilobyte, KB, MB, GB, etc.) must remain in English in singular form when used as measurements. Translate them only when used descriptively, such as 16-bit color → 16 位元色彩.
  - *Source:* "1 MB = 1 million bytes" → *Target:* "1 MB = 1 百萬 byte"
  - *Source:* "The transfer rate is 400 kbits/sec." → *Target:* "傳輸速率為 400 kbit/秒。"
  - *Source:* "16 bit color" → *Target:* "16 位元色彩"
  - *Source:* "64 bit processor" → *Target:* "64 位元處理器"

## Addresses

- **Use Hong Kong Address Order**: Hong Kong addresses go from the largest unit to the smallest (Country → Province → City → Street → Building → Room), opposite to English order. Do not change phone numbers to local numbers unless instructed. Example format: 九龍油麻地彌敦道405號九龍政府合署13樓A室.

## Numerals

- **Use Arabic Numerals for Technical Specs**: Technical specifications, dates, currencies, and speed should use Arabic numerals. Do not localize Arabic numerals. Use a comma as the thousands separator when needed.
  - *Source:* "1,000,000 songs" → *Target:* "1,000,000首歌曲"

## Punctuation

- **Use Full-Width Punctuation with Corner Bracket Quotation Marks**: Use full-width punctuation marks (，。！？；：) throughout. No space is needed before or after full-width punctuation. Use corner brackets 「」 as quotation marks for app names, menu items, command names, path names, document and file names, and chapter titles. Use 《》 for song, album, and movie titles.
  - *Source:* "Find My Device enabled" → *Target:* "已啟用「尋找裝置」"
  - *Source:* "Cloud Photo Sync" → *Target:* "「雲端相片同步」"
  - *Source:* "Voice and Dictation" → *Target:* "「語音與聽寫」"
  - *Source:* "Now playing: %@" → *Target:* "正在播放《%@》" (%@ is a song title)

- **Remove or Add Quotes Around Variables Based on Content Type**: Remove corner brackets when a variable contains account names, dates, times, email addresses, URLs, person names, place names, or server names. Add or keep corner brackets when the variable represents a document or file name, folder path, mailbox name, mail subject, calendar title, event title, or an app name written in Chinese.
  - *Source:* "%@ started sharing location with you." → *Target:* "%@開始與你分享位置。"
  - *Source:* "Could not save to path %1$@. Choose a different path." → *Target:* "無法儲存至路徑「%1$@」。請選擇其他路徑。"
  - *Source:* "The %@ calendar does not support events." → *Target:* "「%@」日曆不支援行程。"

- **Ellipsis: Use the Midline Three-Dot Form**: Use the midline horizontal ellipsis ⋯ (省略號).
  - *Source:* "Loading..." → *Target:* "載入中⋯"

- **Use Fullwidth Tilde for Ranges**: Use the fullwidth tilde ～ (連接號) to indicate ranges between times or numbers (for date ranges, use 至 as described under Date And Time). No space is needed before or after the tilde.
  - *Source:* "1:45 PM to 2:45 PM" → *Target:* "下午1:45～下午2:45"
  - *Source:* "Week 1 to Week 2" → *Target:* "第1星期～第2星期"

- **Keep Special Math and Navigation Symbols Half-Width**: Plus +, minus -, asterisk *, and greater-than > signs must remain in half-width form. Use the half-width solidus / (not fullwidth ／) for slashes, with no spaces around it.
  - *Source:* "Settings > General > Storage" → *Target:* "「設定」>「一般」>「儲存空間」"

## Special Characters

- **Localize & and # Symbols When Used as Words**: When & represents 'and', translate it as 與. When # represents 'number', localize it with an appropriate ordinal construction. Keep these symbols unchanged when they are part of brand names or untranslated technical strings.
  - *Source:* "Voice & Data" → *Target:* "語音與數據"
  - *Source:* "#%1$@ of %2$@ players" → *Target:* "第%1$@位（共%2$@位玩家）"

## Trademarks And Product Names

- **Do Not Translate Trademarks and Product Names**: Keep trademarks, trademarked terms, and product names in the source language — do not translate or transliterate them unless the source does. Other company names likewise remain untranslated, or use their established Chinese name where one exists.

## Terminology

- **Use Singular Capitalized Form for Countable English Software Terms**: If a countable English software term appears in plural form, capitalize it and drop the -s. Use this form consistently. If a term exists only in plural form, always keep the plural. For product names, keep the singular or plural form as written in the source.
  - *Source:* "Accept cookies" → *Target:* "接受Cookie"

## Grammar

- **Add Measure Words After Number Placeholders**: When a variable represents a number, insert the appropriate Chinese measure word between the variable and the noun that follows it. Check the UI or string comment to confirm the correct measure word.
  - *Source:* "%@ Contacts" → *Target:* "%@位聯絡人"

- **Use Imperative Form with 請 for Instructions**: Translate directive sentences using 請 followed by the action. For negative directives, use 請勿 to maintain a polite, instructional tone.
  - *Source:* "Try again later." → *Target:* "請稍後再試。"
  - *Source:* "Do not unplug or reset this wireless router until it is available." → *Target:* "請勿拔下此無線路由器的電源或對其進行重設，直至它可以使用。"

## Variables

- **Preserve All Variables; Number Them When Reordered**: Keep every runtime variable (%@, %1$@, %s, ^1, etc.) exactly as in the source — except to add the `[tt]` technical-term flag described in the next rule. Never change a variable's format in any other way (e.g., %@ must not become %e). When reordering two or more variables, number all of them with positional markers.
  - *Source:* "%@ at %@ on %@" → *Target:* "%3$@%2$@%1$@"

- **Add `[tt]` to a `%@` Variable That Holds a Name or Technical Term**: `%[tt]@` asks the system to wrap the substituted value in corner brackets 「…」 at runtime, so a name or technical term is quoted correctly whether it arrives as Latin or Chinese text. Add `[tt]` to a `%@` only when BOTH hold: (a) the string is formatted with a modern localized API (`String(localized:)`, `localizedStringWithFormat`, `Text()`, or `LocalizedStringResource`) — never `String(format:)`, where a literal `%[tt]@` can appear in the UI; and (b) the value is a name, app name, or technical term (inferred from the source, the developer comment, the key, or the code). `[tt]` attaches only to `%@` object specifiers (never `%d`, `%f`, `%ld`), and takes the positional form `%2$[tt]@` when variables are reordered.
  - Do not add `[tt]` when the value is a number, date, duration, count, URL, email address, file path, or image/icon name.
  - Do not add `[tt]` when the value is already set off on both sides in the source — for example already inside 「」, quotation marks, or parentheses — because the runtime brackets would double up.
  - When in doubt, leave `%@` unchanged: a plain `%@` is always safe, whereas a wrong `%[tt]@` can ship a literal token.
  - *Source:* "Open %@" → *Target:* "開啟%[tt]@" (value is an app name — the runtime wraps it in 「」, e.g. 開啟「⋯」)
  - *Source:* "Please go to %@ and sign out" → *Target:* "請前往%[tt]@登出" (value is a settings section — the runtime wraps it in 「」, e.g. 請前往「帳戶設定」登出)
  - *Source:* "Delete \u201C%@\u201D?" → *Target:* "要刪除「%@」嗎？" (value already set off by 「」 — do not add `[tt]`)

## General Advice

- **Translate from the User's Perspective and Avoid Redundancy**: Remove redundant pronouns, particles, and overly literal constructions (e.g., 你, 的, 以便) that make text feel heavy. Choose words that reflect what the user is doing rather than the system's internal perspective.
  - *Source:* "This update is not available because you are not connected to the Internet." → *Target:* "由於尚未連接互聯網，因此無法下載此更新項目。"

- **Restate Subject Instead of Using Ambiguous Pronouns**: For clarity, repeat the noun rather than using a pronoun when the referent could be misread. This is especially important when the subject changes mid-sentence or when a relative clause could point to multiple antecedents.
  - *Source:* "The pass cannot be read because it isn't valid." → *Target:* "無法讀取票證，因為票證已失效。"
  - *Source:* "You followed a link that requires the app \u201C%@\u201D, which is no longer on your %@." → *Target:* "你跟隨了一個需要「%@」App的網址，不過你的%@已沒有此App。"

- **Use All Available Context to Disambiguate Meaning**: Use all the context available for a given string—the key ID, the developer comment, surrounding strings, and the code—to resolve ambiguous terms. For example, a key containing MUSIC_ALBUM means 'album' → 專輯 not 相簿, and a font or typography context means 'Weight' → 粗幼 (font weight), not 體重 (body weight).
  - *Source:* "Your album is now downloading." → *Target:* "正在下載你的專輯。"
  - *Source:* "Weight" → *Target:* "粗幼" (a font/typography context — the font-weight sense, not 體重)

## Diversity And Inclusion

- **Use Gender-Neutral Language and People-First Disability Terms**: Avoid binary gender representations; prefer 不同性別 over 兩性 or 男女, and use 家長 instead of 父母 where applicable. Use 其 as a possessive pronoun to avoid 他／她的. For disability, describe people before their condition and use terms like 輪椅使用者 rather than 受限於輪椅. Never use 正常人, 一般人, or 普通人 for non-disabled people; use 非身障人士 instead.
  - *Source:* "A wheelchair-bound person" → *Target:* "輪椅使用者"
  - *Source:* "He or she will need to approve the request." → *Target:* "其需要核准此請求。"
