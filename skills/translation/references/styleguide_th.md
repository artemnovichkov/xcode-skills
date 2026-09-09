# Thai (th) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Thai uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "\u201C%1$@\u201D is sharing %2$ld contact cards." → *Target:* "\u201C%1$@\u201D กำลังแชร์บัตรรายชื่อ %2$ld ใบ"

## Tone And Voice

- **Break Away from the Source Sentence Structure — Translate Meaning, Not Form**: Thai translations must not mirror the source word order or sentence structure literally. Restructure the sentence so it sounds natural to a Thai speaker, changing word order and rephrasing as needed. The translation succeeds when it reads like Thai written by a native speaker, not like a rendered translation.
  - *Source:* "Enter the approval code provided by your recovery contact." → *Target:* "ป้อนรหัสการอนุญาตที่ผู้ติดต่อการกู้คืนของคุณให้มา"
  - *Source:* "Pair with this device to use it again." → *Target:* "จับคู่กับอุปกรณ์นี้อีกครั้งเมื่อต้องการใช้งาน"

## Addressing Users

- **Use Gender-Neutral Pronouns — คุณ, ฉัน, เรา; do not use ท่าน or พวกเรา**: Address the user as คุณ (you) and use ฉัน for the first-person singular and เรา for the first-person plural. Do not use the formal ท่าน and do not use พวกเรา for "we". These pronouns (คุณ, ฉัน, เรา) carry no gender, which keeps the translation gender-neutral.
  - *Source:* "I / You / We" → *Target:* "ฉัน / คุณ / เรา"

## Abbreviations

- **Keep US English Abbreviations and Their Expansions in English; Translate Only the Surrounding Context**: Do not translate or transliterate US English abbreviations. When the source provides a full expansion in parentheses after the abbreviation, keep both in English. Only the descriptive context surrounding them is translated into Thai.
  - *Source:* "USB (Universal Serial Bus)" → *Target:* "USB (Universal Serial Bus)"

## Acronyms

- **Keep Acronyms in English; Add Thai Classifier Prefixes for Physical Media**: Acronyms such as RAM do not require translation. For physical media acronyms like CD and DVD, prefix with the appropriate Thai noun (แผ่น for a disc, เครื่องเล่น for a player) to produce natural Thai phrasing.
  - *Source:* "CD" → *Target:* "แผ่น CD"
  - *Source:* "DVD player" → *Target:* "เครื่องเล่น DVD"
  - *Source:* "RAM" → *Target:* "RAM"

## Grammar

- **Add a Thai Verb in Front of Every Transliterated English Verb**: When a transliterated English verb is used in Thai, it cannot function as a verb on its own. Prefix it with an appropriate Thai action verb to make the phrase grammatically complete.
  - *Source:* "partition" (verb) → *Target:* "แบ่งพาร์ติชั่น"
  - *Source:* "email" (verb) → *Target:* "ส่งอีเมล"
  - *Source:* "filter" (verb) → *Target:* "ใส่ฟิลเตอร์"

- **Omit the Pronoun "it" — Replace Only When Needed to Prevent Ambiguity**: Never use มัน (it) for a person — it is impolite and offensive. For a non-human referent, drop "it" from the Thai translation entirely. Restate the referent only when dropping "it" would make the sentence ambiguous — in that case name the noun it refers to rather than using มัน.
  - *Source:* "It's %@ O'clock." → *Target:* "เวลา %@ นาฬิกา" (dummy "it" — dropped entirely)
  - *Source:* "Do you want to replace it with the one you are moving?" → *Target:* "คุณต้องการแทนที่เพลย์ลิสต์นั้นด้วยเพลย์ลิสต์ที่คุณกำลังย้ายหรือไม่" (real referent — "it" restated as the noun เพลย์ลิสต์นั้น, not มัน)

- **Reduce Possessive Pronouns — Keep Only Where Omission Causes Ambiguity**: English uses possessive pronouns far more frequently than Thai does. Omit ของคุณ (your) and similar possessives when the owner is obvious from context. In a short string with multiple occurrences, keep enough to prevent ambiguity — typically one instance toward the end of the sentence.
  - *Source:* "Add songs by dragging them from your Library to your iPod." → *Target:* "เพิ่มเพลงโดยลากจากคลังไปยัง iPod ของคุณ"

