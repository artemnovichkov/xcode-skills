# Spanish (es) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Spanish uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and single curly quotation marks ‘ (\u2018) and ’ (\u2019) only for nesting quotes inside already-quoted text.

## Tone And Voice

- **Informal but Respectful Tone**: Address the user with the informal 'tú' form. The style should feel warm and personal but never overly casual or slangy.
  - *Source:* "Do you want to continue?" → *Target:* "¿Quieres continuar?"

## Addressing Users

- **Avoid Possessives — Use Definite Articles Instead**: English possessives are frequently avoided in Spanish. Prefer the definite article over a possessive pronoun unless the context specifically requires a sense of personal belonging, such as Welcome screens or when talking about passwords or passcodes.
  - *Source:* "Turn off your computer." → *Target:* "Apaga el ordenador."
  - *Source:* "Welcome to your new iPhone" → *Target:* "Te damos la bienvenida a tu nuevo iPhone"

- **Gender-Neutral Language — Avoid Gendered References to the User**: When writing gendered sentences, make them as gender-neutral as possible. Avoid gendered nouns like 'el administrador del sistema' and prefer neutral rephrasing such as 'la persona que administra el sistema'.
  - *Source:* "the administrator" → *Target:* "la persona que administra"

## Grammar

- **Prefer Compound Past Tense Over Simple Past**: When the context allows both, use the compound past tense (pretérito perfecto compuesto) rather than the simple past tense (pretérito indefinido).
  - *Source:* "Could not…" → *Target:* "No se ha podido…"

- **'New' Placement — Before Noun for Creation, After for Information**: Place “nuevo” or “nueva” before the noun when the meaning involves creation of something new. Place it after the noun when the meaning is informative or descriptive.
  - *Source:* "New message" → *Target:* "Nuevo mensaje"
  - *Source:* "2 new messages" → *Target:* "2 mensajes nuevos"

- **Preposition 'In' with Time — Use 'dentro de'**: Translate 'in' as 'dentro de' when it is followed by the time remaining until something happens.
  - *Source:* "In 3 hours" → *Target:* "Dentro de 3 horas"

- **Articles with App and Utility Names**: App names, utility names, and update names do not take articles. A few system elements are exceptions and do take an article, most notably 'el Finder' and 'el Dock'. Hardware terms always use an article matching the gender of the implicit noun.
  - *Source:* "Open System Settings" → *Target:* "Abre Ajustes del Sistema"
  - *Source:* "Open the Finder" → *Target:* "Abre el Finder"
  - *Source:* "the iPod" → *Target:* "el iPod"

## Punctuation

- **Curly Double Quotation Marks — Not Angle Quotes**: Always use curly double quotation marks regardless of the quotation style in the source. Use single curly quotation marks only when nesting quotes inside already-quoted text. The period is placed after the closing quotation mark.
  - *Source:* "The \u201CHey Siri\u201D feature will resume…" → *Target:* "La función \u201CAl oír \u2018Oye Siri\u2019\u201D se reanudará…"
  - *Source:* "Select \u201CStart automatically.\u201D" → *Target:* "Selecciona \u201CIniciar automáticamente\u201D."

- **Quotation Marks for Multi-Word UI Items in Sentences**: Use quotation marks for UI options, buttons, and menu items that contain two or more words when they appear within a sentence. Single-word UI items do not need quotation marks. Only the first word inside the quotes is capitalized. Quotation marks are not needed for UI items in paths followed by ‘>’. Quotes are not needed if the option has two or more words and those words are in title case because they are proper nouns.
  - *Source:* "Click OK or More Information." → *Target:* "Haz clic en Aceptar o en \u201CMás información\u201D."
  - *Source:* "Go to General > Accessibility Options > VoiceOver" → *Target:* "Selecciona General > Opciones de accesibilidad > VoiceOver"
  - *Source:* "Tap an environment (like White Sands or Yosemite) or tap one option such as \u201CSummer light\u201D or \u201CWinter light\u201D to change…" → *Target:* "Toca un entorno (como White Sands o Yosemite) o toca una opción como \u201CLuz de verano\u201D o \u201CLuz de invierno\u201D para cambiar…"

