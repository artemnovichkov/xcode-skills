# Catalan (ca) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Catalan uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting and the curly apostrophe ’ (\u2019) for elision and possessives.

## Tone And Voice

- **Natural and Concise Style**: Translations should read naturally in Catalan, not like word-for-word renderings of English. Keep sentences short, grammatically simple, and avoid unnecessary connectors or filler words — especially in instructional content.
  - *Source:* "Press the Home button twice and then tap an app to open it." → *Target:* "Prem dues vegades el botó d\u2019inici i toca una app per obrir-la."

## Special Characters

- **Use Single Ellipsis Character**: Always use the single ellipsis glyph (…) rather than three consecutive periods. This ensures correct rendering, proper spacing between dots, and accurate screen-reader narration.
  - *Source:* "Loading..." → *Target:* "Carregant…"

## Abbreviations

- **Spell Out Abbreviations Where Space Allows**: Catalan uses abbreviations far less frequently than English. Spell out fully whenever space is not a constraint. When abbreviating is unavoidable, use only well-known Catalan abbreviations that end with a period and are cut after a consonant.
  - *Source:* "e.g." → *Target:* "p. ex."

## Acronyms

- **Keep Acronyms in English Form**: Do not translate acronyms unless a widely recognised Catalan equivalent exists. Acronyms are written without periods, spaces, or plural endings.
  - *Source:* "USB, RAM, HTML" → *Target:* "USB, RAM, HTML"

## Date And Time

- **Date Format DD/MM/YYYY and 24-Hour Clock**: Catalan dates follow the day/month/year order using a slash separator. Use the 24-hour clock for time. Omit leading zeros from day and month. Write 'a. m.' and 'p. m.' only when the US format must be preserved.
  - *Source:* "01/03/2012, 4:30 PM" → *Target:* "3/1/2012, 16:30"

## Numerals

- **Ordinal Number Abbreviations**: Abbreviate ordinals by appending the last letter of the full word to the numeral (e.g. 1r, 2a, 10è). For plurals, append the last two letters (e.g. 1rs, 2es). Never use superscripted ordinal indicators (ª, º).
  - *Source:* "1st, 2nd, 10th" → *Target:* "1r, 2a, 10è"

## Addresses

- **Catalan Address Format**: When localizing postal addresses, follow Catalan conventions: translate generic street types ("Main Street" → "Carrer Major", "Avenue" → "Avinguda") and use Catalan order (street name and number, then postal code and locality, then province). Do not leave English sample data in production strings. Example format: `Carrer Major, 123, Localitat, CP Província`.

## Interface Elements

- **Undo Strings Must Be Lowercase Noun Phrases**: Undo action strings are inserted as direct objects into the runtime string "Desfés %@". Translate them as lowercase noun phrases so the combined string reads naturally. Never use an imperative form for undo strings.
  - *Source:* "Adjust Saturation" → *Target:* "l\u2019ajustament de la saturació"

## Trademarks And Product Names

- **Do Not Translate Trademarked Names**: Apple product names, trademarked slogans, and font names must not be translated. Descriptive feature names may be translated as lowercase common nouns with an article.
  - *Source:* "Game Center, Spotlight" → *Target:* "Game Center, Spotlight"
  - *Source:* "Notification Center" → *Target:* "el centre de notificacions"

## Variables

- **Preserve Variables and Use Positional Indices When Reordering**: All source variables must appear in the translation. If Catalan word order requires variables in a different sequence, add positional indices (e.g. %1$@, %2$@) to every variable in the string — including when variable types differ. Never modify the characters inside a variable format specifier.
  - *Source:* "%@\u2019s %@" → *Target:* "%2$@ de %1$@"
  - *Source:* "Page %1$@ of %2$@" → *Target:* "Pàgina %1$@ de %2$@"

## General Advice

- **Use Context Clues to Resolve Ambiguous Short Strings**: Short strings often have multiple valid translations. Before committing to a translation, examine the string ID, surrounding strings, and file name for context clues about the string's function, expected length, and grammatical role.
  - *Source:* "All" → *Target:* "Tot / Tota / Tots / Totes" (depending on context)
  - *Source:* "Right" → *Target:* "Dreta" (position) or "Correcte" (adjective)

- **Articles**: Apps, devices, online services, operating systems update names, and utility names use articles. Some app names may sound unnatural when the number of the article doesn't match the application name, therefore a descriptor word "app" should be used.
  - *Source:* "You can manage parental controls in Screen Time settings on your iPhone." → *Target:* "Pots gestionar els controls parentals a la configuració del temps d\u2019ús de l\u2019iPhone."
  - *Source:* "Welcome to Photos" → *Target:* "Et donem la benvinguda a l\u2019app Fotos."

- **Descriptive style**: App names for "Settings" and "System Settings" should be used descriptively in lowercase and no descriptor. This criterion does not apply when mentioning a path with ">".
  - *Source:* "Turn on two-factor authentication in System Settings." → *Target:* "Activa l\u2019autenticació de doble factor a la configuració del sistema."
  - *Source:* "Open Settings to the Stocks app pane." → *Target:* "Obre la configuració de l\u2019app Borsa."

