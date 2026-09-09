# Traditional Chinese (zh-Hant) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual, Traditional Chinese First**: The tone should be direct, friendly, and closer to formal than informal, but never stiff or trendy. Use Traditional Chinese terminology as much as possible even when English equivalents are more common in everyday speech. Prioritize capturing the meaning naturally over literal word-for-word translation.

## Addressing Users

- **Use Informal 你 for All Software**: Use the informal 你 in all software. This keeps a consistent, friendly, and conversational tone.
  - *Source:* "You can sync photos and videos using the desktop app." → *Target:* "你可以透過桌面版App將照片和影片同步。"

## Abbreviations

- **Keep Abbreviations in English Unless a Common Local Equivalent Exists**: Do not translate abbreviations unless there is a well-known Traditional Chinese equivalent. When retaining an abbreviation, you may show the Chinese translation followed by the English abbreviation in parentheses for clarity.
  - *Source:* "Frequently Asked Questions (FAQ)" → *Target:* "常見問題（FAQ）"

## Acronyms

- **Retain Acronyms When Meaning Is Apparent to Users**: Do not translate acronyms (CD-ROM, RAM, SIM, HTTP, RTSP) unless a very common localized equivalent exists.
  - *Source:* "Components for managing HTTP and RTSP cookies" → *Target:* "用於管理HTTP與RTSP Cookie的元件"
  - *Source:* "SIM card" → *Target:* "SIM卡"

## Spacing

- **No Space Between Chinese and Latin**: Write a Chinese character and an adjacent Latin letter or number with no space between them. Keep spaces only where the format requires them, such as date/time and date/week.
  - *Source:* "Export the document as a PDF file" → *Target:* "將文件輸出為PDF檔案"

## Date And Time

- **Follow Traditional Chinese Date and Time Format**: Use the Traditional Chinese date and time format. Preserve spaces between date and time components where the format requires them.
  - *Source:* "Mon June 8 3:17PM" → *Target:* "6月8日週一 下午3:17"

- **Space between date and time or date and week**: Space should be kept for date/time, date/week, etc.
  - *Source:* "On %1$@, at %2$@, %3$@ wrote:\n\n" → *Target:* "%3$@於%1$@ %2$@寫道：\n\n"

## Measurements

- **Do Not Convert Measurements; Keep Digital Storage Units in English Singular**: Do not convert imperial to metric in software strings. Storage units (bit, byte, kilobyte, KB, MB, GB, TB, etc.) stay in English singular form when used as measurements. Use the standard abbreviations (KB/MB/GB/TB/PB/EB/ZB/YB) for larger units rather than spelling them out. When units are used descriptively (e.g., 16-bit color), translate them into Chinese.
  - *Source:* "Choose the size scale as kilobytes (KB), megabytes (MB), or gigabytes (GB)" → *Target:* "選擇以KB、MB或GB作為大小單位"
  - *Source:* "64 bit processor" → *Target:* "64位元處理器"

## Names And Addresses

- **Follow Taiwan Address Convention**: Addresses must follow the Taiwan (Chunghwa Post) convention: ZIP code on the first line, then County/City and District/Township, then street address. Both three-digit and five-digit zip codes are acceptable. Example format: 40867台中市南屯區向上路2段199號.

## Numerals

- **Follow Source for Numerals; Use Comma as Thousands Separator**: Follow the source when deciding between Arabic numerals and spelled-out numbers. Use a comma as the thousands separator. When the source spells out a number, translate it into Traditional Chinese.
  - *Source:* "two hundred books and 1,000,000 songs" → *Target:* "兩百本書和1,000,000首歌曲"

## Special Characters

- **Localize & and # When Used as Words**: When & represents 'and' in translated text, localize it as 與. When # represents 'number', localize with an appropriate ordinal construction. Keep & and # unchanged when they are part of untranslated brand names or technical strings.
  - *Source:* "Languages & Dialects" → *Target:* "語言與方言"
  - *Source:* "#%1$@ of %2$@ player" → *Target:* "第%1$@名（共%2$@位玩家）"

