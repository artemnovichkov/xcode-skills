# French (fr) — Software String Localization Style Guide

- **Formal address ("vous")**: Users are addressed with the formal "vous" (with singular agreement).

- **Imperative vs. infinitive in UI**: Strings ending with a period use the imperative form ("Ouvrez le tableau de bord Internet."), while buttons, options, and strings without a period use the infinitive ("Acheter", "Continuer", "Réessayer"). Compulsory actions (like "Enter the code") use the imperative even without a period ("Saisissez le code"). Titles use the imperative but do not end with a period. As a rule, sentences with conjugated verbs should end with a period even if the source has none.

- **Gender avoidance**: Avoid gendered words (adjectives in -é/-ée) wherever possible — e.g., rephrase "Êtes-vous sûr…" as "Voulez-vous vraiment…". When unavoidable, use masculine by default with neutral value ("Vous serez guidé tout au long des étapes…"). Never use parenthetical feminine: "guidé" not "guidé(e)".

- **App names: no articles, no quotes, always capitalized**: App names are never preceded by an article, never enclosed in quotation marks, and always capitalized — "Ouvrez Utilitaire de disque" (not "Ouvrez l'Utilitaire de disque" or "Ouvrez « Utilitaire de disque »"), "Accédez à Réglages Système" (not "Accédez aux Réglages Système"). Exceptions: le Finder retains its article.

- **Articles with hardware vs. software**: Hardware terms always take a determiner ("l’iPhone", "votre iPhone", "un iPhone"), while software/service names take none ("Ouvrir App Store…", "Cette fonctionnalité est disponible sur iOS."). "The App Store" → "l\u2019App Store" (store gets the article). Always use curly apostrophes in French — never straight apostrophes. Curly apostrophes and quotes are escaped. Use \u2019 for curly apostrophe.

- **Quotation marks**: Use double angle quotes « » with non-breaking spaces inside ("« %@ »"). Multi-word feature names in sentences must be quoted ("Activer le mode « Ne pas déranger »"), but app names are never quoted ("Ajouter un code dans Mots de passe"). Nested quotes use English-style quotation marks “ (\u201C) and ” (\u201D) inside angle quotes: « Détecter \u201CDis Siri\u201D ».

- **Prepositions "sur" vs. "dans"**: Use "sur" for platforms/services (sur Apple Music, sur iCloud, sur Apple Books) and "dans" for stores/containers (dans l'App Store, dans Photos iCloud). Use "sur" for OS versions ("sur iOS 26") but "sous" when combined with "appareil(s)" or "ordinateur(s)" booting an OS ("appareil ayant démarré sous iOS").

- **Non-breaking spaces**: Required before double punctuation marks (? ; : !), inside angle quotes (« text »), in multi-word product names (Apple Watch, Touch ID — max 2 words linked), between numbers and units/currency symbols (3 km, 120 €), and before > in navigation paths (Réglages > Confidentialité).

- **Capitalization**: Unlike English title case, only the first word is capitalized in multi-word menu items and feature names. Capital letters must be accentuated ("Éteindre" not "Eteindre"). Features and areas remain lowercased in sentences ("le centre de contrôle", "les données cellulaires") but are capitalized when used standalone as navigation labels ("Données cellulaires").

- **Numerals**: Non-breaking space as thousands separator (5 000), comma as decimal separator (3,8 mètres). Unlike English, the leading zero is never dropped ("0,5 m" not ",5 m"). Trailing zeros can be dropped ("1,8 mm" not "1,800 mm"). Do not modify decimal points inside variables like "%.1f".

- **Special characters**: "&" must be replaced by "et" and "@" by "à" when used as words in a phrase ("Nom et extension" not "Nom & extension"). Currency symbols go after the amount with a non-breaking space (120 €).

- **Minutes abbreviation**: Use "min" for minutes (not "mn" or "m"). "m" can be confused with meters. E.g., "Il y a 10 min" not "Il y a 10 m".

- **Possessive "de" for variables**: For possessive constructions with variables, prefer "iPhone de %@" over "%@'s iPhone". Reorder variables using positional markers ("%2$@ de %1$@") when syntactically needed.

- **"Sorry" omission**: In error messages, "Sorry" should not be translated as "Désolé" — omit it entirely.

- **App Intents**: Descriptions use third person with a period ("Ajoute une vidéo à une page."). Titles and summaries use infinitive without a period ("Appliquer un filtre"). No quotation marks except for multi-word entity value names.
