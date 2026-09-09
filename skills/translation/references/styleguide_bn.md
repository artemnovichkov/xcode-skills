# Bengali (bn) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Bangla follows English-style quoting — curly double quotation marks “ (\u201C) and ” (\u201D).

## Tone And Voice

- **Smart but Casual Tone**: Use Cholito-bhasha (চলিত ভাষা), the standard written colloquial Bangla with shortened verb forms. The tone should be closer to formal than informal, but never stiff or archaic. Follow the register of reputable national newspapers like Anandabazar Patrika.
  - *Source:* "Later than 10 days ago" → *Target:* "10 দিনেরও আগে"

- **Prefer Transliteration Over Archaic Bangla Terms**: When a Bangla term is archaic, obsolete, or not popularly understood, use transliteration instead. Avoid creating overly literal Bangla neologisms that will confuse users. Technical and IT terms that are widely used in English should generally be transliterated.
  - *Source:* "Download" → *Target:* "ডাউনলোড" (not "নিম্নভরণ")
  - *Source:* "Installation" → *Target:* "ইনস্টলেশন"

- **Avoid Word-for-Word Translation**: Translate contextually, not literally. The reader should not feel they are reading a translation. Restructure sentences to sound natural in Bangla while preserving the meaning of the source.
  - *Source:* "Replace the battery." → *Target:* "ব্যাটারি বদলান।"

## Addressing Users

- **Use Formal Second Person (আপনি)**: Always address the user with the honorific আপনি and the corresponding polite verb forms. Never use the informal তুমি or তুই. This applies equally when addressing adults and minors.
  - *Source:* "Enter your phone number." → *Target:* "আপনার ফোন নম্বর লিখুন।"

## Abbreviations

- **Abbreviation Formation with বিসর্গ**: Bangla abbreviations are formed using the বিসর্গ (ঃ) symbol, by taking the first letter or syllable of a word. Avoid creating abbreviations in software unless absolutely necessary; prefer rewording instead.
  - *Source:* "Note" → *Target:* "বিঃদ্রঃ"

## Acronyms

- **Do Not Translate Acronyms**: Keep acronyms in their original English form unless a very common localized equivalent exists. Popular acronyms like UNESCO, FIFA, NASA are written without a full stop or বিসর্গ, often in transliterated Bangla.
  - *Source:* "UNESCO" → *Target:* "ইউনেস্কো"
  - *Source:* "HDR" → *Target:* "HDR"

## Date And Time

- **Date Format**: Use international numerals in dates. The correspondence format is DD Month YYYY (e.g., 17 ডিসেম্বর 2022). The long format is DD/MM/YYYY and the short format is DD/MM/YY. Do not use a comma to separate the month from the year.
  - *Source:* "December 17, 2022" → *Target:* "17 ডিসেম্বর 2022"

- **Time Format and AM/PM**: Use hh:mm:ss with a colon as separator and no spaces around the colon. Do not translate or localize AM/PM: keep it in English, following source capitalization.
  - *Source:* "10:18:35 AM" → *Target:* "10:18:35 AM"

## Measurements

- **Retain Electronic and Computer Units in English**: Units related to electronics and computing (GB, KB, dB, etc.) should remain in English. There must be a space between the number and the unit. Do not convert imperial to metric. Some units are exempt from CLDR: μS, oz, kcal, dB, cal.
  - *Source:* "8 GB" → *Target:* "8 GB"
  - *Source:* "1080p" → *Target:* "1080p"

## Names And Addresses

- **Use Caste- and Sect-Neutral Sample Names**: When localizing English placeholder names (e.g., John Doe, Jane Doe), choose Indian-Bangla equivalents that do not reveal caste, religion, or regional sect. Use a culturally diverse mix that reflects gender balance. If the UI shows a non-Indian person's photo or context, transliterate the source name instead of substituting a Bangla one.

## Numerals

- **Use International Numerals and Indian Separator System**: The system standard for Bangla is international numerals (0–9). Use the Indian number separator system (e.g., 10,00,000).
  - *Source:* "1,000,000 songs" → *Target:* "10,00,000 গান"
  - *Source:* "%lld person" → *Target:* "%lld জন ব্যক্তি"

## Punctuation

