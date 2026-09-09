# Kazakh (kk) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Kazakh uses guillemet quotation marks « (\u00AB) and » (\u00BB) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "Turn on \u201CDo Not Disturb\u201D." → *Target:* "\u00ABМазаламау\u00BB функциясын қосыңыз."

## Tone And Voice

- **Smart but Casual Tone**: The tone should be closer to formal than informal but never stiff or archaic. Keep a neutral, descriptive style and avoid trendy or hip expressions. Use Kazakh as much as possible, though some terms that do not translate well may remain in English.
  - *Source:* "HTTPS, True Tone, Bluetooth" → *Target:* "HTTPS, True Tone, Bluetooth" (left in English)

- **Avoid Literal Word-for-Word Translation**: The goal of translation is reached when the reader does not feel they are reading a translation. Restructure sentences to sound natural in Kazakh, use short concise sentences, and avoid cryptic or pedantically literal renderings.
  - *Source:* "You're all set!" → *Target:* "Барлығы дайын!" (a literal calque would be nonsensical; restructure for meaning)

## Addressing Users

- **Use Formal Pronoun Сіз Sparingly**: Address the user in a polite and respectful tone using the formal Сіз form, but omit it wherever the sentence reads naturally without it. Kazakh grammar often carries sufficient politeness through verb endings alone, so overusing Сіз sounds unnatural.
  - *Source:* "You can create, save, edit, move, copy and delete files." → *Target:* "Файлдарды жасауға, сақтауға, өзгертуге, жылжытуға, көшіруге және жоюға болады."

- **Omit 'Your' When Possessive Ending Suffices**: The English pronoun 'your' can almost always be omitted in Kazakh translation. The possessive case ending -ыңыз/-іңіз attached to the noun conveys the same meaning without adding the explicit pronoun.
  - *Source:* "Using your device you can do the following." → *Target:* "Құрылғыңызбен төмендегі әрекеттерді орындауға болады."

- **Avoid 'Please' Constructions**: Polite commands with 'Please' do not translate naturally into Kazakh. The formal imperative already conveys sufficient politeness, so simply use the imperative form without adding a Kazakh equivalent of 'please'.
  - *Source:* "Please enter your password." → *Target:* "Құпиясөзді енгізіңіз."

- **Action Descriptions in Tips Name the User**: When translating action-description strings that serve as VoiceOver alt-text for images, passive voice sounds unnatural. Instead, explicitly name the user performing the action in the translation.
  - *Source:* "Done is tapped, then Set as Wallpaper Pair is tapped." → *Target:* "Пайдаланушы \u00ABДайын\u00BB опциясын, содан кейін \u00ABЖұп тұсқағаз ретінде орнату\u00BB опциясын түртеді."

## Abbreviations

- **Avoid Abbreviations in Software Strings**: Do not shorten words through abbreviations in UI translations. If a string is too long, use a shorter alternative translation rather than abbreviating. A fixed set of accepted abbreviations exists for units such as сағ, мин, сек, КБ, МБ, ГБ.
  - *Source:* "hour / minute / second" → *Target:* "сағ / мин / сек"
  - *Source:* "kilobyte / megabyte / gigabyte" → *Target:* "КБ / МБ / ГБ"

## Acronyms

- **Keep Acronyms in English**: Do not translate acronyms unless a standard industry equivalent exists in Kazakh. If the source spells the acronym out (e.g. an expansion in parentheses), translate that expansion; do not add one the source doesn't include.
  - *Source:* "RAM (random access memory)" → *Target:* "RAM (кездейсоқ қол жеткізу жады)"

## Date And Time

- **Kazakh Date Format**: Kazakh documents use the format YYYY жылғы DD MMMM. Use the 24-hour time format.
  - *Source:* "August 29, 2021" → *Target:* "2021 жылғы 29 тамыз"

## Measurements

- **Do Not Convert Measurements**: Do not convert imperial measurements to metric or local equivalents. Use the double prime symbol (″ (\u2033)) as the abbreviation for inches. Spell out miles as 'миль'; if an abbreviation is unavoidable, use 'ми' (not 'мл', which means milliliters).
  - *Source:* "5 miles" → *Target:* "5 миль"

## Names And Addresses

- **Kazakh Address Format**: Follow the Kazakh post-office convention — street/avenue name and building number, apartment or office number, city, postal index, country, with the 6-digit postal index placed after the city name (e.g. "Абай даңғылы, 10, Алматы, 050000, Қазақстан"). Foreign addresses outside CIS countries are kept as-is.
  - *Source:* "Apple Inc. One Apple Park Way, Cupertino, CA 95014, United States" → *Target:* "Apple Inc. One Apple Park Way, Cupertino, CA 95014, United States" (foreign address kept as-is)

