# Danish (da) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Danish uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting and the curly apostrophe ’ (\u2019) for inflection of loanwords and acronyms (e.g. `tv’et`, `id’et`).

## Tone And Voice

- **Smart but Casual Style**: Danish text should feel "smart but casual" — closer to formal than informal, but never stiff or trendy. Use neutral, descriptive language that feels natural to Danish users and avoids leaving traces of English sentence structure.
  - *Source:* "To start downloading, press OK." → *Target:* "Tryk på OK for at starte overførsel."

- **Remove "Please" from Instructions**: English "please" is typically dropped in Danish translations. Formality is already conveyed through the verb form, so keeping "please" sounds unnatural and redundant.
  - *Source:* "Please use another name." → *Target:* "Brug et andet navn."

- **Natural Danish — Prioritize the Reader**: Translations should read naturally. The reader should not feel like they are reading a translation. Avoid cryptic or pedantic word-for-word renderings of the original.
  - *Source:* "The application has encountered an error and needs to quit." → *Target:* "Der opstod en fejl, og appen skal lukke."

## Addressing Users

- **Avoid Literal Translation of "Your"**: Do not always translate the English "your" with a possessive pronoun in Danish. The definite form of the noun is usually more idiomatic unless you need to contrast ownership explicitly.
  - *Source:* "Your software has been updated." → *Target:* "Softwaren er blevet opdateret."

- **Colloquial but Correct Register**: Use a friendly, colloquial style that makes the user feel comfortable. Avoid formal or complicated structures, and write as you would in correctly spoken Danish rather than producing overly literal translations.
  - *Source:* "You may have to restart your computer." → *Target:* "Du skal muligvis starte computeren igen."

## Grammar

- **End-Weight Syntax — Avoid Long Subordinate Clauses at Start**: Danish favors end-weight sentence structure. When localizing, avoid long subordinate clauses at the start of sentences. Consider swapping clauses so the main action comes first. Restructure clauses rather than mirroring the English word order.
  - *Source:* "To start downloading, press OK." → *Target:* "Tryk på OK for at starte overførsel."

- **Translating "May/Might" — Use "måske/muligvis"**: Where English uses "may" or "might" as a modal auxiliary, prefer "måske" or "muligvis" in Danish for natural flow. Avoid long subordinate constructions such as "Det kan være, at…".
  - *Source:* "You may have to restart your computer." → *Target:* "Du skal muligvis starte computeren igen."

- **"Føj til" vs. "Tilføj"**: Use "føj til" when an item is added to a specific receiver ("føj X til Y"). Use "tilføj" on its own or with just a direct object when no receiver is mentioned.
  - *Source:* "Add an item to the Login items list." → *Target:* "Føj et emne til listen over log ind-emner."
  - *Source:* "Add a user account." → *Target:* "Tilføj en brugerkonto."

- **Pronouns — Include in Both Nouns When Inflection Differs**: According to Dansk Sprognævn, include the pronoun in both noun phrases when the inflection of each noun is different, to maintain grammatical correctness.
  - *Source:* "What make and model is your wireless router?" → *Target:* "Hvilket mærke og hvilken model er din trådløse router?"

- **Imperative Forms — Avoid Truncated Endings**: Do not use imperative forms ending in "r" such as "Ændr", "Bladr", or "Forhindr". Replace these with more natural alternatives like "Skift", "Gennemse", and "Undgå".
  - *Source:* "Change" → *Target:* "Skift"
  - *Source:* "Browse" → *Target:* "Gennemse"

- **Genitive with Variables — Rephrase to Avoid Possessive Suffix Errors**: Never apply a genitive suffix directly to a variable placeholder, as names ending in s, x, or z will produce incorrect output at runtime. Rephrase using a preposition instead.
  - *Source:* "%@\u2019s video" → *Target:* "Video fra %@"
  - *Source:* "%@\u2019s %@ Birthday" → *Target:* "%@ fylder %@ år"

- **Conjunctions — Translate "Or" as "og" with "Any"**: When English uses "any" followed by "or", translate "or" as "og" and use plural in Danish. Use common sense to ensure the translation reflects the correct meaning.
  - *Source:* "Keynote accepts any QuickTime or iTunes file type." → *Target:* "Keynote accepterer alle QuickTime- og iTunes-arkivtyper."

