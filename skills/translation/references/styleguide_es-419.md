# Latin American Spanish (es-419) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Latin American Spanish uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and single curly quotation marks ‘ (\u2018) and ’ (\u2019) only for nesting quotes inside already-quoted text — not straight ASCII quotes and not angle guillemets.

## Tone And Voice

- **Natural, Concise, and Pragmatic Style**: Translations should read naturally to a Latin American user, conveying meaning directly and without unnecessary wordiness. Sentences should be short and grammatically simple where possible, but avoid a robotic, telegraphic feel — use semicolons or conjunctions to join related ideas when it improves flow.
  - *Source:* "Apple Watch is a device that allows you to keep track of your heart beat. By wearing your Apple Watch and resting your arm on a flat surface, you only have to open the ECG app to start measuring your heart rhythm." → *Target:* "El Apple Watch te permite medir tu pulso; al traerlo puesto, solo tienes que abrir la app ECG para comenzar las mediciones al colocar tu brazo sobre una superficie plana."

## Addressing Users

- **Use Informal Second-Person Singular (tú)**: Address users informally using 'tú' across all software products. Avoid overly casual slang or colloquial phrases — the tone should feel warm and personal but still polished.
  - *Source:* "Do you want to continue?" → *Target:* "¿Quieres continuar?"

- **Omit 'Please' in Instructions**: English frequently uses 'please' when directing the user to perform an action. This word should be dropped in Spanish, as it is redundant and sounds unnatural in instructional contexts.
  - *Source:* "Please use another name." → *Target:* "Usa otro nombre."

- **Avoid Gendered Language When Referring to the User**: Do not assume the user's gender. Reword sentences to avoid gendered adjectives or verbs whenever possible. When a gendered word is unavoidable, use the masculine form as the grammatical neutral.
  - *Source:* "Are you sure?" → *Target:* "¿Quieres…?" (not "¿Estás seguro de que…?")
  - *Source:* "You are connected to the Internet." → *Target:* "Te conectaste a Internet." (not "Estás conectado a Internet.")

- **Prefer Simple Past Compound Past Tense**: When the context allows both, use the compound past tense (pretérito perfecto compuesto) rather than the simple past tense (pretérito indefinido).
  - *Source:* "Could not…" → *Target:* "No se pudo"

## Grammar

- **Prefer Active Voice and 'Voz Pasiva Refleja'**: Spanish uses the passive voice far less than English. Prefer active constructions or the reflexive passive ('se' + verb) over direct passive translations.
  - *Source:* "This file is required by macOS to display text. It has been restored." → *Target:* "macOS requiere este archivo para mostrar texto, por lo que se restauró."

- **Reduce English Redundancy**: English often repeats subjects and nouns across consecutive sentences. In Spanish, substitute repeated nouns with articles or implicit verb subjects to create a more streamlined translation.
  - *Source:* "Log in using your Apple ID. If you've forgotten your Apple ID, please visit…" → *Target:* "Inicia sesión con tu Apple ID. Si lo olvidaste, visita…"

- **'New' Placement — Before Noun for Creation, After for Information**: Place “nuevo” o “nueva” before the noun when the meaning involves creation of something new. Place it after the noun when the meaning is informative or descriptive.
  - *Source:* "New message" → *Target:* "Nuevo mensaje"

- **Avoid Cacophony Through Word Variation**: When a direct translation creates a jarring repetition of sounds, reorder the sentence or use a synonym to improve readability — even if this slightly departs from consistent terminology conventions.
  - *Source:* "Your computer is authenticating your data. Please try again later." → *Target:* "Se están autenticando los datos. Intenta después." (not "Tu computadora está autenticando tus datos. Intenta más tarde.")

- **Articles with App and Utility Names**: App names, utility names, and update names do not take articles. A few system elements are exceptions and do take an article, most notably 'el Finder' and 'el Dock'. Hardware terms always use an article matching the gender of the implicit noun.
  - *Source:* "Open System Settings" → *Target:* "Abrir Configuración del Sistema"
  - *Source:* "Open the Finder" → *Target:* "Abre el Finder"
  - *Source:* "the iPod" → *Target:* "el iPod"

