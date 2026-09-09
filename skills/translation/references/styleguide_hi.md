# Hindi (hi) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual Tone**: Hindi tone should feel natural and approachable — closer to formal than informal, but never stiff. Follow the written colloquial style used in respected national newspapers like Jansatta or Hindustan, which blend formal and spoken Hindi.
  - *Source:* "Update available. Tap to install." → *Target:* "अपडेट उपलब्ध है। इंस्टॉल करने के लिए टैप करें।"

## Addressing Users

- **Use Formal Address (आप)**: Always address the user with आप (formal you) and use formal verb forms like करें. Never use informal forms like तुम, तू, करो, or कीजिए. This applies equally when addressing minors.
  - *Source:* "You can cancel" → *Target:* "आप रद्द कर सकते हैं"
  - *Source:* "Cancel" → *Target:* "रद्द करें"

- **Third-Person Roles Use Singular Informal**: When translating common nouns describing roles (e.g. 'user', 'administrator') or indefinite pronouns like 'someone', use the informal singular form, not the formal plural.
  - *Source:* "Administrator can do this" → *Target:* "ऐडमिनिस्ट्रेटर कर सकता है"
  - *Source:* "Someone joined the note" → *Target:* "कोई नोट में शामिल हुआ"

## Grammar

- **Avoid Translating English Articles as 'एक'**: Hindi has no articles, so English 'a' or 'an' should not be mechanically translated as एक (one). Only use एक when the meaning genuinely requires the numeral one.
  - *Source:* "Please take a cupcake" → *Target:* "कपकेक लें"

- **Use Passive Voice When Subject Is Absent**: When a string has no explicit subject (i.e., you cannot answer 'who is doing this?'), use the passive voice. This covers gerunds, gerund + object, and status messages.
  - *Source:* "updating…" → *Target:* "अपडेट किया जा रहा है…"
  - *Source:* "Adding %@ Videos" → *Target:* "%@ वीडियो जोड़े जा रहे हैं"
  - *Source:* "Sharing from: %@" → *Target:* "इनसे शेयर किया जा रहा है : %@"

- **Gender Neutrality in User-Facing Strings**: Strings that address an unspecified user should be kept gender-neutral where possible. Use constructions with ने or की ओर से instead of द्वारा to avoid forcing a gendered subject.
  - *Source:* "Apple will send you an email." → *Target:* "Apple की तरफ़ से एक ईमेल भेजा जाएगा।"

- **Nuqta Usage**: Nuqta (a dot below certain consonants) must be used for loan words from Arabic, Persian, Urdu, and English where it is present in the source language, particularly to distinguish फ (pha) from फ़ (fa) and ज (ja) from ज़ (za). When in doubt, consult Rekhta Dictionary.
  - *Source:* "file" → *Target:* "फ़ाइल (not फाइल)"
  - *Source:* "sadness (Urdu: ग़म)" → *Target:* "ग़म (not गम)"

- **Chandrabindu vs. Anuswara**: Chandrabindu should be used wherever it avoids ambiguity between homonyms and reflects the correct pronunciation. Do not substitute anuswara for chandrabindu when they carry different sounds.
  - *Source:* "Mother" → *Target:* "माँ (not मां)"

- **Use of Anuswar over Panchamakshar**: Use of Anuswar is preferred over Panchamakshar
  - *Source:* "End" → *Target:* "अंत (not अन्त)"

- **Pronouns: 'Your' and 'Our' in the Same String**: When 'you/your' appear together in one string, translate 'your' as अपने (not आपके). Similarly, when 'we/our' appear together, translate 'our' as अपने (not हमारे).
  - *Source:* "You can see more details in the Health app on your iPhone." → *Target:* "अपने iPhone पर सेहत ऐप में आप अधिक विवरण देख सकते हैं।"

## Terminology

- **Prefer Colloquial Hindi Over Archaic Terms**: Choose words that are widely understood in everyday spoken and written Hindi rather than formal or archaic equivalents. Prefer तस्वीर over चित्र, नक़्शा over मानचित्र, and दोस्त over मित्र. The deciding factor is linguistic suitability and common usage, not word origin.
  - *Source:* "photo" → *Target:* "तस्वीर (preferred over चित्र)"
  - *Source:* "map" → *Target:* "नक़्शा (preferred over मानचित्र)"

- **Transliterate Technical Jargon**: Technical and software terms that are widely known in English should be transliterated rather than awkwardly translated. If a Hindi equivalent exists but is archaic or unclear (e.g. कलन विधि for 'Algorithm'), use the transliteration instead.
  - *Source:* "Installation" → *Target:* "इंस्टॉलेशन"
  - *Source:* "Algorithm" → *Target:* "एल्गोरिदम (not कलन विधि)"

- **Use British English as Transliteration Base**: When transliterating from English, prefer British or Indian English pronunciations over American English. Use Mobile instead of Cellular, Cycling instead of Biking. However, where American forms dominate in India (e.g. ATM, not Cashpoint), follow popular usage.
  - *Source:* "Cellular" → *Target:* "मोबाइल"
  - *Source:* "Elevator" → *Target:* "लिफ़्ट"

## Abbreviations

- **Use Devanagari Abbreviation Sign (लाघव चिह्न)**: Hindi abbreviations use the Devanagari Abbreviation Sign (॰) after the first syllable of the abbreviated word. Technical file format abbreviations (PDF, DOC, RTF) should remain unlocalized. Country codes like US and UK take the form यू॰एस॰ and यू॰के॰.
  - *Source:* "US" → *Target:* "यू॰एस॰"