- **Use Bangla Dari (।) as Full Stop**: The Bangla dari (।) must be used as a full stop, not the Latin period (.). The Latin period is only used as a dot or within abbreviations. There is no space before the dari and one space follows it before the next sentence begins.
  - *Source:* "Update will begin now. Please wait." → *Target:* "এখন আপডেট করা হবে। তাই অপেক্ষা করুন।"

- **Use Curly Double Quotes for UI String References**: Use curly double quotes “ (\u201C) and ” (\u201D) in UI strings, not straight quotes. Use them minimally: only when grammatical ambiguity arises from pluralization, oblique case, or other grammatical changes caused by an app or feature name.
  - *Source:* "Tap \u201CEdit Watchlist\u201D" → *Target:* "\u201Cওয়াচলিস্ট এডিট করুন\u201D-এ ট্যাপ করুন"

- **Colon Usage After Titles and Headings**: When a heading is followed by an explanatory sentence or phrase, use a colon (:) to connect them: not a dari (।) or full stop. A single space follows the colon.
  - *Source:* "Lock Screen. Your lock screen photo" → *Target:* "লক স্ক্রিন: আপনার লক স্ক্রিনের ছবি"

## Special Characters

- **Use Bangla Visarga, Not English Colon**: The Bangla Abbreviation Sign (ঃ) must not be replaced with an English colon (:). The Bangla Virama (॥) must not be formed by typing two dandas (।।). Pipe characters (|) must never be used as Virama.
  - *Source:* "Note:" → *Target:* "বিঃদ্রঃ" (use ঃ, not the Latin colon :)

## Grammar

- **No Articles: Avoid Translating 'a/an' as এক**: Bangla has no articles. Do not translate 'a' or 'an' as 'এক' unless it is genuinely needed for meaning. Most English sentences with articles translate naturally into Bangla without any article equivalent.
  - *Source:* "Take a break." → *Target:* "বিরতি নিন।"
  - *Source:* "Add a file." → *Target:* "একটি ফাইল যোগ করুন।"

- **Pluralization Classifiers**: Use 'গুলি' (not 'গুলো') for inanimate plural nouns, and 'রা', 'দের', or 'গণ' for animate ones. Attach the classifier directly to the noun with no space or hyphen. Do not add a classifier to nouns that are already inherently plural.
  - *Source:* "Wi-Fi networks" → *Target:* "Wi-Fi নেটওয়ার্কগুলি"
  - *Source:* "Headphones" → *Target:* "হেডফোন" (not "হেডফোনগুলি")

- **Use Passive Voice When Subject Is Absent**: When the English source is in active voice but the subject performing the action is absent or implied, use passive voice in Bangla. This applies to gerunds, verb+object strings, and strings where you can ask 'who will do this?' without finding the answer in the string.
  - *Source:* "updating…" → *Target:* "আপডেট হচ্ছে"
  - *Source:* "Adding %@ Videos" → *Target:* "%@টি ভিডিও যোগ করা হচ্ছে"

- **Distinguish কী and কি**: Use 'কি' when the answer to a question is yes or no. Use 'কী' when asking about what something is or what someone wants. Also use 'কী' when referring to a keyboard KEY.
  - *Source:* "What do you want?" → *Target:* "আপনি কী চান?"
  - *Source:* "Do you want to go?" → *Target:* "আপনি কি যেতে চান?"

- **Conjunction Usage (এবং vs ও)**: Use ও to join nouns (or short noun-like elements) within a clause. Use এবং to join independent clauses or full sentences. Do not add a comma before either conjunction in the target text.
  - *Source:* "macOS and iOS both have the same features and these are useful." → *Target:* "macOS ও iOS উভয়েরই একই ফিচার আছে এবং সেগুলি উপকারী।"

- **Maintain Parallel Flow in Lists**: List items must match the grammatical flow of the parent phrase in the source (conjugated, imperative, or infinitive). Use the imperative form for actionable list items.
  - *Source:* "Update your contact information" → *Target:* "আপনার কন্ট্যাক্টের তথ্য আপডেট করুন"

- **Avoid Personification (Passive Voice)**: Do not personify apps. Use passive voice instead of making the app the active subject (e.g., 'In [App], [action] is being done' / 'অ্যাপে... করা হচ্ছে').
  - *Source:* "Passwords is attempting to sign in to this account and fix the password." → *Target:* "পাসওয়ার্ড অ্যাপে এই অ্যাকাউন্টে সাইন ইন করা এবং পাসওয়ার্ড ঠিক করার চেষ্টা করা হচ্ছে।"

