# Malayalam (ml) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Malayalam uses single curly quotation marks ‘ (\u2018) and ’ (\u2019) for UI feature references, double curly quotation marks “ (\u201C) and ” (\u201D) for nested quotes, and the curly apostrophe ’ (\u2019).
  - *Source:* "Hold Select to clear" → *Target:* "മായ്ക്കാൻ, \u2018തിരഞ്ഞെടുക്കൂ\u2019 അമർത്തി പിടിക്കൂ"

## Tone And Voice

- **Smart but casual**: Use a written colloquial Malayalam — a fine balance between spoken and formal written language — that sounds natural and is closer to formal than informal. Do not use words that are very hip or trendy; keep a neutral, descriptive style. Follow the style of respected Malayalam publications, which blend formal and colloquial Malayalam effectively.
  - *Source:* "%@ may not have arrived at their destination yet." → *Target:* "%@ ലക്ഷ്യസ്ഥാനത്ത് ഇതുവരെ എത്തിയിട്ടുണ്ടാവില്ല."

- **Prefer Transliteration Over Unnatural or Archaic Malayalam Terms**: When a Malayalam equivalent is archaic, obscure, or not widely used in its specific context, transliterate the English term instead. Common technical terms like Desktop, Click, Menu, Installation should be transliterated because Malayalam users encounter them in that form daily.
  - *Source:* "Installation" → *Target:* "ഇൻസ്റ്റലേഷൻ (not സ്ഥാപിക്കൽ)"

## Command Verb Form

- **The verb form**: UI command labels (buttons, menu commands) use the semi-formal imperative ‘ചെയ്യൂ’. Avoid the longer തിരഞ്ഞെടുക്കുക form to save space.
  - *Source:* "Select a network connection" → *Target:* "ഒരു നെറ്റ്‌വ൪ക്ക് കണക്ഷൻ തിരഞ്ഞെടുക്കൂ"

## Addressing Users

- **Address Users with Semi-Formal നിങ്ങൾ**: Use നിങ്ങൾ, നിങ്ങളുടെ, and നിങ്ങൾക്ക് for the English words you and your. This is the appropriate semi-formal register for all user-facing content. Omit the pronoun in sentences where Malayalam naturally drops it to keep text concise and natural.
  - *Source:* "You're sending info about websites you visit to Apple" → *Target:* "സന്ദർശിക്കുന്ന വെബ്‌സൈറ്റുകളെക്കുറിച്ചുള്ള വിവരങ്ങൾ നിങ്ങൾ Apple-ലേക്ക് അയയ്ക്കുന്നു"

## Abbreviations

- **Abbreviation Rules for Malayalam Words and Units**: Abbreviated Malayalam words end with a period unless the abbreviated form has become an accepted standalone word (e.g., ഡോ., ഉദാ.). Commonly accepted English acronyms such as TV and SMS may be written in Malayalam script without full stops (ടിവി, എസ്എംഎസ്). All other abbreviations stay in English as in the source.
  - *Source:* "Dr." → *Target:* "ഡോ."

## Acronyms

- **Keep Acronyms in English Unless a Common Malayalam Equivalent Exists**: Acronyms like WiMAX and LAN that have no common Malayalam equivalent should remain in English. Acronyms that have effectively become Malayalam words (e.g., LASER) do not need to be kept in English. Technical file format abbreviations (PDF, RTF, DOC) must never be translated or transliterated.
  - *Source:* "LAN" → *Target:* "LAN"
  - *Source:* "LASER" → *Target:* "ലേസർ" (acronym that has become a Malayalam word)

## Date And Time

- **Date Format and Month/Day Names**: Write dates as DD Month YYYY in Malayalam (e.g., 03 ഓഗസ്റ്റ് 2001). Do not use numeric-only formats like 03.08.2001. Do not translate or localize AM/PM — keep it in English, matching source capitalization. Do not add Malayalam plural suffixes to units of time (use മൂന്ന് മണിക്കൂർ, not മൂന്ന് മണിക്കൂറുകൾ).
  - *Source:* "August 3, 2001" → *Target:* "3 ഓഗസ്റ്റ് 2001"

