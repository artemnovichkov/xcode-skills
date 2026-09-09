# Turkish (tr) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Turkish uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019) — including when attaching a suffix to an acronym or loan word.
  - *Source:* "to the podcast" → *Target:* "podcast\u2019i"

## Tone And Voice

- **Smart but Casual Tone**: Write in a neutral, descriptive style that is closer to formal than informal, but never stiff or overly hip. Use short and concise language; there is no need to repeat every source word. The translation succeeds when the reader does not feel they are reading a translation.
  - *Source:* "Choose the XX option." → *Target:* "XX seçeneğini seçin."

## Addressing Users

- **Second-Person Plural Imperative — Avoid Over-Formal Suffixes**: Address users with second-person plural forms such as "açın" and "sürükleyin". Never use the over-formal "-iniz/-ınız" suffix forms like "açınız" or "kapatınız". In buttons use the plain imperative (e.g. "Aç", "Kapat"). For App Intents or App Shortcuts phrases, use second-person singular.
  - *Source:* "Open the file." → *Target:* "Dosyayı açın."
  - *Source:* "Close the window." → *Target:* "Pencereyi kapatın." (not the over-formal "kapatınız")

## Abbreviations

- **Avoid Abbreviations; Handle Ambiguous Ones Carefully**: Do not use abbreviations in software strings unless absolutely necessary. When abbreviations are unavoidable, follow standard Turkish abbreviation rules — most end with a period (dk., sa.) except SI units (km, m, kg). Be especially careful when the same abbreviation represents different English source terms.
  - *Source:* "approx." → *Target:* "yaklaşık" (spell out — avoid the abbreviation)
  - *Source:* "Min" → *Target:* "dk." (minutes — only when an abbreviation is unavoidable)
  - *Source:* "Min" → *Target:* "Min." (minimum — disambiguate identical abbreviations)

## Acronyms

- **Add Turkish Pronunciation-Based Suffixes to Acronyms**: Do not translate acronyms unless a very common localized equivalent exists. Attach Turkish suffixes based on how the acronym is pronounced in Turkish, not how it is spelled in English.
  - *Source:* "HDR" → *Target:* "HDR\u2019ye"
  - *Source:* "URL" → *Target:* "URL\u2019ye"

## Date And Time

- **Turkish Date and Time Format**: The standard Turkish short date format is DD.MM.YYYY (e.g. 05.01.2014) and the long form is "5 Ocak 2014 Pazar". The default time format is the 24-hour clock (e.g. 13:08). Do not transliterate format placeholders like MM/DD/YY into AA/GG/YY; instead apply the correct functional format for the locale.
  - *Source:* "05/01/2014" → *Target:* "05.01.2014"
  - *Source:* "1:08 PM" → *Target:* "13:08" (24-hour clock)

## Measurements

- **Measurements — No Conversion; Specific Spacing Rules**: Do not convert imperial to metric units. Place a non-breaking space between a number and its unit symbol (e.g. 3 cm, 25 ºC), but write the percent sign before the number with no space (e.g. %30). Time abbreviations dk. and sa. take a period; SI units (cm, m, kg) do not.
  - *Source:* "2 GB" → *Target:* "2 GB"
  - *Source:* "6 ft" → *Target:* "6 ft" (keep imperial units; do not convert to metric)

## Names And Addresses

- **Turkish Address Format**: Format addresses with street name and number first, then postal code, district, and city. Turkish postal codes are five digits.
- **Sample Email and Web Addresses**: When an email or web address uses the example.com domain (the conventional placeholder), adapt only the name before the @ to something informative for Turkish users, avoiding Turkish-specific characters (ç, ğ, ş); keep example.com itself unchanged. Leave all other email and web addresses exactly as written. Example: kullanici@example.com.

## Numerals

- **Turkish Number Formatting — Comma Decimal, Period Thousands**: Use a comma as the decimal separator and a period as the thousands separator for numbers with five or more digits (e.g. 25.000 parça). Four-digit numbers need no separator (e.g. 1800 dosya). Never drop the leading zero before a decimal point — ".5" in the source becomes "0,5" in Turkish.
  - *Source:* "25,000 pieces" → *Target:* "25.000 parça"
  - *Source:* ".5 m" → *Target:* "0,5 m"