- **Avoid Translating "their" When Omission Does Not Cause Ambiguity**: The possessive pronoun "their" (ของพวกเขา / ของเขา) is often redundant in Thai and should be omitted when the owner is clear from context. Retaining it unnecessarily makes Thai sound unnatural.
  - *Source:* "Have your Family Member put on their Apple Watch and hold it up to the Camera." → *Target:* "ให้สมาชิกครอบครัวของคุณสวม Apple Watch แล้วยกขึ้นมาที่หน้ากล้อง"

- **Thai Nouns Are Not Inflected for Number**: Thai has no plural form. A plural English noun ("books", "songs") becomes the bare Thai noun; plurality is conveyed by a classifier or by context, never by a plural marker on the noun.

- **Use Classifier Nouns for All Counting Constructions**: Every countable noun in Thai is counted using a specific classifier noun placed after the numeral. The format is (countable noun) [numeral] [classifier]. When the noun and its classifier are the same word, the noun may be omitted without loss of meaning.
  - *Source:* "Moving %@ books…" → *Target:* "กำลังย้ายหนังสือ %@ เล่ม…"
  - *Source:* "\u201C%1$@\u201D is sharing %2$ld Calendar Events." → *Target:* "\u201C%1$@\u201D กำลังแชร์กิจกรรมปฏิทิน %2$ld กิจกรรม"
  - *Source:* "Undo Check %S Songs" → *Target:* "เลิกเลือก %S เพลง"

- **Use "on" (บน) for Cloud Services and Devices; Use "in" (ใน) for Local Device Storage**: When data is associated with a cloud service, or displayed on a device screen, use บน (on). When data is physically stored inside a device or local file system, use ใน (in). This distinction reflects how Thai speakers conceptualize where data lives and directly affects which preposition sounds natural.
  - *Source:* "Enter your password to continue using iCloud on this Mac." → *Target:* "ป้อนรหัสผ่านของคุณเพื่อใช้ iCloud บน Mac เครื่องนี้ต่อไป" (iCloud is a cloud service → บน)
  - *Source:* "Do you want to keep the music that's on your iPad?" → *Target:* "คุณต้องการเก็บเพลงที่อยู่ใน iPad ของคุณหรือไม่" (the music is stored inside the device → ใน)

## Terminology

- **Translate "all" as ทุก (every) When It Means "Every Device/Item"; ทั้งหมด Otherwise**: When "all" means "every device" or "every item" (as in "across all your devices"), translate it as ทุก + classifier (e.g. ทุกเครื่อง, อุปกรณ์ทุกเครื่อง) to convey "every". For other senses of "all", use ทั้งหมด or the most appropriate term.
  - *Source:* "iCloud keeps them updated across all your devices." → *Target:* "iCloud อัปเดตล่าสุดอยู่เสมอบนอุปกรณ์ทุกเครื่องของคุณ" (every device → ทุก)
  - *Source:* "See all messages" → *Target:* "ดูข้อความทั้งหมด" (all of a set → ทั้งหมด)

- **Transliterate Loan Words; Use Established Thai Spellings for Common Ones**: Transliterate loan words into Thai using standard Thai transliteration conventions. Several high-frequency loan words have established Thai spellings that differ from strict phonetic transliteration — always use these established forms for consistency.
  - *Source:* "software" → *Target:* "ซอฟต์แวร์"
  - *Source:* "update" → *Target:* "อัปเดต"
  - *Source:* "internet" → *Target:* "อินเทอร์เน็ต"
  - *Source:* "Bluetooth" → *Target:* "บลูทูธ"
  - *Source:* "download" → *Target:* "ดาวน์โหลด"
  - *Source:* "application / app" → *Target:* "แอปพลิเคชัน / แอป"

## Punctuation

- **Thai Has No Terminal Full Stop — End Sentences Without a Period**: Thai does not use a period to end a sentence. Simply allow the sentence to end naturally or follow it with a space. Do not add a full stop at the end of Thai sentences when one appears in the source.
  - *Source:* "The requested operation could not be completed." → *Target:* "ไม่สามารถดำเนินการตามที่ร้องขอได้"

- **Remove Question Marks — Use Thai Interrogative Phrases Instead**: Thai does not use question marks. Remove them and replace with the appropriate interrogative phrase at the end of the sentence, such as หรือไม่, ใช่หรือไม่, or อย่างไร, choosing the form that matches the source's tone.
  - *Source:* "Do you want to keep a copy of your iCloud contacts on this Mac?" → *Target:* "คุณต้องการเก็บสำเนารายชื่อของ iCloud ใน Mac เครื่องนี้หรือไม่"

