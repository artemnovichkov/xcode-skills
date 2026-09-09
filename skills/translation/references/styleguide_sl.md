# Slovenian (sl) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Slovenian uses reversed guillemets — » (\u00BB) to open a quotation and « (\u00AB) to close it — with single quotation marks ‘ (\u2018) to open and ’ (\u2019) to close a nested quotation. The curly apostrophe is the same character as that closing single quotation mark, ’ (\u2019).
  - *Source:* "Tap \u201CSay \u2018Hello\u2019\u201D." → *Target:* "Tapnite \u00BBRecite \u2018Živijo\u2019\u00AB."

## Tone And Voice

- **Smart but Casual Register**: Translations should be clear, concise, and closer to formal than informal, but never stiff or overly rigid. Avoid jargon, slang, colloquialisms, and regional expressions. Prefer stylistically neutral Slovenian terms over borrowed English ones.
  - *Source:* "server" → *Target:* "strežnik"
  - *Source:* "problem" / "issue" → *Target:* "težava"

## Addressing Users

- **Use Second-Person Plural (Vikanje)**: Address users with the formal second-person plural (vikanje) throughout. Use the informal second-person singular (tikanje) only when the source string's tone is distinctly casual, or when the developer's instructions call for an informal voice (e.g. a social or youth-oriented app). Active voice should be used whenever possible.
  - *Source:* "Install and set up your software." → *Target:* "Namestite in nastavite programsko opremo."

## Grammar

