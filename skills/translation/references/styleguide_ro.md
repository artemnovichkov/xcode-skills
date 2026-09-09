# Romanian (ro) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Romanian uses curly double quotation marks „ (\u201E) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "Tap \u201CMake Into Smart List.\u201D" → *Target:* "Apăsați pe \u201ETransformați în listă inteligentă\u201D."

## Tone And Voice

- **Smart but Casual Tone**: Write in a neutral, descriptive style that is closer to formal than informal without being stiff or trendy. Prefer Romanian terminology over English borrowings even when users commonly use the English word.

## Addressing Users

- **Use Formal Polite Form (dvs./doriți) for System-to-User Interactions**: When the computer asks the user to make a decision or reports information, use the polite second-person plural form (dvs.) rather than the informal second-person singular (tu).
  - *Source:* "Touch ID does not recognize your fingerprint. Enable %@." → *Target:* "Touch ID nu recunoaște amprenta dvs. Activați %@."

- **Avoid Overusing 'dvs.'**: Do not repeat “dvs.” in the same sentence; drop the possessive where the meaning stays clear.
  - *Source:* "Open this request on your iPhone to select your items." → *Target:* "Deschideți această solicitare pe iPhone pentru a selecta articolele."

- **Use Informal Imperative for App Intents and User-to-Device Commands**: When the user is issuing a command to the device — as in App Intents parameter summaries and Shortcuts phrases — use the informal second-person singular imperative. Commands directed at the computer do not require the formal address style. Rely on the source string's own phrasing (a user-issued command) or a developer comment marking the string as an App Intent or Shortcuts phrase.
  - *Source:* "Go to the ${target} in ${applicationName}" → *Target:* "Accesează ${target} în ${applicationName}"

- **Do Not Translate 'Please' Literally**: Expressions beginning with 'Please' should not be translated as 'Vă rugăm să…'. Convey politeness through the formal second-person verb form instead.
  - *Source:* "Please choose another name." → *Target:* "Alegeți alt nume."

- **Use Passive Voice or Long Infinitives for Computer-Initiated Actions**: When the computer reports a state or performs an action without the user's intervention, use passive voice or long infinitive (noun) forms. A first-person construction such as 'Nu mă pot conecta la server' is never appropriate for system messages.
  - *Source:* "Could not connect to the server. Receiving file \u201C%@\u201D from \u201C%@\u201D…" → *Target:* "Conectarea la server nu a reușit. Primire fișier \u201E%@\u201D de la \u201E%@\u201D…"

## Abbreviations

- **Avoid Abbreviations; Accepted Exceptions Are 'dvs.', Address Fields, Editorial references**: Do not shorten words to make a string fit. The polite pronoun 'dumneavoastră' is always abbreviated as 'dvs.' with a period, even when followed by other punctuation. If the “dvs.” appears at the end of the sentence and a full stop is also required, only use 1 period, not 2. Standard address abbreviations (jud., sect., nr.) and editorial references (vol., pag.) are also acceptable.
  - *Source:* "Enter your password." → *Target:* "Introduceți parola dvs." (one period, not "…dvs..")

## Special Characters

- **Use Correct Unicode Romanian Diacritics — Comma Below, Not Cedilla**: Always use the comma-below variants: ș (U+0219), ț (U+021B), Ș (U+0218), Ț (U+021A). The Windows cedilla variants (ş, ţ) are incorrect and must never be used in software or documentation.
  - *Source:* "Delete items" → *Target:* "Ștergeți articolele" (not "Ştergeţi articolele")

- **Translate Ampersand as 'și'**: The ampersand (&) is uncommon in Romanian and must be translated as the conjunction 'și'.
  - *Source:* "Mac & PC" → *Target:* "Mac și PC"

- **Place Currency Symbols After the Amount**: Currency symbols are placed after the numeric amount and separated from it by a non-breaking space.
  - *Source:* "120€" → *Target:* "120 €"

## Grammar

- **Loan Words: No Hyphen If Final Letter Is Pronounced as in Romanian**: Do not use a hyphen before a Romanian article or suffix when the borrowed word's final letter is pronounced the same as in Romanian. Use a hyphen only when the final letter's spelling differs from its pronunciation.
  - *Source:* "blogs" → *Target:* "bloguri" (no hyphen — final letter pronounced as in Romanian)
  - *Source:* "cookies" → *Target:* "cookie-uri" (hyphen — spelling differs from pronunciation)