- **No Commas Between Thai Phrases — Use a Space Instead**: Thai uses spaces, not commas, to separate phrases and list items composed of Thai words. Commas are only acceptable between English words in a list, in a mixed English-Thai list, or to prevent ambiguity where adjacent English or untranslated proper names would otherwise run together.
  - *Source:* "Disconnect all external devices except keyboard, mouse and Ethernet adapter." → *Target:* "ถอดอุปกรณ์ภายนอกทั้งหมดออกยกเว้นแป้นพิมพ์ เมาส์ และอะแดปเตอร์อีเธอร์เน็ต"

- **Use the Single Ellipsis Character (…) — Never Three Separate Dots**: Always insert a single Unicode ellipsis character (… U+2026) rather than three consecutive periods. Accessibility software pronounces these differently, and the character spacing also differs.
  - *Source:* "Downloading..." → *Target:* "กำลังดาวน์โหลด…"

## Date And Time

- **Date Format — Day Before Month; Add วันที่ and เวลา as Prefixes**: Thai always places the day before the month (DD/MM/YY). When writing a full date, prefix it with วันที่ for the date and insert เวลา between the date and time components. These prefixes may be omitted only when space is critically limited. When the source string contains a hard-coded Gregorian year (e.g. "2013"), convert it to the Buddhist Era — the Gregorian year plus 543 (2013 → 2556), as the examples show — since the Buddhist Era is standard in Thailand. Do not convert a year that arrives through a variable or date placeholder: the system formats those from the user's calendar setting. Keep the Gregorian year in software-update strings, where the Gregorian year is the standard convention.
  - *Source:* "September 11th, 2013" → *Target:* "วันที่ 11 กันยายน 2556"
  - *Source:* "9/11/13 8:30 am" → *Target:* "11/9/56 เวลา 8.30 น."

- **Use 24-Hour Format with น. Suffix**: Thai defaults to 24-hour time written as HH.mm น. or HH:mm:ss น. If a 12-hour time with a.m./p.m. is kept, leave a.m./p.m. in English — do not translate them as ก่อนเที่ยง/หลังเที่ยง, which are not used in everyday Thai.
  - *Source:* "4:29 pm" → *Target:* "16.29 น."

## Special Characters

- **No Space Before Thai Repetition Mark (MaiYaMok ๆ) in Software UI**: In software UI strings, do not insert a space before the Thai MaiYaMok character (ๆ, U+0E46). A space at this position would allow the text to break onto a new line at that character, producing an awkward layout. This is an intentional exception to the Royal Society spacing guidelines, which apply to other content types.
  - *Source:* "others" → *Target:* "อื่นๆ" (no space before ๆ — not "อื่น ๆ")

## Measurements

- **Do Not Convert Units — Follow the Source; Never Use " for Inch**: Do not convert imperial to metric or vice versa. For the inch mark use the double prime ″ (\u2033); never use a straight or curly double quotation mark. Thai uses the metric system in general.
  - *Source:* "Place iPad 10 to 20 inches from your face." → *Target:* "ให้ iPad ห่างจากใบหน้าของคุณ 10 ถึง 20 นิ้ว"

## Trademarks And Product Names

- **Keep Trademarks and Product Names in Their Original Form**: Do not translate or transliterate trademarks, product names, or brand names (the app's own or a third party's, such as YouTube or Facebook); keep them in their original form unless the source or a developer comment directs otherwise.

## Interface Elements

- **Do Not Add Spaces Around Software UI Element Names Embedded in Thai Text**: Thai already uses spaces to separate phrases rather than as word boundaries. Adding extra spaces around a translated UI element name fragments the surrounding sentence unnaturally. Embed the element name directly without surrounding spaces.
  - *Source:* "Configure displays in System Preferences." → *Target:* "กำหนดค่าจอภาพในการตั้งค่าระบบ" (no extra spaces around การตั้งค่าระบบ)

- **Wrap Multi-Word UI Element Names in Curly Double Quotes**: Thai has no capitalization to signal a UI element name the way English does. When a translated UI element name contains two or more words (i.e. includes internal spaces), wrap it in the curly double quotes from the escaping section above to mark it as a distinct interface element and prevent it from blending into surrounding text.
  - *Source:* "Use iCloud Settings on your iPhone to turn off Find My iPhone." → *Target:* "ใช้การตั้งค่า iCloud บน iPhone ของคุณเพื่อปิดใช้ \u201Cค้นหา iPhone ของฉัน\u201D"

