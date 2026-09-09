# Tamil (ta) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Tamil uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "Hold \u201CSelect\u201D to clear" → *Target:* "அழிக்க \u201Cதேர்ந்தெடு\u201D என்பதை அழுத்திப் பிடிக்கவும்"

## Tone And Voice

- **Modern Written Colloquial Style**: Use the modern written colloquial style (koṭuntamiḻ) for choosing vocabulary and modern literary and formal style (centamiḻ) for sentence composition. Translations should be formal, easy to understand and readable. Avoid Sanskritized vocabulary whenever possible.

## Abbreviations

- **Avoid Abbreviations in Software**: Do not use abbreviations in software translations unless it is really necessary and other workarounds fail. Country abbreviations use Tamil abbreviation sign (e.g., யூ.எஸ். for US).

## Acronyms

- **Keep Acronyms Unless Common Tamil Equivalent Exists**: Do not translate acronyms unless there is a very common localized equivalent. Popular Tamil acronyms like யுனெஸ்கோ (UNESCO), இஸ்ரோ (ISRO), நாஸா (NASA) are used like common Tamil terms. The expansion provided in brackets can be translated if the expansion is very popular in Tamil.
  - *Source:* "UNESCO" → *Target:* "யுனெஸ்கோ"

## Date And Time

- **Date Format**: Use international numbers in hardcoded dates. Comma should not be used to separate the month from the year. In the correspondence (spelled-out) format, transliterate the month name (e.g. 17 மார்ச் 2022). The numeric long format is DD/MM/YYYY and the numeric short format is DD/MM/YY.
  - *Source:* "March 17, 2022" → *Target:* "17 மார்ச் 2022" (correspondence format, spelled month)
  - *Source:* "03/17/2022" → *Target:* "17/03/2022" (numeric long format, DD/MM/YYYY)

- **Time Format HH:mm:ss with Colon Separator**: Use international numbers in hardcoded time. Use a colon (:) as the time separator, with no space before or after it. Translate 'o'clock' as 'மணி'. Do not localize AM/PM; keep it in English following the source capitalization.
  - *Source:* "13:18:35" → *Target:* "13:18:35" (24-hour; colon separator, no surrounding space)
  - *Source:* "08:30 AM, 12:30 PM" → *Target:* "08:30 AM, 12:30 PM" (12-hour; AM/PM kept in English)
  - *Source:* "9 o'clock" → *Target:* "9 மணி"

## Measurements

- **Do Not Convert Measurements**: Do not convert the measurements (e.g., imperial to metric).
  - *Source:* "km²" → *Target:* "km²"

## Names And Addresses

- **Tamil Sample Names**: Use generic Tamil names that are inclusive and diverse, avoiding surnames that reveal a particular sect or caste. When a name is a generic placeholder, replace it with a locally-appropriate Tamil name. When the name refers to a specific, real individual named in the source or developer comment (of any nationality), keep that person's actual name, transliterating it into Tamil script if it is in Latin letters.

- **Follow Indian Address Conventions**: Address formatting follows the conventions set forth by the Department of Post, Government of India; the general structure is name, house/door number, street/road, locality/area, city/town, district, state, and PIN code. PIN codes are 6 digits in international numerals with no space between the digits. Addresses outside India are kept in English.

## Currency

- **Indian Currency Format**: Do not use a blank space after the Indian currency symbol (₹). Rupees can be translated as ரூபாய்.
  - *Source:* "₹ 500.45" → *Target:* "₹500.45" (no space after the ₹ symbol)
  - *Source:* "500 Rupees" → *Target:* "500 ரூபாய்"

## Numerals

- **International Numerals with Indian Grouping**: Keep numerals as international digits (0–9); do not change the numeral system yourself. Group large numbers using the Indian separator system (e.g., 10,00,000).
  - *Source:* "500000" → *Target:* "5,00,000"

## Grammar

- **Do Not Translate Articles as ஒரு**: There are no articles in Tamil. Do not literally translate 'a' or 'an' to 'ஒரு' (one). Most Tamil sentences do not need an article. Consider using ஒரு only if it is not possible to render a sentence without it.
  - *Source:* "You liked an image" → *Target:* "படத்திற்கு விருப்பம் தெரிவித்துள்ளீர்கள்"

- **Tamil vs. Transliteration**: Use transliteration only for complex technical terms that would be difficult to understand if translated, or when the non-technical Tamil term is archaic. Follow British English pronunciation for transliteration spellings.
  - *Source:* "Computer" → *Target:* "கம்ப்யூட்டர்"