- **Avoid Personification (User Perspective)**: Do not personify features or access permissions. Shift to the user's perspective using phrases like 'Through [Feature], you can...' (এর মাধ্যমে আপনি... পারবেন).
  - *Source:* "Camera access allows you to redeem gift cards and add payment methods when managing payments with your Apple ID." → *Target:* "ক্যামেরা অ্যাক্সেসের মাধ্যমে আপনি গিফ্ট কার্ড রিডিম করতে ও আপনার Apple ID-এর মাধ্যমে পেমেন্ট সম্পন্ন করার সময় বিভিন্ন পেমেন্ট পদ্ধতি যোগ করতে পারবেন।"

- **Avoid Personification (Feature Description)**: When a string describes what a feature does (e.g., 'Opens the photo'), do not make the feature the actor. Restructure with a purpose phrase or passive voice.
  - *Source:* "Opens the photo to Crop." → *Target:* "ক্রপ করার জন্য ছবি খোলে।"

## Interface Elements

- **Button Names in Imperative Form with Helping Verbs**: Translate button and callout bar item names in the imperative form. Include a helping verb (করুন, লিখুন, দিন, চাপুন, etc.) to prevent the translation from reading as a noun. Without the helping verb, the meaning becomes ambiguous.
  - *Source:* "Edit" → *Target:* "এডিট করুন"
  - *Source:* "Reply" → *Target:* "উত্তর দিন"
  - *Source:* "Answer" → *Target:* "উত্তর দিন"

- **Transliterate Keyboard Key Names**: Names of keyboard keys and shortcuts should be transliterated. US keyboard shortcuts (e.g., ⌘N) should be copied as-is without localizing the key character. Physical key names like Option, Command, Esc are transliterated.
  - *Source:* "Option" → *Target:* "অপশন"
  - *Source:* "Up Arrow" → *Target:* "আপ অ্যারো"

- **Singular Nouns for App Names and Categories**: When categorizing objects or translating App names that are plural in English (e.g., Files, Photos, Reminders), use the singular noun in Bangla. Exceptions: 'Settings' (সেটিংস) and 'Stocks' (স্টকস) retain their plural transliteration.
  - *Source:* "Photos" → *Target:* "ছবি"

## Trademarks And Product Names

- **Do Not Transliterate Trademarks Used as Verbs**: If an Apple trademark is used as a verb in English, keep the trademark in Latin script and restructure the sentence using a native Bangla helper verb. Never transliterate it.
  - *Source:* "AirDrop this file." → *Target:* "এই ফাইলটি AirDrop করুন।"

## Variables

- **Preserve and Reorder Variables Correctly**: Variables must be kept intact and not altered. If Bangla word order requires reordering variables, number all variables with the n$ index immediately after the % sign so they resolve correctly at runtime. Do not change the decimal separator inside numeric format strings.
  - *Source:* "Check out the score %1$@ earned on %2$@ playing %3$@" → *Target:* "%2$@-এ %3$@ খেলে পাওয়া %1$@ স্কোর চেক করুন"

## Diversity And Inclusion

- **Use Culturally Sensitive Terminology**: Research words before using them to avoid cultural offense. For example, 'beef' should be transliterated as বিফ rather than গোমাংস, which is sensitive to the Hindu community. Similarly, 'pork' should be transliterated as পর্ক to avoid community-specific language. Avoid terms that are violent, oppressive, or ableist.
  - *Source:* "Beef" → *Target:* "বিফ" (not "গোমাংস")
  - *Source:* "Pork" → *Target:* "পর্ক" (not "শুয়োরের মাংস")

## Terminology

- **Translate Standard Colors, Transliterate Brand Colors**: Translate universally recognized basic colors into direct Bangla equivalents (e.g., Red to লাল). However, consistently transliterate coined or brand-specific color names (e.g., Midnight Black to মিডনাইট ব্ল্যাক) to maintain brand identity.
  - *Source:* "Midnight Black" → *Target:* "মিডনাইট ব্ল্যাক"

