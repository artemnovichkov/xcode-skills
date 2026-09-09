# Finnish (fi) — Software String Localization Style Guide

## Tone And Voice

- **Smart-Casual, Reader-Centered Tone**: The general tone for Finnish Apple content is 'smart but casual' — closer to formal than informal, but never stiff or trendy. The translation must read as natural Finnish and never feel like a translated text. Avoid jargon and overly colloquial language; prefer neutral, descriptive phrasing.
  - *Source:* "Start by typing a search term or web address in the Smart Search field - it knows the difference and will send you to the right place." → *Target:* "Kirjoita ensin hakusana tai verkko-osoite älykkääseen hakukenttään. Se tunnistaa eron ja lähettää sinut oikeaan paikkaan."

## Grammar

- **Use Active and Passive Structures for Variety; Never Use 1st Person for System Actions**: Alternate between active and passive sentence structures to create natural variation. For progress notifications and inanimate system actions, always use the impersonal passive — never translate as if the device is speaking in the first person.
  - *Source:* "Loading library…" → *Target:* "Ladataan kirjastoa… (not Lataan kirjastoa…)"

- **Simplify 'Are You Sure' Confirmation Strings**: Translate 'Are you sure you want to…' constructions into a direct, shorter Finnish form using the passive or a plain question. This sounds more natural and is considerably shorter. Use the English-modeled form only for second-level confirmation dialogs.
  - *Source:* "Are you sure you want to end navigation?" → *Target:* "Lopetetaanko navigointi?"

- **Finnish Word Order: Subject–Verb–Object**: Follow Finnish SVO word order. Avoid translating English 'do X using Y' constructions literally — use an instrumental case instead, which is the natural Finnish structure.
  - *Source:* "Browse the list using the arrow keys." → *Target:* "Selaa luetteloa nuolinäppäimillä. (not Selaa luetteloa käyttämällä nuolinäppäimiä.)"

- **Avoid Non-Finite Clauses Except for Very Short Phrases**: Prefer subordinate clauses over non-finite clause constructions (lauseenvastike) as they are clearer and easier to read. Use non-finite forms only for very short (1–2 word) subordinate equivalents where they are idiomatic.
  - *Source:* "Unlock after startup so you can use the device." → *Target:* "Avaa lukitus käynnistyksen jälkeen, jotta voit käyttää laitetta."
  - *Source:* "if needed" → *Target:* "tarvittaessa (non-finite short form is fine here)"

## Punctuation

- **No Full Stops in Finnish Titles**: Finnish does not use a full stop at the end of titles and headings, even when the English source does. Always remove trailing periods from translated titles.
  - *Source:* "Downloading Apps to Your Mac." → *Target:* "Appien lataaminen Maciin"

- **Comma Rules for Conjunctions and Subordinate Clauses**: Finnish requires commas before co-ordinate conjunctions between independent clauses, before relative clauses, before reported clauses, and before subordinate conjunction clauses. These are the most common translation errors — review Finnish comma rules regularly.
  - *Source:* "Check if there is space on the disk." → *Target:* "Tarkista, onko levyllä tilaa."

- **Whitespace**: No whitespace before punctuation.
  - *Source:* "Go for it!" → *Target:* "Anna palaa!"

- **Ellipsis**: Use single character ellipsis, not three periods.
  - *Source:* "..." → *Target:* "…"

- **Hyphens**: Use hyphens (-) for hyphenation or compounding words or parts of words, e.g. when compounding foreign words.
  - *Source:* "Ethernet Cable" → *Target:* "Ethernet-kaapeli"

- **En-dash for ranges**: Use en-dash (–) to indicate a range of values.
  - *Source:* "The meeting time is 6-8 pm." → *Target:* "Kokous järjestetään klo 18.00–20.00."

- **En-dash replacing em-dash**: Replace the em-dashes in the source as en-dashes in the target, making sure it is preceded and followed by a whitespace.
  - *Source:* "This option is available only if the document uses the same color space as the printer—for example, when printing an RGB document on an RGB printer." → *Target:* "Tämä vaihtoehto on käytettävissä vain, jos dokumentti käyttää samaa väriavaruutta kuin tulostin – esimerkiksi, jos tulostat RGB-dokumentin RGB-tulostimella."