- **Undo/Redo Strings — Lowercase Noun Phrases**: Undo strings are concatenated at runtime as "Fortryd %@". The action string must be a lowercase noun phrase so it reads naturally when inserted into the undo/redo sentence.
  - *Source:* "New Group" → *Target:* "ny gruppe"

- **Changing Gender — Adjust Articles and Adjectives**: When replacing a common-gender term with a neuter-gender term (or vice versa), make sure all articles and adjectives in the phrase are adjusted accordingly.
  - *Source:* "a new document" → *Target:* "et nyt dokument" (not "en ny dokument")

## Abbreviations

- **Abbreviation Periods — Follow DSN Rules**: Follow Dansk Sprognævn conventions for abbreviation periods. Common abbreviations like "ca.", "bl.a.", "kr." take a period, while metric units (cm, m, kg, g) do not. When an abbreviation ends a sentence, do not add a second period.
  - *Source:* "about 10 km" → *Target:* "ca. 10 km"
  - *Source:* "n/a" → *Target:* "i/t (ikke tilgængelig)"

- **No Period After "auto" and "OK"**: The words "auto" and "OK" are used without abbreviation period in Danish.
  - *Source:* "auto." → *Target:* "auto"

- **Prefer Rewording Over Abbreviating**: To provide the best user experience, prefer shortening strings by rewording or removing redundant text rather than abbreviating words. Look at surrounding strings for context that may allow omission.
  - *Source:* "Description: Not available" → *Target:* "Ikke tilgængelig" (preferred over "Beskr.: Ikke tilgængelig")

- **"vha." for "with/using"**: In software, "vha." (ved hjælp af) is often used when the source says "with" or "using" to refer to performing an action by means of something.
  - *Source:* "Connect using PPP" → *Target:* "Opret forbindelse vha. PPP"

## Acronyms

- **Swap Acronym and Expansion Order**: For well-known IT acronyms, place the acronym first and the spelled-out form in parentheses. Do not repeat the acronym inside the parentheses. If the acronym is compounded with another word, attach the hyphen and word directly after the acronym, not after the closing parenthesis.
  - *Source:* "a Post Office Protocol (POP) account" → *Target:* "en POP-konto (Post Office Protocol)"

- **Lowercase Common Acronyms**: In Danish, common acronyms such as CD, DVD, PC, TV, and ID are written in lowercase (cd, dvd, pc, tv, id). Use an apostrophe when inflecting them.
  - *Source:* "the TV" → *Target:* "tv\u2019et"
  - *Source:* "the ID" → *Target:* "id\u2019et"

## Date And Time

- **Danish Date and Time Format**: Use the format day.month.year for dates (e.g. 20. august 2020 or 02.12.2020). Danish uses a 24-hour clock with a period as the time separator (e.g. kl. 16.15). Do not translate AM/PM; use it only when clearly referencing the American time format.
  - *Source:* "Sunday, August 20, 2020" → *Target:* "søndag den 20. august 2020"
  - *Source:* "4:15 PM" → *Target:* "kl. 16.15"

## Numerals

- **Decimal and Thousands Separators**: Danish uses a comma as the decimal separator and a period as the thousands separator. Always include a space between a number and its unit.
  - *Source:* "1,000,000 songs" → *Target:* "1.000.000 sange"
  - *Source:* "2.5 GB" → *Target:* "2,5 GB"

## Measurements

- **Do Not Convert Imperial to Metric in Sentences**: Do not convert units such as inches to centimetres in software strings or sentences.
  - *Source:* "11\" MacBook Air" → *Target:* "11\" MacBook Air"

## Addresses

- **Danish Address Format**: Addresses follow Danish convention — street name and number, then postcode and city. Danish postal codes consist of 4 digits (optionally prefixed with DK- when sending from abroad).

## Punctuation

- **Curly Quotes and Apostrophes**: Always use curly double quotes “ (\u201C) and ” (\u201D) in software and help text. Never use straight quotes or single quotes where double curly quotes are required. Similarly, use the curly apostrophe (right single quotation mark) rather than the straight apostrophe. Replace single quotes in software with curly double quotes.
  - *Source:* "\"%@\"" → *Target:* "\u201C%@\u201D"

- **Punctuation Placement — Outside Quotation Marks**: Add punctuation outside quotation marks in Danish.
  - *Source:* "She said \"yes\"." → *Target:* "Hun sagde \u201Cja\u201D."

