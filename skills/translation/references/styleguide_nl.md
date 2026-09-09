# Dutch (nl) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Dutch UI references use single straight quotes ' ' (not curly quotes), so the only curly glyph to escape inside a string value is the curly apostrophe ’ (\u2019) — which Dutch produces when pluralizing vowel-final loanwords (the example below turns "videos" into "video\u2019s"), and which also appears in English source strings via typographic tooling.
  - *Source:* "one place for your saved videos" → *Target:* "Eén plek voor je bewaarde video\u2019s."

## Tone And Voice

- **Informal but Polished Tone**: Dutch translations use the informal 'je' throughout. The tone is smart and casual, never stiff or overly trendy. Prefer Dutch terminology over English equivalents even when users colloquially use English words.
  - *Source:* "just print the file" → *Target:* "even het bestand afdrukken"

## Addressing Users

- **Use 'je', Not 'u'**: Always use 'je' as the second-person form of address, never 'u'. This applies uniformly across all content types. Use gender-neutral references for objects ('deze'/'die') and persons ('deze persoon' or plural forms) to be inclusive.
  - *Source:* "You" → *Target:* "je"
  - *Source:* "his/her/their account" → *Target:* "de account van deze persoon"

## Abbreviations

- **Write Out Common Expressions in Full**: Do not abbreviate expressions such as 'met betrekking tot' (m.b.t.) or 'enzovoort' (enz.). Avoid all abbreviations in software unless the string truly cannot fit any other way.
  - *Source:* "Was this photo taken at a celebration (graduation, ceremony, etc.)?" → *Target:* "Is deze foto op een feest (afstuderen, ceremonie, enzovoort) gemaakt?"

## Acronyms

- **Acronyms Are Written Without Periods**: Dutch 'initiaalwoorden' (e.g. pc, cd) and 'letterwoorden' (e.g. pin, RAM) are written without internal periods. Follow the capitalization of the source acronym. Do not translate acronyms unless a well-established Dutch equivalent exists.
  - *Source:* "PC" → *Target:* "pc"
  - *Source:* "RAM" → *Target:* "RAM"

## Date And Time

- **Time Abbreviations Use a Full Stop**: When abbreviating time units in running text, add a full stop after 'min.' and 'sec.' In software strings with space constraints or all-caps display, the full stop may be omitted. Follow the target locale's date and time conventions.
  - *Source:* "5 s / 2 min" → *Target:* "5 sec. / 2 min." (in running text)

## Measurements

- **Do Not Convert Measurements; Space Between Value and Unit**: Do not convert imperial measurements. Always insert a space between the numeric value and the unit of measurement. When the number and unit form an adjective compound, join them with a hyphen.
  - *Source:* "2 MB" → *Target:* "2 MB"
  - *Source:* "2.5 GHz 6-core processor" → *Target:* "2,5-GHz 6-core-processor" (adjective compound → hyphen)

## Addresses

- **Use Dutch Address Format**: Dutch postal addresses follow the format: street + number, then postal code (4 digits, space, 2 capitalized letters) followed by two spaces and the city name in capitals (e.g. Grote Kerkplein 15, 8011 PK  ZWOLLE).

## Numerals

- **Digits for References; 0,5 Takes Singular**: Use numeric form for references to chapters, rules, and similar. Follow the source when it uses digits, even for numbers below 20. After '0,5', use the singular form of the following noun where possible. Ordinal numbers are written as digit + 'e' (e.g. 4e, 15e).
  - *Source:* "chapter 3" → *Target:* "hoofdstuk 3"
  - *Source:* "0.5 hours" → *Target:* "0,5 uur"

## Punctuation

- **Single Straight Quotes for UI References**: Use single straight quotes around command names, UI option names, file names, and direct UI path references in UI strings. Do not use quotes around application names or service names (except multi-word service names in running text for readability).
  - *Source:* "Go to Settings > General" → *Target:* "Ga in Instellingen naar 'Algemeen'"
  - *Source:* "Choose Print from the File menu" → *Target:* "Kies 'Druk af' uit het Archief-menu"

- **Avoid Semicolons and Exclamation Marks**: Dutch style avoids semicolons—split the sentence into two instead. Exclamation marks should also be avoided. Use a full stop at the end of the last sentence in a paragraph even when the source omits it.

- **Dutch Dash Is an En Dash**: The Dutch 'gedachtestreepje' is an en dash (–), not a hyphen or em dash. It can often be replaced by a comma or parentheses. Use sparingly to avoid cluttered text.

## Special Characters

- **Diacritical Marks and 'één'**: Dutch uses acute, grave, and umlaut accents, including on uppercase letters. The word 'één' (one) is an exception: when it begins a sentence, the capital E does not take an accent. Do not use accents on 'een' in 'een of meer' and 'een van de'. The umlaut is replaced by a hyphen when it falls between parts that can stand as separate words.
  - *Source:* "One place for your saved videos." → *Target:* "Eén plek voor je bewaarde video\u2019s." (sentence-initial één → Eén: capital E unaccented, é keeps its accent)
  - *Source:* "zee-egel / zo-even" → *Target:* "zee-egel / zo-even" (hyphen instead of umlaut)

## Trademarks And Product Names

- **Do Not Translate or Transliterate Trademarks**: Trademarks, slogans, company names, and product names must not be translated or transliterated. Use a non-breaking space between the parts of multi-word product names like 'App Store' or 'Apple Vision Pro'. Never use a hyphen in combinations with Apple, except for 'Apple-menu' and 'Apple-symbool'.
  - *Source:* "App Store" → *Target:* "App Store" (non-breaking space)

