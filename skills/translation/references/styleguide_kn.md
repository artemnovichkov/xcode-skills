# Kannada (kn) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Kannada uses curly double quotation marks “ (\u201C) and ” (\u201D), and the curly apostrophe ’ (\u2019).
  - *Source:* "Open \u201C%@\u201D." → *Target:* "\u201C%@\u201D ಅನ್ನು ತೆರೆಯಿರಿ."

## Abbreviations

- **Translate Abbreviations to Full Form; Abbreviate Only Under Space Constraint**: Prefer translating abbreviations to their full Kannada form. Abbreviate only when space restrictions make the full form impossible. Use a period after abbreviated terms. Keep abbreviated country names (UAE, UK, etc.) in English. Date/time abbreviations follow CLDR entries.
  - *Source:* "No." → *Target:* "ಸಂಖ್ಯೆ" (full form) / "ಸಂ." (space-restricted)
  - *Source:* "Dept." → *Target:* "ವಿಭಾಗ"

## Acronyms

- **Transliterate Well-Known Acronyms; Keep Technical Ones in English**: Transliterate commonly recognized acronyms into Kannada script (e.g., UNESCO → ಯುನೆಸ್ಕೋ, NASA → ನಾಸಾ). For technical file-format abbreviations and other IT acronyms that are better left unlocalized (PDF, MAC, POP), keep them in English.
  - *Source:* "UNESCO" → *Target:* "ಯುನೆಸ್ಕೋ"
  - *Source:* "POP Server" → *Target:* "POP ಸರ್ವರ್"

## Addressing Users

- **Use Formal Honorific Forms for 'You' and Verbs**: Always address the user with the formal second-person ನೀವು/ನಿಮ್ಮ rather than the informal ನೀನು/ನಿನ್ನ. Use the honorific verb form ending in ಮಾಡಿ, ಹೇಳಿ, etc. rather than the plain ಮಾಡು, ಹೇಳು. Use the formal plural ಅವರು for he/she and ಅವರ for him/her.
  - *Source:* "Your information" → *Target:* "ನಿಮ್ಮ ಮಾಹಿತಿ" (not "ನಿನ್ನ ಮಾಹಿತಿ")
  - *Source:* "Make a call" → *Target:* "ಕರೆ ಮಾಡಿ" (not "ಕರೆ ಮಾಡು")

## Date And Time

- **Date Format DD/MM/YYYY; Keep AM/PM in English**: Format dates as DD/MM/YYYY or in the form '12ನೇ ಮಾರ್ಚ್ 2023' (for 12th March 2023). Always write the month name in Kannada when it is spelled out. Keep AM/PM labels in English as per the source. For time ranges, use a hyphen (e.g., 9 am - 6 pm) to avoid space and suffix issues.
  - *Source:* "March 12, 2023" → *Target:* "12 ಮಾರ್ಚ್ 2023"
  - *Source:* "9 am to 6 pm" → *Target:* "9 am - 6 pm"

## Diversity And Inclusion

- **Use Gender-Neutral Language**: Use the honorific form to address users generically, which is inherently gender-inclusive in Kannada. Avoid gendered terms whenever possible; prefer neutral terms like ಜನರು (people), ಬಳಕೆದಾರರು (users), or ವ್ಯಕ್ತಿ (person). When gender must be expressed, use both masculine and feminine forms or rephrase.
  - *Source:* "You're becoming a world-building master!" → *Target:* "ನೀವು ವಿಶ್ವ ನಿರ್ಮಾಣದ ಮಾಸ್ಟರ್ ಆಗುತ್ತಿದ್ದೀರಿ!"

## General Advice

- **Prioritize Readability and Conciseness in Space-Constrained UI**: Kannada translations are generally longer than their sources. In iOS and watchOS contexts, be as concise as possible to avoid truncation. Suppress articles where safe, choose shorter verb variants, and avoid verbose constructions. Abbreviation is the last resort.
  - *Source:* "%@ sent you an email." → *Target:* "%@ ಅವರು ನಿಮಗೆ ಇಮೇಲ್ ಅನ್ನು ಕಳುಹಿಸಿದ್ದಾರೆ." (full) / "%@, ನಿಮಗೆ ಇಮೇಲ್ ಕಳುಹಿಸಿದ್ದಾರೆ" (space-restricted)

## Grammar

- **No Articles: Do Not Translate 'a/an' as ಒಂದು**: Kannada has no articles. Do not translate English 'a' or 'an' as ಒಂದು (one) unless the meaning genuinely requires the numeral one. Most sentences are grammatically correct and natural without it.
  - *Source:* "Buy a pen" → *Target:* "ಪೆನ್ ಖರೀದಿಸಿ" (not "ಒಂದು ಪೆನ್ ಖರೀದಿಸಿ")