## Punctuation

- **Use Full-Width Punctuation with Corner Bracket Quotation Marks**: Use full-width punctuation marks (，。！？；：) throughout. Use corner brackets 「」 as quotation marks around technical terms, UI element names, user-generated content that may be in Chinese, file and folder names, and chapter titles. Do not add quotes around proper nouns on menu bars or window titles unless a variable is present.
  - *Source:* "Save changes to the \u201C%1$@\u201D %2$@ account?" → *Target:* "要將更動儲存至「%1$@」%2$@帳號嗎？"
  - *Source:* "Check the settings in Settings > Mail." → *Target:* "檢查「設定」>「郵件」裡的設定。"

- **Remove or Add Quotes Around Variables Based on Content Type**: Remove corner brackets when the variable contains account names, dates, times, email addresses, URLs, person names, place names, server names, or service names. Add or keep corner brackets when the variable represents a document name, folder path, mailbox name, mail subject, calendar title, event title, or an app name that may render in Chinese.
  - *Source:* "Could not save to path %1$@. Choose a different path." → *Target:* "無法儲存至路徑「%1$@」。請選擇其他路徑。"

- **Ellipsis: Use the Midline Three-Dot Form**: Use the midline horizontal ellipsis ⋯ (刪節號).
  - *Source:* "Downloading..." → *Target:* "下載中⋯"

- **En Dash with Spaces for Ranges; Avoid Dashes Where Possible**: For ranges between dates, times, or numbers, use an en dash with a space on each side, unless the source already uses a specific dash or hyphen, in which case match the source's type. Outside of ranges, avoid dashes; prefer commas or parentheses.
  - *Source:* "9:00 AM – 5:00 PM" → *Target:* "上午9:00 – 下午5:00"

- **Keep Special Math and Navigation Symbols Half-Width**: Plus +, minus -, asterisk *, and greater-than > signs must remain in half-width form.
  - *Source:* "Click the Add (+) button." → *Target:* "按一下「新增」（+）按鈕。"
  - *Source:* "Go to Settings > General" → *Target:* "前往「設定」>「一般」"
  - *Source:* "Fields marked with * are required." → *Target:* "標有*的欄位為必填。"

- **Keep Forward Slash Half-Width**: Solidus / (斜線) should be used instead of fullwidth solidus ／ or division slash ∕. No space is needed before or after the slash.

## Trademarks And Product Names

- **Do Not Translate Trademarks and Product Names**: Keep trademarks, trademarked terms, and product names in the source language — do not translate or transliterate them unless the source does. Other company names likewise remain untranslated, or use their established Chinese name where one exists.

## Terminology

- **Use Singular Capitalized Form for Countable English Software Terms**: When a countable English software term appears, capitalize it and use the singular form. If a term exists only in plural form, always keep the plural. For product names, keep the singular or plural form as written in the source.
  - *Source:* "Apps on your device" → *Target:* "裝置上的App"

## Grammar

- **Use 正在 for Progressive Actions; 中 When No Noun Follows**: Translate present-progressive actions as 正在⋯ when a noun follows the verb. When no noun follows (for example, in loading indicators), use the verb followed by 中⋯ instead.
  - *Source:* "Downloading…" → *Target:* "下載中⋯"
  - *Source:* "The app is updating your existing files" → *Target:* "App正在更新現有的檔案"

- **Standardized Sentence Starters for Common English Patterns**: Several English sentence patterns have standard Traditional Chinese translations. Use 若要⋯請⋯ for 'To…'
  - *Source:* "To connect to the device, click Connect." → *Target:* "若要連接裝置，請按一下「連線」。"
  - *Source:* "For more information, choose Help > User Guide." → *Target:* "如需更多資訊，請選擇「輔助說明」>「使用手冊」。"

