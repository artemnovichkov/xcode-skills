# Marathi (mr) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Marathi uses single curly quotation marks ‘ (\u2018) and ’ (\u2019) for UI feature references, and the curly apostrophe ’ (\u2019). Double curly quotation marks “ (\u201C) and ” (\u201D) are used only for dialogue.
  - *Source:* "Network Configuration Missing Required Key" → *Target:* "नेटवर्क कॉंफिगरेशनमध्ये आवश्यक \u2018की\u2019 उपलब्ध नाही."

## Tone And Voice

- **Written Colloquial Style — Smart but Casual**: Use a written colloquial Marathi that balances spoken and formal language, following the register of respected newspapers. The tone should be closer to formal than informal but never stiff. Avoid Sanskritized vocabulary and word-for-word translation. The reader should not feel they are reading a translation.
  - *Source:* "I will show you how to do this task" → *Target:* "मी तुम्हाला हे टास्क कसे करायचे ते दाखवतो. (not कसं करायचं)"

- **Transliterate Only When No Easily Understood Marathi Word Exists**: First look for a Marathi word that the primary and secondary target audience can easily understand. Transliterate the English term only when no such word exists.
  - *Source:* "configuration
Install" → *Target:* "कॉंफिगरेशन (not विन्यास)
इंस्टॉल"
  - *Source:* "Install" → *Target:* "इंस्टॉल"

## Addressing Users

- **Use Formal तुम्ही / तुमचे**: Always address users with the honorific तुम्ही (formal you) and the corresponding verb form करा instead of the informal तू / कर. This must be strictly adhered to in all UI strings. Use the informal तू / तुझे only when the source string's tone is distinctly casual or a developer comment calls for an informal, youth-oriented voice (e.g. a children's app).
  - *Source:* "Select your network connection." → *Target:* "तुमचे नेटवर्क कनेक्शन निवडा."

- **Use Inclusive आपण for 'We' only, not for 'you'**: Marathi distinguishes inclusive and exclusive 'we'. Use आपण when 'we' includes the user or listener, and आम्ही when the user is excluded.
  - *Source:* "We can explore this together" → *Target:* "आपण हे एकत्र पाहू शकतो"

## Abbreviations

- **Marathi Abbreviation Formation**: Marathi abbreviations are formed by taking the first letter or syllable of a word, followed by a full stop. Country names like UK are written with periods between each letter: यू.के. For months use the first two letters (डिसें. for December, सप्टें. for September). Do not create new abbreviations in software unless all workarounds have failed.
  - *Source:* "Dr." → *Target:* "डॉ."
  - *Source:* "UK" → *Target:* "यू. के."

## Acronyms

- **Popular Acronyms Written Without Full Stops in Marathi Script**: Keep acronyms in English, unless Marathi localization is very common. Popular acronyms like HDR (एचडीआर), NASA (नासा), FIFA (फिफा) are written in Marathi script without full stops. Technical file format abbreviations (PDF, RTF, DOC) must stay untranslated.
  - *Source:* "Wi-Fi" → *Target:* "Wi-Fi"
  - *Source:* "PDF" → *Target:* "PDF"

## Date And Time

- **Date and Time Formats**: The correspondence date format is DD Month YYYY (e.g., 22 एप्रिल 2022). Long format is DD/MM/YYYY and short format is DD/MM/YY. Use international numerals in hardcoded dates. Do not use a comma to separate month from year. AM and PM are written as AM/PM following CLDR. Time uses a colon separator (HH:mm:ss) with no space before or after it.
  - *Source:* "April 22, 2022" → *Target:* "22 एप्रिल 2022"
  - *Source:* "10:18:30 AM" → *Target:* "10:18:30 AM"

## Measurements

- **Retain Electronic Units in English; Space Between Number and Unit**: Units related to electronics and computing (GB, KB, 1080p) must stay in English. There must be a space between the digit and the unit, matching the source spacing. Do not convert imperial to metric. Follow the latest CLDR release for all other unit representations.
  - *Source:* "10KB" → *Target:* "10KB"

## Numerals

- **Use International Numerals and Indian Separator System**: Keep numerals as international digits (0–9) — do not convert them to Devanagari numerals. Whether digits ultimately display as international or native is a user setting the translation can't see, so don't change the numeral system yourself. Group large numbers using the Indian separator system (e.g., 10,00,000). Follow ordinal forms पहिला/पहिली, दुसरा/दुसरी, etc. — avoid styles like 1ला, 2रा.
  - *Source:* "1000000" → *Target:* "10,00,000"
  - *Source:* "First / Second" → *Target:* "पहिला/पहिली / दुसरा/दुसरी"

## Special Characters

- **Translate 'and' as आणि and '&' as व**: In Marathi, the conjunction 'and' in general text is आणि. The ampersand symbol '&' used as a separator in feature or setting names is translated as व. Do not use the & symbol directly in Marathi UI text.
  - *Source:* "Files and folders" → *Target:* "फाइल आणि फोल्डर"
  - *Source:* "Display & Brightness" → *Target:* "डिस्प्ले व ब्राइटनेस"

## Punctuation

- **Add Space Before Colon to Distinguish from Visarga**: A space must be added before the colon (:) in Marathi text to prevent confusion with the Marathi visarga (ः). This space is required when the colon follows a Marathi word. When the colon follows an untranslated English word or number, the space can be omitted. Do not add a space before visarga in native Marathi words.
  - *Source:* "To:" → *Target:* "प्रति :"
  - *Source:* "Self (visarga)" → *Target:* "स्वतः (no space)"

