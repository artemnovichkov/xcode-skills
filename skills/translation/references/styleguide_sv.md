# Swedish (sv) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual Tone**: The overall tone should be friendly, approachable, and closer to formal than informal, but never stiff. Avoid hip or trendy vocabulary and maintain a neutral, descriptive style. Use Swedish terminology as much as possible even when English terms are common in everyday speech.
  - *Source:* "Your time of arrival is 7 PM" → *Target:* "Du kommer fram 19:00"

## Names And Addresses

- **Swedish Address Format and Approved Example Names**: Use the Swedish address format (name, street address and number, postal code and city, country). The approved name set includes 'Mats Utberg' (John Appleseed), 'Bjorn Olsberg' (John Doe), and 'Sara Engberg' (Jane Doe). 'Johnny Appleseed' is kept as-is.
  - *Source:* "John Doe" → *Target:* "Mats Utberg / Bjorn Olsberg"
  - *Source:* "Jane Doe" → *Target:* "Sara Engberg"

## Trademarks And Product Names

- **Hyphens for Inflecting Product Names**: Use a hyphen to create Swedish compound words from trademarked names for inflection or to form nouns. Where possible, avoid inflecting product names altogether by using a descriptor like 'Mac-dator' or rephrasing the sentence.
  - *Source:* "iPod settings" → *Target:* "iPod-inställningar"
  - *Source:* "the new Mac" → *Target:* "den nya Mac-datorn"

## Diversity And Inclusion

- **Inclusive Example Names Reflecting Swedish Diversity**: When example names are needed, use names that reflect Swedish society's diversity—including traditional Sami names and names common among immigrant communities (e.g., from Syria, Somalia, or Finland), not only mainstream Swedish names.
  - *Source:* "Laura opens a document" → *Target:* "Fatima öppnar ett dokument"

## Variables

- **Preserve Variables; Number Them When Reordering**: Variables must not be altered arbitrarily. When Swedish grammar requires reordering, add positional numbering to all variables. In plural strings, variables may be removed for grammatical reasons only if the remaining variables are numbered.
  - *Source:* "Your meeting is %@ the %d." → *Target:* "Mötet är den %2$d %1$@."

## General

- **Sentence length**: Avoid making sentences overly complicated and long. Long sentences in English are often better split up into at least two in Swedish.
  - *Source:* "This is the control on the Screen Time settings pane that lets you enable the screen distance setting, which reports when you do not hold your device at a safe distance." → *Target:* "Det här är reglaget på inställningspanelen för Skärmtid som gör att du kan aktivera inställningen Skärmavstånd. Den varnar dig när du inte håller enheten på ett tryggt avstånd."

- **Units**: Convert all measurement units to the metric system (kilograms, Celsius, liters, kilometers, etc.). Remove original values and units. Use contextually appropriate conversions and round down to one decimal if needed. 
  - *Source:* "Hold iPad 10 to 20 inches from your face." → *Target:* "Håll iPad mellan 25 och 50 cm från ansiktet."

- **Currency**: Convert currency values to SEK using the rates $1 USD=10 SEK and 1€=10 SEK. Use "kr" as the Swedish currency symbol. Remove the original values and units.
  - *Source:* "Subject to a service fee of $99 for screen damage or external enclosure damage." → *Target:* "En självrisk på 990 kr för skada på skärm eller yttre hölje tillkommer."

- **Forms of address**: Omit translation or transcreation of the English word "Dear" at the start of letters or messages. In very formal texts, "Bäste" may be used if the addressee is male or "Bästa" if they are female.
  - *Source:* "Dear Lisa," → *Target:* "Hej Lisa!"

- **Apps**: Software applications are called "app/appar" in Swedish, not "program" or "applikation".
  - *Source:* "All third-party apps must explain why they are requesting access to your Health app data." → *Target:* "Alla tredjepartsappar måste förklara varför de begär åtkomst till data i appen Hälsa."

- **Use of your**: For devices, do not translate the word "your".
  - *Source:* "Turn off your iPhone" → *Target:* "Stäng av iPhone"

- **List format**: In a list of items, if one or more of the items contains the word "och" or "eller", the last item in the list should be preceded by "samt" instead of "och" for clarity.
  - *Source:* "Location Data, Security and Privacy, and Settings" → *Target:* "Platsinformation, Säkerhet och integritet samt Inställningar"

