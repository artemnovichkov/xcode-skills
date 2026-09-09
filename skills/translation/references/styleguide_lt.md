# Lithuanian (lt) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Lithuanian uses low-high quotation marks „ (\u201E) as the opening mark and ” (\u201D) as the closing mark, and the curly apostrophe ’ (\u2019).
  - *Source:* "Click \u201CApp Store\u201D." → *Target:* "Spustelėkite \u201EApp Store\u201D."

## Tone And Voice

- **Smart but Casual Tone**: The overall tone should be neutral and descriptive — closer to formal than informal, but never stiff or stilted. Avoid trendy slang and hip expressions. Prefer established Lithuanian vocabulary over English loan words wherever a natural Lithuanian equivalent exists.
  - *Source:* "Get your iChat Account" → *Target:* "Sukurti \u201EiChat\u201D paskyrą" (not "Gauti \u201EiChat\u201D paskyrą")

## Addressing Users

- **Address Users with Formal jūs**: Always use the formal second-person pronoun jūs and its declensions. Write jūs, jūsų, jums in lower case, unless it's the very first word of a sentence or a phrase. Avoid repeating the pronoun where Lithuanian naturally omits it.
  - *Source:* "Your settings" → *Target:* "Jūsų nustatymai"

- **Use Gender-Neutral Naudotojas**: To sidestep gender agreement issues, use the word Naudotojas (User) instead of gendered forms. When a neutral construction is impossible, masculine gender serves as the generic form in Lithuanian. Only switch to the informal tu when strings are explicitly addressed to children or close friends and family.
  - *Source:* "Do you really want to call this group?" → *Target:* "Ar tikrai skambinti šiai grupei?" (not "Ar tikrai norite skambinti šiai grupei?" when addressing children)

## Abbreviations

- **Avoid Abbreviations in Software; Use Lithuanian Equivalents**: Do not abbreviate UI strings unless all other workarounds have failed and space genuinely cannot be increased. When a commonly accepted Lithuanian abbreviation exists for an English one, use it consistently.
  - *Source:* "e.g." → *Target:* "pvz."
  - *Source:* "etc." → *Target:* "ir t. t."

## Date And Time