## Special Characters

- **Replace Ampersand with "ve"; Use Circumflex to Distinguish Words**: Never use the "&" character in regular text; write "ve" instead. Some Turkish words require a circumflex vowel to distinguish meanings — for example, "hâlâ" (still) vs. "hala" (aunt) and "resmî" (official) vs. "resmi" (his/her picture). Use the precomposed (NFC) circumflex letters â (\u00E2), î (\u00EE), û (\u00FB) — not a base vowel followed by a combining circumflex, and never the caret ^ (\u005E), which is an unrelated ASCII character.
  - *Source:* "Settings & Privacy" → *Target:* "Ayarlar ve Gizlilik"
  - *Source:* "still" → *Target:* "hâlâ"

## Punctuation

- **Do Not Mirror English Comma Usage in Turkish**: English and Turkish comma rules differ significantly — do not carry English commas over into Turkish. In particular, avoid the Oxford comma (no comma before "ve" or "veya"); see the specific no-comma cases below.

- **No Comma After 'için'**: Do not place a comma after 'için' (for/to). Following the source comma here is one of the most common Turkish punctuation errors.
  - *Source:* "To reset your password, go to example.com." → *Target:* "Parolanızı sıfırlamak için example.com adresine gidin."

- **No Comma After Conditional Mood (-se/-sa)**: Do not place a comma after a conditional clause ending in -se or -sa. English uses a comma after 'if' clauses; Turkish does not.
  - *Source:* "If you need assistance, contact your card issuer." → *Target:* "Yardıma ihtiyacınız varsa kartı veren kuruluşa danışın."

- **No Comma After Single Verbal Adverb (Zarf-fiil)**: Do not place a comma after a single verbal adverb (zarf-fiil) mid-sentence. A comma may be used only when multiple verbal adverbs appear in sequence.
  - *Source:* "The distortion increases with the distance from the center." → *Target:* "Dairenin merkezine olan mesafe arttıkça görüntünün bozulması da artar."

- **Quotation Marks and Full Stop Placement**: Turkish uses curly apostrophes and curly quotation marks. Place the full stop after the closing quotation mark or closing parenthesis, not before it. Use double quotation marks as the default; single quotation marks are only used for a quote within a double-quoted sentence. Do not convert straight quotes in code samples.
  - *Source:* "Select \u201CStart automatically.\u201D" → *Target:* "\u201COtomatik olarak başlat\u201Dı seçin."

## Grammar

- **Plural vs. Singular with Determiners and Numbers**: Use the plural form when the source contains determiners like "all", "other", or phrases like "and more". Use the singular form when items are listed as examples (introduced by "such as") or when a number precedes the noun, since Turkish does not pluralize nouns after numerals.
  - *Source:* "Looking for other iPads, iPhones…" → *Target:* "Diğer iPad\u2019ler, iPhone\u2019lar aranıyor…"
  - *Source:* "Profiles contain settings, such as names and passwords." → *Target:* "Profiller, ad ve parola gibi ayarları içerir." (singular after 'such as')

- **Distinguish Noun vs. Verb Forms in Context**: Many English terms can be either a noun or a verb (View, Edit, Record, Play, etc.) and require different translations. Use context, string notes, and surrounding strings to determine which form is needed. Menus use noun forms; buttons and commands use imperative forms.
  - *Source:* "Edit" → *Target:* "Düzen" (menu title)
  - *Source:* "Edit" → *Target:* "Düzenle" (button)
  - *Source:* "View" → *Target:* "Görüntü" (menu)
  - *Source:* "View" → *Target:* "Görüntüle" (button)

- **Uppercase-Lowercase Conversion Rules**: Follow Turkish uppercase-lowercase conversion pairs, specifically ı → I and i → İ. Be aware this can cause functional issues in programmatic conversions.

- **Loan Words — Curly Apostrophe Before Turkish Suffix**: Treat loan words as proper names. Always separate a Turkish grammatical suffix from a loan word using a curly apostrophe (\u2019), the same way suffixes attach to acronyms above.