- **Punctuation within quotes**: If a punctuation character is a part of a quote, it should be put inside the quotation mark, even if the source text places it after the quotation mark.
  - *Source:* "\u201CThis is a quote\u201D." → *Target:* "\u201CTämä on lainaus.\u201D"

- **Punctuation within parenthesis**: A full sentence within a parenthesis should have the full stop before the right parenthesis.
  - *Source:* "(This is a complete sentence)." → *Target:* "(Tämä on kokonainen lause.)"

- **Acronyms in compound words**: If an acronym is a part of a compound, a hyphen is used.
  - *Source:* "USB printer" → *Target:* "USB-tulostin"

- **List format**: In a list of three or more items, do not use a comma before the final "and" or "tai".
  - *Source:* "%1$@, %2$@, and %3$ld others" → *Target:* "%1$@, %2$@ ja %3$ld muuta"

- **Minus sign**: Use en dash as the minus sign.
  - *Source:* "The value is -10" → *Target:* "The value is –10"

## Abbreviations

- **Avoid Abbreviations in Software; Use Full Words**: Do not abbreviate words in software translations unless every other option has been exhausted. Instead of abbreviating, try rewording to make the string shorter. In general, prefer full words over abbreviations.
  - *Source:* "Restart (too long)" → *Target:* "If 'Käynnistä uudelleen' does not fit, remove 'uudelleen': 'Käynnistä'"

## Trademarks And Product Names

- **Inflect Apple Product Names Using Written Vowel Harmony**: Apply Finnish vowel harmony based on how the product name is written, not how it is pronounced. Inflect directly without a colon for names pronounced as words.
  - *Source:* "from GarageBand" → *Target:* "GarageBandista"
  - *Source:* "with AirPlay" → *Target:* "AirPlaylla"

- **Drop 'Apple' from App Names When Referring to the App, Keep It for Services**: When 'Apple Music', 'Apple Health', 'Apple Podcasts', etc. refer to the app, drop 'Apple' and use only the Finnish app name (Musiikki, Terveys, Podcastit, Sää). When referring to the service, keep the full English name.
  - *Source:* "Open Apple Music to start listening." → *Target:* "Avaa Musiikki ja aloita kuuntelu."
  - *Source:* "Subscribe to Apple Music." → *Target:* "Tilaa Apple Music."

## Interface Elements

- **Commands Use Imperative; Menu Names Prefer Verb Form; Titles Use Nouns**: Menu command items must use the 2nd person singular imperative (Lataa, Avaa, Sulje). Menu names prefer verb forms (Näytä, Lisää) though nouns are also used. Window and dialog titles sound better with nouns. Keyboard key names are written in lowercase as compound words.
  - *Source:* "File (menu name)" → *Target:* "Arkisto"
  - *Source:* "Download (command)" → *Target:* "Lataa"
  - *Source:* "esc and control keys" → *Target:* "esc- ja control-näppäimet"

## Date And Time

- **Follow Finnish System Standard for Date and Time Formats**: Use the Finnish system standard for date and time as shown in System Settings. Duration is formatted with a full stop as separator (e.g. 0.15.25,05 for 0 hours, 15 minutes, 25 seconds, and 5 hundredths).
  - *Source:* "0:15:25.05" → *Target:* "0.15.25,05"

## Measurements

- **Do Not Convert Measurements; Use Number + Space + Unit**: Do not convert imperial measurements to metric. Always format measurements as number + space + unit. The degree sign is written without a space when used alone (10°) but with a space when combined with a scale letter (+20 °C).
  - *Source:* "27-inch iMac" → *Target:* "27 tuuman iMac"
  - *Source:* "+20°C" → *Target:* "+20 °C"
  - *Source:* "5°" → *Target:* "5°"

## Names And Addresses