- **Conjunction “y” (and) before product names beginning with i-**: While it’s grammatically incorrect to use “y” when the last item in a list begins with “i” (like “idea”), names of Apple products can be preceded with a “y” conjunction.
  - *Source:* "Apps for iPad and iPhone" → *Target:* "Apps para iPad y iPhone"

## Punctuation

- **No Oxford Comma; Semicolons for Nested Lists**: Do not use a comma before the final 'and' or 'or' in a list (no Oxford comma). When a list contains sub-lists, separate the groups with a semicolon.
  - *Source:* "Connects your iPhone, iPod, or iPad." → *Target:* "Conecta tu iPhone, iPod o iPad."
  - *Source:* "Apple ID gives you access to stores like iTunes Store, App Store, and the Tones Store; sites like iCloud and Apple Music; and services like Apple Music, Genius, and Videos." → *Target:* "Apple ID te brinda acceso a tiendas como iTunes Store, App Store y la tienda de tonos; sitios como iCloud y Apple Music; y servicios como Apple Music, Genius y Videos."

- **Use Curly Quotation Marks**: Always use curly (typographic) quotation marks (“ (\u201C) and ” (\u201D)) instead of straight quotation marks. Quotation marks are used for things a user types or says — such as file names, Wi-Fi network names, device names, or voice commands — but not for app names or UI elements.
  - *Source:* "Select the file named \u201Creport\u201D." → *Target:* "Selecciona el archivo \u201Creporte\u201D."

- **Restrict Exclamation Marks to Casual Contexts**: Unlike in English, exclamation marks in Spanish signal intense excitement or shouting. Avoid them in standard technical strings. They may be used at your discretion in casual, marketing-adjacent content.
  - *Source:* "Select a utility first!" → *Target:* "Selecciona primero una utilidad."
  - *Source:* "You reached your daily Move goal for the 100th time! Incredible stuff!" → *Target:* "Lograste tu objetivo diario de Moverse 100 veces. ¡Increíble!"

- **Curly Double Quotation Marks, Not Angle Quotes**: Always use curly double quotation marks regardless of the quotation style in the source. Use single curly quotation marks only when nesting quotes inside already-quoted text. The period is placed after the closing quotation mark in Spanish.
  - *Source:* "The 'Hey Siri' feature will resume." → *Target:* "La función \u201CAl oír \u2018Oye Siri\u2019\u201D se reanudará."

- **URLs**: When a complete sentence ends with a URL, a period is still needed after the URL.
  - *Source:* "Available at https://www.apple.com/legal/sla/" → *Target:* "Disponible en https://www.apple.com/es/legal/sla/."

- **No Space Around Slashes**: In Spanish there should be no space before or after a slash used to separate elements or alternatives, unlike the common English practice.
  - *Source:* "Play / Pause" → *Target:* "Reproducir/pausa"

## Special Characters

- **Use the Ellipsis Character, Not Three Dots**: Always use the single ellipsis character (…) rather than three consecutive periods (...). This ensures correct rendering, spacing, and correct accessibility interpretation by assistive technologies.
  - *Source:* "Loading..." → *Target:* "Cargando…" (use the … character, not ...)