- **Do Not Mirror Source Periods**: If the source string does not end with a period, do not add one to the Danish translation. The absence may be intentional — the string may be a title, be concatenated at runtime, or have a period added programmatically.
  - *Source:* "No service" → *Target:* "Ingen tjeneste"

- **Capitalisation After Colons**: Follow DSN rules for capitalisation after a colon. Capitalise the first word of a complete sentence after a colon. Use lowercase after a colon when what follows is a subordinate clause or a partial sentence. In lists, capitalise the first word of each item for consistency.
  - *Source:* "Time remaining: About a minute left." → *Target:* "Tid tilbage: Der er omkring et minut tilbage."
  - *Source:* "Time remaining: about a minute" → *Target:* "Tid tilbage: omkring et minut"

- **Comma Style — Use Grammatisk Komma**: Use "grammatisk komma" (tilvalgt startkomma) in all translations. Do not insert a comma between closely connected imperatives sharing the same object (rend og hop-reglen). Use a comma when imperatives have different objects.
  - *Source:* "Export and import contacts" → *Target:* "Eksporter og importer kontakter"

- **Accent Signs — Avoid in General UI**: Do not use accent aigu in general UI translations. Exceptions: when a sentence could be misinterpreted (e.g. "én pris" vs. "en pris") and in VoiceOver strings where pronunciation requires the accent (e.g. "aktivér", "markér"). Siri strings always use accents.
  - *Source:* "Activate" → *Target:* "aktiver"

- **Parentheses — Period Placement**: If a sentence ends after the closing parenthesis, place the period after it. If a whole sentence is in parentheses, place the period inside. Avoid putting whole sentences in parentheses — remove the parentheses instead.
  - *Source:* "Setup is complete (see details)." → *Target:* "Indstillingen er fuldført (se detaljer)."

- **Characters Used as Words — Translate & and #**: In Danish, translate "&" as "og" and "#" as "nummer".
  - *Source:* "Tips & Tricks" → *Target:* "Tips og tricks"

## Special Characters

- **Use the Ellipsis Character — Not Three Dots**: Replace three separate full stops in the source with the proper ellipsis character (…, …). There is no space between the preceding word and the ellipsis.
  - *Source:* "Save as..." → *Target:* "Gem som…"

## Interface Elements

- **Apple Product Name Inflection**: Product names such as iPhone, iPad, iPod, HomePod, and Apple Watch are not inflected in Danish. Add a possessive pronoun ("din", "min") or demonstrative ("dette", "en") when a definite or possessive form is needed. Avoid appending "-enheden" except when no other option exists.
  - *Source:* "Your iPhone is locked." → *Target:* "Din iPhone er låst."
  - *Source:* "Turn off your Mac." → *Target:* "Sluk din Mac."

- **"Mac" Definite Form — Use "Mac-computeren"**: When the definite form of "Mac" is required, use "Mac-computeren". Sometimes "Mac'en" or "din Mac" can also be used depending on context. Do not use "Macintosh".
  - *Source:* "the Mac" → *Target:* "Mac-computeren"

- **Tabs and Menu Titles — Prefer Nouns**: When translating tabs, panels, and menu titles, use nouns instead of verbs where possible.
  - *Source:* "View" → *Target:* "Oversigt" (menu title)

- **Tooltips — End with Full Stop**: Tooltips have limited space. Be concise and creative. Tooltips normally end with a full stop.
  - *Source:* "Opens the selected file." → *Target:* "Åbner det valgte arkiv."

- **Capitalization — Proper Names Indefinite vs. Definite**: For tools or functions with a localized proper name, use either upper-case initial letter with indefinite form, or lower-case initial letter with definite form. Do not mix (e.g. "Åbn Indstillingsassistent" or "Åbn indstillingsassistenten", not "Åbn indstillingsassistent").
  - *Source:* "Open Setup Assistant." → *Target:* "Åbn Indstillingsassistent."

- **Touch and Hold**: Translate "Touch and hold" as "Hold en finger på…" or "Hold knappen nede…". Translate "Press xxx and hold down xxx" as "Tryk på og hold xxx nede".
  - *Source:* "Touch and hold the icon." → *Target:* "Hold en finger på symbolet."

## Variables