- **Use Finnish Placeholder Names and Address Format**: Replace English placeholder names with locally-appropriate Finnish names; keep John Appleseed in English as an exception. Use Finnish postal address conventions for sample addresses. Example format: `Kauppakatu 5 C 24, 99999 Jokukylä`.

## Variables

- **Keep Variables Intact; Use Nominative or Dummy Objects for Unknown Variables**: Preserve all variables exactly as they appear in the source. If the grammatical case of a variable's referent is unknown, translate so that the variable stands in nominative. Use a dummy object such as 'kohde' as a fallback, or reorder variables using positional notation (1$, 2$, etc.).
  - *Source:* "%@ cannot be downloaded." → *Target:* "%@ ei ole ladattavissa."
  - *Source:* "%@ Ratings for Version %@" → *Target:* "Versiolla %2$@ on %1$@ arviota."

## General

- **Currency**: Place currency symbols after the number, separated by whitespace.
  - *Source:* "USD 00,000.00" → *Target:* "00.000,00 USD"

- **Forms of address**: When English uses the word "Dear" at the start of letters or messages, use "Hei" instead. In very formal texts, "Hyvä" may be used. Omit the comma in the end of salutations.
  - *Source:* "Dear Lisa," → *Target:* "Hei Liisa"

- **Apps**: Software applications are called "appi" (inflects like nappi) in Finnish, not "sovellus", "ohjelma" or "applikaatio".
  - *Source:* "All third-party apps must explain why they are requesting access to your Health app data." → *Target:* "Kaikkien muiden valmistajien appien on kerrottava, miksi ne pyytävät Terveys-apin tietojen käyttöoikeutta."

- **Use of your**: For devices, do not translate the word "your".
  - *Source:* "Turn off your iPhone" → *Target:* "Sammuta iPhone"

- **List format**: In a list of items, if one or more of the items contains the word "and", the last item in the list should be preceded by "sekä" instead of "ja".
  - *Source:* "Location Data, Security and Privacy, and Settings" → *Target:* "Sijaintitiedot, Tietosuoja ja suojaus sekä Asetukset"

- **Time**: Use the 24 hour clock for time format. Use a full stop as a separator. If a 12 hour clock must be used, use "ap." for "AM" and "ip." for "PM".
  - *Source:* "7:30 pm" → *Target:* "19.30"

- **Choice of word - generate**: To clarify and maintain distinction between "create", "generate" and "produce", translate the verb "generate" with the verb "generoida".
  - *Source:* "The generated files may contain some of your personal information" → *Target:* "Generoidut tiedostot voivat sisältää henkilökohtaisia tietojasi,"

- **Choice of word - create**: Translate the verb "create" with the verb "luoda".
  - *Source:* "Turn on Apple Intelligence to create images in Genmoji." → *Target:* "Laita Apple Intelligence päälle, jotta voit luoda kuvia Genmojeissa."

- **Choice of word - produce**: Translate the verb "produce" with the verb "tuottaa".
  - *Source:* "Sunlight also helps the body produce Vitamin D" → *Target:* "Auringonvalo auttaa myös kehoa tuottamaan D-vitamiinia"

- **Conditional mood**: Do not use conditional mood in your translation when English uses it. Use indicative mood instead.
  - *Source:* "Would you like to respond?" → *Target:* "Haluatko vastata?"

- **Translation of for**: In cases where "for" acts as a possessive in English, it should not be translated in allative case, but as genitive.
  - *Source:* "Open the Reset Privacy Identifier setting for Stocks." → *Target:* "Avaa Pörssi-apin Nollaa tietosuojatunniste -asetus."

## Cultural Adaptation

- **Loan words**: Prioritize using Finnish words and expressions.
  - *Source:* "Clear Project Render Cache?" → *Target:* "Tyhjennetäänkö projektin mallinnusvälimuisti?"

- **Politeness**: Avoid translating and including "Please" or similar polite imperatives from the source text. It is rarely used or needed in Finnish.
  - *Source:* "Please activate the account in Settings" → *Target:* "Aktivoi tili Asetuksissa"