- **Quotation Marks Not Needed**: Quotation marks are not needed for email addresses containing “@”, websites, extension or server names, “likes”, and similar.
  - *Source:* "Use the .mov extension for…" → *Target:* "Usa la extensión .mov para…"
  - *Source:* "Your Apple Account %@ does not support FaceTime." → *Target:* "Tu cuenta de Apple %@ no es compatible con FaceTime."
  - *Source:* "This post has 5 likes. The likes on this post…" → *Target:* "Esta publicación tiene 5 me gusta. Los me gusta de esta publicación…"

- **Footnote Markers**: Footnote markers are placed before the punctuation mark without any space.
  - *Source:* "60 fps.***" → *Target:* "60 fotogramas por segundo***."
  - *Source:* "60 fps.*⁺" → *Target:* "60 fotogramas por segundo*,⁺."
  - *Source:* "*Requires iMovie for…" → *Target:* "* Requiere iMovie para…"

- **URLs**: When a complete sentence ends with a URL, a period is still needed after the URL.
  - *Source:* "Available at https://www.apple.com/legal/sla/" → *Target:* "Disponible en https://www.apple.com/es/legal/sla/."

- **Exclamation Marks — Usually Not Needed**: English exclamation marks often do not carry the same weight in Spanish and should typically be removed.
  - *Source:* "Select a utility first!" → *Target:* "Selecciona primero una utilidad."

- **Avoid Slashes — Use 'y' or Rephrase**: Only use a slash when a single button toggles between two actions (Mostrar/ocultar). When there are two different buttons for two different actions, use 'y' instead.
  - *Source:* "Toggle" → *Target:* "Mostrar/ocultar"
  - *Source:* "Back/Forward" → *Target:* "Atrás y adelante"

- **Period After Closing Parenthesis**: When a sentence ends after a closing parenthesis, the period is always placed after the closing parenthesis in Spanish.
  - *Source:* "Turn off AirPort when not in use. (Use the status menu.)" → *Target:* "Desactiva AirPort cuando no esté en uso. (Utiliza el menú de estado)."

- **Lists — Introductory Sentence**: When list items continue an introductory sentence, each item starts with a lowercase letter and ends with a comma, except the last item which ends with a period.
  - *Source:* "The computer is: on, off, locked." → *Target:* "El ordenador está: encendido, apagado, bloqueado."

- **Lists — Independent Items**: When list items are independent (not continuing a sentence), each item starts with a capital letter and no punctuation is used at the end.
  - *Source:* "• Turn on device\n• Connect to Wi-Fi" → *Target:* "• Enciende el dispositivo\n• Conéctate a la red Wi-Fi"

- **Lists — Internal Punctuation**: In lists where items contain internal punctuation, use semicolons to separate items and a period after the last one.
  - *Source:* "• Mac, which is fast\n• iPad, which is portable" → *Target:* "• Mac, que es rápido;\n• iPad, que es portátil."

- **Lists — Consistent Style**: Punctuation style must be consistent across all items in the same list. Do not mix styles.
  - *Source:* "• Wi-Fi\n• Bluetooth" → *Target:* "• Wi-Fi\n• Bluetooth"

## Capitalization

- **Capitalize Less Than English — First Word Only for UI Items**: For UI items only the first word is capitalized, but for app names, utility names, and update names capitalize every major word (excluding prepositions, articles, and conjunctions). Avoid ALL CAPS in software.
  - *Source:* "Language & Text" → *Target:* "Idioma y texto"
  - *Source:* "Align Objects" → *Target:* "Alinear objetos"
  - *Source:* "WARNING: It is important…" → *Target:* "Advertencia: Es importante…"

- **Lowercase After Colon — Unless Preceded by a Title or Warning**: In Spanish, lowercase is generally used after a colon when the text continues on the same line. Use uppercase after a colon only when preceded by a section title or a word like 'Advertencia', 'Nota', or 'Importante'.
  - *Source:* "Silent Mode: Off" → *Target:* "Modo Silencio: desactivado"
  - *Source:* "Important: Do not close this window." → *Target:* "Importante: No cierres esta ventana."