- **Translation of for**: In cases where "for" acts as a possessive in English, it should not be translated as "per a" in Catalan but as "de". To avoid grammar problems with variables, add a descriptor word when possible.
  - *Source:* "Enter the password for \u201C%@\u201D." → *Target:* "Introdueix la contrasenya del compte %@."
  - *Source:* "Signing out of the last Apple Account for this profile will remove the profile entirely." → *Target:* "Si tanques la sessió de l\u2019últim compte d\u2019Apple del perfil, s\u2019eliminarà el perfil per complet."

- **Possessives**: English possessives are frequently avoided in Catalan translations. Instead, the article is preferred. Only use possessives when they are really needed to avoid confusion.
  - *Source:* "Turn off your computer." → *Target:* "Apaga l\u2019ordinador."
  - *Source:* "Your Apple Account can only be used from devices you approve." → *Target:* "Només pots utilitzar el compte d\u2019Apple als dispositius que hagis aprovat."

- **Form of address**: The informal form "tu" is used to address the user in all software.
  - *Source:* "Enjoy photos with a delightful 3D effect while you move your iPhone in your hand." → *Target:* "Gaudeix de les fotos amb un efecte 3D espectacular tan sols en moure una mica l\u2019iPhone."
  - *Source:* "Delete all downloaded languages from your device?" → *Target:* "Vols eliminar del dispositiu tots els idiomes descarregats?"

- **Passive voice**: In Catalan, the passive voice is not used as often as in English. Instead, use the active voice or a reflexive passive with "es".
  - *Source:* "This font file is required by macOS to display onscreen text. It has been restored." → *Target:* "El macOS necessita aquest arxiu de tipus de lletra per mostrar text a la pantalla. S\u2019ha restaurat l\u2019arxiu."
  - *Source:* "Failed to download file." → *Target:* "No s\u2019ha pogut descarregar l\u2019arxiu."

- **Gerunds**: Do not translate English gerunds as Catalan gerunds when these represent a nominal form and not a continuous action.
  - *Source:* "Sending information to Apple" → *Target:* "Enviament de la informació a Apple"
  - *Source:* "Measuring Your Heart Rate" → *Target:* "Mesurament de la freqüència cardíaca"
  - *Source:* "Deleting Text" → *Target:* "Eliminació de text"

- **Repetitions**: English source text often repeats the same noun or subject across adjacent sentences. Merge these into a single fluent Catalan sentence using pronouns, semicolons, or coordinated clauses to avoid awkward redundancy.
  - *Source:* "If you didn't get a code, you can send another code to another device signed in with your Apple Account." → *Target:* "Si no has rebut cap codi, pots enviar‑ne un de nou a un altre dispositiu en què hagis iniciat la sessió amb el compte d\u2019Apple."

- **Plural forms**: Following ésAdir's recommendations, device types are pluralized: iPhones, iPads, Macs, HomePods, AirTags, AirPods.
  - *Source:* "iPad batteries, like all rechargeable batteries, have a limited lifespan." → *Target:* "Les bateries dels iPads, com totes les bateries recarregables, tenen una vida útil limitada."
  - *Source:* "To add this item, remove one or more AirTags or AirPods currently paired to your Apple Account." → *Target:* "Per afegir l\u2019objecte, elimina un o diversos dels AirTags o AirPods que tinguis enllaçats al compte d\u2019Apple."

- **Time**: Use the 24 hour clock for time format. Use a colon as a separator. If a 12 hour clock must be used, use "a. m." for "AM" and "p. m." for "PM".
  - *Source:* "7:30 PM" → *Target:* "19:30"

## Software Forms

- **Actions and commands**: The verbal tense used for actions, commands, buttons, CTAs and other related software actions is the imperative.
  - *Source:* "Select a Network" → *Target:* "Selecciona una xarxa"
  - *Source:* "Don't Allow" → *Target:* "No permetis"
  - *Source:* "Continue and Show IP Address" → *Target:* "Continua i mostra l\u2019adreça IP"

- **Titles**: Use nominal forms for succinct titles. If the title needs to use a conjugated verbal form, then add a period.
  - *Source:* "Failed to Add the Message" → *Target:* "Error en afegir el missatge"
  - *Source:* "Memory Creation is Unavailable" → *Target:* "Creació de records no disponible"
  - *Source:* "Review Activity History" → *Target:* "Revisió de l\u2019historial d\u2019activitat"

- **Descriptions and explanations**: Translate full-sentence descriptions and explanations with the imperative form.
  - *Source:* "Personalize Mac with new looks for app icons." → *Target:* "Personalitza el Mac amb estils nous per a les icones de les apps."
  - *Source:* "Opens Braille Access and allows Braille input using a keyboard." → *Target:* "Obre l\u2019accés amb la pantalla Braille i permet l\u2019entrada Braille amb el teclat."

- **Tooltips and accessibility hints**: Tooltips and accessibility hints are instructions in message form and are to be translated in a descriptive, declarative way with an imperative and a closing period.
  - *Source:* "Tap to add suggestion" → *Target:* "Fes un toc per afegir el suggeriment."
  - *Source:* "Activate to begin download" → *Target:* "Activa aquesta opció per iniciar la descàrrega."