## Grammar

- **Capitalization: Only First Word of Headers and Feature Names**: Dutch capitalizes far less than English. In headers, feature names, and UI labels, only the first word takes a capital. Do not capitalize every content word as English does.
  - *Source:* "System Preferences" → *Target:* "Systeemvoorkeuren"
  - *Source:* "Dark Mode" → *Target:* "Donkere modus"

- **Use Present Perfect Instead of Past Tense**: Where English uses simple past tense, Dutch typically uses the present perfect (voltooid tegenwoordige tijd). When 'could not' appears in English, follow it with a past-tense equivalent in Dutch rather than the present tense.
  - *Source:* "You earned this award for your first hiking workout." → *Target:* "Je hebt deze medaille verdiend voor de eerste wandeltocht."
  - *Source:* "The message could not be retrieved." → *Target:* "Het bericht kon niet worden opgehaald."

- **Avoid Future Tense; Prefer Present**: Dutch prefers the present tense where English uses future constructions. Avoid 'zullen'. Use 'voortaan', 'dan', or a form of 'gaan' to express a genuine future or 'from now on' meaning.
  - *Source:* "Your future Daily Cash earnings will be directed to your Savings account." → *Target:* "Wat je verdient aan Daily Cash gaat voortaan rechtstreeks naar je spaarrekening."

- **Past Participle Follows Auxiliary Verb**: In Dutch, the past participle must come after the auxiliary verb, not before it.
  - *Source:* "Als het bestand afgedrukt wordt" → *Target:* "Als het bestand wordt afgedrukt"
  - *Source:* "Nadat je het document geopend hebt" → *Target:* "Nadat je het document hebt geopend"

- **Use Compounds Not Spaces for English Loan Words**: English compounds that are two separate words are usually written as one word or hyphenated in Dutch. For combinations with 'online', 'offline', and 'live', use a space only if the compound is not established as a single word.
  - *Source:* "software update" → *Target:* "software-update"
  - *Source:* "desktop computer" → *Target:* "desktopcomputer"
  - *Source:* "live captions" → *Target:* "live bijschriften"

## Interface Elements

- **Buttons and Commands Use Imperative Form**: Button names, command names, and option names are always translated in the imperative form, not the infinitive. Menu names use a mix of imperative and nouns, never the infinitive. Window titles follow the imperative convention. Undo/Redo are followed by the action in single quotes.
  - *Source:* "Print" → *Target:* "Druk af" (not 'Afdrukken')
  - *Source:* "Undo Delete Message" → *Target:* "Herstel 'Verwijder bericht'"

## Diversity And Inclusion

- **Gender-Neutral References**: Do not use 'hun' as a singular pronoun for a gender-unknown person. Restructure the sentence using singular nouns/verbs, rewrite in plural, or omit the pronoun. Use 'deze' or 'persoon' when a neutral reference is necessary. 'Zij/hun/hen' for a single person is not officially accepted in Dutch grammar.
  - *Source:* "As an essential worker, they should talk to their work about…" → *Target:* "Als deze persoon een cruciaal beroep heeft, moet er met de werkgever worden overlegd…"

## Variables

- **Variables May Be Renumbered for Word Order**: Never alter variable tokens. You may reorder variables for natural Dutch word order and must renumber unnumbered variables (e.g. %@ %@) using positional syntax (%1$@, %2$@) if their order changes. Quotes around variables should be converted to single straight quotes.
  - *Source:* "Are you sure you want to remove the "%@" %@ account?" → *Target:* "Weet je zeker dat je de %2$@-account '%1$@' wilt verwijderen?"

## General Advice

- **Translate 'not…until' as 'pas…nadat'**: When English uses 'not…until', Dutch naturally uses 'pas…nadat' rather than a literal rendering with 'totdat'. This produces more idiomatic Dutch.
  - *Source:* "New messages not automatically received until relaunching Mail" → *Target:* "Nieuwe berichten worden pas automatisch ontvangen nadat Mail opnieuw is opgestart"

- **Avoid Repetition: Vary Word Choice**: When the same English word appears more than once in a string, find a different Dutch equivalent for one instance to improve readability. Similarly, restructure sentences that would sound unnatural when translated literally.
  - *Source:* "Add a debit or credit card to add more payment methods." → *Target:* "Voeg een betaalkaart of creditcard toe om meer betalingsmethoden te bieden." (second 'add' becomes 'bieden')

## Spaces

- **Do not use double spaces between sentences**: Use one space between sentences. Use a non-breaking space to keep fixed combinations together, for example iPhone 16, Apple Vision Pro, watchOS 12.

## Diminutives

- **Do not use diminutives**: Dutch uses many diminutives (the "-tje" form), but avoid them in translations — they make UI text read as overly informal. Use a diminutive only when it is the standard or only accepted form of a word, not to soften tone: for example, "apenstaartje" (the @ symbol) is the usual term, and "mondkapje" (face mask) occurs only in the diminutive form.

## Hyphens

- **Do not use a hyphen after a plus sign**: Avoid a hyphen after the plus symbol (+); reword so the plus sign isn't followed by a hyphenated suffix (use a prepositional phrase instead of a compound).
  - *Source:* "Apple Fitness+ subscription" → *Target:* "Abonnement op Apple Fitness+" (not "Apple Fitness+-abonnement")