- **Animacy Subgender for Software Assistants**: The words 'pomočnik' (assistant), 'asistent', and 'krmar' (navigator) refer to software objects but are declined like animate nouns (Slovenian's animacy subgender). Apply this declension consistently even though these are inanimate digital entities.
  - *Source:* "Close Migration Assistant" → *Target:* "Zapri Pomočnika za migracijo"

- **Slovenian Capitalization Rules**: Names of days, months, and most holidays are not capitalized in Slovenian. English-style title case must not be carried over into the translation.
  - *Source:* "Christmas" → *Target:* "božič"
  - *Source:* "February" → *Target:* "februar" (month names are not capitalized)

## Abbreviations

- **Avoid Abbreviations; Use Slovenian Forms When Necessary**: Abbreviations harm readability and should be avoided whenever possible — prefer a shorter word or reword the sentence instead. Only when an abbreviation is genuinely unavoidable: never start a sentence with one, use well-established forms, and prefer the Slovenian abbreviation over an English one. The hash '#' must not be used for 'število'.
  - *Source:* "e.g." → *Target:* "na primer" (spell out in full; use "npr." only where space is too tight)
  - *Source:* "#" → *Target:* "št." (never use the "#" symbol for "število")

## Acronyms

- **Decline Acronyms with a Hyphen**: Do not translate acronyms unless a common Slovenian equivalent exists. When an acronym must fit Slovenian grammar, either place a descriptor noun in front of it (so the descriptor takes the inflection and the acronym stays unchanged) or attach the case ending directly with a hyphen. Base the hyphenated ending on how the acronym's final letter is pronounced when spelled aloud (e.g., SMS-jem, not SMS-om).
  - *Source:* "PIN" → *Target:* "koda PIN" (with descriptor) / "PIN-a" (declined with a hyphen)
  - *Source:* "RAM" → *Target:* "pomnilnik RAM" (with descriptor) / "RAM-a" (declined with a hyphen)

## Date And Time

- **Date and Time Format**: Prefer the long date format (e.g., '8. februar 2023'). In short format, use non-breaking spaces after each period. Leading zeros are not allowed in general text. Format elapsed time (timers, stopwatches) as m:ss with a comma for decimal fractions (e.g. 2:03,12).
  - *Source:* "08/02/1849" → *Target:* "8. 2. 1849"
  - *Source:* "8:00 AM" → *Target:* "8.00" (not 08.00)
  - *Source:* "8:00 PM" → *Target:* "20.00"
  - *Source:* "2m 3.12s" → *Target:* "2:03,12"

## Numerals

- **Spell Out Numbers Zero to Ten; Use Thousands Period**: Spell out numbers from zero to ten; use numerals for 11 and above. Always spell out numbers at the start of a sentence. Use a period as the thousands separator from five digits up (e.g. 10.000); four-digit numbers take no separator (e.g. 9999).
  - *Source:* "2 Macs are needed…" → *Target:* "Dva Maca sta potrebna …"
  - *Source:* "The result is 0.3 in 9,999 out of 10,000 cases." → *Target:* "Rezultat je 0,3 v 9999 od 10.000 primerov."
  - *Source:* "iOS 12.5.7" → *Target:* "različica iOS 12.5.7"

## Currency

- **Do Not Convert Currencies; Place Code After Value with NBSP**: Do not convert currencies unless instructed to do so. Translate the € currency symbol to "EUR" and $ to "USD", and in each case place the code after the numerical value with a non-breaking space in between.
  - *Source:* "The package costs $100." → *Target:* "Paket stane 100 USD."

## Style Conventions

- **Avoid Using "nahajati se" Verb**: Do not translate "there is"/"there are" with "se nahaja"/"se nahajajo"; this is poor style. Instead use the verb "biti" ("je"/"so").
  - *Source:* "If you are located in this region…" → *Target:* "Če ste v tej regiji …" (not "Če se nahajate v tej regiji …")

## Measurements

- **Do Not Convert Measurements; Use Non-Breaking Space**: Do not convert imperial or other measurements to Slovenian equivalents. Always insert a non-breaking space between a numeral and its unit. Spell out the percent word ("odstotkov") in full sentences; use the % symbol only in short labels or space-restricted places like tables, with a non-breaking space before it. Exception: when the degree symbol is used without C or F following it, omit the space.
  - *Source:* "Battery 100%" → *Target:* "Baterija 100 %"
  - *Source:* "The screen dims to 25%." → *Target:* "Osvetlitev zaslona se zmanjša na 25 odstotkov."
  - *Source:* "20°C" → *Target:* "20 °C" (non-breaking space before the unit; "20°" takes no space when the C or F is omitted)

## Names And Addresses

- **Slovenian Address Format and Personal Names**: For sample personal names, use common Slovenian placeholder names; keep foreign personal names in their original form, applying Slovenian grammatical declension. Leave US or international addresses in their source notation — do not reformat them. Use the Slovenian format only for Slovenian addresses: street name and house number, then the four-digit postal code and city (e.g. Sosedova ulica 1, 1000 Ljubljana), with the postal code written without spaces or separators.

## Punctuation

- **Use Double-Angle Quotation Marks**: Always use the Slovenian reversed guillemets, opening » and closing «. Do not substitute English-style curly quotes or other quotation forms; use single upper marks only for nested quotations.
  - *Source:* "Found in \u201C%@\u201D" → *Target:* "Najdeno v \u00BB%@\u00AB"

- **No Em-Dashes**: Em dashes must not be used; use an en dash instead.
  - *Source:* "—" → *Target:* "–"

- **Ellipsis Usage**: Always use the single ellipsis character preceded by a non-breaking space in Slovenian. An ellipsis on a command the user triggers signals an action to start — translate with the imperative; an ellipsis on a status message describing an ongoing process takes the noun/gerund form.
  - *Source:* "Add Printer..." → *Target:* "Dodaj tiskalnik …"
  - *Source:* "Adding user..." → *Target:* "Dodajanje uporabnika …"

- **Formatting of Lists**: In a list, items usually end with a comma, with the last item ending in a period. As an exception, longer list items may end with a semicolon — the last item still ending in a period. Some lists may instead have every item end with a period, particularly when the items are long, compound, and not tightly related to the introductory phrase. In all cases, keep list punctuation consistent within a list.

## Special Characters

- **Ampersand Conventions**: The ampersand is not standard Slovenian and should be translated as 'in', except in company or product names.
  - *Source:* "drag & drop; AT&T" → *Target:* "povleci in spusti; AT&T"

- **Slash Conventions**: Slashes should have no spaces around them. Use 'oziroma' instead of 'in/ali' where more appropriate.
  - *Source:* "and / or" → *Target:* "in/ali" or "oziroma"

## Trademarks And Product Names

- **Do Not Inflect Most Product Names; Use Descriptors**: Product names are generally not declined. Use a Slovenian descriptor (e.g., 'naprava', 'računalnik') in front of the product name when inflection is grammatically needed. A small set of names (Mac, iPhone, iPad, Apple TV, Safari) may be inflected naturally.
  - *Source:* "On your Mac" → *Target:* "V vašem Macu" (exception; inflection allowed, no descriptor required)
  - *Source:* "with AirDrop" → *Target:* "S funkcijo AirDrop" (descriptor required)

- **Keep Product, Feature, and Brand Names in Their Original Form**: Product, feature, and brand names — the app's own or a third party's — must not be translated or transliterated. Keep the original notation, and use a descriptor when the name needs to be declined in a sentence.
  - *Source:* "Time Machine" → *Target:* "Time Machine"

## Interface Elements

- **Interface Element Grammar Forms**: Buttons, commands, and menu items take the imperative singular form; menu titles take the gerund (noun) form; tooltips and placeholders address the user with the formal plural (vikanje).
  - *Source:* "Save" (button) → *Target:* "Shrani" (imperative)
  - *Source:* "Edit" (menu title) → *Target:* "Urejanje" (gerund)
  - *Source:* "Edit" (menu item) → *Target:* "Uredi" (imperative)
  - *Source:* "Save document" (tooltip) → *Target:* "Shranite dokument" (formal plural, vikanje)
  - *Source:* "Enter new password" (placeholder) → *Target:* "Vnesite novo geslo" (formal plural, vikanje)

- **App Intent Translation Forms**: Intent titles and parameter summaries use the imperative; intent descriptions use the third-person indicative.
  - *Source:* "Add new reminder" (intent title) → *Target:* "Dodaj nov opomnik"
  - *Source:* "Adds a new reminder" (intent description) → *Target:* "Doda nov opomnik."
  - *Source:* "Close ${application}" (intent parameter summary) → *Target:* "Zapri aplikacijo ${application}"

## Terminology

- **Standardized UI Term Translations**: Use the standard, established Slovenian translations for common UI actions and gestures. Do not invent alternatives or use English terms where a Slovenian equivalent is established.
  - *Source:* "tap" (verb) → *Target:* "tapniti"
  - *Source:* "swipe" → *Target:* "podrsniti"
  - *Source:* "OK / Cancel" → *Target:* "V redu / Prekliči"
  - *Source:* "turn on / turn off" → *Target:* "vklopiti / izklopiti"

## Diversity And Inclusion

- **Gender-Neutral and Inclusive Language**: Use formal plural address (vikanje) to avoid most gendered constructions. When a specific gender reference is unavoidable, use round-bracket notation (e.g., zaključil(-a)), or rephrase using 'oseba'. Avoid binary gender assumptions and stereotypes in all content.
  - *Source:* "finished" (gender unknown) → *Target:* "zaključil(-a)"

## Variables

- **Preserve Variables; Handle Plural Categories Correctly**: Never alter variable syntax. Slovenian has four plural categories (one, two, few, other) that must each be translated correctly. When a source string in the 'one' category lacks a variable that Slovenian grammar requires, insert it. Check all variants of a string together to ensure consistency across plural forms.
  - *Source:* "%d videos will be removed" (plural: two) → *Target:* "Odstranjena bosta %d videa."

## General Advice

- **Translate for the Reader, Not Word-for-Word**: The translation is successful when the reader does not feel they are reading a translation. Promotional and onboarding strings in particular should read as if originally written in Slovenian. Rephrase awkward structures, split overly long sentences, and omit words that add no meaning — but never lose key information.

- **Prefer Slovenian Terms Over English Borrowings**: Even when English terms have entered everyday spoken Slovenian, the written language should use established Slovenian equivalents. Only use English terms if they convey the meaning more precisely, are commonly kept in original form, or no adequate Slovenian term exists.
  - *Source:* "automatic" → *Target:* "samodejno" (not avtomatsko)
  - *Source:* "e-mail" → *Target:* "e-pošta" (not email)