## Abbreviations

- **Spell Out Abbreviations — Use Non-Breaking Spaces in Multi-Word Abbreviations**: Translate English abbreviations as fully spelled-out words when there are no space restrictions. Use non-breaking spaces in multi-word abbreviations. Abbreviations include periods; symbols do not.
  - *Source:* "e.g." → *Target:* "p. ej." (use   between "p." and "ej.")
  - *Source:* "U.S." → *Target:* "EE. UU." (use   between "EE." and "UU.")

## Acronyms

- **Do Not Translate Acronyms — No Periods, No Spaces, No Plurals**: Do not translate acronyms unless a very common Spanish equivalent exists. Acronyms do not use periods or spaces between letters and have no plural form.
  - *Source:* "CDs" → *Target:* "CD"
  - *Source:* "USB" → *Target:* "USB"

## Numerals

- **Comma for Decimal, Period for Thousands (5+ Digits), No Separator for 4 Digits**: Use a comma as the decimal separator. Use a period as the thousands separator only for numbers with five or more digits. Four-digit numbers do not use any thousands separator. Version numbers retain the period (Versión 2.0).
  - *Source:* "0.5 meters" → *Target:* "0,5 metros"
  - *Source:* "100,000 songs" → *Target:* "100.000 canciones"
  - *Source:* "1,000 files" → *Target:* "1000 archivos"

- **Ordinals — Prefer Written-Out Forms**: Write ordinal numbers in words (tercer, primeras).
  - *Source:* "1st" → *Target:* "primero"

- **Speed and Zoom — 'x' Before the Number**: When 'x' or '×' represents a magnitude of speed or zoom, place it before the number in Spanish. Prefer using the letter 'x' over the symbol '×'.
  - *Source:* "24x" → *Target:* "x24"
  - *Source:* "×24" → *Target:* "x24"

- **Software Strings — Use Figures for Numbers by Default**: In software strings, numbers are written with figures by default.
  - *Source:* "3 files selected" → *Target:* "3 archivos seleccionados"

- **Informal or Slogan-Like Strings — Small Numbers Can Be Written in Words**: In informal or slogan-like strings, small numbers can be written out in words when space allows.
  - *Source:* "Live a better day by achieving 3 daily fitness goals." → *Target:* "Mantente en forma con tres objetivos diarios."

- **Number 1 — Prefer Written-Out Form**: Write the number 1 as "uno/una" when possible, except in contexts where it could represent a variable or a different number.
  - *Source:* "1 file selected" → *Target:* "Un archivo seleccionado"

- **Version Numbers — Remove the 'v' Prefix**: Remove the 'v' prefix from version numbers.
  - *Source:* "Requires macOS v10.12." → *Target:* "Se requiere macOS 10.12."

## Date And Time

- **Time Format — Use 24-Hour Clock**: Use the 24-hour time format with colons separating hours, minutes, and seconds. No leading zero for single-digit hours (2:00 not 02:00).
  - *Source:* "4:30 PM" → *Target:* "16:30"

- **Time Format — Midnight and Noon**: Midnight is 00:00 and noon is 12:00.
  - *Source:* "12:00 AM" → *Target:* "00:00"

- **AM/PM — Write as 'a. m.' and 'p. m.' with Non-Breaking Spaces**: When AM/PM cannot be avoided, write them as 'a. m.' and 'p. m.' using non-breaking spaces between the letters.
  - *Source:* "10:00 AM" → *Target:* "10:00 a. m." (use   between "a." and "m.")

- **Date Format — Use DD/MM/YYYY**: Use the DD/MM/YYYY date format. Weekdays and months are not capitalized.
  - *Source:* "Monday, September 9" → *Target:* "lunes, 9 de septiembre"

## Addresses

- **Use Spanish Postal Address Format**: Replace English placeholder addresses with the standard Spanish postal address format. Example format: `Calle, 123, Localidad, C. P. Provincia`.

## Special Characters