- **Translate Symbol-as-Word Characters**: Characters used as words in English must be replaced with their Spanish equivalents in translation, not left as symbols.
  - *Source:* "Settings & Privacy" → *Target:* "Configuración y privacidad" (& → y)
  - *Source:* "#results" → *Target:* "número de resultados" (# → número)
  - *Source:* "Reply @user" → *Target:* "Responder a usuario" (@ → en)

- **Non-Breaking Space in Multi-Word Product Names**: Use non-breaking spaces between all words in multiple-word Apple product names.
  - *Source:* "Apple Vision Pro" → *Target:* "Apple Vision Pro"

- **Non-Breaking Space Before '>' in UI Paths**: Use a non-breaking space before the '>' separator in UI navigation paths.
  - *Source:* "General > About" → *Target:* "General > Información"

## Capitalization

- **Capitalize App Names; Lowercase Feature Names**: Names of apps, utilities, and software updates capitalize all major nouns and modifiers. Translated names of features, services, and tools are treated as generic common nouns — written in all lowercase, preceded by an article, and without quotation marks.
  - *Source:* "System Settings" → *Target:* "Configuración del Sistema" (app name)
  - *Source:* "Notification Center" → *Target:* "el centro de notificaciones" (feature name)
  - *Source:* "Airplane Mode" → *Target:* "el modo de vuelo" (feature name)

- **Lowercase After Colon — Unless Preceded by a Title or Warning**: In Spanish, lowercase is generally used after a colon when the text continues on the same line. Use uppercase after a colon only when preceded by a section title or a word like 'Advertencia', 'Nota', or 'Importante'.
  - *Source:* "Important: Do not close this window." → *Target:* "Importante: No cierres esta ventana."

## Interface Elements

- **Use Infinitive for Buttons; Imperative or Noun for Instructions**: UI actions (buttons, options, menus) use the infinitive form to indicate the user can perform the action at any time. Instructions that ask the user to complete a step use the imperative. Titles in Welcome screens, alerts, and What's New sections prefer a noun phrase over a verb.
  - *Source:* "Enable Face ID" → *Target:* "Activación de Face ID" (title)
  - *Source:* "Send a Message" → *Target:* "Envía un mensaje" (instruction)
  - *Source:* "Select to play a sound" → *Target:* "Reproducir un sonido" (tooltip)

## Abbreviations

- **Spell Out Abbreviations When Space Allows**: Abbreviations are much less common in Spanish than in English. Fully spell out English abbreviations whenever space permits. Abbreviating by truncating the last letters is a last resort — try rewording the string first before abbreviating.
  - *Source:* "disp." → *Target:* "dispositivo" (preferred when space allows)

## Acronyms

- **Do Not Translate Acronyms; No Periods or Plural Forms**: Keep international technical acronyms in their English form unless a widely understood Spanish equivalent exists. Acronyms have no periods, no spaces between letters, and no plural 's'.
  - *Source:* "USBs" → *Target:* "USB" (no plural 's')
  - *Source:* "RAM" (random access memory) → *Target:* "RAM"

## Numerals

- **Period as Decimal Separator; Comma as Thousands Separator**: Use a period for decimal values and a comma to separate thousands in numbers with four or more digits. Write small cardinal numbers (1–10) as words in most contexts; use figures from 11 onward. Ordinal numbers use superscript-free suffixes (1o., 2a., 3er.).
  - *Source:* "0.5 m" → *Target:* "0.5 m"
  - *Source:* "25,000 songs" → *Target:* "25,000 canciones"
  - *Source:* "2nd generation" → *Target:* "2a. generación"

- **Ordinals — Prefer Written-Out Forms**: Write ordinal numbers in words (tercer, primeras)
  - *Source:* "1st" → *Target:* "primero"

## Measurements

- **Convert Imperial to Metric and Round**: English measurements in imperial units must be converted to the metric system. Round the result to a natural value and add the original if helpful for context.
  - *Source:* "Your device needs to be within 30 feet of your computer." → *Target:* "El dispositivo debe estar en un radio de 9 metros con respecto a tu computadora."

## Date And Time

- **Day-Month-Year Date Format; 12-Hour Clock**: Use the day-month-year order for dates. Use the 12-hour time format for Mexico and most of Latin America.
  - *Source:* "January 25, 2010" → *Target:* "25 de enero de 2010" (or "25/1/2010")

## Addresses

- **Use Latin American Address Format**: Replace English postal address placeholders with Latin American conventions. Mexican postal address format is a common default. Example format: `Calle 123, Colonia, CP, Estado`.

## Trademarks And Product Names

- **Hardware Product Names Take a Gendered Article; Software Names Generally Do Not**: Hardware Apple product names (iPhone, Mac, etc.) always take a Spanish article that agrees with the implicit noun's gender. Software terms (Mission Control, App Store, etc.) are generally used without an article. Do not add a plural 's' to untranslated product names.
  - *Source:* "iPhone" → *Target:* "el iPhone"
  - *Source:* "Mac" → *Target:* "la Mac"
  - *Source:* "iPods" → *Target:* "los iPod" (no added 's')

## Variables

- **Preserve All Variables; Reorder with Positional Notation**: Every variable (%@, %d, %1$@, etc.) from the source must appear in the translation. If the natural Spanish word order requires variables to be rearranged, add positional notation (n$) to each variable rather than reordering by other means.
  - *Source:* "%@'s %@" → *Target:* "%2$@ de %1$@" (person's item)
  - *Source:* "Page %1$@ of %2$@" → *Target:* "Página %1$@ de %2$@"