- **Use Correct Prepositions: 'în' for Folders/Apps/Accounts, 'pe' for Disks/Devices**: The correct preposition depends on the destination. Use 'în' for folders, apps, accounts, and services; use 'pe' for disks, devices, servers, websites, and cloud-storage platforms (e.g. iCloud). The generic common noun 'cloud' takes 'în' (stocat în cloud). When signing in with an account, use 'în contul' to avoid the awkward 'cu contul'.
  - *Source:* "Sign in to this application" → *Target:* "Autentificați-vă în această aplicație"
  - *Source:* "Sign in to other device" → *Target:* "Autentificați-vă pe un alt dispozitiv"
  - *Source:* "Stored in iCloud" → *Target:* "stocat pe iCloud" (not "în iCloud")

- **Agreement with Disjunctive Subjects: Singular with the Nearest Noun**: When a nominal predicate has multiple subjects separated by a disjunctive conjunction (sau, ori), the verb agrees in singular with the nearest noun, not plural with all subjects. Alternatively, rephrase to avoid ambiguity.
  - *Source:* "The user name or password is incorrect." → *Target:* "Numele de utilizator sau parola este greșită."

- **Sentence Case Only — No Title Case in Romanian**: Romanian does not use Title Case. Only the first letter of the first word is capitalized in menu items, titles, and other UI strings.
  - *Source:* "Show Related Messages" → *Target:* "Afișați mesajele asociate"

- **Capitalization — Only When the Feature Name Is Directly Referenced**: Feature names are capitalized only when the actual UI element is directly referenced; use lowercase when treating them as common nouns in a sentence.
  - *Source:* "Notification Center" → *Target:* "centrul de notificări" (lowercase — treated as a common noun)

## Punctuation

- **No Comma Before Copulative Conjunctions**: Romanian does not use a comma before copulative conjunctions. Remove any serial comma, and any comma immediately before 'și' or 'sau'.
  - *Source:* "%1$@, %2$@, or %3$@" → *Target:* "%1$@, %2$@ sau %3$@"

- **No Comma before “etc.”**: Romanian does not use a comma before etc.
  - *Source:* "%1$@, %2$@, %3$@, etc." → *Target:* "%1$@, %2$@, %3$@ etc."

- **Period After the Closing Quotation Mark**: In Romanian, when a sentence ends immediately after a closing quotation mark, the period is placed after the closing mark, not inside it as in English.
  - *Source:* "Tap \u201CMake Into Smart List.\u201D" → *Target:* "Apăsați pe \u201ETransformați în listă inteligentă\u201D."

- **Use En Dash (–) Instead of Em Dash (—)**: When the source uses em dashes as substitutes for commas, parentheses, or colons, replace them with en dashes (–) in Romanian.
  - *Source:* "that's about %@ a day — to get this award." → *Target:* "asta înseamnă aproximativ %@ pe zi – pentru a primi acest premiu."

- **Use Romanian Curly Quotes**: Romanian uses low-9 opening „ (\u201E) and high-9 closing ” (\u201D) curly double quotes. Single straight quotes are replaced with curly double quotes. Use guillemets « (\u00AB) » (\u00BB) for nested quotations. Multi-word UI element names appearing in a sentence must be enclosed in quotation marks for readability, unless already set apart by bold or italics.
  - *Source:* "a button \u201CAttach Files\u201D in Mail" → *Target:* "un buton \u201EIncludeți fișiere atașate\u201D în Mail"

- **Use the Single Ellipsis Character — Not Three Dots**: Always use the single ellipsis character … (U+2026), not three separate periods.
  - *Source:* "Rename..." → *Target:* "Redenumire…"

## Interface Elements

- **Buttons Use Formal Imperative**: Button labels in dialog boxes use the polite second-person plural imperative form.
  - *Source:* "Add" (button) → *Target:* "Adăugați"

- **Toggles Use Long Infinitives**: Toggle option names (checkboxes, radio buttons), and window titles use long infinitive (noun) forms.
  - *Source:* "Allow notifications" (toggle) → *Target:* "Permitere notificări"