- **Handling Transliteration Words**: The Aytam character (ஃ) must be used before the consonant to create “F” or “Ph” sound.
  - *Source:* "Phone, Fitness" → *Target:* "ஃபோன், ஃபிட்னஸ்"

- **Transliteration: Usage of ண் (ṇ) before ட**: In transliterated terms, use ண் (ṇ) before ட (ṭa) when pronounced as a soft syllable (like the "nd" in "cylinder").
  - *Source:* "Brand, Conductor, Cylinder" → *Target:* "பிராண்டு, கண்டக்டர், சிலிண்டர்"

- **Transliteration: Usage of ன் (ṉ) before ட**: In transliterated terms, use ன் (ṉ) before ட (ṭa) when pronounced as a hard syllable (like the "nt" in "container"). Note: Exceptions exist for highly established common spellings (e.g., “payment - பேமெண்ட்“ uses ண்).
  - *Source:* "Container" → *Target:* "கன்டெய்னர்"

- **Compounds and Hyphens in Transliteration**: When transliterating, it is not necessary to use a hyphen even though it is present in the source. The transliteration can be with or without space depending on pronunciation. Some words use hyphens as in source like பிளக்-இன், செக்-இன், பாப்-அப்.

- **Prefer Passive Voice for System Messages**: The passive style is preferred when the string involves a message directed to a user without specifying an explicit subject. If the answer to 'What' or 'Who' cannot be found in the string and the source is active voice, Tamil must use passive voice.
  - *Source:* "updating…" → *Target:* "புதுப்பிக்கப்படுகிறது…"
  - *Source:* "Adding %@ Videos" → *Target:* "%@ வீடியோக்கள் சேர்க்கப்படுகின்றன"

- **Sandhi (Consonant Mutation) Rules**: Follow standard Tamil Sandhi rules for consonant mutation. வல்லினம் must be applied correctly when composing compound words and phrases.

- **Case Markers for Terms Kept in Original Form**: Use the standalone case marker forms (ஐ, இல், இன், க்கு etc.) when inflecting terms that are kept in their original form (e.g. product or brand names).
  - *Source:* "Some of your contacts are on Apple Music." → *Target:* "உங்கள் தொடர்புகளில் சிலர் Apple Musicஇல் உள்ளனர்."

## Variables

- **Hyphenating Variables and Case Markers**: A hyphen (-) must be inserted between the variable and its case marker whenever the variable's replacement text is not a term kept in its original form. Without this hyphen, these variable-case marker combinations appear visually incorrect at runtime.
  - *Source:* "You're now blocking %s." → *Target:* "%s-ஐ இப்போது தடுக்கிறீர்கள்."

- **Preserve Variables; Reorder with Numbering**: If there is no need to change the order of variables, leave them unchanged. If the order needs to change for Tamil sentence structure, number the variables so they are replaced correctly at runtime. Do not change the period to a comma in number variables like '%.1f GB'.
  - *Source:* "Move the USB cable plugged into your %1$@ named \u201C%2$@\u201D to your %3$@." → *Target:* "\u201C%2$@\u201D என்ற உங்கள் %1$@ சாதனத்தில் பிளக்-இன் செய்யப்பட்டுள்ள USB கேபிளை %3$@ சாதனத்திற்கு மாற்றவும்."

## Punctuation

- **Reduce Comma and Semicolon Usage**: Reduce comma and semicolon usage as much as possible as it breaks the natural flow of the sentence. Instead, use a fullstop (.) to separate the sentence and convey the meaning clearly.

- **Curly Double Quotes for UI Strings**: When highlighting a feature or button name, wrap it in the curly double quotes shown in the escaping section above, not straight quotes — except in HTML or code, where straight quotes are kept as-is. Minimize the use of curly quotes overall.

- **Full Stop**: Use the period (.) as the sentence-ending full stop. For question marks, follow the source's punctuation.

## Interface Elements

- **Button Names Use Imperative Form**: For buttons and commands where the system performs an action proposed to the user, use Second Person Singular form. Do not use the academic -க suffix.
  - *Source:* "Cancel" → *Target:* "ரத்துசெய்"
  - *Source:* "Save" → *Target:* "சேமி"

- **Descriptions Use Declarative Style with -லாம்**: Footer and description texts that explain the purpose and functionality of a feature should use the declarative -லாம் form rather than the instructional -வும் form.
  - *Source:* "Turn on extra light when you need it." → *Target:* "தேவையானபோது கூடுதல் லைட்டை ஆன் செய்யலாம்."

- **Headings and Titles Use Gerund Form with தல்**: Verbs in headings and title text should be translated in the gerund form rather than using an instructional tone.
  - *Source:* "Setup basics" → *Target:* "அடிப்படைச் செயல்களை அமைத்தல்"