- **Use Ellipsis Character — Not Three Dots**: Always use the ellipsis character (…) instead of three consecutive dots.
  - *Source:* "Searching..." → *Target:* "Buscando…"

- **Non-Breaking Space Between Figures and Nouns**: Use a non-breaking space between a number and the noun that follows it.
  - *Source:* "25 pages" → *Target:* "25 páginas" (use   between "25" and "páginas")

- **Non-Breaking Space Between Numbers and Symbols**: Use a non-breaking space between a number and its associated symbol.
  - *Source:* "25%" → *Target:* "25 %" (use   between "25" and "%")

- **Non-Breaking Space in Multi-Word Abbreviations**: Use non-breaking spaces between the parts of multi-word abbreviations.
  - *Source:* "e.g." → *Target:* "p. ej." (use   between "p." and "ej.")

- **Non-Breaking Space in Multi-Word Product Names**: Use non-breaking spaces between all words in multi-word Apple product names.
  - *Source:* "Apple Vision Pro" → *Target:* "Apple Vision Pro" (use   between each word)

- **Non-Breaking Space Before '>' in UI Paths**: Use a non-breaking space before the '>' separator in UI navigation paths.
  - *Source:* "General > Accessibility" → *Target:* "General > Accesibilidad" (use   before ">")

- **No Non-Breaking Spaces Around '+' in Keyboard Shortcuts**: Do not use non-breaking spaces around the '+' sign in keyboard shortcuts.
  - *Source:* "Command + C" → *Target:* "Comando + C" (regular spaces around "+")

- **Translate Characters Used as Words**: The English character '#' must be replaced with “N.º” if context indicates a reference to numbers.
  - *Source:* "#23" → *Target:* "N.º 23"

- **Non-Breaking Hyphen for Mid-Word Hyphens**: Use non-breaking hyphens for mid-word hyphens (like Wi‑Fi) to prevent line breaks. Do not use non-breaking hyphens when translating language codes (snk-Latn).
  - *Source:* "Wi-Fi" → *Target:* "Wi‑Fi"

## Interface Elements

- **Keyboard Shortcuts — Use '+' Not Hyphen**: Use a '+' with spaces on both sides (Key1 + Key2) when translating keyboard shortcuts. When a key name appears mid-sentence, capitalize the first letter.
  - *Source:* "Command-C" → *Target:* "Comando + C"
  - *Source:* "Hold the option key while dragging" → *Target:* "Mantén pulsada la tecla Opción al arrastrar"

- **Buttons and Interactive Elements — Use Infinitive**: Use the infinitive form for buttons, checkboxes, action links, switches, menu items, commands, and tooltips.
  - *Source:* "Delete" → *Target:* "Eliminar"

- **Instructional Sentences and Titles — Use Imperative**: Use the imperative form for instructional sentences and titles that tell the user to perform an action.
  - *Source:* "Select a file to continue." → *Target:* "Selecciona un archivo para continuar."

- **Tabs, Panels, and Menu Titles — Use Nouns When Possible**: Use nouns and not verbs for tabs, panels, and menu titles.
  - *Source:* "Printing" → *Target:* "Impresión"

- **Menu Names — Use Noun Form**: Use nouns and not verbs to translate menu names.
  - *Source:* "Edit menu" → *Target:* "menú Edición"

- **Periods Only for Complete Sentences — Not for Titles or Labels**: Titles do not end with a period.
  - *Source:* "Select a photo" → *Target:* "Selecciona una foto"

- **Mode Names — Descriptive Style Preferred**: Translate mode names descriptively when possible (modo oscuro, modo privado). If a descriptive translation is not possible, only capitalize the first letter and enclose names with two or more words in quotation marks.
  - *Source:* "dark mode" → *Target:* "modo oscuro"
  - *Source:* "Do Not Disturb mode" → *Target:* "modo \u201CNo molestar\u201D"
  - *Source:* "Lost Mode" → *Target:* "modo Perdido"

- **Undo Strings — Lowercase Noun Phrases**: Undo action strings are lowercased noun phrases so they read naturally when composed into an "Undo %@"-style container.
  - *Source:* "Undo Adjust Saturation" → *Target:* "Deshacer ajuste de la saturación"