- **Vibhakti (Case Suffixes) with Transliterated and DNT Terms**: Attach case suffixes to transliterated and DNT terms following Kannada Sandhi rules. For Dwitiya Vibhakti (ಅನ್ನು): add a space before ಅನ್ನು if the word ends with virama (್); attach directly (using phonetic Sandhi) if it ends with a vowel. For other cases, use ZWNJ after virama-ending words.
  - *Source:* "Update" (accusative) → *Target:* "ಅಪ್‌ಡೇಟ್ ಅನ್ನು"
  - *Source:* "Face ID" (accusative) → *Target:* "Face IDಯನ್ನು"
  - *Source:* "Finder" (locative) → *Target:* "Finderನಲ್ಲಿ"

- **Pluralization: Use Kannada Suffix ಗಳು for Transliterated Words**: Pluralize transliterated English words using the Kannada suffix ಗಳು (not the English -s). Attach the suffix directly to the word with no space. Exception: app and feature names that are inherently plural in English (e.g., Podcasts, AirPods) should match the source form.
  - *Source:* "Passcodes" → *Target:* "ಪಾಸ್‌ಕೋಡ್‌ಗಳು" (not "ಪಾಸ್‌ಕೋಡ್ಸ್")
  - *Source:* "HomePods" → *Target:* "HomePodಗಳು" (not "HomePod ಗಳು")

- **Syntax: Use Imperative Form for Commands and Buttons**: For user-action buttons, command names, dialog box titles, and instructions, use the imperative verb form. Include a helping verb (ಮಾಡಿ, ನೀಡಿ) where omitting it would create ambiguity. In space-restricted contexts, the helping verb may be dropped.
  - *Source:* "Install" → *Target:* "ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡಿ"
  - *Source:* "Reply" → *Target:* "ಪ್ರತ್ಯುತ್ತರಿಸಿ"
  - *Source:* "Share" → *Target:* "ಹಂಚಿಕೊಳ್ಳಿ"

- **Active vs. Passive Voice**: Follow the voice of the source as closely as possible. Prefer passive constructions when the string is directed at the user without identifying an explicit subject (i.e., when neither 'what' nor 'who' is stated in the string).
  - *Source:* "Updating…" → *Target:* "ಅಪ್‌ಡೇಟ್ ಮಾಡಲಾಗುತ್ತಿದೆ…"
  - *Source:* "You blocked this contact." → *Target:* "ನೀವು ಈ ಸಂಪರ್ಕವನ್ನು ಬ್ಲಾಕ್ ಮಾಡಿದ್ದೀರಿ."

- **Headings and Titles: Use Nominalized and Infinitive Forms**: Titles should convey as much information as possible about the ensuing text. If the heading begins with a gerund, use a nominalized form in Kannada (e.g., ಮಾಡುವಿಕೆ). If the source title uses an imperative verb (e.g., Make), translate it using the infinitive verb form (e.g., ಮಾಡುವುದು). Use the infinitive form for 'How to' section headings. Titles should be concise and use active nouns.
  - *Source:* "Installing software" → *Target:* "ಸಾಫ್ಟ್‌ವೇರ್ ಇನ್‌ಸ್ಟಾಲ್ ಮಾಡುವಿಕೆ"
  - *Source:* "How to send the file" → *Target:* "ಫೈಲ್ ಅನ್ನು ಕಳುಹಿಸುವುದು ಹೇಗೆ"
  - *Source:* "Make a FaceTime video call" → *Target:* "FaceTime ವೀಡಿಯೊ ಕರೆಯನ್ನು ಮಾಡುವುದು"

## Interface Elements

- **Category Labels: Countable Items (Common Noun)**: When a category label refers to actual, literal countable items inside an app (rather than the app container itself), treat it as a common noun and apply the native Kannada plural suffix '-ಗಳು'.
  - *Source:* "unread messages" → *Target:* "ಓದದಿರುವ ಸಂದೇಶಗಳು"

- **App Names in Sentences: Use 'ಆ್ಯಪ್' as a Morphological Buffer**: When an app name is used in a sentence, append the generic noun 'ಆ್ಯಪ್' (app) immediately after it. Attach any case suffixes (Vibhakti) directly to 'ಆ್ಯಪ್' to preserve the app name's exact identity and prevent unnatural consonant conjuncts.
  - *Source:* "Go to Settings" → *Target:* "ಸೆಟ್ಟಿಂಗ್ಸ್ ಆ್ಯಪ್‌ಗೆ ಹೋಗಿ"