- **Preserve Variables Exactly as in Source**: Keep all runtime variables (such as %@, %d, %1$S) unchanged and in the correct position in the translated string. Do not alter variable formatting strings like "%.1f GB" to change decimal separators — that conversion is handled internally by the software.
  - *Source:* "%d%% Charged" → *Target:* "%d %% opladet"

## Diversity And Inclusion

- **Use Gender-Neutral Language**: Avoid gendered nouns when gender-neutral equivalents exist (use "politibetjent" not "politimand", "lærer" not "lærerinde"). Do not use binary gender pronouns for people of unspecified gender; instead omit the pronoun or use "vedkommende". In Danish, using "they" (de) as a singular pronoun is not yet common and should be avoided.
  - *Source:* "When a child turns 18, they can request…" → *Target:* "Når et barn fylder 18 år, kan vedkommende anmode om…"

## Compounds And Hyphens

- **Avoid Long Compounds — Break Up or Rephrase**: Avoid very long compound nouns. Rewrite or break them up using prepositions. Use a hyphen when combining an English word or name with a Danish word (e.g. iCloud-konto). Avoid multiple hyphens in one compound — rephrase instead (e.g. "adgangskode til Apple-id" not "Apple-id-adgangskode").
  - *Source:* "Headset jack" → *Target:* "Stik til hovedtelefoner"
  - *Source:* "Audio playback controls" → *Target:* "Knapper til lydafspilning"

- **Hyphenation Rules — Follow New Danish Standards**: Follow the current Danish rules for hyphens. For example, "e-mailadresse" is now one compound. Add a hyphen when it improves readability (e.g. multitasking-linjen) or when combining an English word/name with a Danish word (e.g. iCloud-konto). Check for consistency before adding hyphens.
  - *Source:* "email address" → *Target:* "e-mailadresse"

## Url Localization

- **URL Localization — Apple.com Country Code**: URLs with "apple.com/xxx" are generally localized by adding the country code /dk. Always follow project-specific URL instructions.
  - *Source:* "http://www.apple.com" → *Target:* "http://www.apple.com/dk"

## Units

- **Units — Danish Conventions**: KB is written as "kB" in Danish. Always include a space between a number and its unit (e.g. 40 GB). No period after metric abbreviations (cm, m, kg, kHz, dB). Time abbreviations: t., min./m., sek./s. Inch uses the "-symbol.
  - *Source:* "40GB" → *Target:* "40 GB"

## Phone Numbers

- **Phone Numbers — Danish Format**: Danish phone numbers have 8 digits written as "12 34 56 78". International format: (+45) 12 34 56 78. In software strings, follow the system standard.
  - *Source:* "(408) 111 5555" → *Target:* "12 34 56 78"

## Software Formatting

- **Line Breaks — No Space Around \n**: The text variable \n is used for non-breaking line breaks. There is no space around \n.
  - *Source:* "to\nManage" → *Target:* "til\nAdministration"

- **Implicit Subject — Use Inflected Verb Form**: When software strings have an implicit subject (the application or function), translate past-tense verbs using the inflected verb form as normal.
  - *Source:* "Added 3 items" → *Target:* "Tilføjede 3 emner"

## Terminology

- **Noun Inflections — Approved Spellings**: Use the approved inflections for common terms: e-mail/e-mails/e-mailene, højttaler/højttalere/højttalerne, album/album/albummene, app/apps/appsene, podcast/podcasts/podcastene.
  - *Source:* "emails" → *Target:* "e-mails"

- **Consistent Terminology**: Keep terminology consistent across the app's strings — reuse the established software translation for a term rather than coining a new one.
  - *Source:* "Preferences" → *Target:* "Indstillinger"

- **Third-Party Terms — Follow Their Danish Translations**: When referencing terms from non-Apple products (Facebook, Twitter, YouTube, Microsoft Windows, etc.), follow the translations used by those products in Danish.
  - *Source:* "tweet" → *Target:* "tweet"

## Locale Conventions

- **Sorting Order — Danish Alphabet**: The Danish alphabet ends with æ, ø, å (in that order). Follow the system standard for sorting in software.
  - *Source:* "a-z" → *Target:* "a-z, æ, ø, å"

- **Chapter Numbering — Period Separator**: Use a period as the tiered numbering separator. Example: Kapitel 2, afsnit 1 is written as "2.1".
  - *Source:* "Chapter 2, Section 1" → *Target:* "2.1"
