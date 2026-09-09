# Hungarian (hu) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Hungarian uses curly double quotation marks „ (\u201E) as the lower opening mark and ” (\u201D) as the upper closing mark, and the curly apostrophe ’ (\u2019).
  - *Source:* "Select \u201CStart\u201D." → *Target:* "Válassza a(z) \u201EStart\u201D lehetőséget."

## Tone And Voice

- **Smart But Casual Tone**: Write in a neutral, descriptive style that leans formal without being stiff. Avoid trendy slang. For marketing copy, adopt a more expansive, positive style — for example, prefer 'akár 10 sablon' over 'legfeljebb 10 sablon' to convey optimism.
  - *Source:* "up to 10 templates" → *Target:* "akár 10 sablon"

## Addressing Users

- **Formal Third-Person Singular Addressing**: Address the user formally using the third-person singular imperative (magázás). Use informal 'te' forms only when the source string's own tone is distinctly casual, or when the developer's instructions call for an informal voice (e.g. a social or youth-oriented app).
  - *Source:* "Click the Close button." → *Target:* "Kattintson a Bezárás gombra."

## Abbreviations

- **Minimize Abbreviations and Match Source Length**: Avoid abbreviations wherever possible. The only mandated abbreviation is 'stb.' for 'és a többi'. Never let a Hungarian translation become roughly twice the length of the source — this will clip at runtime.
  - *Source:* "View in <app>" → *Target:* "Megtekintés itt: <app>"

## Acronyms

- **Suffix Acronyms According to Pronunciation**: Do not translate acronyms unless a very common localized equivalent exists. When adding Hungarian suffixes to acronyms or product names, match the suffix to the actual spoken pronunciation of the word, not its spelling. Some acronyms have become common nouns and take no hyphen before their suffixes.
  - *Source:* "with iPad" → *Target:* "iPaddel" (not "iPaddal")

## Special Characters

- **Non-Breaking Spaces for Apple Product Names and IDs**: Insert a non-breaking space between the brand name and its number or qualifier in Apple product names and identifiers such as Apple ID, Touch ID, Face ID, Apple TV, Apple Watch SE, and OS version names. Convert double spaces to single spaces.
  - *Source:* "Apple TV" → *Target:* "Apple TV" (with a non-breaking space between "Apple" and "TV")

## Grammar

- **Compound Words and Hyphenation**: If a compound word is made up of three or more words (multiple compounds), write them solid when the total syllable count (excluding inflectional suffixes) is below seven, and insert a hyphen at a meaningful word boundary when the count reaches seven or more. Service and protocol names are never hyphenated: 'DHCP szolgáltatás', 'TCP/IP protokoll'. When a proper name forms part of a compound, attach the rest with a hyphen to the second element of the name.
  - *Source:* "software license agreement" → *Target:* "szoftver-licencszerződés"

- **Articles Before Variables**: When a variable placeholder stands alone and its value is unknown at translation time, use the constructed article 'a(z)' to cover both vowel-initial and consonant-initial replacements. Only use a definite 'a' or 'az' when you are completely certain which value will fill the placeholder.
  - *Source:* "the %@ device" → *Target:* "a(z) %@ eszköz"

- **Loan Words and Localized Spellings**: Keep certain terms in their English form: 'stream', 'web', 'e-mail', 'build'. Translate 'application' as 'alkalmazás' and 'app' as 'app' (with vowel-harmony suffix: 'appot'). Several loan words use Hungarian spelling: 'domén', 'szerver', 'bájt', 'fájl'. Never translate 'app' as 'alk.'
  - *Source:* "application" → *Target:* "alkalmazás"
  - *Source:* "app" → *Target:* "app"

- **Word Order and Natural Hungarian Syntax**: Hungarian word order is far more flexible than English. Do not mirror the source sentence structure; instead use Hungarian conventions to naturally place emphasis. Avoid calquing article usage — 'Add a file' should become the articleless 'Fájl hozzáadása', not 'Egy fájl hozzáadása'.
  - *Source:* "Add a file" → *Target:* "Fájl hozzáadása"

- **Singular vs. Plural Nouns**: When the source uses an indefinite singular noun to describe a general concept, Hungarian may naturally require the plural. Assess the context rather than following the source form blindly.
  - *Source:* "Adjust a file's attributes" → *Target:* "Fájlok tulajdonságainak szerkesztése"

## Date And Time

- **Date, Time, and Calendar Abbreviations**: Never use Roman numerals for months or a period as a time separator. For abbreviated time units write them with a space before the abbreviation and no trailing period: 'ó' (hour), 'p' (minute), 'mp' (second). Preferred day abbreviations are Hé, Ke, Sze, Csüt, Pé, Szo, Vas; preferred month abbreviations end with a period: jan., febr., márc., etc.
  - *Source:* "45 min to home" → *Target:* "45 p hazáig"

## Measurements

- **Measurement Units and Spacing**: Do not convert imperial measurements to metric. Always write a space between a quantity and its unit symbol, and never follow the unit with a period: '50 Hz', '12 m', '23 °C'. Exception: the percent sign (%) and degree sign (°) require no space: '99%', '45°-kal'.
  - *Source:* "50 Hz" → *Target:* "50 Hz"
  - *Source:* "0.99" → *Target:* "0.99"

## Numerals