- **Gerunds in status updates**: Use a gerund with an ellipsis for real time actions like status updates. Use a gerund in full present continuous form when the status update is in full sentence form.
  - *Source:* "Adding card" → *Target:* "Afegint la targeta…"
  - *Source:* "Activating" → *Target:* "Activant…"

## Cultural Adaptation

- **Loan words**: Always use Catalan words and expressions, making sure that no loans, especially from Spanish, are used.
  - *Source:* "You can still close your Move ring. Get after it!" → *Target:* "Encara pots tancar l\u2019anell de moviment. Ves a totes!"
  - *Source:* "Cartoon Party Horn" → *Target:* "Espanta-sogres"

- **Politeness**: Avoid translating and including "Please" or similar polite imperatives from the source text. It is rarely used or needed in Catalan.
  - *Source:* "Sorry, an unexpected error has occured." → *Target:* "Hi ha hagut un error inesperat."
  - *Source:* "Please Wait" → *Target:* "Un moment…"

- **Gender neutrality**: Use gender-neutral language and constructs. Generally, the best practice is to try to rewrite any sentence to exclude pronouns or binary representations of gender.
  - *Source:* "You must be connected to the internet." → *Target:* "Has de tenir connexió a internet."
  - *Source:* "When a friend or family member adds you as a legacy contact, their name will appear here." → *Target:* "Quan algú de la família o una amistat t\u2019afegeixi com a herent digital, aquí se\u2019n mostrarà el nom."

## Punctuation

- **Quotation marks**: Use Catalan curly double quotation marks “ and ” around multi-word UI items when they are referenced rather than used descriptively. Quotation marks are not necessary for app names, email addresses, utility names, or operating-system update names, and are not used when UI options are referenced through a path with ">".
  - *Source:* "Click Agree or Learn More." → *Target:* "Fes clic a \u201CAccepta\u201D o a \u201CMés informació\u201D."

- **Units**: Do not convert imperial measurements to metric. When the English measurement is purely illustrative (a rounded ballpark figure rather than a precise spec), substitute a comparable rounded Catalan figure instead of a literal conversion.
  - *Source:* "Hold iPhone 10 to 20 inches from your face" → *Target:* "Mantén l\u2019iPhone a una distància de 10 a 20 polzades de la cara."

- **Spacing**: There must be a non-breaking space between the number and the unit symbol.
  - *Source:* "100% zoom level" → *Target:* "Nivell del zoom del 100\u00A0%"

- **Exclamation marks**: The exclamation marks used in some English sentences are generally not needed in Catalan.
  - *Source:* "It's a Draw!" → *Target:* "Empat"

- **Punctuation within quotes**: Place the period (or other terminal punctuation) outside the closing quotation mark, even when the source text places it inside. This follows standard Catalan/European typography.
  - *Source:* "Select \u201CStart automatically.\u201D" → *Target:* "Selecciona \u201CInicia automàticament\u201D."

- **Punctuation within parenthesis**: A full sentence within a parenthesis should have the full stop outside of the parenthesis.
  - *Source:* "(This may take a few moments.)" → *Target:* "(El procés pot tardar uns minuts)."

## Orthography

- **Capitalization in headings**: Use capital letter in beginning of sentences and in proper names. Do not capitalize every word in headings, even if the source text does.
  - *Source:* "Setting Up Your New Computer" → *Target:* "Configuració de l\u2019ordinador nou"
  - *Source:* "Suggested Profiles" → *Target:* "Perfils suggerits"

- **Capitalization of common nouns**: Do not use capital letter for: days of the week, months, currencies, nationalities, languages, professions.
  - *Source:* "Create a meeting on Monday" → *Target:* "Crea una reunió per a dilluns."
  - *Source:* "Show in English" → *Target:* "Mostra en català"

- **Lowercase product names**: Some product names always start with a lowercase letter. In that case, do not capitalise them even if they start a sentence.
  - *Source:* "iPhone Restricted by Carrier" → *Target:* "iPhone restringit per l\u2019operador"
  - *Source:* "iMac (24-inch, 2024)" → *Target:* "iMac (24 polzades, 2024)"

- **Numbers**: Use period as thousand separator.
  - *Source:* "2000 Fitness+ Meditations" → *Target:* "2.000 meditacions del Fitness+"
  - *Source:* "Maximum folder size 10,000 items" → *Target:* "Mida màxima de la carpeta: 10.000 ítems"

- **Decimal separator**: Use comma as a separator for decimal numbers. Exact numbers do not need decimals.
  - *Source:* "2.5 cm" → *Target:* "2,5 cm"
  - *Source:* "100.00 m" → *Target:* "100 m"
  - *Source:* "0.5" → *Target:* "0,5"

- **Software version numbers**: Although commas normally should be used as the separator for decimals, periods are instead used for software versions.
  - *Source:* "version 2.5" → *Target:* "version 2.5"
  - *Source:* "iOS 26.1" → *Target:* "iOS 26.1"
  - *Source:* "HomePod software version 16.4" → *Target:* "Versió 16.4 del programari del HomePod"
