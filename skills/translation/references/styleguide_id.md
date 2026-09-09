# Indonesian (id) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Indonesian uses curly double quotation marks “ (\u201C) and ” (\u201D), and the curly apostrophe ’ (\u2019).
  - *Source:* "Open \u201C%@\u201D." → *Target:* "Buka \u201C%@\u201D."

## Tone And Voice

- **Smart But Casual Tone**: Write in a formal register that emulates spoken Indonesian rather than written prose. Casual does not mean informal — standard EYD/PUEBI grammar and spelling always apply, but phrasing should sound like something a fluent speaker would naturally say aloud, not something they would write in a document. Smart means phrasing is idiomatic and culturally appropriate; avoid clunky or wordy constructions; avoid word redundancy.
  - *Source:* "What\u2019s new with Voice Control in visionOS 27" → *Target:* "Yang baru di Kontrol Suara visionOS 27"

- **Context-Specific Tone Variants**: Target tone must match the source — when the source is formal, the translation is formal; when the source is conversational, the translation follows suit and may use the informal second-person address kamu. Explicitly conversational strings such as smack-talk and encouragement may use colloquial verb forms like nge- + verb + -in to match the register of the source. In strings where ambiguity could lead to misinterpretation, a more verbose rendering is acceptable.
  - *Source:* "Nice moves! Keep it up — you're getting better every round." → *Target:* "Keren! Terus begitu — kamu makin jago tiap ronde." (informal kamu — casual, youth-oriented source)

## Addressing Users

- **Use 'Anda' as Standard Second-Person Pronoun**: Capitalize 'Anda' in all standard software strings per Pedoman Umum Ejaan Bahasa Indonesia. Use 'kamu' only when the source string's tone is distinctly casual or the developer's instructions call for an informal voice (e.g. a social or youth-oriented app). When switching to 'kamu', adjust related words for tonal consistency — for example, change 'dapat' to 'bisa'.
  - *Source:* "Your settings have been saved." → *Target:* "Pengaturan Anda telah disimpan."

## Abbreviations

- **Avoid Abbreviations in Software Strings**: Do not abbreviate words in software translations. Use a shorter alternative translation if needed.
  - *Source:* "Choose Notifications to Summarize" → *Target:* "Pilih Notifikasi"

## Acronyms

- **Retain Acronyms Without Translation**: Do not translate acronyms unless a widely recognized Indonesian equivalent already exists. Common technical acronyms such as CD-ROM and RAM are kept as-is.
  - *Source:* "ADSR" → *Target:* "ADSR"

## Grammar

- **Compounds and Hyphens with Loan Words**: Use hyphens to join Indonesian words with English loan words, for example 'antar-app'. The plural form 'undang-undang' in copyright notices is written with a hyphen even though Indonesian does not otherwise distinguish plural nouns. English compound words typically expand into a phrase in Indonesian — do not carry over the hyphen. For example, In-App Purchase becomes Pembelian di App, not Pembelian di-App.
  - *Source:* "between apps" → *Target:* "antar-app"

- **Article Omission and Disambiguation**: Articles (the, a, an) are usually omitted in Indonesian. However, when omitting an article would obscure whether the source refers to a specific item or to things in general, translate 'a' as 'satu' to preserve the intended specificity.
  - *Source:* "John likes a photo." → *Target:* "John menyukai satu foto."

- **Conjunction Substitution**: When a direct translation of a source conjunction produces grammatically awkward Indonesian, replace it with a functionally equivalent alternative rather than forcing a literal rendering.
  - *Source:* "And, this update also improves stability." → *Target:* "Selain itu, pembaruan ini juga meningkatkan stabilitas."

- **Prepositions Must Not Be Embedded Into the Following Word**: Write prepositions as separate, free-standing words. A common error is fusing a preposition with the next word as though it were a prefix — this is grammatically incorrect and must be avoided.

- **Capitalization Follows Source; Multi-Word Translations Capitalize All Words**: Mirror the capitalization pattern of the source string in both software and help content. When a single source word translates to two or more Indonesian words, capitalize every word in the translation. Write 'internet' in all lowercase in sentence-case strings, but follow the source's casing pattern when it appears alone or in title-case or all-uppercase strings.
  - *Source:* "Resize" → *Target:* "Ubah Ukuran"