- **Capitalization Exceptions for Conjunctions**: Do not capitalize conjunctions (ve, veya, ile) or the word "için" in titles, except for specific visual phrases.
  - *Source:* "iWork for iOS" → *Target:* "iOS için iWork"

- **Use Passive Voice to Avoid Variable Inflection**: Use the passive voice when necessary to avoid attaching inflections directly to variables.
  - *Source:* "Deleting the preferences will…" → *Target:* "Tercihler silindiğinde…"

- **Grammar Constraints & Concatenation**: Adapt to Turkish sentence structure in concatenated strings. Nouns following a number must be singular in Turkish, unlike English.
  - *Source:* "1 Application / %d Applications" → *Target:* "1 Uygulama / %d Uygulama"

- **Tooltips — Tense and Punctuation**: Use simple present tense for button tooltips. Do not end with a period unless it is a full sentence with a subject and conjugated verb.
  - *Source:* "Crop as portrait" → *Target:* "Düşey olarak kırp"

- **Undo and Redo Strings**: Translate Undo/Redo variables using a colon format to avoid attaching suffixes to the variable.
  - *Source:* "Undo %@" → *Target:* "Geri Al: %@"
  - *Source:* "Redo %@" → *Target:* "Yinele: %@"

## Interface Elements

- **Button and Command Capitalization — Imperative Form**: Use the plain imperative for buttons (Aç, Kapat, Düzenle) and command names in menus (Yazdır, Çık). Menu titles use noun forms (Dosya, Düzen, Görüntü). Capitalization follows the source for buttons and pane titles; do not capitalize words mid-sentence just to follow English style.
  - *Source:* "Open" → *Target:* "Aç" (button)
  - *Source:* "Print" → *Target:* "Yazdır" (menu command)
  - *Source:* "File" → *Target:* "Dosya" (menu title)


## Trademarks And Product Names

- **Use Non-Breaking Space with Product Names in Software**: In software strings, place a non-breaking space between multi-word product names and surrounding text to prevent the name from wrapping across lines. Apply this to any multi-word product name — including the app's own.
  - *Source:* "Apple Watch" → *Target:* "Apple Watch" (non-breaking space before "Watch")

- **Attach Suffixes to Product Names Based on English Pronunciation**: Attach Turkish suffixes to product names that are kept in their original form based on their English pronunciation, not their spelling.
  - *Source:* "to Apple Music" → *Target:* "Apple Music\u2019e"

## Terminology

- **Prefer Turkish Equivalents Over Anglicisms**: Use Turkish terminology even when users commonly say the English word in everyday speech. When multiple Turkish words are available, prefer the standard, established Turkish term for common UI actions.
  - *Source:* "Only" → *Target:* "Yalnızca" (not Sadece)
  - *Source:* "Reply" → *Target:* "Yanıt" (not Cevap)
  - *Source:* "Device" → *Target:* "Aygıt" (not Cihaz)

- **Context-Specific Term Choices for Common Words**: Several common English words have multiple Turkish equivalents that depend on context. "Play" is "çalmak" for audio, "oynatmak" for video, and "oynamak" for games. "Edit" is "Düzen" for menu titles and "Düzenle" for buttons. "Message" is "İleti" for Mail/UI and "Mesaj" for text messaging. "Size" is "Büyüklük" generally, "Boyut" only for dimensional contexts (window, box), and "Punto" for font size; never use "Boyut" for file sizes.
  - *Source:* "Play" → *Target:* "Çal" (audio)
  - *Source:* "Play" → *Target:* "Oynat" (video)
  - *Source:* "Play" → *Target:* "Oyna" (game)
  - *Source:* "Message" → *Target:* "İleti" (Mail)
  - *Source:* "Message" → *Target:* "Mesaj" (SMS)
  - *Source:* "File size" → *Target:* "Dosya büyüklüğü"
  - *Source:* "Window size" → *Target:* "Pencere boyutu"

- **Use the Platform-Standard Turkish Term**: For standard UI actions, use the established platform Turkish term rather than the common alternative (e.g. use "Vazgeç" for Cancel, not "İptal"; and "Saptanmış" for Default, not "Varsayılan").
  - *Source:* "Cancel / Default" → *Target:* "Vazgeç / Saptanmış"

