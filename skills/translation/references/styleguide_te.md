# Telugu (te) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Telugu uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting UI strings, single curly quotation marks ‘ (\u2018) and ’ (\u2019) for UI-element references in running text, and the curly apostrophe ’ (\u2019).
  - *Source:* "Please see the \u201CFAQ\u201D section." → *Target:* "\u201CFAQ\u201D విభాగాన్ని చూడండి."

## Abbreviations

- **Avoid Abbreviations — Use Full Forms**: Do not shorten translated words to fit space-constrained UI strings — keep the full Telugu or transliterated form even when it makes the string longer. When abbreviation is absolutely unavoidable, denote it with a period and ensure the shortened term is unambiguous.
  - *Source:* "Number" → *Target:* "సంఖ్య" (abbreviate as "సం." with a period only when forced by a character limit)

## Acronyms

- **Keep Technical Acronyms in English; Do Not Add Full Stops Between Letters**: Standard technical acronyms such as HTML, XML, CSS, RAM, and ROM must stay in their English form without periods between letters. Expand or transliterate the full form only when it is widely recognized in Telugu. File formats (DOC, PDF, RTF) are always kept unlocalized.
  - *Source:* "RAM" → *Target:* "RAM"

## Addressing Users

- **Always Use Formal Plural Address (మీరు / మీ)**: Address the user exclusively with the second-person plural forms మీరు and మీ in all content types. Never use the informal singular నువ్వు, నీ, నిన్ను or the condescending forms వాడిని or అతడిని. The tone must always be polite even when direct.
  - *Source:* "We use your location to show you delivery options faster." → *Target:* "మేము మీకు డెలివరీ ఎంపికలను వేగంగా చూపడానికి మీ లొకేషన్‌ను ఉపయోగిస్తాము."

- **Use Honorific Imperative Verb Forms for Buttons and Commands**: Button labels, command names, and dialog actions must use the honorific imperative ending in ‑ండి.
  - *Source:* "Create" → *Target:* "సృష్టించండి"

## Alt-Text Elements

- **Inline Alt-Text Elements**: Do not change the markup inside the angle brackets — tags, attribute names, and file names stay as-is; translate only the human-readable text, such as the value of the alt attribute. This alt text may be shown when images do not load, or read aloud to people who have difficulty seeing.
  - *Source:* "<img src="settings_gear.jpg" alt="Gear icon for Settings" width="25" height="25">" → *Target:* "<img src="settings_gear.jpg" alt="సెట్టింగ్స్ కోసం గేర్ ఐకాన్" width="25" height="25">"

## Color Names

- **Translate Standard Color Names Into Direct Telugu Equivalents**: Translate universally recognized basic colors into their direct Telugu equivalents without adding రంగు. These are standard colors with established Telugu terms that are widely understood.
  - *Source:* "Red" → *Target:* "ఎరుపు"

- **Transliterate Non-Standard Color Shades and Color Variations**: Transliterate color variations, non-standard shades, and coined/branded color names to maintain clarity and brand identity — even when a native Telugu word exists.
  - *Source:* "Gray" → *Target:* "గ్రే" (transliterated, not the native బూడిద)

## Currency

- **Do Not Add Space After Indian Currency Symbol**: Do not place a blank space after the Indian currency symbol ₹. Indian Rupees can be written as రూపాయలు or రూ. in sentences based on context. Always use international numerals with currency.
  - *Source:* "₹ 100.11" → *Target:* "₹100.11" (no space after ₹)
  - *Source:* "100 Rupees" → *Target:* "100 రూపాయలు"

## Date And Time

- **Transliterate Month Names; Numeric Dates Use DD/MM/YYYY**: For a spelled-out date, transliterate the month name and place the day first, with no comma between the month and the year. For an abbreviated/numeric date, use DD/MM/YYYY. Always use international numerals.
  - *Source:* "20th December 2023" → *Target:* "20 డిసెంబర్ 2023" (spelled month, no comma)
  - *Source:* "12/20/2023" → *Target:* "20/12/2023" (numeric date, DD/MM/YYYY order)

- **Keep AM/PM Untranslated in Time Strings**: Do not translate AM/PM - keep them as-is in all time strings. Use a colon (:) as the time separator, with no surrounding spaces (e.g. 12:11:15). Use నుండి to translate "to" when indicating a time range. Always use international numerals for hardcoded time values.
  - *Source:* "7 PM to 11 PM" → *Target:* "7 PM నుండి 11 PM"

## Diversity And Inclusion

- **Use Gender-Neutral Language; Default to Masculine Only as Last Resort**: Prefer neuter or gender-neutral constructions whenever possible. Phrase sentences so they are valid for both male and female readers by using the plural or impersonal form. Do not use slash-separated gender variants (e.g. చేసాడు/చేసింది). Use the masculine form only in plural contexts where Telugu grammar provides no neutral alternative.
  - *Source:* "You were able to solve this problem without using %@" → *Target:* "మీరు %@ని ఉపయోగించకుండానే ఈ సమస్యను పరిష్కరించగలిగారు"