- **Decimal and Thousand Separators**: Use a comma as the decimal separator and a non-breaking space as the thousand separator. Apply the thousand separator only when a number has five or more digits; numbers up to 9999 are written without a separator.
  - *Source:* "100,000.00" → *Target:* "100 000,00" (non-breaking space for thousands, comma for the decimal)
  - *Source:* "12.50 cm" → *Target:* "12,50 cm"

## Names And Addresses

- **Hungarian Name Order and Address Format**: Hungarian names place the family name first, matching gender carefully in context. Address formatting places the city first, followed by street address and postal code, or inline as 'postal-code city, street address'.

## Punctuation

- **Hungarian Quotation Marks**: Always use Hungarian-style curly quotation marks: lower opening „ (\u201E) and upper closing ” (\u201D). Never use straight quotes or follow English placement rules. When a full sentence appears inside quotes or parentheses, place the closing punctuation inside; when only part of a sentence is quoted, the punctuation goes outside.
  - *Source:* "\u201Cquoted text\u201D" → *Target:* "\u201Eidézett szöveg\u201D"

- **Dashes: Hyphens vs. N-Dashes**: Hungarian uses only hyphens (-) and n-dashes (–); never use m-dashes (—). Use hyphens for compound words, suffixes on abbreviations or foreign words, key combinations, and the '-e' question particle. Use n-dashes for parenthetical clauses (surrounded by spaces) and numerical ranges (without spaces). Use non-breaking hyphens inside 'Wi-Fi', 'e-mail', the '-e' question particle and for single-character suffixes on foreign proper nouns.
  - *Source:* "4–12 items can be added" → *Target:* "4–12 elem adható meg"

- **Commas in Enumerations and Conjunctions**: Omit the comma before a coordinating conjunction ('és', 'vagy', 'meg') at the end of a list. Also omit the comma before 'stb.' if the enumeration only contains words/expressions, because it already contains 'és'. But keep the comma if the elements of the enumeration are comma-separated clauses. Always place a separator between clauses. When pairing correlative conjunctions such as 'akár–akár' or 'vagy–vagy', a comma must precede the second occurrence.
  - *Source:* "Prompts for name and password, certificate, etc." → *Target:* "Név, jelszó, tanúsítvány stb. bekérése"
  - *Source:* "Add Apple Card to Wallet to make payments, track spending, and more." → *Target:* "Adjon hozzá egy Apple Cardot a Tárcához, hogy fizethessen vele, nyomon követhesse költségeit, stb."

- **Exclamation and Question Marks**: Hungarian conventions sometimes require an exclamation mark where the source omits one, or vice versa. When the source leaves out an exclamation mark but the Hungarian phrasing demands one for the same emotional weight, add it. Similarly, if a title is clearly a question in Hungarian, append a question mark even if the source title lacks one.
  - *Source:* "Why Time in Daylight Is So Important" → *Target:* "Miért olyan fontos a nappali fényben töltött idő?"

## Interface Elements

- **UI Element Grammar: Nouns, Not Imperatives**: Buttons, menu items, commands, option names, and toolbar buttons must be translated as nouns or noun phrases, never imperative verbs. Only use the imperative when the device is instructing the user to take an action in a sentence. Window titles follow sentence case — only the first letter is capitalized, not every word.
  - *Source:* "Delete" → *Target:* "Törlés"
  - *Source:* "Text Format Settings" → *Target:* "Szövegformátum beállítása"

- **Tooltips Use Noun Phrases**: Translate tooltip strings as gerundive noun phrases rather than verb sentences.
  - *Source:* "Modifies the text color" → *Target:* "Szöveg színének módosítása"

## Trademarks And Product Names

- **Do Not Translate Trademarks; Inflect by Pronunciation**: Never translate or transliterate trademarks, product names, or marketing slogans. When Hungarian suffixes must be attached to such terms, base the suffix vowel on the spoken pronunciation of the name, not its spelling.
  - *Source:* "with iPhone Pro Max" → *Target:* "iPhone Pro Maxszal" (not "iPhone Pro Maxval")

## Variables

- **Preserve Variables and Reorder When Needed**: Never alter variable placeholders such as '%@' or '%.1f' — they are replaced at runtime and any change breaks the substitution. If the Hungarian word order requires reordering multiple '%@' variables, add positional specifiers: the first '%@' becomes '%1$@', the second '%2$@', and so on. Do not change a period inside a numeric format string to a comma.
  - *Source:* "%1$@ shared %2$@" → *Target:* "%2$@-t megosztotta: %1$@"

## Diversity And Inclusion

- **Gender-Neutral Language and Disability Terminology**: Hungarian has no grammatical gender, so pronouns are not an issue, but avoid stereotyped phrases such as 'szebbik nem' or 'férfierő'. When writing about people with disabilities, use the adjective-first Hungarian convention ('látássérült ember') rather than the English people-first order. Follow the color neutrality of the source — if 'black list' is replaced by 'block list' in the source, use 'tiltólista' instead of 'feketelista'.
  - *Source:* "blind people" → *Target:* "látássérült ember"

## Terminology

- **Avoid Common Translation Errors**: Several words have established Hungarian equivalents that differ from common usage. Use these approved forms consistently and avoid the listed incorrect alternatives.
  - *Source:* "photo" → *Target:* "fotó" (not "fénykép")
  - *Source:* "link" → *Target:* "link" (not "hivatkozás")
  - *Source:* "Cancel" (iOS/macOS) → *Target:* "Mégsem" (not "Mégse")
  - *Source:* "attachment" → *Target:* "melléklet" (not "csatolmány")
