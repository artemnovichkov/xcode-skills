# Slovak (sk) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Slovak uses curly double quotation marks „ (\u201E) and “ (\u201C) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "\u201CFile\u201D menu" → *Target:* "ponuka \u201ESúbor\u201C"

## Tone And Voice

- **Smart but Casual Tone**: The overall tone should be intelligent and approachable — closer to formal than informal, but never stiff or overly academic. Avoid trendy or hip expressions and keep a neutral, descriptive style. Use Slovak terminology as much as possible, even though users in everyday speech may default to English words.

## Addressing Users

- **Formal Plural Address (T-V Distinction)**: Slovak requires formal T-V distinction. Always address the user with polite plural pronouns. The formal style is the default for all standard software strings.
  - *Source:* "Your changes will be lost if you don\u2019t save them." → *Target:* "Ak ich neuložíte, všetky zmeny budú stratené."

- **Omit "Please" and "Now" from Instructions**: Unlike English, Slovak does not routinely use "please" in instructions; the imperative form already conveys sufficient politeness, so omit it. Similarly, the word "now" is usually implied by context and should be left out unless grammatically necessary.
  - *Source:* "Restart now / Apply Now to Entire Document" → *Target:* "Reštartovať / Aplikovať na celý dokument"

- **Reduce Redundant Possessive Pronouns**: English uses possessive pronouns ("your") more freely than Slovak; do not mirror that. Translate «váš/vaše» only when it adds marketing value or is grammatically required; otherwise drop it.
  - *Source:* "Your changes will be lost." → *Target:* "Zmeny budú stratené." (omit "vaše")

- **Informal Gender-Neutral Style for Casual or Youth-Oriented Strings**: Use informal, gender-neutral language instead of the formal plural style only when the source string's tone is distinctly casual, or when the developer's instructions call for an informal, youth-oriented voice (e.g. a kids' or fitness app).

## Grammar

- **Default to Neuter Gender**: When grammatical gender cannot be determined with certainty, always use the neuter form. Switch to masculine or feminine only when the source string or a developer note makes the intended gender unambiguous.
  - *Source:* "None" → *Target:* "Žiadne" (neuter default)

- **Status Messages Use First Person**: Short progress strings ending with an ellipsis (…) should use first-person singular rather than the reflexive «sa» construction. This gives the system a more direct, active voice.
  - *Source:* "Copying messages… / Deleting…" → *Target:* "Kopírujem správy… / Vymazávam…"

- **Verb-Only Strings Use the Infinitive**: Single-word button labels, menu items, and other standalone verb strings should almost always be translated in the infinitive. Exceptions apply when the string is a runtime-composed fragment (see Variables section).
  - *Source:* "Open / Close / Play / Never use font sizes smaller than…" → *Target:* "Otvoriť / Zatvoriť / Prehrať / Nepoužívať písmo menšie ako…"

- **Plural Agreement in Software Strings**: Slovak has more plural forms than English. When the count feeds a numerical format specifier (%lld, %d), translate each plural case directly — the String Catalog's plural variation supplies the correct form; do not work around it. A workaround is needed only when the count arrives as a **pre-formatted number interpolated as a non-numerical %@** (so plural categories can't apply): place the variable after a colon (preferred, shorter) or inside brackets, keep the item name in the plural nominative, and report back that the string needs a numerical placeholder for correct plural agreement (a code fix in the source).
  - *Source:* "%@ items" (where %@ is a pre-formatted count) → *Target:* "Položky: %@"

## Abbreviations

- **Avoid Abbreviations in UI Strings**: Do not shorten words through abbreviations when a software string is too long. Rephrase the string instead. Never use more than one abbreviation per string. The abbreviation «Autom.» is the only accepted short form for "Automatic" (do not use "Automat.").
  - *Source:* "Automatic" → *Target:* "Autom."

## Acronyms

- **Keep Acronyms Before the Noun**: Do not translate acronyms unless a widely accepted localized equivalent exists. When used with a noun, place the acronym before the noun following Slovak word order.
  - *Source:* "USB cable" → *Target:* "USB kábel"

## Formatting

- **Non-Breaking Spaces to Prevent Bad Wrapping**: Insert non-breaking spaces (U+00A0) so that single-character words (o, u, k, s, v, z, a) do not fall at the end or beginning of a line, and so that fixed terms such as OS X and Wi-Fi stay together.
  - *Source:* "OS X / Wi-Fi" → *Target:* "OS X / Wi‑Fi" (non-breaking space in "OS X"; non-breaking hyphen in "Wi-Fi")

## Date And Time

- **24-Hour Notation and Slovak Date Order**: Slovak does not use AM/PM; always apply 24-hour notation (HH:mm). Use the day/month/year date order (year/month/day is also acceptable). Standalone month names use the nominative case; month names within sentences use the genitive. Use the official abbreviations h, min, s, d for time units (written without a full stop).
  - *Source:* "1 hour / %@ minutes / 08/05/1999" → *Target:* "1 h / %@ min / 08. 05. 1999"

## Measurements

- **Do Not Convert Imperial Measurements**: Do not convert units (e.g. inches to centimeters). Units in Slovak are written without a full stop and are separated from the number by a space. The only exceptions are degrees Celsius/Fahrenheit and angles.
  - *Source:* "2 GB / 30 min / 25 %" → *Target:* "2 GB / 30 min / 25 %"

## Names And Addresses