- **Use Passive Voice for Gender Neutrality**: When translating any string where active voice would result in a gendered construction, use passive voice to maintain gender neutrality. This ensures the translation is valid for both male and female readers without specifying gender. Passive voice is especially recommended when the sentence has no explicit subject.
  - *Source:* "The app can recognize your voice" → *Target:* "యాప్ ద్వారా మీ వాయిస్ గుర్తించబడుతుంది"

## General Advice

- **Use Single Curly Quotes When Referencing UI Elements**: When citing a UI element such as a feature name, button, or page title in running text, wrap it in single curly quotes. This helps differentiate UI references from surrounding text.
  - *Source:* "To edit a query, click \u201CEdit\u201D." → *Target:* "క్వెరీని ఎడిట్ చేయడానికి \u2018ఎడిట్\u2019పై క్లిక్ చేయండి." (UI reference wrapped in single curly quotes)

- **Translate Feature Descriptions and Explanations in a Descriptive Tone**: When descriptions or explanations for features, options, etc. are complete sentences with indicative verbs, translate them in a descriptive (declarative) tone in Telugu, matching the context. Do not use imperative forms for descriptive strings that explain what a feature does.
  - *Source:* "Play music based on mood." → *Target:* "మూడ్‌కు తగినట్లు సంగీతం ప్లే చేయబడుతుంది."

## Grammar

- **Pluralize Transliterated Common Nouns With Telugu Suffix -లు; Not English -స్**: Transliterated English common nouns that are not app names must take the Telugu plural suffix -లు attached directly without a hyphen or space. Do not add the English -స్ suffix to common nouns. This rule applies to general UI terms, category labels and section headers that are not app names. App names functioning as proper noun identifiers are explicitly excluded from this rule and must retain the English plural marker -స్.
  - *Source:* "Apps, Downloads, Albums, Playlists, Updates" → *Target:* "యాప్‌లు, డౌన్‌లోడ్‌లు, ఆల్బమ్‌లు, ప్లేలిస్ట్‌లు, అప్‌డేట్‌లు"

- **Add Telugu Plural Suffix ‑లు Directly to English Proper Nouns**: English proper nouns and retained product names that stay in their original English form must take the Telugu plural suffix ‑లు attached directly to the English word without a hyphen or space, replacing the English ‑s suffix.
  - *Source:* "iPhones" → *Target:* "iPhoneలు"

- **Telugu Uses Postpositions, Not Prepositions**: Unlike English, Telugu places its relational particles after the noun. Be careful when translating English prepositions such as in, on, at, with, and for — find the correct Telugu postposition and place it after the noun phrase rather than before it.
  - *Source:* "Update iOS on your device" → *Target:* "మీ డివైజ్‌లో iOSను అప్‌డేట్ చేయండి"

- **Avoid Literal Translation of "and" as మరియు Everywhere**: The conjunction మరియు is a valid translation of "and" but can feel stiff when overused. Prefer alternatives like అలాగే or ఇంకా or ఆ తర్వాత, or restructure the sentence to avoid the conjunction entirely, where it improves flow. Do not add a comma before మరియు or లేదా.
  - *Source:* "How do I change my Apple ID and not lose all of my contacts?" → *Target:* "నేను నా కాంటాక్ట్‌లను కోల్పోకుండా నా Apple IDని ఎలా మార్చాలి?"

- **Prefer Passive Voice; Use Active Only for Readability Exceptions**: Telugu translation should generally follow a passive or neutral voice to maintain gender neutrality and natural flow. Use active voice only when the passive form is awkward, causes truncation, or when running sentences clearly benefit from it.
  - *Source:* "WLAN Calling Enabling" → *Target:* "WLAN కాలింగ్ ఎనేబల్ చేయబడుతోంది"

- **No Articles in Telugu — Do Not Translate "a", "an", or "the"**: Telugu has no grammatical articles. Simply drop English articles in translation. Do not render "a" as ఒక unless the numerical sense of "one" is genuinely intended by the source.
  - *Source:* "Enjoy easy pickup from an Apple Store" → *Target:* "Apple Store నుండి సులభ పికప్ సదుపాయం పొందండి"

- **Do Not Add Space Before Telugu Postposition Suffixes**: Never add a space before Telugu postposition case-suffixes such as కి, కు, ని, ను, లో etc., when they are attached to a word. The suffix must be attached directly to the word, with a ZWNJ inserted between them only when the word ends with a halant (్).
  - *Source:* "Lower Case" → *Target:* "లోయర్ కేస్‌కు" (postposition ‑కు attached directly, with no space before it)