- **Abbreviations**: Only use the following abbreviations: bl.a., m.m., d.v.s., o.s.v., etc., s.k., fr.o.m., t.ex., m.fl., and t.o.m. Only use the abbreviation if the Swedish phrase is a good translation of the English phrase or abbreviation.
  - *Source:* "%3$S audiobooks, including "%2$S", have been removed from the iPad "%1$S"." → *Target:* "%3$S ljudböcker, bl.a. "%2$S", har tagits bort från iPad-enheten "%1$S"."
  - *Source:* "Games, Apps, Stories, and More" → *Target:* "Spel, appar, artiklar m.m."
  - *Source:* "While not yet hypertension (i.e. high blood pressure), this range is a warning sign that blood pressure is starting to rise" → *Target:* "Även om det här intervallet ännu inte är hypertoni (d.v.s. högt blodtryck) är det en varningssignal om att blodtrycket börjar stiga"
  - *Source:* "Apple Music uses Gracenote data to display a CD's name, song titles, and so on." → *Target:* "Musik använder Gracenote-data till att visa namnet på en CD, låttitlar, o.s.v."
  - *Source:* "Example: Safari, Notes, Finder, etc…" → *Target:* "Exempel: Safari, Anteckningar, Finder etc…"
  - *Source:* "This manual is protected under the copyright law about literary and artistic creations." → *Target:* "Den här handboken är skyddad enligt lagen om upphovsrätt till litterära och konstnärliga verk, s.k. copyright."
  - *Source:* "Your order with %1$@ is arriving from %2$@." → *Target:* "Din beställning från %1$@ kommer fram fr.o.m. %2$@."
  - *Source:* "For example, you can use a text style to set the appearance of text in a `Label`:" → *Target:* "Du kan t.ex. använda en textstil som ställer in utseendet på text i `Label`:"
  - *Source:* "%@, and others." → *Target:* "%@, m.fl."
  - *Source:* "Illustrate entries with drawings or even your own handwriting." → *Target:* "Illustrera inlägg med teckningar eller t.o.m. din egen handskrift"

- **Time**: Use the 24 hour clock for time format. Use a colon as a separator. If a 12 hour clock must be used, use "fm" for "AM" and "em" for "PM". Use a leading 0 for times between 00:00 and 09:59.
  - *Source:* "7.30 PM" → *Target:* "07:30"

- **Use of Mac**: "Mac", "your Mac" and "the Mac" should be translated as "datorn".
  - *Source:* "Teach your Mac to recognize your name" → *Target:* "Lär datorn att känna igen ditt namn"

## Cultural Adaptation

- **Loan words**: Prioritize using Swedish words and expressions, however in very informal language or texts containing slang, English loan words are permitted.
  - *Source:* "Download the file" → *Target:* "Hämta filen"

- **Politeness**: Avoid translating and including "Please" or similar polite imperatives from the source text. It is rarely used or needed in Swedish.
  - *Source:* "Please activate the account in Settings" → *Target:* "Aktivera kontot i Inställningar"

- **Formality**: Always address the user with "du", "dig" or "din", never use "Ni/ni" or "Er/er" when addressing a single person. Always use lowercase for "du", "dig", "din", "ni" and "er".
  - *Source:* "Adding this accessory to Find My requires you to be signed in to your Apple Account." → *Target:* "Om du vill lägga till det här tillbehöret i Hitta måste du vara inloggad på ditt Apple‑konto."

- **Use of constructions with man**: Do not use constructions with "man".
  - *Source:* "If you want to change settings…" → *Target:* "Om du vill ändra inställningar…"

- **Gender neutrality**: Use gender-neutral language and constructs. Generally, the best practice is to try to rewrite any sentence to exclude pronouns or binary representations of gender.
  - *Source:* "Once you approve, they can add, remove, and reorder music in this playlist." → *Target:* "Efter ditt godkännande kan personen lägga till, ta bort och ändra ordningen på musiken i den här spellistan"
  - *Source:* "If %@ do not answer their phone, you can send them a message instead." → *Target:* "Om %@ inte svarar på telefon kan du istället skicka ett meddelande."

- **Use of hen**: If gender-neutral rewriting is not possible or creates constructs that deviate from the expected tone of voice, use "hen". Hen can be used both as a subject and an object. Do not use "henom" or other object forms. Never use "han/henne, han eller henne" or similar constructs.
  - *Source:* "If you remove %@ from the list of approved people, they will no longer be able to access the app." → *Target:* "Om du tar bort %@ från listan med tillåtna personer kommer hen inte längre att ha tillgång till appen."
  - *Source:* "You can send a message so the person know they have been invited." → *Target:* "Du kan skicka ett meddelande så att personen får veta att hen har bjudits in."

- **Brand names and product names**: Leave names of brands and products untranslated.
  - *Source:* "Return items to Costco" → *Target:* "Lämna tillbaka varor till Costco"

## Punctuation

- **Whitespace**: No whitespace before punctuation, but always after.
  - *Source:* "Go for it!" → *Target:* "Kör hårt!"

- **Ellipsis**: Use single character ellipsis, not three periods.
  - *Source:* "..." → *Target:* "…"

- **Hyphens**: Use hyphens (-) for hyphenation or compounding words or parts of words, e.g. when compounding foreign words.
  - *Source:* "Ethernet Cable" → *Target:* "Ethernet-kabel"