- **Plurals: Use 'Beberapa'/'Sejumlah' Only When Critical**: Indonesian does not inflect nouns for number. Only add 'beberapa' or 'sejumlah' when the plural count is critical to the message. Reduplicated forms such as 'anak-anak' are also acceptable when the plural meaning must be explicit.
  - *Source:* "children" → *Target:* "anak-anak"

## Date And Time

- **Indonesian Date and Time Format**: Use a dot (.) to separate hours, minutes, and seconds, and a comma for milliseconds (e.g. 00.00.00,00). Never place a comma between month and year in written dates.
  - *Source:* "1 January, 2018" → *Target:* "1 Januari 2018"

## Measurements

- **Measurement Handling and Imperial-to-Metric Swap**: Do not convert imperial measurements to metric. When a sentence already contains both a metric and an imperial value in parentheses, swap their positions so the metric value appears first and the imperial value moves inside the parentheses.
  - *Source:* "a workout of at least a mile (1.6K)" → *Target:* "berolahraga setidaknya sejauh 1,6 km (satu mil)"

## Numerals

- **Indonesian Numeral Separators**: Use a comma (,) as the decimal separator and a dot (.) as the thousand separator in accordance with the Indonesian convention.
  - *Source:* "1,000,000" → *Target:* "1.000.000"
  - *Source:* "3.14" → *Target:* "3,14"

## Punctuation

- **Oxford Comma for Multiple Successive Nouns**: Always use the Oxford (serial) comma when listing three or more successive nouns in a sentence.
  - *Source:* "Photos, Videos and Documents" → *Target:* "Foto, Video, dan Dokumen"

- **Em-Dash for Parenthetical Clarity**: Use an em-dash without surrounding spaces to isolate a parenthetical part of a sentence when the sentence already contains many commas and readability would suffer.
  - *Source:* "Your photos, videos, and files are backed up — along with your contacts, calendars, and app data — automatically every day." → *Target:* "Foto, video, dan file Anda—beserta kontak, kalender, dan data app—dicadangkan secara otomatis setiap hari."

- **Full Stop Placement After Closing Quote**: When a sentence ends with a word or phrase in quotation marks, place the full stop after the closing quotation mark, not before it.

## Interface Elements

- **UI Elements: Imperative for Buttons and Commands**: Translate button names, menu commands, and toolbar buttons using the imperative form. Examine the button's functionality to determine the correct form. For example, tambah implies increasing a quantity, while Tambahkan implies placing a specific object into a destination. Keyboard key names such as function, command, option, control, shift, return, delete, tab, and caps lock must not be localized.
  - *Source:* "Cancel" → *Target:* "Batalkan"
  - *Source:* "Show Font" → *Target:* "Tampilkan Font"

- **Tooltips Use Imperative Form**: Translate tooltip strings using the imperative.

## Variables

- **Preserve Runtime Variables**: Never modify placeholders such as '%@' or '%.1f' — they are substituted at runtime and any alteration will break the substitution. Be especially mindful of differences between Indonesian and English syntax when repositioning variables within a sentence.
  - *Source:* "%1$@ liked %2$@'s photo" → *Target:* "%1$@ menyukai foto %2$@"

## General Advice

- **Distinguish Nouns From Verbs in Translation**: English and Indonesian differ significantly in word formation, making it easy to confuse a verb for a noun. Always identify the grammatical role of the source word before translating.
  - *Source:* "Download" (noun) → *Target:* "Pengunduhan"
  - *Source:* "Download" (verb) → *Target:* "Unduh"

## Diversity And Inclusion

- **Gender-Neutral Language and Disability Terminology**: Avoid gendered suffixes -wan/-wati where a neutral equivalent exists: use 'pekerja' instead of 'karyawan' and 'murid' instead of 'siswa'. For disability terms, use people-first language in most cases, but research community preferences — for example, the Indonesian Deaf community prefers 'Tuli' (capitalized) over 'tunarungu'. Avoid colloquial expressions that are only familiar to certain regional dialects.
  - *Source:* "students" → *Target:* "murid" (not "siswa")
  - *Source:* "workers" → *Target:* "pekerja" (not "karyawan")