## Interface Elements

- **Translate App Names That Have a Clear Colloquial Telugu Equivalent and Apply Native Plural Suffix**: When an app name has a well-known colloquial Telugu equivalent, translate it and apply the native Telugu plural suffix -లు following standard Telugu morphology. Vowel-ending stems take -లు directly. Nouns ending in -అం drop -అం and take -ఆలు. Never split or partially translate an app name. Add the word యాప్ only when the app name clashes with a common Telugu word in running text and disambiguation is necessary.
  - *Source:* "Messages, Books, Tips" → *Target:* "సందేశాలు, పుస్తకాలు, చిట్కాలు"

- **Retain English Plural Marker -స్ for Transliterated App Names; Never Add -లు**: When no suitable colloquial Telugu equivalent exists, transliterate the app name and retain the English plural marker -స్ as an integral part of the proper noun identifier. Never add Telugu plural suffix -లు to a transliterated app name that already carries -స్ as this produces unnatural double pluralization. Forms like కాంటాక్ట్స్‌లు and సెట్టింగ్స్‌లు must be strictly avoided. When these app names appear in a sentence followed by a postposition, insert a ZWNJ between the word and the postposition.
  - *Source:* "Settings, Contacts, Notes, Maps, Stocks" → *Target:* "సెట్టింగ్స్, కాంటాక్ట్స్, నోట్స్, మ్యాప్స్, స్టాక్స్"
  - *Source:* "Contacts" → *Target:* "కాంటాక్ట్స్", not "కాంటాక్ట్స్‌లు" (do not add -లు to a name already ending in -స్)

- **Use Helping Verb for Standalone Action Buttons With Telugu Verbs**: When a button uses a Telugu verb as a standalone label, add a helping verb such as చేయండి or ఇవ్వండి so it reads as a command rather than a noun. (Established standalone command terms are the exception — see the next rule.)
  - *Source:* "Answer" → *Target:* "సమాధానమివ్వండి"

- **Do Not Add Helping Verb to Standalone Command Terms**: Certain standalone command terms do not require a helping verb. These include: Save, Cut, Duplicate, Cancel, Redeem, Share, Insert, Copy, Paste, Delete. Translate or transliterate them as-is without appending చేయండి.
  - *Source:* "Cancel" → *Target:* "రద్దు"

## Measurements

- **Translate or Transliterate Measurement Units in Full Written Form; Retain Abbreviations in English**: When a measurement unit appears in its full written form, translate or transliterate it into Telugu (e.g. కిలోమీటర్, సెంటీమీటర్, అడుగులు). When it appears in abbreviated form, keep the English abbreviation unchanged. Always use international numerals with measurement units.
  - *Source:* "Kilometer (km)" → *Target:* "కిలోమీటర్ (km)"

- **Always Retain Electronic and Computing Units in English**: Electronic or computing units such as MB, GB, TB, KB, 1080p, 720p must always be left in English regardless of whether they appear in full or abbreviated form. Always leave a space between the number and the unit.
  - *Source:* "2 GB" → *Target:* "2 GB"

- **Do Not Convert Measurement Units**: Do not convert measurements (e.g. imperial to metric) to local measurements. For example, do not convert inches to cm. Keep the source units as given.

## Names And Addresses

- **Use Locally-Appropriate Names for Placeholders; Keep a Specific Real Individual's Name**: When the source uses a generic placeholder name, replace it with a generic, locally-appropriate Telugu name so the UI reads naturally. When the name refers to a specific, real individual (rather than a generic placeholder), keep that person's actual name, transliterating it into Telugu script if it is written in Latin letters. Tools, software/application, third-party brand, company, and product names must not be translated.

- **Follow Indian Address Conventions**: Address formatting follows the Telugu conventions used by the Department of Post, Government of India. There is no single defined format for Indian addresses; the general structure is name, block/building/house number, street/road/village, locality/colony/post office, suburb/district, city/town, state, and PIN code. PIN codes consist of 6 digits with no space between digits, written in international numerals, generally placed after the city or district name. Addresses outside India are recommended to be kept in English.

## Numerals

- **Use Correct Ordinal Number Format in Telugu**: Hard-coded numbers must be in international numeral form (0–9). Ordinals follow the pattern మొదటి/1వ, రెండవ/2వ, మూడవ/3వ and so on. Always leave a space between a number and the following word or unit.
  - *Source:* "First / 1st" → *Target:* "మొదటి / 1వ"

- **Apply Indian Comma Grouping System for Large Numbers**: The Indian comma system must be used for large numbers - commas are placed after thousands, then lakhs and crores (e.g. 10,00,000 not 1,000,000). Hard-coded numbers must always be in international numeral form (0-9). Always leave a space between a number and the following word or unit.
  - *Source:* "10,00,000 songs" → *Target:* "10,00,000 పాటలు"

