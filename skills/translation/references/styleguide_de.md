# German (de) — Software String Localization Style Guide

- **Informal address ("du")**: Users are addressed informally with "du" in lowercase ("du", "dein", "ihr", "euch" — never capitalized).

- **Imperative vs. infinitive in UI**: Strings ending with a period use the imperative form ("Bearbeite das Bild."), while strings without a period use the infinitive ("Bild bearbeiten"). This single punctuation cue determines the verb form.

- **Passive over direct address**: Where possible, prefer passive or impersonal constructions over directly addressing the user. E.g., "Möchtest du die Nachricht senden?" → "Soll die Nachricht gesendet werden?"

- **Gender-inclusive colon**: Use the gender colon (`:`) to form inclusive nouns — e.g., "Benutzer:in", "Mitarbeiter:innen". Avoid flooding strings with multiple colons; prefer gender-neutral terms ("Person", "Studierende", "Fachwissen") or plural forms to maintain readability. The order is masculine:feminine ("der:die Expert:in").

- **Compound hyphenation with app/product names**: App names in compounds require a hyphen ("Mail-Einstellungen", "iTunes-Mediathek"), but germanized loan words like "Server" or "Account" form closed compounds without hyphens ("Servereinstellungen", "Accountname").

- **Quotation marks for UI references**: Use German-style 9-low/6-high quotes: „ (\u201E) and “ (\u201C). UI element names must be quoted — e.g., Klicke auf \u201EWeiter\u201C. Nested quotes use single curly quotes: \u201EIn \u201AKarten\u2019 anzeigen\u201C. English app names (Safari, Health) generally do not get quotes.

- **No genitive-s on product names**: Never add a genitive -s to Apple product names or brand names. Use "von" instead: "Das neue iPhone von Apple" (not "Apples neues iPhone"), "die Seitentaste des iPhone" (not "des iPhones").

- **Variables with "von" for possessives**: For `%@'s` patterns, prefer "iPhone von %@" over "%@s iPhone" to avoid issues with names ending in s/x/z. Use the -s form only when space is critical. When reordering variables, add positional markers: `%1$@`, `%2$@`.

- **Ellipsis with non-breaking space**: In software, an ellipsis indicates a process ("Laden …" not "Wird geladen") and is always preceded by a non-breaking space. Also use ellipsis to signal that an action leads to a follow-up dialog, even if the source omits it.

- **Decimal comma and space thousands**: German uses comma as the decimal separator ("1.234,50 Euro") and non-breaking spaces (or periods in monetary amounts) for thousands grouping. Version numbers keep periods ("iOS 17.2"). Do not modify decimal points inside variables like "%.1f".

- **Non-breaking spaces in product names**: Multi-word product names ("Apple Watch", "Touch ID") use non-breaking spaces to prevent line breaks. Also use non-breaking spaces in abbreviations ("z. B."), between numbers and units ("3 %", "2 GB"), and percentage signs.

- **Units have no plural**: German units never take a plural form — "2 GB", "100 Byte" (not "Bytes"). Insert a non-breaking space between number and unit. For playback speed, no space before "x": "1,5x".

- **App name vs. service name distinction**: The translated app name uses German quotes and German terms ("die Musik-App", \u201EMusik\u201C), while the trademarked service name stays in English ("Apple Music"). Compounds with English service names use a hyphen: "Apple Music-App".

- **Key terminology diverging from Windows/common usage**: Apple German uses distinct terms — "sichern" (not "speichern") for save, "Taste" (not "Schaltfläche") for button, "Zeiger" (not "Cursor") for pointer, "Menü \u201EAblage\u201C" (not "Datei") for File menu, "streichen" (not "wischen") for swipe, "Batterie" (not "Akku") for battery.

- **Ampersand usage**: Use "&" in category names and titles ("Sicherheit & Datenschutz") following the source. In general text, spell out "und" or abbreviate as "u." — only fall back to "&" or "+" as a last resort for space constraints.
