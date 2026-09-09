# Polish (pl) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Polish uses curly lower-upper quotation marks „ (\u201E) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "The concept of \u201Cprivacy\u201D" → *Target:* "Pojęcie \u201Eprywatności\u201D"

## Tone And Voice

- **Smart but Casual Register**: The overall tone should lean formal rather than informal, but must never feel stiff or pedantic. Use neutral, descriptive language and avoid trendy or hip expressions. Prefer Polish terminology over English borrowings whenever a natural Polish equivalent is broadly understood.
  - *Source:* "Sign in with your account." → *Target:* "Zaloguj się na swoje konto."

- **Avoid Diminutives Except Established Ones**: Avoid diminutive forms unless their use is well established (e.g., 'obrazek', 'miniaturka'). Default to the neutral non-diminutive form.
  - *Source:* "small picture / thumbnail" → *Target:* "obrazek / miniaturka" (established diminutives; do not coin arbitrary ones)

## Addressing Users

- **Direct Second-Person Address; Capitalize Pronouns; Avoid Gender-Specific Forms**: Address the user directly in the second person — not via formal titles like Pani or Państwo. Capitalize all personal and possessive pronouns (Ty, Ciebie, Ci, Twój, Twoje) and use implied-subject constructions wherever possible. Never reveal the user's gender through past-tense or conditional-mood verb forms; rephrase to nominalized or impersonal structures instead.
  - *Source:* "Shut down your computer." → *Target:* "Wyłącz komputer." (implied subject)
  - *Source:* "You won." → *Target:* "Wygrana." (noun form, not Wygrałeś/Wygrałaś)

## Abbreviations

- **Avoid Abbreviations in Software Strings**: Do not abbreviate words in software translations unless all other approaches (such as rewording) have been exhausted. Common accepted abbreviations include m.in., wg, zob. Translated equivalents for 'e.g.' and 'etc.' are np. and itd./itp. respectively.
  - *Source:* "e.g. / etc." → *Target:* "np. / itd."

## Acronyms

- **Retain English Acronyms Unless a Standard Polish Equivalent Exists**: Do not translate acronyms unless a very common localized equivalent exists in standard technical dictionaries. If the source already provides a spelled-out expansion, translate it; do not add one the source lacks. De-facto industry-standard acronyms (ISO, ASCII, ANSI) are left unchanged.
  - *Source:* "RAM (random access memory)" → *Target:* "RAM (pamięć o dostępie swobodnym)"

## Date And Time

- **Follow Polish Time Format**: Use the system standard for date and time in software strings. When displaying actual time (not format labels), convert 12-hour (AM/PM) notation to the 24-hour Polish format. Keep 'AM' and 'PM' in English only when the string is itself a 12-hour time-format label (the actual text being displayed).
  - *Source:* "4 PM" → *Target:* "16:00"

## Measurements

- **Do Not Convert Measurement Units; Follow Polish Notation**: Do not convert imperial units to metric in general contexts. In combined units, replace the English 'per' indicator with a slash: kbps becomes kb/s and FPS becomes kl./s. Separate the value from the unit with a non-breaking space. The correct abbreviation for minutes is 'min' (no full stop); use 'godz.' for hours unless space is very limited.
  - *Source:* "kbps / FPS" → *Target:* "kb/s / kl./s"
  - *Source:* "1024 KB / 100 m" → *Target:* "1024 KB / 100 m"

- **Bytes vs Bits Casing; No Space Before Percent or Degree**: Use uppercase B for bytes (KB, MB, GB) and lowercase b for bits (Kb, Mb, Gb). Lowercase k stands for 1000 units; uppercase K stands for 1024 units. Do NOT insert a non-breaking space before the percent sign or the degree symbol (write '15%' and '20°', not '15 %' or '20 °').
  - *Source:* "15 % / 20 ° / 5 Mb" → *Target:* "15% / 20° / 5 Mb" (5 Mb = bits; 5 MB = bytes)

## Numerals

- **Polish Number Notation**: In Polish, thousands are separated by spaces and the decimal separator is a comma. Do not use periods as thousands separators.
  - *Source:* "1,000,000 songs / 1,000,000.00 currency" → *Target:* "1 000 000 piosenek / 1 000 000,00"

## Addresses

- **Use Locally-Appropriate Placeholder Names and Polish Address Format**: Replace English placeholder names with locally-appropriate Polish names. Format addresses in Polish order: Full Name, Street Address, Postal-Code City, COUNTRY. The Polish postal code format is XX-XXX (two digits, dash, three digits). Example format: `ul. Cicha 132/16, 62-200 Gniezno`.

## Special Characters

- **Always Use Polish Diacritics**: Polish diacritic characters (ą, ć, ę, ł, ń, ó, ś, ź, ż) must always be used in text. Exceptions are only functional or technical contexts where diacritics are not supported, such as URLs or email addresses. Never localize the domain 'example.com' as 'przyklad.com'.
  - *Source:* "firstname.lastname@example.com" → *Target:* "imie.nazwisko@example.com" (no diacritics in email addresses)