- **App Names: Use Singular Form for Translated Apps**: When translating app names into Kannada, use the singular form. The native plural suffix '-ಗಳು' strictly denotes a physical count and creates semantic contradictions for app containers. Use the singular form to represent a unified category.
  - *Source:* "Books" → *Target:* "ಪುಸ್ತಕ"

- **App Names: Retain English Plural 's' in Transliterations**: Transliterated app names function as proper nouns and loan words. Treat the English plural marker '-s' as an indivisible part of the proper noun's root identity. Do not replace it with or add Kannada plural suffixes.
  - *Source:* "Settings" → *Target:* "ಸೆಟ್ಟಿಂಗ್ಸ್"

- **UI Categories: Use Native Plural '-ಗಳು' for General Collections**: For general UI elements that function as common nouns representing a collection of items, use the native Kannada plural suffix '-ಗಳು' following standard grammar rules.
  - *Source:* "Downloads" → *Target:* "ಡೌನ್‌ಲೋಡ್‌ಗಳು"

- **Key Names and Keyboard Shortcuts**: Transliterate key names (⌘ command → ಕಮಾಂಡ್, ⇧ shift → ಶಿಫ್ಟ್). When a key name is followed by the word 'key', render it as e.g. ಕಮಾಂಡ್ ಕೀ. For keyboard shortcut combinations such as ⌘N, copy them unchanged—do not localize the letter.
  - *Source:* "command key" → *Target:* "ಕಮಾಂಡ್ ಕೀ"
  - *Source:* "⌘N" → *Target:* "⌘N" (unchanged)

## Terminology

- **Prefer Transliteration Over Archaic Kannada for Technical Terms**: For technical terms that have become part of everyday speech, transliterate rather than translate. Use a natural Kannada term only when it is immediately clear to the target audience. Avoid archaic Sanskritized vocabulary that users will not recognize.
  - *Source:* "Password" → *Target:* "ಪಾಸ್‌ವರ್ಡ್" (not "ಗುಪ್ತಪದ")
  - *Source:* "Update" → *Target:* "ಅಪ್‌ಡೇಟ್" (not "ನವೀಕರಣ")

- **Prefer Natural Kannada for General Terms (Non-App)**: Use a natural, widely understood Kannada term when it is immediately clear to the audience. When a word like 'Books' is used as a general common noun (and not as the singular Apple App name), translate it using the native plural suffix. Avoid archaic Sanskritized vocabulary that users will not recognize.
  - *Source:* "Books" → *Target:* "ಪುಸ್ತಕಗಳು" (widely understood Kannada term)

- **Color Names: Translate Standard Colors**: Translate universally recognized basic colors with established Kannada terms into their direct Kannada equivalents.
  - *Source:* "Red" → *Target:* "ಕೆಂಪು"

- **Color Names: Transliterate Coined Colors**: Consistently transliterate coined color names designed for specific aesthetic or marketing purposes to maintain brand identity and marketing appeal.
  - *Source:* "Midnight Black" → *Target:* "ಮಿಡ್‌ನೈಟ್ ಬ್ಲ್ಯಾಕ್"

- **Color Names: Do Not Translate Proprietary Brand Colors**: Leave proprietary or brand-specific color names in English to maintain brand identity and avoid naming conflicts, especially when indicated by an engineering comment.
  - *Source:* "Bleu Pastel" → *Target:* "Bleu Pastel"

- **Transliteration: Follow Indian/UK English Pronunciation**: When transliterating, use Indian or UK English equivalents as the reference pronunciation rather than American English. The standard reference is the Oxford Dictionary of English (ODE). For example, use Network Provider instead of Carrier, Mobile instead of Cellular and Full-stop instead of Period.
  - *Source:* "Carrier" → *Target:* "ನೆಟ್‌ವರ್ಕ್ ಪೂರೈಕೆದಾರರು"
  - *Source:* "Carrier Network" → *Target:* "ಮೊಬೈಲ್ ನೆಟ್‌ವರ್ಕ್"

## Measurements

- **Keep Electronic/Computer Units in English; Translate Expanded Forms**: Units related to electronics and computing (MB, GB, TB, 720p, 4K) should remain in English as per the source. For other units with expanded Kannada equivalents (e.g., kilometer → ಕಿಲೋಮೀಟರ್), translate the full form and keep the abbreviation in English in parentheses.
  - *Source:* "Kilometer (km)" → *Target:* "ಕಿಲೋಮೀಟರ್ (km)"
  - *Source:* "Gigabyte (GB)" → *Target:* "ಗಿಗಾಬೈಟ್ (GB)"

## Numerals