- **En-dash**: Use en-dash (–) to indicate a range of values.
  - *Source:* "The meeting time is 6-8 pm." → *Target:* "Mötet pågår 18:00–20:00."

- **Punctuation within quotes**: If a punctuation character is a part of a quote, it should be put inside the quotation mark, even if the source text places it after the quotation mark.
  - *Source:* ""This is a quote"." → *Target:* "\u201CDet här är ett citat.\u201D"

- **Punctuation within parenthesis**: A full sentence within a parenthesis should have the full stop before the right parenthesis.
  - *Source:* "(This is a complete sentence)." → *Target:* "(Det här är en fullständig mening.)"

- **Translation of acronyms**: Acronyms are usually not translated unless there is an official Swedish acronym, e.g. FN for UN. Acronyms are written without periods in Swedish.
  - *Source:* "Download today\u2019s astronomy image from NASA and save it in Camera Roll or share it." → *Target:* "Hämta dagens astronomibild från NASA och spara den i kamerarullen eller dela den."
  - *Source:* "AQI" → *Target:* "AQI"

- **Acronyms in compound words**: If an acronym is a part of a whole expression, a hyphen is used.
  - *Source:* "USB printer" → *Target:* "USB-skrivare"

- **Genitive form of acronyms**: For the genitive form of acronyms a colon is used.
  - *Source:* "EU rules" → *Target:* "EU:s regler"

- **Plural form of acronyms**: Plural of acronyms are constructed with a colon.
  - *Source:* "MP3s" → *Target:* "MP3:or"

- **Form of abbreviations**: Use periods for abbreviations, without whitespace.
  - *Source:* "Enter the router address of your network, for example, 192.128.0.0" → *Target:* "Ange nätverkets routeradress, t.ex. 192.128.0.0"

- **List format**: In a list of three or more items, do not use a comma before the final "och" or "eller".
  - *Source:* "%1$@, %2$@, and %3$ld others" → *Target:* "%1$@, %2$@ och %3$ld andra"

- **Hyphen in multipart words**: When there are more than two parts, use a hyphen in front of the last part only.
  - *Source:* "Apple HDMI to DVI Adapter" → *Target:* "Apple HDMI till DVI-adapter"
  - *Source:* "Lightning to SD Camera Card Reader" → *Target:* "Lightning till SD-kamerakortläsare"
  - *Source:* "Apple Thunderbolt to FireWire Adapter" → *Target:* "Apple Thunderbolt till FireWire-adapter"

## Orthography

- **Capitalization in headings**: Use capital letter in beginning of sentences and in proper names such as places, names, titles, etc. Do not capitalize every word in headings, even if the source text does.
  - *Source:* "Setting Up Your New Computer" → *Target:* "Ställa in den nya datorn"

- **Capitalization of common nouns**: Do not use capital letter for: days of the week, months, currencies, nationalities, languages, professions, holidays.
  - *Source:* "Create a meeting on Monday" → *Target:* "Skapa ett möte på måndag"

- **Lowercase product names**: Some product names always start with a lowercase letter. In that case, do not capitalise them even if they start a sentence.
  - *Source:* "iPhone can help during an Emergency" → *Target:* "iPhone kan hjälpa dig i en nödsituation"

- **Numbers**: Follow the source text if numerals should be written out as words or as digits. Use hard whitespace as thousand separator.
  - *Source:* "2000 Fitness+ Meditations" → *Target:* "2 000 meditationer i Fitness+"

- **Decimal separator**: Use comma as a separator for decimal numbers.
  - *Source:* "2.5 cm" → *Target:* "2,5 cm"

- **Software version numbers**: Although commas normally should be used as the separator for decimals, periods are instead used for software versions.
  - *Source:* "version 2.5" → *Target:* "version 2.5"

- **Unit symbols**: All symbols are considered a word and should be preceded by a hard whitespace.
  - *Source:* "50%" → *Target:* "50 %"

- **Time format**: Use the 24 hour clock for time format. Use a colon as a separator. If a 12 hour clock must be used, use "fm" for "AM" and "em" for "PM". Use an initial 0 for single digits.
  - *Source:* "4:00 am" → *Target:* "04:00"

- **Date format**: Use the Swedish standard date format, YYYY-MM-DD.
  - *Source:* "7/13/2025" → *Target:* "2025-07-13"

- **Quotation marks**: Use double curly quote marks “ (\u201C) and ” (\u201D) on both sides of a quoted word or sentence.
  - *Source:* "%#@count@ matching \u2019${account}\u2019." → *Target:* "%#@count@ matchar \u201C${account}\u201D."

- **Ampersand character**: Use the word "och" instead of the character &.
  - *Source:* "Privacy & Security" → *Target:* "Integritet och säkerhet"

- **Multiplication sign**: For sizes, the × character should be used between two numbers even if the source text writes an x. There should be a space before and after the × character.
  - *Source:* "38x45 cm" → *Target:* "38 × 45 cm"
