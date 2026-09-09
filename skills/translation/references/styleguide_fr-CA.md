# Canadian French (fr-CA) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual Tone**: The tone should be closer to formal than informal, but never stiff or academic. Keep a neutral, descriptive style. In Canadian French, the use of English words must be strictly avoided in written content even when they are commonly used orally.
  - *Source:* "Get started" → *Target:* "Premiers pas"

## Addressing Users

- **Use Formal 'vous' Address**: Always address the user with the formal second-person plural 'vous'. Avoid gender-specific greetings such as Monsieur or Madame; if the gender is unknown, use 'Bonjour' or the user's name instead. Avoid overusing possessive pronouns.
  - *Source:* "Are you sure you want to delete this?" → *Target:* "Voulez-vous vraiment supprimer cet élément ?"

- **Translate 'Please' as 'Veuillez'**: Do not translate 'please' as 's'il vous plaît'. Instead, use the imperative form of 'vouloir' — 'veuillez' — which is more natural and concise in Canadian French UI strings.
  - *Source:* "Please select a file to import" → *Target:* "Veuillez sélectionner le fichier à importer."

## Acronyms

- **Check for Canadian French Equivalents of Acronyms**: Do not translate acronyms unless a recognized Canadian French equivalent exists. Some acronyms have standard French-Canadian counterparts that should be used.
  - *Source:* "PIN" → *Target:* "NIP"

## Date And Time

- **Canadian French Date and Time Formats**: Use the short date format yyyy-MM-dd (e.g. 2023-02-25) and long format d MMMM yyyy (e.g. 5 février 2023). Times use a 24-hour clock; hours are never preceded by a leading zero, but minutes under 10 use a leading zero. The 'h' sign is preceded by a non-breaking space.
  - *Source:* "9:05 AM" → *Target:* "9 h 05"
  - *Source:* "February 5, 2023" → *Target:* "5 février 2023"

## Measurements

- **Do Not Convert Measurements**: Do not convert imperial measurements to metric. Canada uses the metric system but do not apply conversions independently. Never use the double-quote symbol as an abbreviation for inches — use 'po' instead.
  - *Source:* "10 in." → *Target:* "10 po"

## Addresses

- **Canadian Address Format**: Follow the Canadian address convention: Title/First Name/Last Name, then company, then house number followed by street type and name, then city (province) and postal code in A1A 1A1 format with a non-breaking space between the third and fourth characters. Example format: `904, rue Saint-Urbain, Montréal (Québec) H2Z 1K4`.

## Numerals

- **Canadian French Number Formatting**: Use a non-breaking space as the thousands separator and a comma as the decimal separator. Numbers below twenty-one are generally written in words in non-technical contexts, but numerals are accepted in software strings due to space constraints and variables.
  - *Source:* "1,000,000 songs" → *Target:* "1 000 000 de chansons"
  - *Source:* "3.14" → *Target:* "3,14"
  - *Source:* ".5m" → *Target:* "0,5 m"

## Special Characters

- **Translate Symbols Used as Words**: When '&' or '@' appear as words within a sentence, replace them with their French equivalents. Capital letters must carry the same accents as lowercase letters.
  - *Source:* "Black & white" → *Target:* "Noir et blanc"
  - *Source:* "State" → *Target:* "État (not: Etat)"

## Punctuation

- **Use French Angle Quotation Marks with Non-Breaking Spaces**: Use « » (French guillemets) with a non-breaking space after the opening mark and before the closing mark. Use English double quotation marks “ (\u201C) and ” (\u201D) for nested quotes within guillemets, and English single quotes ‘ (\u2018) and ’ (\u2019) for a third level of nesting.
  - *Source:* "Select folder \u201Cxyz\u201D and delete it." → *Target:* "« Sélectionnez le dossier \u201Cxyz\u201D, puis supprimez-le. »"

- **Non-Breaking Space Before Colon**: A colon must always be preceded by a non-breaking space. Do not capitalize the word following a colon unless it begins a complete quotation, follows a heading, or follows a label like 'Remarque' or 'Avertissement'.
  - *Source:* "Note: Do not turn off the device." → *Target:* "Remarque : N\u2019éteignez pas l\u2019appareil."

- **No Space Before Question or Exclamation Mark**: Unlike French Universal, Canadian French does not use a space before the question mark or exclamation mark. The period, question mark, or exclamation mark goes inside the closing quotation mark when the full sentence is within quotes.
  - *Source:* "Are you sure?" → *Target:* "Confirmez-vous?"

## List Punctuation Scenarios