- **Drop-Down Menus — Capitalization Depends on Context**: If the content before a drop-down menu is a title (with or without a colon), capitalize the first letter of each option. If the drop-down is integrated within a sentence with hard-coded text before and after, use lowercase.
  - *Source:* "Select an option: / Option 1" → *Target:* "Selecciona una opción: / Opción 1"

## Measurements

- **Do Not Convert Units — Keep Same as English**: Do not convert units except when the English measurement is illustrative. Unit symbols are lowercase, have no periods, and no plural forms.
  - *Source:* "Your device needs to be within 30 feet of your computer." → *Target:* "El dispositivo debe estar en un radio de 9 metros con respecto al ordenador."

## Trademarks And Product Names

- **Hardware Articles (Masculine)**: Hardware terms take a gendered article matching the implicit noun (e.g., el reproductor → el iPod).
  - *Source:* "the iPod" → *Target:* "el iPod"

- **Hardware Articles (Feminine)**: Hardware terms take a gendered article matching the implicit noun (e.g., la barra → la Touch Bar).
  - *Source:* "the Touch Bar" → *Target:* "la Touch Bar"

- **Software Articles**: Most software terms do not take an article, with exceptions like 'el Finder', 'el Dock', and 'el Dashboard'.
  - *Source:* "Open Finder" → *Target:* "Abre el Finder"

- **Store Articles**: The Stores (iTunes Store, App Store) are feminine but should not be preceded by an article.
  - *Source:* "Sign in to iTunes Store." → *Target:* "Inicia sesión en iTunes Store."

- **Pluralization (With 's')**: Do not add a plural 's' to trademark names unless the product takes it natively (e.g., los AirPods, los AirTags).
  - *Source:* "AirTags" → *Target:* "los AirTags"

- **Pluralization (Without 's')**: Do not add a plural 's' to trademark names unless the product takes it natively (e.g., los iPhone, los iPad).
  - *Source:* "the iPhones" → *Target:* "los iPhone"

- **'y' Never Becomes 'e' Before Lowercase 'i' Product Names**: When a product name starts with a lowercase 'i' followed by a capital letter (iPad, iTunes) and is preceded by the conjunction 'y', do not change 'y' to 'e'.
  - *Source:* "music and iTunes" → *Target:* "música y iTunes"
  - *Source:* "tablets and iPad" → *Target:* "tabletas y iPad"

## URL Localization

- **Localize Only Example/Demonstrative URLs**: Only localize URLs that are used as examples or are demonstrative. Never translate real URLs. When an illustrative URL is translated, apply the change to both the visible text and the underlying link.
  - *Source:* "example.com/folder" → *Target:* "example.com/carpeta"
  - *Source:* "name@example.com" → *Target:* "nombre@example.com"

## File And Path Names

- **Localize File Names**: Sample file names should be localized.
  - *Source:* "MyImage.jpg" → *Target:* "Mi_imagen.jpg"

- **Localize Path Names**: If the source contains path names, localize those parts of the path that are translated on the target system.
  - *Source:* "Current file will be renamed to \u201C/Library/Preferences/edu.mit.Kerberos.pre-Active Directory\u201D" → *Target:* "El archivo actual pasará a llamarse \u201C/Biblioteca/Preferences/edu.mit.Kerberos.pre-Active Directory\u201D"

## Phone Numbers

- **Localize Phone Numbers**: Phone numbers are divided into groups of three digits, separated by a space. Spain regional prefixes are not written in parentheses.
  - *Source:* "Call 923233322" → *Target:* "Llama al 923 233 322"

## Sorting Order

- **Sort Alphabetically Equivalent Words**: When two alphabetically equivalent words are present, one accented and the other unaccented, the unaccented word precedes the accented one.
  - *Source:* "aria / ártico / asno" → *Target:* "aria / ártico / asno"

## Inches

- **Use the Double Prime for Inches**: For inches use the double prime (″ (\u2033)) rather than the quotation mark symbol.
  - *Source:* "2\u201D" → *Target:* "2\u2033"