- **Add แอป Before App Name Only When the App and Its Content Share the Same Translation**: Some Thai app names are identical to the items they contain (e.g. ข้อความ is both the Messages app and a message). When both appear in the same string and confusion is possible, prefix the app name with แอป. Do not substitute แอป with แอปพลิเคชัน or vice versa.
  - *Source:* "You have a new message in Messages." → *Target:* "คุณมีข้อความใหม่ในแอปข้อความ"

- **Use the Device Classifier Before Demonstratives for Hardware Devices**: When referring to a specific hardware device by name, add the appropriate Thai classifier before the demonstrative pronoun (นี้/นั้น/อื่น/ใหม่): use เครื่อง for most devices (e.g. Mac, iPhone, iPad, iPod, HomePod) and เรือน for a watch (e.g. Apple Watch). When the device type is unknown, omit the classifier.
  - *Source:* "this iPhone" → *Target:* "iPhone เครื่องนี้"
  - *Source:* "this Apple Watch" → *Target:* "Apple Watch เรือนนี้"

## Variables

- **Preserve Variables Exactly; Reorder with Positional Indices as Needed**: Never alter or omit variable format specifiers — except to add the `[tt]` technical-term flag. If Thai word order requires a different variable sequence, add positional indices (%1$@, %2$@, etc.) to every variable in the string. Do not change the period inside numeric format specifiers such as %.1f.
  - *Source:* "Meeting scheduled for %1$@ %2$@." → *Target:* "นัดหมายสำหรับ %2$@ %1$@"

- **Add `[tt]` (Technical Term) to a `%@` Variable That Holds a Name or Technical Term**: `[tt]` controls the spacing where a substituted value meets the Thai text next to it — at runtime it adds a space when the value is non-Thai (e.g. a Latin app name) and none when it is Thai. Add `[tt]` to a `%@` variable — `%@` → `%[tt]@`, or with a positional index `%2$@` → `%2$[tt]@` — when the variable sits directly against Thai characters on its left and/or right (the usual case, since Thai has no spaces between words). Add it only when both hold: (a) the code formats the string with a modern localized API (`String(localized:)`, `LocalizedStringResource`, `localizedStringWithFormat`, or `format:locale:`) — never `String(format:)` / `stringWithFormat`; and (b) the value is a human-readable name, title, or app/device/item name (confirm from the source, developer comment, string key, or code). If either is not clear, leave `%@` unchanged. `[tt]` attaches only to `%@` (object) specifiers, never to `%d`, `%f`, etc.
  - Do not add `[tt]` when the variable is set off from the Thai on both sides — wrapped in quotes or parentheses, or separated by a comma: `"%@"`, `(%@)`, `%@, %@, and others`. A trailing space plus a parenthetical such as ` (Bluetooth)` does not exclude it if the other side still sits against Thai (see the Bluetooth example).
  - Also do not add `[tt]` when the value is an image, glyph, icon, link, or URL, or a number.
  - Adding `[tt]` is the only change permitted to a specifier's contents; otherwise keep variables exactly as the source has them.
  - *Note:* with `String(format:)` / `stringWithFormat`, `[tt]` is not supported and a literal `%[tt]@` can appear in the UI at runtime; only add `[tt]` when the code uses a modern API, or update the code to a modern API if that change is trivial.
  - *Source:* "Send a message to %@" → *Target:* "ส่งข้อความถึง%[tt]@" (value sits against Thai on the left → add)
  - *Source:* "Search %@ or enter your address" → *Target:* "ค้นหา%[tt]@หรือป้อนที่อยู่ของคุณ" (against Thai on both sides → add)
  - *Source:* "Connect to %@ (Bluetooth)" → *Target:* "เชื่อมต่อกับ%[tt]@ (Bluetooth)" (against Thai on the left; the trailing " (Bluetooth)" is space-separated → still add)

## Diversity And Inclusion

- **Avoid Violent, Oppressive, or Ableist Terms**: Do not translate technology using inherently violent terms (like "kill" or "hang"), the oppressive pair "master"/"slave", or terms like "sanity check" that associate mental health with functionality. Avoid describing software or hardware with human attributes, which can carry unintended hurtful implications.

- **Use Gender-Neutral Language**: Thai has no grammatical gender, so translations are naturally gender-neutral; keep them that way — avoid introducing gendered assumptions, and where content is about or addressed to a real person, prefer referring to them by name.

- **Put People First When Translating About Disability**: Focus on what people can do, not on what they can't. In most cases use people-first phrasing that describes the individual before any disability.

- **Don't Use Color to Convey Positive or Negative Qualities**: Use colors only to describe actual colors. Avoid using color to connote security, secrecy, or a good/bad judgment (e.g. "white hat hacker", "black testing environment").