- **Add Measure Words After Number Placeholders**: When a placeholder stands for a number, insert the appropriate Chinese measure word between the placeholder and the noun that follows it. Check the UI or string comment to confirm the correct measure word.
  - *Source:* "%d contacts" → *Target:* "%d位聯絡人"

## Variables

- **Preserve All Variables; Number Them When Reordered**: Keep every runtime variable (%@, %d, %1$@, ^1, $1, etc.) exactly as in the source — except to add the `[tt]` technical-term flag described in the next rule. Never change a variable's format in any other way. When reordering two or more variables, number all of them with positional markers.
  - *Source:* "%@ at %@ on %@" → *Target:* "%3$@%2$@%1$@"

- **Add `[tt]` to a `%@` Variable That Holds a Name or Technical Term**: `%[tt]@` asks the system to wrap the substituted value in corner brackets 「…」 at runtime, so a name or technical term is quoted correctly whether it arrives as Latin or Chinese text. Add `[tt]` to a `%@` only when BOTH hold: (a) the string is formatted with a modern localized API (`String(localized:)`, `localizedStringWithFormat`, `Text()`, or `LocalizedStringResource`) — never `String(format:)`, where a literal `%[tt]@` can appear in the UI; and (b) the value is a name, app name, or technical term (inferred from the source, the developer comment, the key, or the code). `[tt]` attaches only to `%@` object specifiers (never `%d`, `%f`, `%ld`), and takes the positional form `%2$[tt]@` when variables are reordered.
  - Do not add `[tt]` when the value is a number, date, duration, count, URL, email address, file path, or image/icon name.
  - Do not add `[tt]` when the value is already set off on both sides in the source — for example already inside 「」, quotation marks, or parentheses — because the runtime brackets would double up.
  - When in doubt, leave `%@` unchanged: a plain `%@` is always safe, whereas a wrong `%[tt]@` can ship a literal token.
  - *Source:* "Open %@" → *Target:* "開啟%[tt]@" (value is an app name — the runtime wraps it in 「」, e.g. 開啟「⋯」)
  - *Source:* "Please go to %@ and sign out" → *Target:* "請前往%[tt]@登出" (value is a settings section — the runtime wraps it in 「」, e.g. 請前往「帳戶設定」登出)
  - *Source:* "Delete \u201C%@\u201D?" → *Target:* "要刪除「%@」嗎？" (value already set off by 「」 — do not add `[tt]`)

## General Advice

- **Translate from the User's Perspective; Remove Redundant Words**: Remove redundant pronouns and particles (的, 你, 以便) that make translations feel heavy. Restate the subject explicitly rather than using ambiguous pronouns when clarity is needed. Choose words that reflect the user's action, not the system's internal state.
  - *Source:* "You can change your password at any time in your account settings." → *Target:* "隨時可在帳戶設定中更改密碼。"

## Diversity And Inclusion

- **Use Gender-Neutral Terms; People-First Language for Disability**: Avoid binary gender representations; prefer neutral profession titles (警察 not 女警, 護理師 not 男護士, 空服員 not 空姐). When translating the epicene 'they', omit the pronoun, repeat the noun, or use demonstrative pronouns 其, 此, 該. For disability, use people-first terms (身心障礙者, 視覺障礙人士) and never use 正常人, 一般人, or 普通人 for non-disabled people.
  - *Source:* "The blind" → *Target:* "視覺障礙人士"

- **Handle Black/White/Master/Slave Terminology Responsibly**: Choose Traditional Chinese wording a local audience would not find offensive, and don't frame software or hardware as an oppressive human relationship such as 主／奴 (master/slave). Render inclusive source terms with their standard equivalents (block list → 封鎖清單, allow list → 允許清單).
  - *Source:* "blacklist and whitelist" → *Target:* "封鎖清單和允許清單"