## Measurements

- **Retain Electronic and Computer Units in English**: Units related to electronics and computing (GB, KB, dB, kbps) must remain in English. Use °C and °F for temperature short forms. Do not convert imperial to metric.
  - *Source:* "8 GB" → *Target:* "8 GB"

## Numerals

- **Use International Numerals and Indian Separator System**: Keep numerals as international digits (0–9) — do not convert them to native Malayalam numerals. Whether digits ultimately display as international or native is a user setting the translation can't see, so don't change the numeral system yourself. Group large numbers using the Indian separator system (e.g., 10,00,000).
  - *Source:* "1,000,000 songs" → *Target:* "10,00,000 പാട്ടുകൾ"

- **Ordinal Numbers Up to Nine Use Full Malayalam Words**: For ordinal numbers up to 9 without variables, write the full Malayalam word (ഒന്നാമത്തെ, രണ്ടാമത്തെ). For numbers above 9 or when a variable is used, attach the suffix with a hyphen (10-ആമത്തെ). Avoid using dotted circle diacritics (1-ാമത്തെ) as they render visibly on UI.
  - *Source:* "1st, 10th" → *Target:* "ഒന്നാമത്തെ, 10-ആമത്തെ"

## Special Characters

- **Translate & as ആൻഡ്; Use Visarga Correctly**: Do not use the & symbol in Malayalam text. Translate it as ആൻഡ് in fully transliterated phrases where there is no space issue. Use the conjunction ഉം…ഉം (or -ഉം suffix) when linking two Malayalam words. Add visarga (ഃ) wherever it is grammatically required in native words.
  - *Source:* "Display & Brightness" → *Target:* "ഡിസ്പ്ലേയും ബ്രൈറ്റ്‌നസും"
  - *Source:* "Black & White" → *Target:* "ബ്ലാക്ക് ആൻഡ് വൈറ്റ്"

## Punctuation

- **Use Single Curly Quotes for UI Feature References**: In UI strings, enclose feature names and functionality names in single curly quotes ‘ (\u2018) and ’ (\u2019) when grammatical ambiguity could arise. Use them minimally. For nested quotations, double curly quotes go outside and single curly quotes inside. Never use straight quotes (" ") in UI strings.
  - *Source:* "Hold select to clear" → *Target:* "മായ്ക്കാൻ, \u2018തിരഞ്ഞെടുക്കൂ\u2019 അമർത്തി പിടിക്കൂ"

- **Straight quotes in HTML codes**: Straight quotes appearing in program files or HTML codes should retain as is.
  - *Source:* "Tap Settings <img src="settings_gear.jpg" alt="Gear icon for Settings" width="25" height="25">" → *Target:* "ക്രമീകരണത്തിൽ ടാപ്പ് ചെയ്യൂ <img src="settings_gear.jpg" alt="ക്രമീകരണത്തിന്റെ ഗിയർ ഐക്കൺ" width="25" height="25">"

## Interface Elements

- **Naming Conventions — Apps and Feature Names**: This rule is applicable exclusively to transliterated app and feature names. Considering them as proper nouns, transliterated app names do not take Malayalam inflectional suffixes. They retain the English plural marker as an integral part of the identifier itself. When the English app name carries no plural marker, the transliteration stands alone without any suffix. This distinction governs all morphological decisions for app names in Malayalam. Malayalam phonology permits the integration of the ‘-സ്’ suffix in single-word transliterations without violating natural pronunciation. Translated names, by contrast, take the grammatically appropriate Malayalam form of the source term.
  - *Source:* "Photos, Maps, Games" → *Target:* "ഫോട്ടോസ്, മാപ്പ്സ്, ഗെയിംസ്"

