# Italian (it) — Software String Localization Style Guide

- **Imperative for commands and buttons**: Commands, button labels, and option names use the imperative: "Seleziona tutto", "Mostra gli acquisti disponibili". For tabs, panels, and menu titles, prefer nouns over verbs: "Stampa" for "Printing". If the gerund in English refers to an ongoing action, use the 1st singular person of indicative present: "Exporting the files...", "Esporto i file...".

- **Foreign words never take Italian plurals**: English loan words remain in their singular form even when used as plurals. "Mantieni entrambi i file" (not "i files"). This applies universally to all non-Italian words if they are common nouns. If they are product names, keeping the final -S depends on the specific products, e.g. AirPods remains unchanged (gli AirPods), while we drop the S in "AirTags", "gli AirTag".

- **Curly double quotes for multi-word UI options**: Use Italian curly double quotes “ (\u201C) and ” (\u201D) around UI options and items consisting of two or more words within sentences: Fai clic su “Uscita forzata”. Do not quote single-word options (Fai clic su Condivisione), or app names. Nested quotes use single curly quotes (‘, \u2018 and ’, \u2019): “Imposta ‘Non disturbare’”. Apostrophes should always be curly as well (’, \u2019). The inch symbol in product names remains straight as in the source string (MacBook Pro 16").

- **Impersonal form for errors; "tu" for software**: Address users with "tu", but for error messages, use impersonal constructions: "Impossibile aprire il file" or "Avvio della periferica non riuscito" rather than addressing the user directly. 

- **Gender-inclusive rephrasing**: Avoid gendered constructions where possible. Rephrase "Sei sicuro di voler..." as "Confermi di voler..." or "Vuoi...?". "Non sei connesso a internet" becomes "La connessione a internet non è attiva". 

- **Euphonic "d" before Apple product names**: Always use "ad" before products starting with lowercase "i" (ad iPhone, ad iPad, ad iMac) and before products starting with "Apple" (ad Apple Watch, ad Apple Pay), regardless of standard pronunciation-based rules.

- **No space before percent; comma as decimal separator**: The percent sign attaches directly to the number ("50%"). Use comma as decimal separator and period as thousands separator for 5+ digit numbers ("15.000"). Always include leading zero for decimals ("0,8 m" not ".8 m"). No space before degree symbol alone ("12°") but space before scale ("12 °C").

- **Drop "please" and demonstrative adjectives**: Never translate "please" in instructions: "Please use another name" becomes "Utilizza un altro nome". Minimize demonstrative adjectives ("questo/questa") with product names unless needed to distinguish between multiple devices.

- **Suppress possessive adjectives with products**: Omit possessives before hardware/software names: "Inserisci la password" (not "Inserisci la tua password"), "configura iPhone utilizzando i dati cellulare" (not "configura il tuo iPhone").

- **UI option gender defaults to feminine**: When adjectives or past participles refer to a UI option starting with a verb, use the feminine form because the implied nouns (opzione, impostazione, modalità) are feminine: Solo quando "Preferisci WLAN 6E" è disattivata. If the UI option starts with a noun, adjectives and past participles should match the noun gender, e.g. "Voice Recognition is off", ""Riconoscimento vocale" è disattivato".

- **Replace em/en dashes with hyphens or colons**: Italian does not use em dashes in running text. Replace em dashes introducing asides with commas or parentheses. Replace em/en dashes in headings with colons: "Missed call — from your iPhone" becomes "Chiamata persa: da iPhone". Use non-breaking hyphens (\u2011) in compound words like Wi‑Fi.

- **Brevity strategies for space-constrained UI**: Suppress articles when space is tight ("Scarica immagine" over "Scarica l’immagine"). Prefer "Usa" over "Utilizza" and "Vuoi" over "Desideri".