## Punctuation

- **Use Curly Double Quotes in UI Strings**: Wrap quoted UI strings in the curly double quotes shown in the escaping section above, not straight quotes — except inside HTML or code, where straight quotes are kept as-is. Use the single ellipsis character (…), not three separate dots. Do not use a comma before the conjunctions మరియు or లేదా.

- **Retain & Symbol Between Product Names, Feature Names or Mixed-Language Items**: Retain the & symbol when it appears between product names, feature names, or mixed-language items where one or both sides of the symbol remain in English or are transliterated. Do not replace & with a comma in such cases.
  - *Source:* "Display & Brightness" → *Target:* "డిస్‌ప్లే & బ్రైట్‌నెస్"

- **Replace & with Comma When Both Sides Are Fully Translated Telugu Words**: Replace the & symbol with a comma only when both sides of the symbol are fully translated Telugu words. This clause does not apply anywhere else - only when both sides have Telugu word translations, not transliterations.
  - *Source:* "Privacy & Security" → *Target:* "గోప్యత, భద్రత"

- **Do Not Use Space Before or After a Slash**: Do not use a space before or after a slash (/) in Telugu UI strings, unless the source string itself has spaces around the slash.
  - *Source:* "On/Off" → *Target:* "ఆన్/ఆఫ్"

## Region Names

- **Transliterate Location and Country Names; Do Not Translate Into Telugu**: Location, Region, State and Country names except India should be transliterated. Do not translate country names into their Telugu equivalents. This applies to all countries, states and regions outside India.
  - *Source:* "United States" → *Target:* "యునైటెడ్ స్టేట్స్"

## Terminology

- **Prefer Transliteration Over Archaic Telugu for Technical Terms**: When no natural, widely-understood Telugu equivalent exists, transliterate the English term using its Indian/British English pronunciation as the reference. Do not coin archaic Sanskritized translations that the target audience will not recognize.
  - *Source:* "Photo library" → *Target:* "ఫోటో లైబ్రరీ"

- **Use Standardized Telugu Terminology Consistently**: Repetitive phrases and standard UI labels must be translated the same way every time — use the established Telugu term consistently rather than introducing a variant.
  - *Source:* "Settings" → *Target:* "సెట్టింగ్స్"

## Tone And Voice

- **Smart but Casual — Written Colloquial Telugu**: Use a tone that is neither stiff nor excessively informal. Follow the written colloquial style used by major Telugu publications, which blend formal and everyday Telugu. Ensure grammatical correctness including proper use of object markers such as ను, కు etc. where required. The reader should not feel they are reading a translation.
  - *Source:* "Enter your password." → *Target:* "మీ పాస్‌వర్డ్‌ను నమోదు చేయండి."

## Transliteration

- **Localize Standalone "Cellular"**: When "Cellular" appears as a standalone term or is followed by Telugu words, translate it as మొబైల్ సర్వీస్. This applies to cases where Cellular refers to the network service itself.
  - *Source:* "Cellular" → *Target:* "మొబైల్ సర్వీస్"

- **Localize "Cellular" as మొబైల్ When Used as a Modifier With Another English Technical Term**: When "Cellular" appears as a modifier alongside another English technical term such as data, translate it as మొబైల్ only. Do not add సర్వీస్ in such cases.
  - *Source:* "cellular data" → *Target:* "మొబైల్ డేటా"

- **Prefer the Indian/British English Term and Pronunciation for Transliteration**: When an English term has distinct British/Indian and American forms, prefer the Indian/British one — e.g. Mobile not Cellular, Cycle not Bike, Lift not Elevator — and use Indian/British pronunciation (not American) as the reference when spelling the transliteration.
  - *Source:* "Elevator" → *Target:* "లిఫ్ట్"

## URL Addresses

- **Do Not Add ZWNJ or Suffixes Directly Adjacent to URLs**: Never place Zero Width Non-Joiners (ZWNJ) or Telugu suffixes directly next to a URL link. This can make the URL non-functional and non-clickable. Place any Telugu text after a space following the URL.
  - *Source:* "www.apple.com/in/privacy and Apple Privacy Policy" → *Target:* "www.apple.com/in/privacy మరియు Apple గోప్యతా విధానం"

## Variables

- **Reorder and Number Variables When Telugu Grammar Requires Different Word Order**: When Telugu sentence structure requires a different word order from the source, number all variables using the n$ syntax immediately after the % sign to preserve their runtime mapping. Do not add spaces or Telugu characters inside variable placeholders.
  - *Source:* "Check out the score %1$@ earned on %2$@ playing %3$@" → *Target:* "%2$@‌లో %3$@ ఆడుతూ %1$@ సాధించిన స్కోర్‌ను చూడండి"