- **Button Names in Imperative with Helping Verb**: Translate buttons and callout bar items using the semi-formal imperative form with the helping verb ചെയ്യൂ to avoid ambiguity with nouns. Exception — triggered by the source term: when the source string is a single standalone ‘Cut’, ‘Copy’, ‘Paste’, ‘Delete’, or ‘On’/‘Off’, write it without the helping verb.
  - *Source:* "Edit" → *Target:* "എഡിറ്റ് ചെയ്യൂ"

- **Naming Conventions — Generic Collections**: Transliterated nouns must follow Malayalam plural suffixes (കൾ, ക്കൾ, ങ്ങൾ), not English plurals. When a category label describes a generic collection of items, it is a common noun and must always take the appropriate Malayalam suffix, regardless of whether it is transliterated or translated. Use വീഡിയോകൾ (not വീഡിയോസ്).
  - *Source:* "Apps, Widgets, Playlists, Tabs, Filters" → *Target:* "ആപ്പുകൾ, വിജറ്റുകൾ, പ്ലേലിസ്റ്റുകൾ, ടാബുകൾ, ഫിൽട്ടറുകൾ"

## Spelling And Grammar

- **Transliteration Spelling Conventions**: Indian English has adopted words from both American English and British English. Find out which version is more popular for the locale while making this choice. Changing cellular to mobile, biking to cycling, elevator to lift is fine, but not for ATM as cashpoint. ATM is a popular term used in India, so use it. Also, in technical terms, American English is widely used like mail, mailbox. Therefore, evaluate carefully and localize as per the needs of Malayalam language.
  - *Source:* "Elevator, Biking" → *Target:* "ലിഫ്റ്റ്, സൈക്ലിങ്"
  - *Source:* "Import" → *Target:* "ഇംപോർട്ട്"
  - *Source:* "English Spelling" → *Target:* "ഇംഗ്ലീഷ് സ്പെല്ലിങ്"
  - *Source:* "intent/indent" → *Target:* "ഇന്റന്റ്/ഇൻഡന്റ്"
  - *Source:* "Character" → *Target:* "കാരക്റ്റർ"
  - *Source:* "Wallet" → *Target:* "വാലറ്റ്"
  - *Source:* "Port" → *Target:* "പോർട്ട്"
  - *Source:* "Gate, Space" → *Target:* "ഗേറ്റ്, സ്പേസ്"
  - *Source:* "Domain, Train, Portrait, Noise" → *Target:* "ഡൊമെയിൻ, ട്രെയിൻ, പോർട്രെയ്റ്റ് , നോയ്സ്"
  - *Source:* "Service" → *Target:* "സർവീസ്"

- **Use Active Voice; Reserve Passive for Ambiguous Subjects**: Prefer active voice in Malayalam as passive constructions sound overly formal and take more space. Use passive voice only when the subject of the sentence cannot be identified from the string, or when restructuring would create ambiguity (e.g., 'is not supported').
  - *Source:* "Files are being transferred" → *Target:* "ഫയലുകൾ ട്രാൻസ്ഫർ ചെയ്യുന്നു (active)"

- **Postpositions with Variables — Use Descriptive Words**: Never directly append a postposition to a variable when phonotactic combinations like ‘-ന്റെ’ or ‘-യുടെ’ would be ambiguous or incorrect at runtime. Instead, insert a descriptive word (എന്നയാളുടെ for a person, എന്ന ഡിവൈസിന്റെ for a device) to carry the postposition.
  - *Source:* "%@'s iPhone" → *Target:* "%@ എന്നയാളുടെ iPhone"
  - *Source:* "Open in %@" → *Target:* "%@ എന്നതിൽ തുറക്കൂ"

- **Postposition rule for category label, App and feature names when used in running sentences**: When a category label, app name, or feature name appears in a running sentence with a Malayalam postposition attached to it, wrap the name in single curly quotation marks.