## Acronyms

- **Do Not Translate Acronyms Unless Equivalent Exists**: Retain English acronyms (e.g. HDR, RAM) unless a well-known localized equivalent exists. Popular Hindi acronyms such as यूनेस्को, भाजपा, and इसरो are used without the Devanagari Abbreviation Sign.
  - *Source:* "HDR" → *Target:* "HDR"
  - *Source:* "UNESCO" → *Target:* "यूनेस्को"

## Date And Time

- **Date and Time Formatting**: Use international numerals for hardcoded dates and times. Date format follows DD/MM/YYYY. Use a colon as the time separator with no surrounding spaces. 'am' translates as 'पू' and 'pm' as 'अ', both placed before the time with a space after them.
  - *Source:* "March 17, 2022" → *Target:* "17 मार्च 2022"
  - *Source:* "7:15 am" → *Target:* "पू 7:15"
  - *Source:* "7:15 pm" → *Target:* "अ 7:15"

## Numerals

- **Indian Numbering System for Hardcoded Numbers**: Use international (Arabic) numerals, not Devanagari digits, for hardcoded numbers. Apply the Indian grouping system with commas: the first comma appears after three digits, then every two digits (e.g. 10,00,000 not 1,000,000).
  - *Source:* "1,000,000 songs" → *Target:* "10,00,000 गाने"

- **Ordinal Numbers**: Write ordinal numbers 1st–9th as Hindi words (पहला, दूसरा … नवाँ). From 10th onwards, append वाँ to the numeral (10वाँ, 11वाँ).
  - *Source:* "1st" → *Target:* "पहला"
  - *Source:* "10th" → *Target:* "10वाँ"

## Punctuation

- **Hindi Full Stop (पूर्ण विराम)**: Use the Hindi full stop । (poornaviram) to end sentences. Do not use it when the sentence ends with an English word, a number (to avoid confusion with the digit 1), or a URL.
  - *Source:* "Your file has been saved." → *Target:* "आपकी फ़ाइल सहेजी गई।"

- **Space Before Colon**: Add a space before a colon to prevent visual confusion with the Hindi visarga (ः). Exception: omit the space when the colon follows an English word, a number, or a DNT term.
  - *Source:* "Average Depth: %@" → *Target:* "औसत गहराई : %@"

- **Use Curly Quotes for UI Strings**: Always use curly double quotes “ (\u201C) and ” (\u201D) in UI strings, not straight quotes. Minimize their use overall — only employ them when a feature or functionality name would cause grammatical ambiguity in the sentence.
  - *Source:* "Say \u201C%@\u201D Again" → *Target:* "\u201C%@\u201D फिर से कहें"

## Interface Elements

- **Button Names Use Imperative With Helping Verb**: Translate button names in the imperative form. Include a helping verb (करें, दें) when omitting it would make the translation ambiguous — for example, a Hindi or Urdu noun used as a button label needs a verb to signal the action.
  - *Source:* "Edit" → *Target:* "संपादित करें"
  - *Source:* "Reply" → *Target:* "जवाब दें"

- **Callout bar item names**: Callout bar items are generally translated in the imperative form using both the primary and helping verb. However in some cases, where the translation is not ambiguous, and especially when the terms are widely used and understood in that specific context, you may decide to drop the helping verb.
  - *Source:* "Cut" → *Target:* "कट"

- **Keyboard Keys Are Transliterated**: Keyboard key names should be transliterated into Devanagari. When a key name is followed by the word 'key', the combined form uses a hyphen (e.g. कमांड-की). US keyboard shortcuts (⌘N etc.) are copied as-is without localizing to Devanagari characters.
  - *Source:* "Command-keys" → *Target:* "कमांड-कीज़"
  - *Source:* "Fn" → *Target:* "फ़ंक्शन"

## Variables

- **Reorder and Number Variables as Needed**: Variable order may be changed to fit natural Hindi sentence structure. When reordering variables that are not already numbered in the source, add positional numbers (e.g. %1$@, %2$@). Do not change the period to a comma inside numeric format variables like %.1f.
  - *Source:* "%@ payment to %@ will be canceled." → *Target:* "%2$@ को %1$@ का भुगतान रद्द कर दिया जाएगा।"

## Names And Addresses

- **Use Caste-Neutral Indian Names**: Replace generic Western placeholder names (Jane Doe, John Doe) with common Indian names that are inclusive across religions, regions, and castes. Avoid surnames that reveal a specific caste or community.
  - *Source:* "Jane Doe" → *Target:* "प्रिया कुमारी"
  - *Source:* "John Doe" → *Target:* "साहिल कुमार"

## Diversity And Inclusion

- **Avoid Caste and Religion Stereotypes**: Do not translate role-based or occupation-based terms using words that carry caste connotations. For example, translate 'Priest' as पुजारी. Avoid emoji translations that associate religious symbols exclusively with one community.
  - *Source:* "Priest" → *Target:* "पुजारी"

- **People-First Language for Disability**: When referring to people with disabilities, describe the person first and the disability second. Avoid collective labels like 'the blind'; prefer 'people who are blind or have low vision'.
  - *Source:* "The blind" → *Target:* "दृष्टिहीन व्यक्ति or जिन लोगों को कम दिखाई देता है (not अँधा)"
