# Croatian (hr) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Croatian uses curly double quotation marks „ (\u201E) as the opening mark and “ (\u201C) as the closing mark, and the curly apostrophe ’ (\u2019).
  - *Source:* "Open \u201C%@\u201D." → *Target:* "Otvori \u201E%@\u201C."

## Tone And Voice

- **Smart but Casual Tone**: The Croatian tone is smart but casual — closer to formal than informal, without being stiff or trendy. Avoid slang, colloquialisms, and second-person singular (Ti-form), which is too informal and region-specific. Assume the product is intended for all age groups and the entire country, unless otherwise stated in the instructions or user-input.

- **Promotional and Onboarding Strings: Natural and Local**: Promotional, onboarding, and feature-description strings (paywalls, upgrade prompts, "What's New", feature highlights) should read as if originally written in Croatian. Capture the tone and intent of the source — be clear and concise without rigid formality. Rephrase awkward structures, but never omit key information.

## Addressing Users

- **Use Formal Address**: Address the user with the formal second-person plural (the polite "Vi" register) — this uses the plural imperative verb form (kliknite, odaberite, unesite), not the terse singular command form (klikni, odaberi) and not the informal singular Ti-form. Write the pronoun as lowercase 'vi', not capitalized 'Vi'. Use informal address only when the source string's tone is distinctly casual, or when the developer's instructions call for an informal voice (e.g. a social or youth-oriented app).
  - *Source:* "Click Content at the top of the page." → *Target:* "Kliknite Sadržaj na vrhu stranice."
  - *Source:* "Tap Open" → *Target:* "Dodirnite Otvori" ("Dodirnite" addresses the user, so it takes the formal plural imperative, while "Open" is a command name that takes the singular imperative)

## Abbreviations

- **Avoid Abbreviations; Follow Priority Order When Necessary**: Abbreviations hurt readability and should be avoided. When they are unavoidable, try alternatives in this order: shorter synonym, rephrasing, restructuring the sentence, requesting more space, then abbreviating as a last resort. Abbreviations should end with a period, except metric units (ml, kg). Never start a sentence with an abbreviation.
  - *Source:* "Diagnosing" → *Target:* "Dijagnoza" (shorter alternative)

## Acronyms

- **Keep Acronyms in English Unless a Standard Croatian Form Exists**: Do not translate acronyms unless a widely recognized Croatian equivalent exists. Declined forms of acronyms follow Croatian case endings with a hyphen (PDV-a, SAD-a, NATO-a, PC-ju). Acronyms do not use periods between letters.
  - *Source:* "USA" → *Target:* "SAD-a" (genitive)
  - *Source:* "PC" → *Target:* "PC-ju" (dative)

## Date And Time

- **Croatian Date and Time Formats**: Use dd. MMMM yyyy. for long format with the month name in genitive (e.g. 11. veljače 2014.). Short format is dd. MM. yyyy. Croatia uses a 24-hour clock with a colon separator (17:00). Day and month names are not capitalized.
  - *Source:* "February 11, 2014" → *Target:* "11. veljače 2014."
  - *Source:* "5:00 PM" → *Target:* "17:00"

## Measurements

- **Do Not Convert Measurement Units**: Keep measurements in the units used in the source — do not convert inches to centimeters or miles to kilometers. Insert a space between a quantity and its unit.
  - *Source:* "Operating temperature: 32ºF to 122ºF (0ºC to 50ºC)" → *Target:* "Radna temperatura: 32 ºF do 122 ºF (0 ºC do 50 ºC)"

## Numerals

- **Use Spaces as Thousands Separator**: For numbers larger than 9999, use a space between digit groups (10 000, 859 343 286). In financial contexts, a full stop may be used instead. The decimal separator is always a comma, not a full stop. Software version numbers always use a full stop (macOS verzija 10.9.1).
  - *Source:* "1,000,000 songs" → *Target:* "1 000 000 pjesama"
  - *Source:* "3.5" → *Target:* "3.5" (software version number) / "3,5" (regular number)

## Special Characters

- **Croatian Diacritics and Accent on 'o'**: Always use Croatian special characters č, ž, š, ć, and đ. The accent ô on the letter o should be used to differentiate homonyms (e.g. kôd for 'code' only in the nominative, but not in other cases, e.g. "koda").
  - *Source:* "code" → *Target:* "kôd"

## Grammar

- **Capitalization Differences from English**: Croatian capitalizes far less than English. Days, months, and language names are lowercase. Only the first word of institution names, street names, and titles is capitalized (unless a proper noun follows). All words in personal names are capitalized.
  - *Source:* "Monday, January, Croatian" → *Target:* "ponedjeljak, siječanj, hrvatski"
  - *Source:* "Maksimir Street" → *Target:* "Maksimirska ulica"

- **Capitalize After a Colon in Lists**: When a colon introduces a bullet list, start each list item with a capital letter. This also applies to titled bullet items inside larger lists.
  - *Source:* "There are two types:" → *Target:* "Postoje dvije vrste:"
  - *Source:* "- Word processing: For text-heavy documents" → *Target:* "· Obrada teksta: Za dokumente koji sadrže uglavnom tekst"