Malayalam postpositions attach directly to the preceding word through agglutination. When a postposition attaches to a translated/transliterated noun, the combined form can be misread as a native Malayalam word, stripping the name of its noun identity. Single quotation marks preserve the name as a distinct noun within the sentence. When the name is already followed by ആപ്പ് (App), the quotation marks are not required — ആപ്പ് itself signals that the preceding word is an app name.

  - *Source:* "Go to Notifications" → *Target:* "\u2018അറിയിപ്പുകളി\u2019ലേക്ക് പോകൂ" (not അറിയിപ്പുകളിലേക്ക് പോകൂ)
  - *Source:* "Show in Photos" → *Target:* "\u2018ഫോട്ടോസി\u2019ൽ കാണിക്കൂ"
  - *Source:* "Show in Photos App" → *Target:* "ഫോട്ടോസ് ആപ്പിൽ കാണിക്കൂ" (no quotes — ആപ്പ് already marks it as an app name)

## Orthography

- **Encode the ന്റ conjunct consistently**: Encode the conjunct ‘ന്റ’ (nta) as the codepoint sequence ന + ് + റ (U+0D28 U+0D4D U+0D31), not the alternative ൻ + ് + റ (U+0D7B U+0D4D U+0D31). Both render the same glyph, but the ന-based sequence gives one consistent Unicode encoding everywhere for searchability and avoids rendering issues in some fonts. Normalize any ൻ + ് + റ encoding to ന + ് + റ.
  - *Source:* "Internet" → *Target:* "ഇന്റർനെറ്റ്"

## Variables

- **Number Variables When Reordering; Preserve Decimal Format Strings**: Keep all variables exactly as they appear in the source. If Malayalam word order requires reordering, number all variables with the n$ positional index immediately after the % sign. If variables in the source are already numbered, then reorganize them as needed in the translation.
  - *Source:* "Downloaded %@ files out of a total of %@" → *Target:* "മൊത്തം %2$@ ഫയലുകൾ ഉള്ളതിൽ %1$@ ഡൗൺലോഡ് ചെയ്തു"

## Diversity And Inclusion

- **Use Gender-Inclusive Language**: Avoid gendered pronouns (അവൻ, അവന്റെ, അവൾ, അവളുടെ) when the source does not specify a gender — refer to people by name or with gender-neutral alternatives such as അവർ (they) or ആൾ (person); when the source establishes a specific gender, follow it. For role titles use gender-neutral forms: ആർട്ടിസ്റ്റുകൾ (not കലാകാരൻമാർ) for artists.
  - *Source:* "Matthew opened his MacBook." → *Target:* "മാത്യു തന്റെ MacBook തുറന്നു."

- **Avoid biases and stereotypes**: Avoid translations that reinforce biases or stereotypes based on gender, race, physical ability, or age. Use gender-neutral language wherever possible, avoiding binary representations. When translating content related to people with disabilities, apply people-first language by placing the person before the condition, and focus on ability rather than limitation.

Avoid using അന്ധൻ, അന്ധ for the blind
Instead use കാഴ്ചയ്ക്ക് ബുദ്ധിമുട്ടുള്ളവർ;
Avoid using വൃദ്ധൻ, വൃദ്ധ for Elderly
Instead use മുതി൪ന്ന പുരുഷൻ, മുതി൪ന്ന സ്ത്രീ
  - *Source:* "The blind" → *Target:* "കാഴ്ചയ്ക്ക് ബുദ്ധിമുട്ടുള്ളവർ"

- **Emoji — Avoid Demographic and Religious Stereotyping**: Do not associate emoji depicting head coverings or cultural dress with a specific religion, sect, or ethnicity. Use descriptive neutral terms (ടർബൻ, തലപ്പാവ്, മുഖാവരണം, ശിരോവസ്ത്രം) instead of religious identifiers (സിക്ക്, ഹിജാബ്, ബുർഖ). Avoid prepositions and helping words in emoji translations unless necessary.
  - *Source:* "man with turban emoji" → *Target:* "ടർബൻ ധരിച്ചയാൾ ഇമോജി"
