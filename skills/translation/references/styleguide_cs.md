# Czech (cs) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Czech uses curly double quotation marks „ (\u201E) and “ (\u201C) for quoting — not straight ASCII quotes.

## Tone And Voice

- **Smart but Casual Style**: Write in a neutral, descriptive style that leans formal but never becomes stiff or bureaucratic. Avoid trendy or colloquial words in software and documentation; marketing texts may be more casual.
  - *Source:* "Get started with your new device." → *Target:* "Začněte pracovat s novým zařízením."

- **Prefer Czech Terminology**: Use established Czech terminology rather than English loan words wherever a good Czech equivalent exists. Even if users commonly say the English word in conversation, the written translation should favor Czech.
  - *Source:* "Settings" → *Target:* "Nastavení"

## Addressing Users

- **Address Users in the Plural (Vykání)**: Always address the user using the plural form (vykání). The only exceptions are fitness content and content directed at minors, where singular forms may be appropriate.
  - *Source:* "Turn off your iPhone." → *Target:* "Vypněte svůj iPhone."

- **Minimise Passive and Impersonal Voice**: Limit passive and impersonal constructions to cases where they are genuinely required for good style. Prefer active verb forms that address the user directly.
  - *Source:* "The password can be changed in Settings." → *Target:* "Heslo můžete změnit v Nastavení."

## Abbreviations

- **Avoid Abbreviations in UI Strings**: Do not shorten words through abbreviations in software translations unless every other option has been exhausted. If a string is too long, request UI resizing rather than abbreviating.

## Acronyms

- **Keep Acronyms Untranslated**: Do not translate acronyms such as CD-ROM or RAM unless a widely accepted Czech equivalent exists. Retain the original English acronym in all other cases.
  - *Source:* "RAM" → *Target:* "RAM"
  - *Source:* "CD-ROM" → *Target:* "CD-ROM"

## Date And Time

- **Follow System Standard for Date and Time**: Use the date and time format defined by the system locale. Date and time rules for Czech are governed by ČSN ISO 8601.

## Measurements

- **Do Not Convert Measurements**: Never convert imperial measurements to metric (or vice versa). When English measurements are descriptive rather than technical, localize them and round to a natural Czech equivalent.
  - *Source:* "Your device needs to be within 30 feet of your computer." → *Target:* "Vaše zařízení se musí nacházet ve vzdálenosti do 9 metrů."

- **Never Use Inch Symbol as Abbreviation**: The double-prime character (″) must not be used as an abbreviation for inches in Czech translations.

## Numerals

- **Czech Numeral Format**: Use a space as the thousands separator and a comma as the decimal separator, following the Czech convention. For software strings, always defer to the system standard.
  - *Source:* "123456.789" → *Target:* "123 456,789"

## Special Characters

- **Use Non-Breaking Spaces for Units and Short Words**: Insert a non-breaking space ( ) between a number and its unit, and after single-letter words (a, i, k, o, s, u, v, z) to prevent them splitting across lines. Also use it inside multi-word product names such as Apple TV.
  - *Source:* "10 GB" → *Target:* "10 GB" (use   between number and unit)
  - *Source:* "v aplikaci" → *Target:* "v aplikaci" (use   after the single-letter word)

## Trademarks And Product Names

- **Decline Product Names Grammatically**: Although Apple product names are not translated, they must be declined through Czech grammatical cases where syntax requires it. Apply the correct case ending directly to the product name.
  - *Source:* "Open in iPhone" → *Target:* "Otevřít v iPhonu"
  - *Source:* "multiple iPhones" → *Target:* "více iPhonů"

## Interface Elements

- **Use Verbs for Button Labels**: Button labels in Czech software consistently use verb forms (infinitive or imperative as appropriate). Do not use noun phrases where a verb form is natural.
  - *Source:* "Edit" → *Target:* "Upravit"

- **Use Nouns for Menu Names, Noun Phrases for Window Titles**: Menu bar items prefer noun forms. Window titles use heading style and avoid verbs and imperatives wherever possible; rephrase as a noun or noun phrase instead.
  - *Source:* "Edit" (menu name) → *Target:* "Úpravy"
  - *Source:* "Configure VPN" (window title) → *Target:* "Nastavení VPN"

- **Capitalise UI Element References in Sentences**: Capitalise the first letter of a UI element name (menu, button, setting) when it appears as a reference within a sentence. Use lower case when referring to the same concept generically or as a feature.
  - *Source:* "Open Settings and turn on Location Services." → *Target:* "Otevřete Nastavení a zapněte Polohové služby."
  - *Source:* "This action requires location services to be enabled." → *Target:* "Požadovanou akci nelze provést, protože nemáte zapnuté polohové služby."

- **Use Full Key Names for Apple Special Keys**: Spell out Apple special key names in full: Shift, Control, Option, Command. Never abbreviate them as ctrl, alt, or cmd.
  - *Source:* "cmd+C" → *Target:* "Command-C"
  - *Source:* "Shift-Command-1" → *Target:* "Shift-Command-1"

## Punctuation

- **Use Czech Curly Double Quotes**: Czech typography always uses the „lower-upper“ double quote style — „ (\u201E) as the opening mark and “ (\u201C) as the closing mark. Only apply quotes around UI element names within a sentence when omitting them would break natural syntax; never quote app names.
  - *Source:* "Click “General”." → *Target:* "Klikněte na „Obecné“."
  - *Source:* "in the app %@" → *Target:* "v aplikaci %@"

- **No Full Stop in Single-Sentence Callouts**: Czech omits the terminal full stop in single-sentence callout texts. Follow the source for all other punctuation contexts.
  - *Source:* "Your backup is complete." → *Target:* "Zálohování bylo dokončeno"

## Variables

- **Preserve Variable Syntax Exactly**: Never alter variable tokens (%@, %d, %1$@, etc.) — they are replaced at runtime and any change will break assembly. When the order of multiple variables must change to produce natural Czech, convert positional variables (%@ %@ → %1$@ %2$@) rather than reordering the tokens.
  - *Source:* "%@ shared %@ items" → *Target:* "%1$@ sdílel(a) %2$@ položek"

## General Advice

- **Translate Undo/Redo Prefixes Consistently**: Always render the Undo and Redo command prefixes as Odvolat akci and Opakovat akci respectively. This allows the action name that follows to remain in the infinitive form.
  - *Source:* "Undo Paste" → *Target:* "Odvolat akci Vložit"
  - *Source:* "Redo Delete" → *Target:* "Opakovat akci Smazat"

- **IT Terms as Adjectives, Not Postposed Nouns**: Place technology names (USB, IP, etc.) before the noun as attributive adjectives rather than after it. This matches conventions used in respected Czech IT sources.
  - *Source:* "USB keyboard" → *Target:* "USB klávesnice"
  - *Source:* "IP address" → *Target:* "IP adresa"

## Diversity And Inclusion

- **Use People-First Language for Disability**: When referring to people with disabilities, describe the person first and the disability second. Avoid defining people solely by a condition or limitation.
  - *Source:* "The blind" → *Target:* "Lidé se zrakovým postižením nebo slabozrací"
  - *Source:* "A wheelchair-bound person" → *Target:* "Osoba na vozíčku"