- **Use ISO Date Format and 24-Hour Time**: Write dates in YYYY-MM-DD format (e.g., 2023-01-01). Use 24-hour time with a period as the separator (e.g., 16.30). Keep AM/PM in English (don't translate it) only when the string is itself the 12-hour time-format label — that is, when AM/PM is the actual text being displayed. Otherwise, convert to 24-hour time.
  - *Source:* "January 1, 2023" → *Target:* "2023-01-01"
  - *Source:* "4:30 PM" → *Target:* "16.30"

- **Abbreviated Day and Month Names**: Abbreviate days of the week using the approved single-letter codes: P (pirmadienis), A (antradienis), T (trečiadienis), K (ketvirtadienis), Pn (penktadienis), Š (šeštadienis), S (sekmadienis). For months use three-letter abbreviations: Sau, Vas, Kov, Bal, Geg, Bir, Lie, Rgp, Rgs, Spa, Lap, Gru.
  - *Source:* "Monday" → *Target:* "P"
  - *Source:* "January" → *Target:* "Sau"

## Measurements

- **Convert Imperial to Metric; Use Non-Breaking Space**: Convert descriptive or incidental imperial measurements to metric (e.g., inches to centimeters) when they appear in sentences. Exception: keep product display and screen sizes in inches (colių), matching Apple's shipped Lithuanian conventions. Never use the double-quote symbol as an abbreviation for inch. Separate the numerical value from the unit symbol with a non-breaking space.
  - *Source:* "100 m" → *Target:* "100 m"
  - *Source:* "30 min." → *Target:* "30 min."
  - *Source:* "13-inch display" → *Target:* "13 colių ekranas" (display size stays in inches)

- **Lithuanian Unit Abbreviations**: Use Lithuanian abbreviations for time units: min. (minute, with full stop), val. (hour), s (second). Use uppercase B for bytes (KB, MB, GB) and lowercase b for bits (Kb, Mb, Gb). Replace the English 'per' indicator with a slash in combined units.
  - *Source:* "kbps" → *Target:* "Kb/s"
  - *Source:* "FPS" → *Target:* "kadr./s"

## Numerals

- **Thousand Separator and Decimal Mark**: For numbers of five or more digits, use a non-breaking space as the thousand separator. Use a comma as the decimal mark (e.g., 1000,24 EUR). Version numbers retain a period (e.g., OS X 10.9). Replace the 'v' prefix with the word versija.
  - *Source:* "10,000 songs" → *Target:* "10 000 dainų"
  - *Source:* "Requires OS X v10.8.2." → *Target:* "Reikia \u201EOS X 10.8.2\u201D versijos."

## Special Characters

- **Replace # with Nr. and & with ir**: The hash sign # is not used in Lithuanian to indicate numerals; replace it with Nr. followed by a non-breaking space. The ampersand & is also not used in general text; replace it with the Lithuanian word ir. Keep & only when it is part of a registered trademark or product name.
  - *Source:* "Track #5" → *Target:* "Takelis Nr. 5"
  - *Source:* "Display & Brightness" → *Target:* "Ekranas ir ryškumas"

## Punctuation

- **Use Lithuanian Quotation Marks**: Enclose UI element names, feature names, product names, and citations in Lithuanian low-high quotation marks „ (\u201E) and ” (\u201D). Do not use straight quotes or English-style curly quotes. In a keyboard shortcut, wrap a named key such as Ctrl or Shift in „ ” (\u201E \u201D); leave single-letter keys and the connecting + unquoted (correct: „Ctrl” + C; incorrect: „Ctrl” + „C”).
  - *Source:* "Click \u201CApp Store\u201D." → *Target:* "Spustelėkite \u201EApp Store\u201D."
  - *Source:* "Press Ctrl+C" → *Target:* "Paspauskite \u201ECtrl\u201D + C."

- **Dash vs. Hyphen Usage**: Use the en dash (–) for ranges (2021–2023), bilateral relations (pirkimo–pardavimo sutartis), and minus signs (–5 °C). Use a hyphen only in brand names that contain one (Wi-Fi), date formats (2023-01-01), and letter-digit groups. Do not substitute a hyphen for a dash or vice versa.
  - *Source:* "2021-2023" → *Target:* "2021–2023"

## Grammar

- **Lithuanian Capitalization — Lowercase in Mid-Sentence**: Lithuanian does not capitalize common nouns in the middle of a sentence or in headings, even if the source does. Capitalize only proper names, words at the start of a sentence, and direct references to specific UI features or labels. In a UI item name, only the first word is capitalized.
  - *Source:* "System Preferences" → *Target:* "Sistemos nuostatos"
  - *Source:* "Security & Privacy" → *Target:* "Sauga ir privatumas"

- **Preserve Internal-Capitalization Names**: A term written with internal capitalization (a CamelCase product or feature name — including the developer's own) is usually a name, not a translatable word. Keep it as-is: do not translate, transliterate, or change its casing.
  - *Source:* "PhotoMix" → *Target:* "PhotoMix"

- **Use Participial Constructions to Avoid Clumsy Relative Clauses**: When translating gerunds or participial phrases, prefer an active participial form (imituojančias) over a relative clause with kurios. This produces shorter, more elegant Lithuanian. Adverbial participles should have a clear time reference and logical link to the main verb.
  - *Source:* "Use your iPhone to send Animoji messages that mirror your facial expressions." → *Target:* "Siųskite \u201EAnimoji\u201D žinutes iš \u201EiPhone\u201D, imituojančias jūsų veido išraiškas."

- **Lithuanian Plural Forms in Software Strings**: Lithuanian has four plural forms — one (1, 21, 31…), few (2–9, 22–29…), many (decimal values like 1.2, 1.5…), and other (0, 10–20, 30, 40…). Supply the correct Lithuanian plural ending for each form.
  - *Source:* "1 player / 2 players / 10 players" → *Target:* "1 žaidėjas / 2 žaidėjai / 10 žaidėjų"

## Interface Elements

- **Button Names as Verbs; Menu Names as Nouns**: Buttons and dialog box actions must be translated as infinitive verbs (Atšaukti, Atidaryti, Diegti). Main menu bar items are nouns (Peržiūra, Pagalba). Submenu items that lead directly to an action are verbs in infinitive form (Kopijuoti). Window titles must be noun phrases, never verb phrases.
  - *Source:* "Cancel" → *Target:* "Atšaukti"
  - *Source:* "View" (menu) → *Target:* "Rodyti"

- **Add Premodifiers for DNT Terms in Oblique Cases**: When a DNT term such as an app name must appear in a grammatical case that Lithuanian signals with a preposition, add an appropriate context word after the DNT term rather than inflecting it. This prevents ambiguous or grammatically incorrect constructions.
  - *Source:* "The app in the Dock." → *Target:* "Programa yra \u201EDock\u201D juostoje" (not "\u201EDock\u201D.")
  - *Source:* "If data is not in iCloud" → *Target:* "Jei duomenys nėra \u201EiCloud\u201D debesyje"

## Trademarks And Product Names

- **Do Not Translate Trademarks or Product Names**: Trademarks, slogans, and product names must remain in English. Use non-breaking spaces within multi-word DNT terms (Time Capsule, iPod touch) to prevent unwanted line breaks. For very long DNT strings such as Apple Pro Display XDR, do not place a non-breaking space after the company name itself.
  - *Source:* "Time Capsule" → *Target:* "Time Capsule"

## Variables

- **Number Variables When Reordering; Preserve %% in Percent Strings**: If Lithuanian word order requires moving variables, add positional markers (e.g., %1$@, %2$@) to all variables in that string. In software strings, %% represents a literal percent sign and must not be changed to %. Separate %% from the numeric variable with a non-breaking space.
  - *Source:* "%.0f%% completed" → *Target:* "Baigta: %.0f %%"

## Diversity And Inclusion

- **Use Gender-Neutral Language; Avoid Gendered Pronouns**: Avoid gender-specific constructions wherever possible. Rewrite sentences using infinitive structures (Norint padaryti…) or the neutral Naudotojas form instead of masculine or feminine verb agreement. For non-binary references following a singular 'they', use phrases like šis žmogus.
  - *Source:* "If you have doubts, you can always talk to an adult you trust, and they will help you." → *Target:* "Jei abejoji, visada gali pasikalbėti su suaugusiuoju, kuriuo pasitiki. Šis žmogus padės tau priimti tinkamą sprendimą."

- **Prefer People-First Language for Disability**: Avoid labels like aklas (blind) or invalidas (disabled). Instead use people-first or neutral terms: silpnaregis (visually impaired), neįgalusis, žmogus su negalia. Focus on what people can do rather than assumed limitations.
  - *Source:* "blind user" → *Target:* "silpnaregis naudotojas"