- **Formality**: Always address the user with "sinä" (+inflections).
  - *Source:* "Adding this accessory to Find My requires you to be signed in to your Apple Account." → *Target:* "Sinun on oltava kirjautuneena Apple-tilille, jos haluat lisätä tämän lisälaitteen Etsi-appiin."

- **Use of agent structures**: Do not translate "xxx was performed/done by yyy" using the agent structure "toimesta".
  - *Source:* "The live video and uploaded media are sent end-to-end encrypted and cannot be viewed or accessed by Apple." → *Target:* "Livevideo ja lähetetty media lähetetään päästä päähän salatussa muodossa eikä Apple voi tarkastella eikä käyttää niitä."

- **Gender neutrality**: Use gender-neutral terms e.g. for professions.
  - *Source:* "Firefighter" → *Target:* "Pelastaja"
  - *Source:* "Lawyer" → *Target:* "Juristi"

- **Place names**: Use Finnish names for places and locations. When there are no commonly used Finnish translations, leave names of places untranslated.
  - *Source:* "Stockholm" → *Target:* "Tukholma"

- **Brand names and product names**: Leave names of brands and products untranslated.
  - *Source:* "Return items to Costco" → *Target:* "Palauta tuotteet Costcoon"

- **Translation of acronyms**: Acronyms are usually not translated unless there is an official Finnish acronym, e.g. YK for UN.
  - *Source:* "Air Quality Index (AQI)" → *Target:* "Ilmanlaatuindeksi (AQI)"

## Orthography

- **Capitalization in headings**: Do not capitalize every word in headings, titles, feature names or setting names, even if the source text does.
  - *Source:* "Track a Workout with Heart Rate" → *Target:* "Seuraa treeniä ja sykettä"

- **Capitalization of common nouns**: Do not use capital letter within sentences for: days of the week, months, currencies, nationalities, languages, professions, holidays.
  - *Source:* "Create a meeting on Monday" → *Target:* "Luo tapaaminen maanantaille"

- **Lowercase product names**: If a product name starts with a lowercase letter, do not capitalise them even if they start a sentence.
  - *Source:* "iPhone can help during an Emergency" → *Target:* "iPhone voi auttaa hätätilanteessa"

- **Numbers**: Follow the source text if numerals should be written out as words or as digits.
  - *Source:* "You hit all three of your goals and the day is still young." → *Target:* "Saavutit kaikki kolme tavoitettasi, ja päivä on vielä nuori."

- **Thousand separator**: Use hard whitespace as thousand separator.
  - *Source:* "2000 Meditations" → *Target:* "2 000 meditointia"

- **Decimal separator**: Use comma as a separator for decimal numbers.
  - *Source:* "2.5 cm" → *Target:* "2,5 cm"

- **Software version numbers**: Although commas normally should be used as the separator for decimals, periods are instead used for software versions.
  - *Source:* "version 2.5" → *Target:* "versio 2.5"

- **Unit symbols**: All symbols should be preceded by a hard whitespace.
  - *Source:* "50%" → *Target:* "50 %"

- **Date format**: Use the Finnish standard date format, d.M.yyyy.
  - *Source:* "7/13/2025" → *Target:* "13.7.2025"

- **Quotation marks**: Use double curly quote marks “ (\u201C) and ” (\u201D) on both sides of a quoted word or sentence.
  - *Source:* "%@ matching \u2019${account}\u2019." → *Target:* "%@ vastaa tiliä \u201C${account}\u201D."

- **Ampersand character**: Use the word "ja" instead of the character &.
  - *Source:* "Privacy & Security" → *Target:* "Tietosuoja ja suojaus"

- **Multiplication sign**: For sizes, the × character should be used between two numbers even if the source text writes an x. There should be a space before and after the × character.
  - *Source:* "38x45 cm" → *Target:* "38 × 45 cm"

- **Inflected forms of acronyms**: Where the acronyms are pronounced letter by letter, a colon is used for inflected forms. The case ending is determined by the last letter.
  - *Source:* "Use USB Only" → *Target:* "Käytä vain USB:tä"