## Numerals

- **Comma as Decimal Separator, Non-breaking Space as Thousands Separator**: Use a comma as the decimal separator and a non-breaking space as the thousands separator. Do not use a thousands separator in four-digit numbers. Version numbers continue to use a period, and the version number is never followed by a period.
  - *Source:* "11234.50 kg" → *Target:* "11 234,50 кг"
  - *Source:* "OS X v10.8.2" → *Target:* "OS X 10.8.2 нұсқасы"

## Special Characters

- **Translate # as № and & as және**: The hash symbol # is not used in Kazakh; replace it with № followed by a non-breaking space. The ampersand & is also not used except inside registered trademarks or band names; in regular text translate it as 'және'.
  - *Source:* "Track #5" → *Target:* "№ 5 жол"
  - *Source:* "Display & Brightness" → *Target:* "Дисплей және жарықтық"

## Punctuation

- **Use Guillemet Quotation Marks**: Kazakh localization uses guillemet marks « » as the primary quotation marks. Straight double quotes are only used for a quote inside a quote. Do not use any quotation marks around foreign product names or DNT terms.
  - *Source:* "\u201CDo Not Disturb\u201D feature" → *Target:* "\u00ABМазаламау\u00BB функциясы"

- **Use En Dash, Not Hyphen, as Dash**: Never substitute a hyphen for a dash. Use the en dash (–) where an em dash or sentence dash is needed. Use a non-breaking hyphen within hyphenated words such as Wi-Fi to prevent incorrect line-wrapping.
  - *Source:* "This is a paid service." → *Target:* "Бұл – ақылы қызмет." (en dash, not hyphen)

## Grammar

- **Handle the Indefinite Article with Word Order or бір**: Kazakh has no articles. Translate 'a/an' by using natural Kazakh word order (placing the new item at the end of the sentence) or, when genuine singularity must be emphasized, by adding the quantifier 'бір'. Do not use an objective case ending to imply indefiniteness.
  - *Source:* "Create a file." → *Target:* "Файл жасау." (not "Файлды жасау")
  - *Source:* "Select a file." → *Target:* "Бір файлды таңдаңыз."

- **Conjunction Usage: және vs мен/бен/пен**: 'And' can be rendered as 'және' or as the clitic 'мен/бен/пен' depending on context. Between verbs, prefer using a converb (gerund form) with a comma rather than repeating 'және', which sounds unnatural.
  - *Source:* "Save the changes and close the file." → *Target:* "Өзгерістерді сақтап, файлды жабыңыз." (not "...сақтаңыз және файлды жабыңыз.")

- **Imperative Forms in Instructions**: Use the polite imperative (singular) for instructions. Do not use the plural imperative form. Tooltips that are simple hints use the infinitive form; tooltips that include a clause of purpose use the imperative.
  - *Source:* "Select" → *Target:* "таңдаңыз" (not "таңдаңыздар")
  - *Source:* "Press and hold to create a new project." → *Target:* "Жаңа жоба жасау үшін басып тұрыңыз."

## Interface Elements

- **Buttons and Commands as Infinitives**: Translate button names and command names as verbs in infinitive form. Menu names follow the part of speech of the source — nouns remain nouns, verbs become infinitives. Toolbar buttons are typically translated as nouns.
  - *Source:* "Cancel" → *Target:* "Бас тарту"
  - *Source:* "Copy" → *Target:* "Көшіру"
  - *Source:* "Share" → *Target:* "Бөлісу"

## Variables

- **Number Variables When Word Order Changes**: Keep all variables intact. When Kazakh sentence structure requires reordering variables relative to the source, add a positional index (e.g. %1$@, %2$@) so each variable resolves correctly at runtime. Do not change the decimal separator inside numeric format strings.
  - *Source:* "Found %@ with %@ starting from this date." → *Target:* "Осы күннен бастап %2$@ бар %1$@ табылды."

## General Advice

- **Prefer Kazakh Terminology Over English Loan Words**: Use an existing Kazakh term whenever it matches the meaning, function, and context of the source term. Avoid English loan words for the sake of coolness or current spoken tendency. Leave terms in English only as a last resort after careful research.
  - *Source:* "Password" → *Target:* "Құпиясөз"