- **Non-Breaking Hyphens and Spaces in Product Names**: Use non-breaking hyphens in hyphenated product names (Wi-Fi, MultiTouch) to prevent incorrect line breaks. Use non-breaking spaces within multi-word product names (iPod touch, MacBook Pro, iPhone X, Apple Watch) to keep them together.
  - *Source:* "Wi-Fi / iPod touch" → *Target:* "Wi‑Fi / iPod touch"

## Punctuation

- **Polish Comma Rules — Do Not Follow English Conventions**: Do not copy English comma rules into Polish. In particular, do not add a comma after an opening adverbial phrase, and do not place a comma before the conjunctions i or lub. Polish uses a comma before a following clause only when required by Polish syntax.
  - *Source:* "After loading the data, press Return." → *Target:* "Po wczytaniu danych naciśnij klawisz Return." (no comma after adverbial)
  - *Source:* "Do task one, two, and three." → *Target:* "Wykonaj czynność pierwszą, drugą i trzecią." (no comma before i)

- **Quotation Marks — Use Polish Lower-Upper Style**: Where technically possible, use Polish curly lower-upper quotation marks („” — opener \u201E, closer \u201D). Use quotation marks for concepts and terms, not for UI labels.
  - *Source:* "The concept of \u201Cprivacy\u201D" → *Target:* "Pojęcie \u201Eprywatności\u201D"

- **Colon — Lowercase Word Follows**: The word following a colon is written in lowercase (e.g., 'Test „ślepy”: naciśnij każdy klawisz 1 raz').

- **Dash Usage — Hyphen, En-Dash, and Em-Dash**: Polish uses three distinct dash characters. Use a hyphen (-) to join words (biało-czerwony) or numbers with words (32-bitowy). Use an en-dash (–) for value ranges (lata 2012–2013) and as a minus sign. Use an em-dash (—) for pauses or separated phrases; never begin a line with an em-dash — always precede it with a non-breaking space.
  - *Source:* "years 2012–2013 / black-and-white / 32-bit" → *Target:* "lata 2012–2013 / czarno-biały / 32-bitowy"

- **Use the Single Ellipsis Character**: Always use the single ellipsis character (…, Unicode U+2026) rather than three separate full stops. In software strings this distinction affects functionality.
  - *Source:* "Loading..." → *Target:* "Wczytywanie…" (single character, not three dots)

## Grammar

- **Adjective Order Conveys Fixed vs. Temporary Qualities**: In Polish, an adjective placed before a noun usually indicates a temporary or non-fixed feature (e.g., pusty ekran), while an adjective placed after the noun indicates a permanent or fixed one (e.g., dysk twardy). Follow this convention consistently rather than mirroring English adjective placement.
  - *Source:* "empty screen / hard disk / drop-down list" → *Target:* "pusty ekran / dysk twardy / lista rozwijana"

- **Prepositions: Do Not Automatically Translate 'for' as 'dla'**: Pay special attention when translating 'for' — do not automatically render it as 'dla'. Consider other options depending on context. Do not use 'dla' before gerunds. Follow established conventions for prepositions with device names: use 'do' for adding content, 'na' for copying and location, 'na' for installing.
  - *Source:* "Default app for sending messages" → *Target:* "Domyślna aplikacja do wysyłania wiadomości" ('for' → 'do', not 'dla'; no 'dla' before a gerund)
  - *Source:* "add photos to iPhone / files on iPhone" → *Target:* "dodawać zdjęcia do iPhone'a / pliki na iPhonie"

## Syntax

- **Imperative Without „Proszę”**: Translate imperative source strings using the bare Polish imperative; do not insert 'proszę' even if the source contains 'please'.
  - *Source:* "Please click Continue." → *Target:* "Kliknij w Dalej." (not: Proszę kliknąć w Dalej.)

## Interface Elements

- **Buttons: Imperative Form**: Button labels that are verbs use the imperative mood. Aspect is not a single default — most one-shot actions are perfective (Otwórz, Anuluj), but several common buttons are conventionally imperfective (Instaluj, Importuj, Przeglądaj — not Przejrzyj). Reuse the established Polish form for a given button as it appears in previously-translated strings. Other established forms include Edit → Edycja and Continue → Dalej.
  - *Source:* "Open / Install / Cancel / Browse / Import" → *Target:* "Otwórz / Instaluj / Anuluj / Przeglądaj / Importuj"

- **Tooltips: Use Imperative, No Trailing Full Stop**: Translate tooltips using the imperative mood (do not switch from the imperative in the source to the indicative in the target). Do not end tooltips with a full stop. Use the patterns: 'Utwórz nowy plik', 'Zaznacz tę opcję, aby…', 'Kliknij, aby <action>…'.
  - *Source:* "Create a new file." → *Target:* "Utwórz nowy plik" (no full stop)
  - *Source:* "Click to close…" → *Target:* "Kliknij, aby zamknąć…"