- **Locally-Appropriate Names and the Slovak Address Format**: Replace English placeholder names with locally-appropriate Slovak equivalents. Addresses follow Slovak postal conventions: name, street and number, postcode and city, country. The postal code (PSČ) consists of 5 digits written with a space after the third digit.

## Numerals

- **Space as Thousands Separator, Comma as Decimal**: Group digits in threes using a space as the thousands separator. Use a comma as the decimal separator. Ordinal numbers are written with a full stop followed by a space (e.g. 1. miesto). Replace the English ordinal symbol # with the Slovak ordinal form (e.g. #1 → 1.).
  - *Source:* "5,600,258 / 0.75 / #1" → *Target:* "5 600 258 / 0,75 / 1."

## Special Characters

- **Use Slovak Special Characters and Ellipsis**: Always use the proper Slovak diacritical characters (á, ä, č, ď, é, í, ľ, ĺ, ň, ó, ô, ŕ, š, ť, ú, ý, ž). Use the single ellipsis character (…) rather than three separate dots (...). Characters used as words in English (# for "number", & for "and") must be replaced with their Slovak word equivalents in translated text.
  - *Source:* "Music & Movies" → *Target:* "Hudba a filmy" (& → a)

## Punctuation

- **Slovak Curly Quotation Marks**: Use Slovak curly quotation marks („“ \u201E \u201C) instead of straight or English-style quotes. When a quoted phrase ends a sentence, place the final punctuation (full stop, etc.) after the closing quotation mark. In software translations, quotation marks around menu items or commands are generally not needed.
  - *Source:* "\u201CFile\u201D menu" → *Target:* "ponuka \u201ESúbor\u201C" (or omit the quotes in a software context)

- **Capitalization After Colons**: When the text after a colon expands or elaborates on what precedes it, use a lowercase letter. When the colon introduces a quotation or an independent block of text, start with a capital letter.

## Interface Elements

- **UI Elements Use Infinitive or Nominative, Neuter Gender**: Buttons, checkboxes, command names, menu bar items, and toolbar buttons should be translated using the infinitive (for verbs) or nominative (for nouns), always in neuter gender. For ambiguous strings with no context, use the descriptive (informative) form rather than the imperative.
  - *Source:* "Open / Save file / Double tap to pay" (no context hint) → *Target:* "Otvoriť / Uložiť súbor / Dvojitým klepnutím zaplatíte"

- **Tooltips Use Descriptive Style**: Tooltip titles and hints should be written in a descriptive style rather than the infinitive or imperative. They describe what the UI element does, not what the user should do.
  - *Source:* "Screenshot" → *Target:* "Odfotí obrazovku"

- **Undo/Redo Use Colon Separator**: Because actions and buttons are translated in the infinitive, Undo/Redo menu items use a colon between «Odvolať»/«Obnoviť» and the action name in the infinitive.
  - *Source:* "Undo Copy text / Redo Paste" → *Target:* "Odvolať: Kopírovať text / Obnoviť: Vložiť"

- **Capitalize Official UI Element Names**: Avoid mid-sentence capitalization unless referring to proper nouns or official UI element names (menus, buttons, preference panes, applications, features, services, and tools).
  - *Source:* "Mouse pane / in System Settings" → *Target:* "panel Myš / v Systémových nastaveniach"

## Trademarks And Product Names

- **Do Not Translate Trademarks; Allow Inflections**: Trademarks, product names, and other names kept in English must not be translated or transliterated. However, grammatical inflections of product names are permitted and expected in natural Slovak sentences. The copyright symbol © and the word "Copyright" are not translated.
  - *Source:* "Go to the App Store / with Apple Pencil" → *Target:* "Prejdite do Apple Storu / s Apple Pencilom"

## Terminology

- **Established Slovak Terminology**: Use the established Slovak forms: app/apps → apka/apky; chat → čet; end-to-end encryption → E2EE (or "šifrovanie medzi koncovými bodmi"); plugin (not doplnok/modul); hotspot is not localized (use inflected hotspot); subscription/subscribe/subscriber → odber/odoberať/odberateľ; enable/disable (non-security) → zapnúť/vypnúť; get (for downloading content) → stiahnuť (not získať); webpage → webstránka; website → web.
  - *Source:* "Subscribe / Download the app / Webpage" → *Target:* "Odoberať / Stiahnuť apku / Webstránka"

## Variables

- **Preserve Variables and Handle Gender with Brackets**: Keep all variable placeholders (e.g. %@, %d, %1$@) exactly as in the source. If Slovak word order requires a different sequence, add positional indices (%1$@, %2$@) to every variable in the string. When a variable is replaced by a noun at runtime that would require declension, place the variable inside brackets or after a colon to avoid grammar errors. Use «používateľ» before a name variable to resolve gender ambiguity.
  - *Source:* "Are you sure you want to start an audio chat with %@?" → *Target:* "Naozaj chcete spustiť hlasovú konverzáciu s používateľom %@?"
  - *Source:* "%1$@\u2019s %2$@" → *Target:* "%2$@ (%1$@)"

## Diversity And Inclusion

- **Inclusive Language: Avoid Harmful or Ableist Terms**: Do not use terms that are inherently violent (e.g. kill, hang), oppressive (master/slave), or that link mental health with functionality (sanity check). Avoid color-based connotations for security or quality levels. Use people-first language when translating about people with disabilities.
  - *Source:* "The blind / A wheelchair-bound person" → *Target:* "Ľudia so zrakovým postihnutím / Osoba na invalidnom vozíku"