- **Use International Numerals; Spell Out Numbers in Context**: The system default for Kannada is international numerals. Use numerals (420) in scientific, technical, statistical, and UI contexts. Spell out numbers in full (ನಾಲ್ಕು ನೂರಾ ಇಪ್ಪತ್ತು) when appropriate to the prose context. Follow the source format as a guide.
  - *Source:* "10th" → *Target:* "10ನೇ"
  - *Source:* "Ten" → *Target:* "ಹತ್ತು"

- **Apply Indian Comma Grouping System for Large Numbers**: The Indian comma system must be used for large numbers - commas are placed after thousands, then lakhs and crores (e.g. 10,00,000 not 1,000,000). Hard-coded numbers must always be in international numeral form (0-9). Always leave a space between a number and the following word or unit.
  - *Source:* "1,000,000 songs" → *Target:* "10,00,000 ಹಾಡುಗಳು"

## Special Characters

- **Use ಮತ್ತು Instead of & in Kannada Text**: When you render a phrase in Kannada script — whether you translate or transliterate it — write 'and' as ಮತ್ತು, never the ampersand (&). This applies even to English phrases you transliterate (both examples below are English, and both take ಮತ್ತು). A literal & survives only inside a name kept verbatim in Latin script (a brand or product name you are not transliterating), where the & sits between Latin-script words rather than Kannada ones.
  - *Source:* "Display & Brightness" → *Target:* "ಡಿಸ್‌ಪ್ಲೇ ಮತ್ತು ಬ್ರೈಟ್‌ನೆಸ್"
  - *Source:* "Sounds & Haptics" → *Target:* "ಸೌಂಡ್ಸ್ ಮತ್ತು ಹ್ಯಾಪ್ಟಿಕ್ಸ್"

## Transliteration (Indian/UK English Pronunciation)

- **Map Starting Flat 'a' Sound (/æ/)**: When a word starts with an 'a' that makes a flat /æ/ sound (e.g., App, Access, Apple) with no preceding consonant, use the special vowel combination ಆ್ಯ.
  - *Source:* "App" → *Target:* "ಆ್ಯಪ್"

- **Map Flat 'a' Sound (/æ/)**: When the letter 'a' makes a flat /æ/ sound after a consonant (e.g., Tap, Tag), use the ya-vattu suffix ್ಯಾ.
  - *Source:* "Tap" → *Target:* "ಟ್ಯಾಪ್"

- **Map Long 'ah', Short 'o', and 'aw' Sounds (/ɑː/, /ɒ/, /ɔː/)**: When 'a' or 'o' makes a long 'ah' (/ɑː/ e.g., Bar), short 'o' (/ɒ/ e.g., Lock), or 'aw' (/ɔː/ e.g., Install) sound, use the Deergha suffix ಾ.
  - *Source:* "Lock" → *Target:* "ಲಾಕ್"

- **Map Starting Schwa 'A' Sound (/ə/)**: When a word starts with an 'A' that makes a soft 'uh' sound (schwa /ə/, e.g., Alert, Account), use the standard short vowel ಅ.
  - *Source:* "Alert" → *Target:* "ಅಲರ್ಟ್"

- **Map Long 'o' Sound (/oʊ/)**: When 'o' makes a long 'oh' sound (/oʊ/ e.g., Home, Phone), use the Othvasudeergha suffix ೋ.
  - *Source:* "Phone" → *Target:* "ಫೋನ್"

- **Map 'Sa' and 'Sha' Sounds**: Map the 's' sound (/s/) to ಸ, the 'sh' sound (/ʃ/) to ಶ, and the retroflex 'sh' sound (e.g., Washington) to ಷ.
  - *Source:* "Sheet" → *Target:* "ಶೀಟ್"

- **Map 'Ja', 'Za', and 'Fa' Sounds**: Map the 'j' sound (/dʒ/, including soft 'g' like Digit) to ಜ. Map the 'z' sound to ಝ. Map the 'f' or 'ph' sound to ಫ.
  - *Source:* "Format" → *Target:* "ಫಾರ್ಮ್ಯಾಟ್"

- **Map Short and Long 'i' Sounds (/ɪ/, /iː/)**: Map short 'i' sounds (/ɪ/, /iː/ e.g., Click, Kit) to Gudisu ಿ. Map long 'ee' sounds (e.g., Sheet, Screen) to Gudisina Deergha ೀ.
  - *Source:* "Click" → *Target:* "ಕ್ಲಿಕ್"

- **Map Diphthong 'i' Sound (/aɪ/)**: When 'i' makes an 'eye' sound (/aɪ/ e.g., File, Icon), use the Aithva suffix ೈ or the standalone vowel ಐ.
  - *Source:* "File" → *Target:* "ಫೈಲ್"