- **List Punctuation Scenarios**: How a list is punctuated depends on whether the introductory sentence is complete and whether list items are verbal or non-verbal. Non-verbal items under a complete sentence end with no punctuation; verbal items each end with a period; items that complete an incomplete introductory sentence end with semicolons.
  - *Source:* "The app requires the following:
    the latest version of macOS
    a computer
    a printer" → *Target:* "L\u2019app XXX requiert ce qui suit :
    • la dernière version de macOS
    • un ordinateur Mac
    • une imprimante"
  - *Source:* "To reset your settings, follow these steps:
    Open System Settings.
    Click the button located in the top right.
    Reset your settings." → *Target:* "Pour réinitialiser vos réglages, procédez comme suit :
    Ouvrez l\u2019app Réglages système.
    Cliquez sur le bouton qui se trouve en haut à droite.
    Réinitialisez vos réglages."
  - *Source:* "The app requires:
    the latest version of macOS
    a computer
    a printer" → *Target:* "L\u2019app XXX requiert :
    • la dernière version de macOS;
    • un ordinateur Mac;
    • une imprimante."

## Grammar

- **Use Imperative for Instructions to the User**: Instructions or prompts addressed directly to the user should use the imperative form. They should not end with a period.
  - *Source:* "Confirm with iPhone" → *Target:* "Confirmez sur l\u2019iPhone"

- **Use Infinitive for Titles**: Titles should either use a substantive or the infinitive. They should never end with a period. Avoid using articles at the beginning of a title.
  - *Source:* "Enter your passcode" → *Target:* "Entrer le code"
  - *Source:* "Setup your Mac" → *Target:* "Configuration du Mac"

- **Prefer 'ne + pas' Over 'ne' Alone**: Use the full negation 'ne + pas' rather than the literary 'ne' alone for clearer and more natural software strings.
  - *Source:* "The shortcut cannot be the same as an existing shortcut." → *Target:* "Le raccourci ne peut pas être identique à un raccourci existant."

- **Capitalization in Canadian French**: Only the first word of a sentence and proper nouns are capitalized. Titles follow the same rule. References to UI options are treated as proper nouns and capitalized (first letter only). UI area names like 'centre de contrôle' are not capitalized in mid-sentence.
  - *Source:* "Access Settings and sign in with your Apple ID." → *Target:* "Accédez à l\u2019app Réglages et connectez-vous avec votre identifiant Apple."

- **Spelling forms**: Use traditional forms for accents and verbs: words like "Événement" (not "Évènement"), words with an accent circonflexe like "Apparaître" (not "Apparaitre"), traditional accents in verbs like céder, and traditional spellings for -eler and -eter verbs. Use rectified (1990) forms only in proper names or quotations, hyphenations in complex numbers, simplified plurals for compound and borrowed words, and the invariable past participle of the verb laisser.
  - *Source:* "event" → *Target:* "Événement (not: Évènement)"
  - *Source:* "Two thousand twenty-six" → *Target:* "deux-mille-vingt-six (not: deux mille vingt-six)"

## Interface Elements

- **Articles with Hardware vs. Software Names**: Always use a determiner before Apple hardware names (l'iPod, votre iPhone). Do not use an article before software names used as proper names. Always add 'l\u2019app' before the app name in full sentences to avoid ambiguity.
  - *Source:* "To open this link, open Messages on your iPhone." → *Target:* "Pour ouvrir ce lien, ouvrez l\u2019app Messages sur votre iPhone."

## Terminology

- **Strictly Avoid Anglicisms**: English terms must be strictly avoided in Canadian French written content, even when widely used in everyday speech. Always use the established French-Canadian equivalent. This is a stronger requirement than in French Universal.
  - *Source:* "email" → *Target:* "courriel (not: e-mail)"
  - *Source:* "spam" → *Target:* "pourriel (not: spam)"
  - *Source:* "hub" → *Target:* "concentrateur (not: hub)"

## Diversity And Inclusion

- **Use Gender-Neutral Language (Rédaction épicène)**: Prefer gender-neutral formulations whenever possible. Use collective nouns, neutral adjectives, and active voice to avoid gendered structures. Automatic Grammar Agreement can be used selectively for high-visibility strings to provide personalized gendered inflections.
  - *Source:* "customers" → *Target:* "la clientèle"

- **Avoid Color-Based Connotations**: Do not use color terms to imply security levels, positive/negative value, or access permissions. Replace such terms with neutral functional vocabulary.
  - *Source:* "blacklist" → *Target:* "liste de refus"
  - *Source:* "whitelist" → *Target:* "liste d\u2019acceptation"

## Style

- **Avoid using « Créer un nouveau »**: When translating "Create a new…", avoid adding « nouveau » (new) in the target.
  - *Source:* "Create a new file" → *Target:* "Créer un fichier (Button/title)
    Créez un fichier. (Description)"

- **« Depuis » restricted to temporal use**: The preposition "depuis" without temporal value must be avoided. Use "à partir de" or "de" instead:
  - *Source:* "Download the app from the App store" → *Target:* "Téléchargez l\u2019app à partir de l\u2019App Store."