- **Instruction Text Uses Polite Imperative with -வும்**: Instructional text directing the user to perform a specific action (like entering data or making a selection) should be translated using instructional tone with the -வும் suffix.
  - *Source:* "Enter Setup Key" → *Target:* "செட்-அப் கீயை உள்ளிடவும்"

- **App Names: Translation vs Transliteration**: Use translation when a direct, simple native equivalent exists (e.g., Contacts).
  - *Source:* "Contacts" → *Target:* "தொடர்புகள்"
  - *Source:* "Fitness" → *Target:* "ஃபிட்னஸ்"

- **App Names: Pluralization for Translated Terms**: Tamil strictly follows the pluralization of the source text. Apply the Tamil plural suffix (-கள்) when the English source term is plural and the native Tamil word naturally takes a plural form.
  - *Source:* "Books" → *Target:* "புத்தகங்கள்"

- **App Names: Pluralization for Transliterated Proper Nouns**: When a plural term is a proper name (a brand, app, or feature identifier), transliterate it and retain the English plural marker to preserve the identifier — even when the same word can be a common noun in other contexts.
  - *Source:* "Photos, Maps, Messages" → *Target:* "ஃபோட்டோஸ், மேப்ஸ், மெசேஜஸ்"

- **App Names: Transliteration Hybrid Approach**: If retaining the English plural creates difficult consonant clusters (e.g., words ending in -sts, -rds, -gets, -ms) or breaks case marker compatibility, use the transliterated root + Tamil suffix (-கள்).
  - *Source:* "Podcasts, Passwords" → *Target:* "பாட்காஸ்ட்கள், பாஸ்வேர்டுகள்"

- **Category Labels: Generic Terms (Common Nouns)**: When a term is used as a generic category (a common noun) rather than as a proper name, translate it. Choose per term: use a pure Tamil translation with the plural suffix when the Tamil word is commonly understood, otherwise apply the native Tamil plural suffix (-கள்) to the transliterated root.
  - *Source:* "photos, messages" → *Target:* "புகைப்படங்கள், மெசேஜ்கள்"

- **Category Labels: Inline UI Paths**: When directing the user to a label or tab via a path, the term retains its exact localized plural form. Use helper words (like என்பதற்குச்) to attach case markers.
  - *Source:* "Go to Settings > Notifications." → *Target:* "அமைப்புகள் > அறிவிப்புகள் என்பதற்குச் செல்லவும்."

- **Category Labels: Inline Features**: If a feature name appears inline and could cause grammatical ambiguity, wrap the feature name in double curly quotes (“ (\u201C) and ” (\u201D)) and attach the case marker to a helper word (என்பதை).
  - *Source:* "Tap \u201CNotifications\u201D to view alerts." → *Target:* "விழிப்பூட்டல்களைப் பார்க்க \u201Cஅறிவிப்புகள்\u201D என்பதைத் தட்டவும்."

- **Inline Alt-Text Elements**: Do not translate the structural tags placed inside angle brackets (e.g., <AltText>). Also, as per Tamil style the text order can change, which can result in a change in the order of inline Alt-text elements as per the sentence requirements.
  - *Source:* "Tap <AltText>Settings button</AltText> and choose your file." → *Target:* "<AltText>Settings button</AltText>-ஐத் தட்டி உங்கள் கோப்பைத் தேர்வுசெய்யவும்."

## Trademarks And Product Names

- **Do Not Translate or Transliterate Trademarks**: Do not translate or transliterate trademarks, trademarked slogans, or product names.

## Diversity And Inclusion

- **Gender-Neutral Language**: Tamil is a gender-neutral language but gendered bias can still occur. When referring to a person, use the neutral word அவர் instead of the gendered அவன்/அவள்.
  - *Source:* "A message on your child\u2019s device will ask them to confirm if they attempted this payment" → *Target:* "இந்த பேமெண்ட்டை உங்கள் சிறார் தான் மேற்கொண்டாரா என்பதை உறுதிசெய்ய, அவரின் சாதனத்தில் ஒரு மெசேஜ் காட்டப்படும்"

- **People-First Language for Disabilities**: Use people-first translation when referring to people with disabilities. Describe individuals as people before mentioning their disability. Avoid defining or derogatory terms like கண் இல்லாதவர், செவிடு, or ஊனமுற்றோர். Instead, use respectful terms like பார்வைத் திறன் குறைபாடு உடையவர், செவித்திறன் குறைபாடு உடையவர், or மாற்றுத்திறனாளி.
  - *Source:* "A person who uses a wheelchair" → *Target:* "மாற்றுத்திறனாளி"