- **Menus Use Long Infinitives.**: Menu names, toggle option names (checkboxes, radio buttons), and window titles use long infinitive (noun) forms.
  - *Source:* "Edit" (menu name) → *Target:* "Editare"

- **Menu items with ellipsis require long infinitives**: Menu items ending in ellipsis (…) that require further input also use long infinitives.
  - *Source:* "Rename…" (menu item with ellipsis) → *Target:* "Redenumire…"

- **Inflect Translated App Names via the Common Noun, Not the App Name Itself**: Translated app names (e.g. Contacte, Poze) are not inflected directly. When grammatical agreement is required, use the common noun (aplicația, utilitarul) followed by the app name, and inflect the common noun.
  - *Source:* "AirPort Utility could not be found." → *Target:* "Aplicația Utilitar AirPort nu a putut fi găsită."

## Trademarks And Product Names

- **Inflect Hardware Product Names via Hyphen**: When a hardware product name kept in English needs Romanian declension, either append the article/ending with a non-breaking hyphen (Mac-ul, iPad-urile) or use the corresponding common noun (computerul Mac, dispozitivele iPad).
  - *Source:* "the Mac" → *Target:* "Mac-ul" (or, as a common noun, "computerul Mac")

## Measurements

- **Do Not Convert Measurements**: Do not convert measurements (e.g. inches to centimeters) — keep the source unit and match the source's level of precision. A unit symbol is not followed by a period and is separated from the number by a non-breaking space (also for % and °C/°F).
  - *Source:* "2 GB / 30 min / 25 °C" → *Target:* "2 GB / 30 min / 25 °C" (non-breaking space between each value and its unit)

## Numerals

- **Insert 'de' Between Numbers of 20 or More and the Modified Noun**: When a cardinal number of 20 or more determines a noun, insert the preposition 'de' between the number and the noun. For values 0–19, 'de' is not used. The preposition is omitted before unit abbreviations and symbols regardless of value. In full sentences, use a plural-aware format to handle the 'few' (no 'de') and 'other' (with 'de') forms correctly.
  - *Source:* "1,000,000 songs" → *Target:* "1.000.000 de melodii"
  - *Source:* "16 minutes" → *Target:* "16 minute" (no 'de')
  - *Source:* "20 mins" (abbreviated) → *Target:* "20 min." (no 'de' before an abbreviation)

## Variables

- **Preserve Variables Exactly; Reorder with Positional Indices When Needed**: Never alter or omit variable format specifiers. If Romanian word order requires a different variable sequence, add positional indices (%1$@, %2$@, etc.) to every variable in the string. Do not change the period inside numeric format specifiers such as %.1f.
  - *Source:* "%@ Settings" → *Target:* "Configurări %@" (where %@ is an app name)
  - *Source:* "%1$@\u2019s %2$@" → *Target:* "%2$@ (%1$@)"

## Diversity And Inclusion

- **Use Gender-Neutral Language — Prefer Reflexive Forms and Rephrasing**: Avoid binary he/she expressions for persons of unspecified gender. First try to rewrite the sentence to eliminate the need for a gendered pronoun; use reflexive forms where they sound natural. The slash '/' or parenthesis '()' workaround is acceptable sparingly but is not preferred because it excludes non-binary individuals.
  - *Source:* "You will be signed into" → *Target:* "Vă veți autentifica în" (not "Veți fi autentificat(ă) în")
  - *Source:* "Are you sure…?" → *Target:* "Sigur doriți să…?"

## Terminology

- **Use Standardized Romanian Terminology Consistently**: Repetitive phrases and standard UI labels must always be translated the same way. Key standardized translations include 'Configurări' for Settings, 'Dosar' for Folder (macOS), 'Autentificare' for Sign in, 'Anulați' for Cancel, and 'Toate drepturile rezervate.' for 'All Rights Reserved.'
  - *Source:* "Settings" → *Target:* "Configurări"
  - *Source:* "Folder" → *Target:* "Dosar" (macOS) / "Folder" (Windows)
  - *Source:* "Cancel" → *Target:* "Anulați"
  - *Source:* "All Rights Reserved." → *Target:* "Toate drepturile rezervate."
  - *Source:* "Please try again later" → *Target:* "Reîncercați mai târziu"