- **Map Short and Long 'u' Sounds (/ʊ/, /uː/)**: Map short 'u' sounds (/ʊ/, /uː/ e.g., Put, Push) to Kombu ು. Map long 'oo' sounds (e.g., Zoom, Tool) to Kombina Deergha ೂ.
  - *Source:* "Zoom" → *Target:* "ಝೂಮ್"

- **Map Short 'uh' Sound (/ʌ/)**: When 'u' makes a short 'uh' sound (/ʌ/ e.g., Button, Custom), do not use Kombu (ು). Rely on the inherent 'a' sound (ಅ) of the Kannada consonant.
  - *Source:* "Button" → *Target:* "ಬಟನ್"

- **Map 'yoo' Sound (/juː/)**: When 'u' makes a 'yoo' sound (/juː/ e.g., Mute), use ಯೂ at the start of a word or the ್ಯೂ suffix after a consonant.
  - *Source:* "Mute" → *Target:* "ಮ್ಯೂಟ್"

## Tone And Voice

- **Smart but Casual Tone in Written Colloquial Style**: Use a written colloquial Kannada style that balances spoken and written language, making translations sound natural to urban and semi-urban Kannada speakers. The tone should be simple, clear, professional, and friendly — never heavy, stiff, or arrogant. Write short, easy-to-read sentences.

## URL And Links

- **Do Not Attach Suffixes Directly to URLs**: When localizing URL addresses, avoid placing Zero width non-joiners (ZWNJ) or suffixes directly adjacent to the URL link. This practice can cause the URL to become non-functional and non-clickable, blocking the user experience. Instead, use a buffer word like 'ಎಂಬಲ್ಲಿಗೆ'.
  - *Source:* "Visit www.apple.com" → *Target:* "www.apple.com ಎಂಬಲ್ಲಿಗೆ ಭೇಟಿ ನೀಡಿ"

## Variables

- **Preserve Variables; Reorder with Positional Markers if Needed**: Keep all variable tokens (e.g., %@, %1$@) intact. If the natural Kannada word order differs from the source, add or retain positional markers (%1$@, %2$@) on every variable. For person-name variables, add ಅವರು after the variable; for date variables, add ದಿನಾಂಕ; for app variables, add ಆ್ಯಪ್.
  - *Source:* "Check out the score %1$@ earned on %2$@ playing %3$@" → *Target:* "%3$@ ಆಡುವ ಮೂಲಕ %2$@ ಎಂಬಲ್ಲಿ %1$@ ಅವರು ಗಳಿಸಿದ ಸ್ಕೋರ್ ಅನ್ನು ನೋಡಿ"

- **Variables: Add 'ದಿನಾಂಕ' as Buffer for Dates**: When translating strings with date variables in running sentences, add 'ದಿನಾಂಕ' next to the variable. Attach any required grammatical suffixes directly to 'ದಿನಾಂಕ' rather than the variable itself.
  - *Source:* "You earned this award for completing a marathon on %@." → *Target:* "%@ ದಿನಾಂಕದಂದು ಮ್ಯಾರಥಾನ್ ಅನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ್ದಕ್ಕಾಗಿ ನೀವು ಈ ಅವಾರ್ಡ್ ಅನ್ನು ಗಳಿಸಿದ್ದೀರಿ."

- **Variables: Add 'ಸಮಯ' as Buffer for Time**: When translating strings with time variables in running sentences, add 'ಸಮಯ' next to the variable. Attach any required grammatical suffixes directly to 'ಸಮಯ' rather than the variable itself.
  - *Source:* "Tomorrow at %2$@" → *Target:* "ನಾಳೆ %2$@ ಸಮಯಕ್ಕೆ"

- **Variables: Add 'ಅವರು' as Buffer for Person Names**: When translating strings with person name variables in running sentences, add the honorific 'ಅವರು' next to the variable. Attach any required grammatical suffixes directly to 'ಅವರು' rather than the variable itself.
  - *Source:* "%@ Edited" → *Target:* "%@ ಅವರು ಎಡಿಟ್ ಮಾಡಿದ್ದಾರೆ"

- **Variables: Add 'ಆ್ಯಪ್' as Buffer for App Names**: When translating strings with app variables in running sentences, add 'ಆ್ಯಪ್' next to the variable. Attach any required grammatical suffixes directly to 'ಆ್ಯಪ್' rather than the variable itself.
  - *Source:* "Welcome to %@" → *Target:* "%@ ಆ್ಯಪ್‌ಗೆ ಸುಸ್ವಾಗತ"