- **Use Curly Single Quotes for UI References**: Always use curly single quotes (‘ ’) rather than straight quotes. Use double curly quotes only for dialogue. Single curly quotes may be added even when not in the source, where grammatical ambiguity would otherwise arise — but minimize their use.
  - *Source:* "Network Configuration Missing Required Key" → *Target:* "नेटवर्क कॉंफिगरेशनमध्ये आवश्यक \u2018की\u2019 उपलब्ध नाही."

## Grammar

- **Nuqta Is Not Used in Marathi**: Marathi does not use nuqta (nukta) to denote loan words. As per Maharashtra government guidelines, nuqta may only be used when writing Urdu or Sindhi lines within a Marathi document. All English sounds including f and ph are represented by फ without a nuqta.
  - *Source:* "phone / forward" → *Target:* "फोन / फॉरवर्ड (not फ़ोन)"

- **Anuswara Usage and Chandrabindu**: Marathi uses anuswara (ं) to all nasalize sounds. Prefer anuswara over the parsavarn forms exception is वाङ्मय).
  - *Source:* "Configuration" → *Target:* "कॉंफिगरेशन (not कॉन्फिगरेशन)"
  - *Source:* "College" → *Target:* "कॉलेज"

- **No Articles — Do Not Translate 'a/an' as एक**: Marathi has no articles. Do not translate 'a' or 'an' as एक unless omitting it creates a genuinely incomplete sentence. Most sentences translate naturally without an article. Consider using एक only when it is truly necessary for meaning.
  - *Source:* "Have a coffee." → *Target:* "कॉफी प्या."
  - *Source:* "Please bring me a cup of coffee." → *Target:* "माझ्यासाठी एक कप कॉफी आण."

- **Prefer Passive Voice When Subject Is Absent**: When the English source is active but no explicit subject performs the action, use passive voice in Marathi to keep the translation aesthetic and unambiguous. This applies to gerund-only strings, verb+object strings, and strings where you cannot answer 'who will do this?' from the string alone.
  - *Source:* "Adding %@ Videos" → *Target:* "%@ व्हिडिओ जोडले जात आहेत."

- **Variables and Postpositions — Use Independent Words**: Directly concatenating postpositions (विभक्ती प्रत्यय) like च्या/ला/ना/शी to variables causes readability issues at runtime. Use independent words instead: येथे for places, रोजी for dates, वाजता for time, ह्यांनी for persons. Always add a non-breaking space before चा/ची/चे/च्या/ने/ला when they follow a DNT term.
  - *Source:* "%@ shared this folder" → *Target:* "%@ ह्यांनी हे फोल्डर शेअर केले"

- **Pluralization of transliterated words**: When transliterating English plural terms, always use the singular form as the default. Follow the guidelines below:
In a sentence: Use the singular transliterated form, regardless of whether the original English term is plural.
As a stand-alone term: The plural form may be used only when the term appears independently, outside of a sentence.
When plural is not marked in the word itself: Reflect the plural meaning through the verb or sentence structure surrounding the term.
  - *Source:* "We played 4 games" → *Target:* "आम्ही 4 गेम खेळलो"

- **Gender of transliterated words**: To decide the grammatical gender of a transliterated loan word, translate the word into Marathi and give the transliteration the same gender as that Marathi word. For example, "device" translates to साधन/उपकरण (neuter), so डिव्हाइस is also neuter and takes the neuter "that" (ते): ते डिव्हाइस.
  - *Source:* "That Device" → *Target:* "ते डिव्हाइस"

## Interface Elements

- **Category Labels**: All category labels, including app and feature names, must be translated or transliterated in singular form. The exception is a string marked do-not-translate, which is left as-is.
  - *Source:* "Messages" → *Target:* "संदेश"

- **Button Names in Imperative with Helping Verb**: Buttons must be translated in imperative form using helping verbs like करा or द्या to prevent the translation from reading as a noun. Exception: macOS menu bar items classified as NSMenuItems (Edit, View, Format, Arrange) are translated as nouns. Callout bar items generally add करा.
  - *Source:* "Edit (button)" → *Target:* "संपादित करा"
  - *Source:* "Reply" → *Target:* "उत्तर द्या"
  - *Source:* "Edit (macOS menu bar)" → *Target:* "संपादन (noun)"

## Variables

- **Number Variables When Reordering; Preserve Decimal Format Strings**: Keep all variables exactly as they appear in the source. If Marathi word order requires reordering, add positional indices (n$) immediately after the % sign in all variables of that string. Do not change a period to a comma inside numeric format strings such as %.1f — the decimal separator is handled by the software.
  - *Source:* "Check out the score %1$@ earned on %2$@ playing %3$@" → *Target:* "%3$@ खेळून %2$@ वर मिळवलेला %1$@ स्कोअर पहा."

## Diversity And Inclusion

- **Adopt Gender-Inclusive Language**: Avoid using masculine forms as the default for all users wherever possible. Recommended strategies include using neuter terms, phrasing sentences valid for both genders, and using plural masculine forms only when gender-neutral phrasing sounds unnatural. Minimize use of द्वारा for gender-neutral constructions; prefer ने or च्याकडून.
  - *Source:* "Are you sure you want to turn off Zoom?" → *Target:* "तुम्हाला Zoom निश्चितपणे बंद करायचे आहे का?"
  - *Source:* "You're not connected to the internet" → *Target:* "तुम्ही इंटरनेटशी जोडलेले नाहीत."

## Spelling

- **Encode ॲ as a Single Character**: Encode ॲ (U+0972) as the single precomposed character, not the sequence अ + ॅ (U+0905 + U+0945).
  - *Source:* "Actor" → *Target:* "ॲक्टर"

## Emoji

- **Emoji**: Try to avoid using prepositions and helping words in Emoji translations unless necessary.
  - *Source:* "%d black cat emoji " → *Target:* "%d काळी मांजर इमोजी (not %d काळ्या रंगाच्या मांजरीची इमोजी)"