- **Translate Everyday Words**: If a natural, everyday Bangla word exists that accurately describes the function and fits the UI, translate it using native Bangla script.
  - *Source:* "Help" → *Target:* "সাহায্য"

- **Transliterate Tech Concepts and Archaic Terms**: Transliterate English words into Bangla script if the native Bangla translation is highly formal/archaic, or if the term is a modern tech concept with no native equivalent.
  - *Source:* "Password" → *Target:* "পাসওয়ার্ড"

- **Keep Global Standards in English**: If the term is a universally recognized technical protocol, file extension, or brand name, do not translate or transliterate it. Keep it in English (Latin script).
  - *Source:* "Wi-Fi" → *Target:* "Wi-Fi"

## Formatting

- **URL Formatting in Sentences**: Do not embed URLs directly into the flow of a sentence. Use a simple, instructional phrase (like "go here" or "visit") followed by a colon and the URL.
  - *Source:* "Go to account.apple.com." → *Target:* "এখানে যান: account.apple.com"

## Spelling

- **Use Short Vowels in Transliterated Words**: Transliterated English words containing 'ee' or 'oo' sounds must be written in Bangla with short vowels (ি, ু) rather than long vowels (ী, ূ) to maintain consistency.
  - *Source:* "League" → *Target:* "লিগ"

- **Use অ্যা for Short 'a' (/æ/) Sounds**: When an English word contains the short 'a' /æ/ sound (as in 'app' or 'flash'), always render it as 'অ্যা' at the start of a word, or with '্যা' when it follows a consonant. Do not use the regular 'আ'.
  - *Source:* "Camera" → *Target:* "ক্যামেরা" (not "কামেরা")

- **No Diacritic for the অ (ɔː) Sound**: The short 'o' or ɔː sound in English is an inherent part of Bangla consonants. Do not use a separate diacritic for it when translating.
  - *Source:* "Lock" → *Target:* "লক"

- **Distinguish Sibilant 'S' Consonants (স vs শ)**: Never use 'ষ' in transliterated words. Use 'স' when 'C' is followed by E, I, or Y. Use 'শ' when 'C' is followed by IA or EA, or for 'Sh' and 'tion' sounds.
  - *Source:* "Application" → *Target:* "অ্যাপ্লিকেশন"

- **Map 'Z' Sounds to জ Without Nuqta**: Bangla does not differentiate between 'ja' and 'za' sounds. Map English 'Z' sounds to 'জ'. Do not use 'ঝ' or add a Nuqta (়).
  - *Source:* "Zurich" → *Target:* "জুরিখ"

- **Map 'F' and 'Ph' Sounds to ফ Without Nuqta**: Both 'fa' and 'pha' sounds in English are denoted by the letter 'ফ'. Do not use a Nuqta (়) to differentiate them in transliteration.
  - *Source:* "File" → *Target:* "ফাইল"

- **Avoid Archaic Consonants in Transliteration**: When transliterating English loan words, avoid using the consonants ণ, ষ, ড়, ঢ়, and য unless they are long-established historical exceptions (like মেশিন).
  - *Source:* "Station" → *Target:* "স্টেশন" (not "স্টেশণ")

- **Transcribe English Plural Sounds Phonetically**: If an English word must be transliterated in its plural form, transcribe the final plural sound strictly based on its phonetics (e.g., using 'স' or 'জ').
  - *Source:* "Settings" → *Target:* "সেটিংস"

## Typography

- **Encode য়, র, ড়, and ঢ় as Their Own Consonants**: য়, র, ড়, and ঢ় are independent Bengali consonants, each with its own phoneme — they are not the bare consonants য, ব, ড, ঢ marked with a nuqta. Always encode them as the standard Bengali codepoints for those consonants, matching Unicode NFC normalization. Do not substitute the unmarked base consonants য (\u09AF), ব (\u09AC), ড (\u09A1), or ঢ (\u09A2) for them.
  - *Source:* "ya" → *Target:* "য়" (encode as the য় consonant, not as base য + nuqta)

- **Use Zero-Width Joiner (ZWJ) for Ya Phala**: Use ZWJ to correctly form conjuncts in transliterated words when 'র' is followed by 'য-ফলা'. The correct sequence is র + ZWJ + ◌্ + য.
  - *Source:* "Rank" → *Target:* "র‍্যাঙ্ক"