- **Hyphens vs. Dashes**: Use a hyphen (no spaces) in compound words and for adding declension suffixes to abbreviations. Use an en-dash with spaces for 'from–to' ranges, reported speech, and vertical enumeration.
  - *Source:* "2010–2012" → *Target:* "2010. – 2012."
  - *Source:* "Zagreb–Split motorway" → *Target:* "autocesta Zagreb – Split"

- **Plural Handling in Software Strings**: Croatian has multiple plural forms that cannot be served by a single string. Where a plural-aware format is not available (e.g. when the formatter isn't numerical), restructure to place the count in parentheses or after a colon to avoid incorrect agreement (e.g. 'Fotografije: %@' or 'Slanje fotografija (%@) na odredište').
  - *Source:* "%@ photos" → *Target:* "Fotografije: %@"
  - *Source:* "Sending %@ photos to destination." → *Target:* "Slanje fotografija (%@) na odredište."

- **Declension in Concatenated Strings**: Variables inserted at runtime must remain in the Nominative case to work across different host strings. Adjust the host string to accommodate Nominative variables — for example, add a colon or restructure the phrase.
  - *Source:* "Download %@" → *Target:* "Preuzmi: %@"

- **Default Gender for Standalone Strings**: When a standalone string has no context indicating gender, use neuter gender. Use ordinal numbers as digits (1.) to sidestep gender disagreement in ordinals. Colors default to feminine gender as this is most likely correct.
  - *Source:* "connected" → *Target:* "spojeno"
  - *Source:* "blue" → *Target:* "plava"
  - *Source:* "first" → *Target:* "1."

- **Avoid 'od strane' for Passive Constructions**: The structure 'od strane …' is forbidden for passive voice. Rewrite the sentence to use an active construction or a different passive phrasing.
  - *Source:* "The service is provided by a third-party provider." → *Target:* "Uslugu pruža treća strana."

## Interface Elements

- **Button and Command Names Use the Singular Imperative**: Button names, command names, and menu commands are translated in the second-person singular imperative (Otvori, Kopiraj, Zatvori). This terse singular form is reserved for UI control labels; it must not be used in tooltips, footers, or full sentences addressing the user — those take the formal plural form (see "Use Formal Address"). A sentence can therefore contain both: the plural form addressing the user plus a singular command name it refers to.
  - *Source:* "Open" → *Target:* "Otvori"
  - *Source:* "Click Close." → *Target:* "Kliknite Zatvori."
  - *Source:* "File" (menu) → *Target:* "Datoteka"

## Variables

- **Reorder and Number Variables**: The order of variables can be changed to suit Croatian sentence structure. When variables in the source are not numbered, add explicit position numbers in the translation (%1$@, %2$@). Do not change the period to a comma in numeric format specifiers. Remove a trailing sentence-final full stop from the host string when the variable ends in a date already containing one.
  - *Source:* "Enabling the %@ account \u201C%@\u201D will disable \u201C%@\u201D on this Mac." → *Target:* "Omogućivanjem računa \u201E%2$@\u201C za aplikaciju %1$@, onemogućit će se \u201E%3$@\u201C na ovom Mac računalu."
  - *Source:* "Available until %@." → *Target:* "Dostupno do %@"

## Terminology

- **Prefer Croatian Terms; Accepted Loan Words**: Use Croatian wherever a clear, natural translation exists. A curated set of loan words is accepted due to space constraints or established usage: Link (over 'poveznica'), Plugin, Widget, Slideshow, Streaming, Server (iOS only). 'OK' is used on iOS; macOS uses 'U redu'.
  - *Source:* "Link" → *Target:* "link" (not "poveznica")
  - *Source:* "Widget" → *Target:* "widget"
  - *Source:* "Server" (iOS) → *Target:* "server"

- **Common Terminology Reference**: Use the established Croatian translations for key UI terms. Common errors include using wrong synonyms for standard UI vocabulary.
  - *Source:* "Update" → *Target:* "ažuriranje"
  - *Source:* "Upgrade" → *Target:* "nadogradnja"
  - *Source:* "Button" → *Target:* "tipka" (not "gumb")
  - *Source:* "System" → *Target:* "sustav" (not "sistem")

## Diversity And Inclusion

- **Avoid Color-Based Connotations**: Use colors only to describe actual colors, not to imply security levels or moral qualities. Replace 'whitelist'/'blacklist' with inclusive Croatian equivalents.
  - *Source:* "Whitelist" → *Target:* "Popis odobrenih / Popis dozvoljenih"
  - *Source:* "Blacklist" → *Target:* "Popis odbijenih / Popis nedozvoljenih"
  - *Source:* "Master" → *Target:* "Primarni / Glavni"

- **People-First Language and Gender-Neutral Titles**: Refer to people with disabilities by naming the person first (e.g. 'žena starije životne dobi' rather than 'starica'). Use gender-neutral terms like 'korisnik' or 'osoba' when gender is unknown. For honorifics, use 'Pozdrav' rather than gendered 'Poštovani/Poštovana'.
  - *Source:* "elderly woman" → *Target:* "žena starije životne dobi"
  - *Source:* "Dear Sir/Madam" → *Target:* "Pozdrav"