- **Window Titles: Use Noun/Gerund Phrases**: Window titles should use noun-based or gerund-based phrases rather than imperative verbs, to convey a state or ongoing process rather than a command.
  - *Source:* "Add Account" → *Target:* "Dodawanie konta" (gerund, not Dodaj konto)

- **Progress Messages — First-Person Singular Present**: System messages that communicate an ongoing action (Searching…, Loading…, Waiting…) should be translated in the first-person singular present tense. This is the only permitted case where software status messages use a grammatical first person.
  - *Source:* "Searching… / Loading… / Waiting…" → *Target:* "Szukam… / Wczytuję… / Czekam…"

- **Search Placeholders Are Always „Szukaj”**: Due to space restrictions, all search-field placeholders are uniformly translated as 'Szukaj', regardless of the variation in the source ('Search library', 'Search videos', 'Search files', etc.).
  - *Source:* "Search library / Search videos / Search files" → *Target:* "Szukaj"

- **Application Names: Do Not Translate Trademarked Names**: Apple software uses a mix of translated and untranslated application names. Leave trademarked product names untranslated.
  - *Source:* "QuickTime Player" → *Target:* "QuickTime Player" (trademarked name, left untranslated)

- **Callouts: Remove Final Full Stop**: Callouts may be descriptive, instructional, or informative — style varies by context. Regardless of source style, drop the trailing full stop (only on the last sentence in multi-sentence callouts). Other final punctuation, such as ellipses or question marks, is kept.
  - *Source:* "Tap to begin." → *Target:* "Stuknij, aby rozpocząć"

- **Submenu, Radio, and Dropdown Grammatical Continuation**: When a submenu item, radio button, or dropdown option is a grammatical and semantic continuation of its parent label, render it lowercase and matching the parent's grammar. Treat 'standalone' items (typically separated by a horizontal line in the UI) as nominative-case, capitalized phrases.
  - *Source:* "Show: [All / Recent / None]" → *Target:* "Pokazuj: wszystko / ostatnie / brak" (lowercase continuation)

## Key Labels

- **Keep Modifier and Action Key Names in English**: Key names such as Command, Control, Option, Return, Delete, Escape, and Shift are always left in English. Exceptions: 'tabulator', 'spacja', and arrow keys (described as 'klawisze ze strzałkami').
  - *Source:* "Press Command-S to save." → *Target:* "Naciśnij Command-S, aby zachować."

## Trademarks And Product Names

- **Decline Apple Product Names Correctly in Polish**: Trademarks must not be translated or transliterated unless instructed. When Apple product names are used in Polish sentences, they must be declined following approved patterns. iPhone and Mac are masculine-animate nouns. Apple Watch and Apple Vision Pro are masculine-inanimate. AirPods is treated as a brand noun requiring the 'słuchawki' descriptor. AirTags follow the animate declension pattern (GEN AirTaga).
  - *Source:* "Reset this Mac / Reset this Apple Watch" → *Target:* "Wyzeruj tego Maca / Wyzeruj ten Apple Watch"

- **Use „aplikacja” and „system” Descriptors**: Use the descriptor 'aplikacja' before app names (except for Wallet, which is declined as 'Portfel'). Use the descriptor 'system' before all OS names (system macOS, system iOS, system iPadOS, etc.).
  - *Source:* "Open Notes / macOS Sequoia" → *Target:* "Otwórz aplikację Notatki / system macOS Sequoia"

- **Do Not Capitalize the Initial „i” in iPhone, iPad, iTunes**: Never capitalize the first 'i' in product names like iPhone, iPad, iTunes, even when they appear at the start of a sentence.
  - *Source:* "iPhone is required." → *Target:* "iPhone jest wymagany." (not: IPhone)

## Variables

- **Preserve and Reorder Variables Correctly**: Variables must be kept exactly as they appear in the source. When Polish word order requires reordering, number all variables using n$ index syntax (%1$@, %2$@) before rearranging. Do not change a period to a comma inside a numeric format specifier (e.g., %.1f GB) — decimal point changes are handled by the software.
  - *Source:* "Text %@ text %@ text %@." → *Target:* "Tekst %1$@ tekst %3$@ tekst %2$@." (when 2nd and 3rd variables must be swapped)

## Diversity And Inclusion

- **Inclusive Language and Fair Representation**: Translate consciously to include all users. Avoid referring to the user in the masculine gender unless absolutely necessary — prefer plural or impersonal constructions. Avoid terms that are violent, oppressive, or carry harmful historical connotations. Do not use color metaphors to convey positive or negative qualities. Use people-first language when referring to disability.
  - *Source:* "Blind users" → *Target:* "osoby niewidzące lub niedowidzące" (people-first)

## General Advice

- **Use Context to Resolve Ambiguous Strings**: Before translating a short or isolated string, check its surrounding strings, UI context, and comments to understand its role. Polish word order is flexible — use that flexibility to produce natural-sounding text rather than mirroring the English structure word for word.
  - *Source:* "View options" → *Target:* "Opcje wyświetlania" (noun phrase) vs. "Wyświetl opcje" (verb phrase) — context decides