## Variables

- **Preserve and Reorder Variables Correctly**: Keep all variables exactly as they appear in the source. If Turkish word order requires moving a variable, add positional numbering (%1$@, %2$@) to every variable in the string. Never attach Turkish suffixes directly to a variable (e.g. do NOT write %1$@'ye) — the correct suffix depends on the substituted value's vowels, final sound, and whether it is a proper noun (vowel harmony, buffer consonant, apostrophe), which are unknown at translation time, so a fixed suffix is grammatically wrong for most values (the substitution still runs; the result is just incorrect Turkish). Keep the variable count identical to the source; adding or removing variables breaks functionality. Never alter a period inside a variable (e.g. %.1f).
  - *Source:* "%@ %@" → *Target:* "%2$@ - %1$@"
  - *Source:* "Page %1$@ of %2$@" → *Target:* "Sayfa %1$@ / %2$@"

## Formatting

- **Turkish Phone Number Format**: Leave specific phone numbers in strings unchanged — do not localize them. When a Turkish phone number is written out, the general format is 0 (XXX) XXX XX XX (domestic) or +90 (XXX) XXX XX XX (international).
  - *Source:* "(408) 111 5555" → *Target:* "(408) 111 5555" (specific number left unchanged)

- **URL Addresses**: Only localize URLs that are demonstrative or example URLs; never alter real URLs — leave real URLs (including query params and paths) verbatim.

- **Non-Breaking Hyphen in Hyphenated Terms (e.g. Wi-Fi)**: Hyphenated terms such as Wi-Fi must stay on a single line. Replace the regular hyphen with a non-breaking hyphen to prevent line breaks within these terms.
  - *Source:* "Wi-Fi" → *Target:* "Wi‑Fi" (non-breaking hyphen)

## UI Guidelines

- **Inline Alt-Text Elements**: Add "simgesine" or "düğmesi" after inline icon elements. Adjust text to avoid repetitive VoiceOver readings.
  - *Source:* "Tap the Info icon" → *Target:* "Bilgi düğmesi simgesine dokunun"

- **Lock Screen, Home Screen, Side/Top Button — Lowercase; basmak for Hardware**: These terms are capitalized in English but lowercase in Turkish: "kilitli ekran", "ana ekran", "yan düğme", "üst düğme". Use "basmak" for hardware buttons; reserve "tıklamak" for software buttons only.
  - *Source:* "Triple-click the Side Button to toggle Touch Accommodations" → *Target:* "Dokunma Kolaylıkları\u2019nı açmak/kapatmak için yan düğmeye üç kez basın"

## Symbols

- **Currency Symbol After Amount; Percent Sign Before Number No Space**: Place currency symbols after the amount separated by a non-breaking space (e.g. 120 ₺, 120 €). The percent sign is placed before the number with no space (e.g. %30).
  - *Source:* "50%" → *Target:* "%50"
  - *Source:* "€120" → *Target:* "120 €" (non-breaking space before the currency symbol)

## Diversity And Inclusion

- **Avoid Violent, Oppressive, or Ableist Terms**: Do not translate technology using inherently violent terms (like "kill" or "hang"), the oppressive pair "master"/"slave", or terms like "sanity check" that associate mental health with functionality. Avoid describing software or hardware with human attributes, which can carry unintended hurtful implications.

- **Use Gender-Neutral Language**: Because not everyone identifies as male or female, avoid binary representations of gender by rewording with gender-neutral language wherever possible. When content is about or addressed to a real person, prefer referring to them by name.

- **Put People First When Translating About Disability**: Focus on what people can do, not on what they can't. In most cases use people-first phrasing that describes the individual before any disability.
  - *Source:* "Deaf" → *Target:* "İşitme Engelli" (not "Sağır")

- **Don't Use Color to Convey Positive or Negative Qualities**: Use colors only to describe actual colors. Avoid using color to connote security, secrecy, or a good/bad judgment (e.g. "white hat hacker", "black testing environment").

