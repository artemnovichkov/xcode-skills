# Odia (or) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Odia uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting feature or functionality names, and the curly apostrophe ’ (\u2019).
  - *Source:* "Hold select to clear" → *Target:* "କ୍ଲିଅର୍ କରିବା ପାଇଁ \u201Cଚୟନ କରନ୍ତୁ\u201Dକୁ ଦବାଇ ରଖନ୍ତୁ"

## Tone And Voice

- **Smart but Casual Written Colloquial Style**: The Odia tone is professional and positive, closer to formal than informal, but never stiff. Use the written colloquial style that balances spoken and written Odia. Follow the language register of reputable Odia newspapers. Avoid Sanskritized vocabulary whenever a simpler, commonly understood word exists.
  - *Source:* "school" → *Target:* "ସ୍କୂଲ୍"
  - *Source:* "flower" → *Target:* "ଫୁଲ"

## Addressing Users

- **Use Formal Second Person (ଆପଣ) for All Users**: Always address the user with the formal honorific ଆପଣ and the corresponding formal verb form (e.g. କରନ୍ତୁ). The informal ତୁ/ତୁମେ and casual verb forms like କର/କରେ must not be used, as they are not respectful. Non-human entities (apps, devices) use an informal tone.
  - *Source:* "iPad will play ringtones, alerts, and system sounds." → *Target:* "iPad ରିଂଟୋନ୍, ଆଲର୍ଟ୍ ଓ ସିଷ୍ଟମ୍ ସାଉଣ୍ଡ୍‌ଗୁଡ଼ିକୁ ଚଲାଇବ।"

## Terminology

- **Transliterate Technical Terms, Translate Common Ones**: Prefer transliteration for technical jargon that has entered everyday Odia usage or has no natural Odia equivalent. Prefer a genuine Odia word when it is commonly understood and not archaic. Avoid producing text that reads like English written in Odia script. Each term should be evaluated individually based on context, audience familiarity, and frequency in media.
  - *Source:* "Domain" → *Target:* "ଡୋମେନ୍"
  - *Source:* "road" → *Target:* "ରାସ୍ତା"
  - *Source:* "Installation" → *Target:* "ଇନ୍‌ଷ୍ଟଲେଶନ୍"

- **Follow British English Pronunciation for Transliteration**: When transliterating English words, use British English pronunciation as the reference, following the International Phonetic Alphabet (IPA) from the Oxford Dictionary of English.
  - *Source:* "Sync /sɪŋk/" → *Target:* "ସିଙ୍କ୍"
  - *Source:* "Sheet /ʃiːt/" → *Target:* "ଶୀଟ୍"
  - *Source:* "Zoom /zuːm/" → *Target:* "ଜୂମ୍"

- **Hybrid Approach (Translation + Transliteration)**: A hybrid approach is preferred when one part of the phrase is a highly technical or branded term (best transliterated) and the other part is a common, generic word with a perfect Odia equivalent (best translated).
  - *Source:* "Network connection" → *Target:* "ନେଟ୍‌ୱର୍କ୍ ସଂଯୋଗ"

- **Balance British and American English Vocabulary**: When a source term has different US and UK equivalents, generally prefer the UK/Indian English equivalent (e.g., Mobile instead of Cellular). However, do not blindly follow British usage if the American term is more established in India.
  - *Source:* "ATM" → *Target:* "ATM"

## Grammar

- **Always Use Halant in Transliterated Words**: When transliterating English words, always add the halant (୍) where phonetically required to avoid ambiguity between consonant-final syllables and open syllables. For example, 'Bank' ends in a closed syllable and must be written ବ୍ୟାଙ୍କ୍, not ବ୍ୟାଙ୍କ.
  - *Source:* "Password" → *Target:* "ପାସ୍‌ୱର୍ଡ୍"
  - *Source:* "Passcode" → *Target:* "ପାସ୍‌କୋଡ୍"
  - *Source:* "Bank" → *Target:* "ବ୍ୟାଙ୍କ୍"

- **Chandrabindu vs. Anuswara**: Use anuswara (ଂ) for the 'ang' sound and chandrabindu (ଁ) for the 'aum' sound. Prefer the traditional Juktakshyar spelling over the newer anuswara forms. Anuswara is used only for abargya consonants (ଯ, ର, ଳ, ହ, ଶ, ଷ, ସ, ଲ etc.) and for the 'ng' sound in transliterated English words.
  - *Source:* "Rupee" → *Target:* "ଟଙ୍କା"
  - *Source:* "Editing" → *Target:* "ଏଡିଟିଂ"

- **No Literal Translation of English Articles**: Odia has no articles equivalent to 'a', 'an', or 'the'. Do not translate these as ଏକ or ଗୋଟିଏ unless the sentence genuinely requires a number for meaning. In most cases, simply omit the article in the Odia translation.
  - *Source:* "Wish you a very happy birthday." → *Target:* "ଆପଣଙ୍କ ଜନ୍ମଦିନ ଶୁଭ ହେଉ।"
  - *Source:* "I bought a sweater yesterday." → *Target:* "ମୁଁ ଗତକାଲି ଗୋଟିଏ ସ୍ବେଟର୍ କିଣିଲି।"

- **Use ଓ Between Words, ଏବଂ Between Phrases**: Both ଓ and ଏବଂ mean 'and', but they are used in different contexts. ଓ connects two individual words, while ଏବଂ connects two phrases or clauses.
  - *Source:* "Laptop and keyboard" → *Target:* "ଲାପ୍‌ଟପ୍ ଓ କୀ\u2019ବୋର୍ଡ୍"
  - *Source:* "Two laptops & three keyboards" → *Target:* "ଦୁଇଟି ଲାପ୍‌ଟପ୍ ଏବଂ ତିନୋଟି କୀ\u2019ବୋର୍ଡ୍"

- **Bibhakti (Case Markers) Spacing**: Bibhaktis such as ରେ, ରୁ, କୁ, ଙ୍କୁ are written without a preceding space when they follow Odia words. However, a space must appear before a bibhakti when it follows URLs, variables, numbers, or English words.
  - *Source:* "product & services from Apple" → *Target:* "Apple ର ପ୍ରଡକ୍ଟ୍ ଓ ସେବା"
  - *Source:* "features of your face" → *Target:* "ଆପଣଙ୍କ ଚେହେରାର ଫୀଚର୍"
  - *Source:* "Check out the score %1$@ earned on %2$@ playing %3$@" → *Target:* "%2$@ ରେ %3$@ ଖେଳି %1$@ ପାଇଥିବା ସ୍କୋର୍ ଯାଞ୍ଚ କରନ୍ତୁ।"
  - *Source:* "Go to apple.com" → *Target:* "apple.com କୁ ଯାଆନ୍ତୁ"
  - *Source:* "will not open in macOS 27" → *Target:* "macOS 27 ରେ ଖୋଲିବ ନାହିଁ"

- **Passive Voice for System-Initiated Actions**: Use the passive voice when the string does not specify an explicit subject — for example, progress messages, gerund-only strings, and verb + object strings. If you can ask 'Who is doing this?' and the answer is not in the string, use passive voice. When in doubt, default to passive.
  - *Source:* "updating…" → *Target:* "ଅପ୍‌ଡେଟ୍ ହେଉଛି…"
  - *Source:* "Adding %@ Videos" → *Target:* "%@ ଟି ଭିଡିଓ ଯୋଗ କରାଯାଉଛି"

- **Odia Is Gender-Neutral**: Pronouns, adjectives, and verbs in Odia do not change based on the gender of the noun. Transliterated English words also remain gender-neutral. Use gender-neutral phrasing wherever possible and avoid reinforcing male or female stereotypes.
  - *Source:* "Sunita is driving a car. She is driving it slowly." → *Target:* "ସୁନୀତା ଏକ କାର୍ ଚଲାଉଛନ୍ତି। ସେ ଏହାକୁ ଧୀରେ ଚଲାଉଛନ୍ତି।"

- **Canonical Unicode Forms for Vowels**: Always use pre-composed characters for independent vowels (e.g., ଆ, not ଅ+ା).

- **Canonical Unicode Forms for Matras**: Always use single code points for two-part vowel signs (e.g., ୋ, ୌ, not େ+ା, ୈ+ା).

- **Ya-phala Conjuncts (ୟ)**: When creating a consonant conjunct with a 'ya' sound (ya-phala), always use the character ୟ (Oriya Letter YYA, U+0B5F) as the second consonant. Do not use ଯ (Oriya Letter YA, U+0B2F).

- **Ba-phala Conjuncts (ବ)**: When creating a consonant conjunct with a 'ba' sound (ba-phala), always use the character ବ (Oriya Letter BA, U+0B2C). Do not use ଵ (VA) or ୱ (WA).

- **Atomic Character WA (ୱ)**: The letter ୱ (Oriya Letter WA, U+0B71) is an atomic character and must be encoded as its single, dedicated code point. It should never be constructed as a conjunct (e.g., ଓ+୍+ବ).

- **Plurals in Cases of Uncertainty**: When a plural noun in the source text acts as a label for a list or group of items whose exact number is unknown or variable, prefer the singular form in Odia. Use the plural marker ଗୁଡ଼ିକ only when the context explicitly confirms more than one item.
  - *Source:* "Your iPad cannot show the schedules or send reminders for the following medications:" → *Target:* "ଆପଣଙ୍କ iPad ନିମ୍ନଲିଖିତ ଔଷଧ ପାଇଁ ଶେଡ୍ୟୂଲ୍ ଦେଖାଇପାରିବ ନାହିଁ କିମ୍ବା ରିମାଇଣ୍ଡର୍ ପଠାଇପାରିବ ନାହିଁ:"

- **English Articles in Headings, Titles, and other strings**: English articles 'a', 'an', or 'the' should not always be translated literally as ଏକ or ଗୋଟିଏ and can be omitted for a more natural Odia style.
  - *Source:* "Add a personal touch" → *Target:* "ପର୍ସନଲ୍ ଟଚ୍ ଯୋଡ଼ନ୍ତୁ"

- **Standalone Alternative Text**: Standalone Alternative Text strings used to describe images or UI states should be translated using the passive voice (e.g., "is selected" -> "ଚୟନ କରାଯାଇଛି") or as descriptive phrases, matching the context of the image.
  - *Source:* "The AutoFill button is selected." → *Target:* "ଅଟୋଫିଲ୍ ବଟନ୍ ଚୟନ କରାଯାଇଛି।"

- **Passive Voice for strings without an Explicit Subject**: Use the passive voice when the string does not specify an explicit subject, such as when a gerund is followed by a variable or preposition.
  - *Source:* "Adding %@ Videos" → *Target:* "%@ ଟି ଭିଡିଓ ଯୋଗ କରାଯାଉଛି"

- **Active Voice for strings with an Explicit Subject**: Try to follow the active voice and emphasis of the source as much as possible when the string specifies an explicit subject.
  - *Source:* "%@ will send you an email." → *Target:* "%@ ଆପଣଙ୍କୁ ଏକ ଇମେଲ୍ ପଠାଇବ।"

## Orthography

- **Bindu Usage on ଡ and ଢ**: The dot (bindu) is added under ଡ and ଢ to form ଡ଼ and ଢ଼ only when these letters appear in the middle or end of native Odia words. At the beginning of a word they are written without the dot.
  - *Source:* "Left to Right" → *Target:* "ବାମରୁ ଡାହାଣ"
  - *Source:* "Add a custom message" → *Target:* "ଏକ କଷ୍ଟମ୍ ମେସେଜ୍ ଯୋଡ଼ନ୍ତୁ"
  - *Source:* "Audio" → *Target:* "ଅଡିଓ"

- **Zero Width Joiner (ZWJ) Usage**: A ZWJ is present in the encoding of a conjunct formed with ୟ (YYA) as the second element. Encode such conjuncts with the ZWJ in that position; do not insert ZWJ manually elsewhere.
  - *Source:* "Match" → *Target:* "ମ‍୍ୟାଚ୍"

- **Zero Width Non-Joiner (ZWNJ) Usage**: A ZWNJ is present in the encoding where a halant (Virama) is applied twice in the middle of a word to avoid unwanted formation of conjuncts. A ZWNJ should never occur at the word-ending position.
  - *Source:* "update" → *Target:* "ଅପ୍‌ଡେଟ୍"

## Interface Elements

- **Buttons Use Imperative with Helping Verb**: Button labels are translated in the imperative form with a formal tone. Helping verbs like କରନ୍ତୁ or ଦିଅନ୍ତୁ must be included so the label functions as a verb rather than a noun. In callout bars, the helping verb may be dropped only when the meaning is unambiguous and the term is widely understood.
  - *Source:* "Edit" → *Target:* "ଏଡିଟ୍ କରନ୍ତୁ"
  - *Source:* "Cancel" → *Target:* "ବାତିଲ୍ କରନ୍ତୁ"
  - *Source:* "Reply" → *Target:* "ଉତ୍ତର ଦିଅନ୍ତୁ"

- **App Names Use Singular Form**: When localizing app names and category labels, use the singular noun form even when the source is plural. Plural forms sound awkward as standalone labels in Odia. One exception is 'Settings', which is rendered as ସେଟିଂସ୍ (retaining the plural marker); for other words that keep their plural marker, see 'App and Feature Names Exception: Plural Retention' below.
  - *Source:* "Photos" → *Target:* "ଫଟୋ" (app name)
  - *Source:* "Settings" → *Target:* "ସେଟିଂସ୍"

- **Double Curly Quotes for Grammatically Ambiguous UI Terms**: Use double curly quotes (“ (\u201C) and ” (\u201D)) around feature or functionality names in a sentence only when their use would otherwise create grammatical ambiguity (e.g. change in number, oblique case, or other grammatical issue). Minimize the use of quotes and never use straight quotes in UI strings.
  - *Source:* "Hold select to clear" → *Target:* "କ୍ଲିଅର୍ କରିବା ପାଇଁ \u201Cଚୟନ କରନ୍ତୁ\u201Dକୁ ଦବାଇ ରଖନ୍ତୁ"

- **App and Feature Names: Translation vs Transliteration**: Translate app and feature names if a natural, widely recognized Odia equivalent exists (e.g., Books -> ବହି). Transliterate if it is an established global digital concept or technical jargon (e.g., Apps -> ଆପ୍). The default form should be singular.
  - *Source:* "Books" → *Target:* "ବହି"

- **App and Feature Names Exception: Plural Retention**: Retain the plural marker ('s') during transliteration for words that function exclusively as plural nouns (e.g., Vitals), colloquially established plural loanwords (e.g., Tips, Credits), or discipline/system nouns ending in '-ics' (e.g., Haptics, Analytics).
  - *Source:* "Vitals" → *Target:* "ଭାଇଟଲ୍ସ୍"

- **Category Labels in Sentences**: When a transliterated category label refers to the UI tab/feature or is preceded by a number/quantifier, keep it singular (e.g., 3 notifications -> 3 ଟି ନୋଟିଫିକେଶନ୍). Use the plural marker (ଗୁଡ଼ିକ) only when specifically referring to multiple distinct items in a descriptive sentence.
  - *Source:* "3 new notifications" → *Target:* "3 ଟି ନୂଆ ନୋଟିଫିକେଶନ୍"

- **Button Names in Sentences**: When a button name is referenced in running text, use double curly quotes (“ (\u201C) and ” (\u201D)) if the name breaks the sentence flow or creates grammatical ambiguity. Quotes are not needed if the button or CTA is already bound by asterisk signs.
  - *Source:* "click Add button" → *Target:* "\u201Cଯୋଡ଼ନ୍ତୁ\u201D ବଟନ୍ ଉପରେ କ୍ଲିକ୍ କରନ୍ତୁ"

- **Inline Alt-Text Elements**: Do not translate the structural tags placed inside angle brackets (e.g., <AltText>). However, the text inside the tags may be translated, and the order of inline elements can be changed to fit Odia sentence structure.
  - *Source:* "Tap <AltText>Settings button</AltText>" → *Target:* "<AltText>ସେଟିଂସ୍ ବଟନ୍</AltText> ରେ ଟାପ୍ କରନ୍ତୁ"

## Punctuation

- **Use Odia Full Stop Where Source Has a Period as full stop.**: The Odia full stop ପୂର୍ଣ୍ଣଚ୍ଛେଦ (।) must be used wherever a sentence ends if the source contains a period. Do not add or remove periods from strings that do not have them in the source, as they may be part of string concatenation or programmatic formatting.
  - *Source:* "Sunita is driving a car." → *Target:* "ସୁନୀତା ଏକ କାର୍ ଚଲାଉଛନ୍ତି।"

## Abbreviations

- **Abbreviation Formation in Odia**: Avoid abbreviations in software translations unless space constraints make them unavoidable. Odia abbreviations are formed by taking the first syllable of the word followed by a dot (.). For example, ଦ.ପୂ. for ଦକ୍ଷିଣ-ପୂର୍ବ. Technical file format abbreviations (PDF, DOC, RTF) are kept in English.
  - *Source:* "South-East" → *Target:* "ଦ.ପୂ." (abbreviated)

## Acronyms

- **Keep Acronyms in English Unless a Common Odia Form Exists**: Acronyms are not translated unless a very common Odia localized equivalent exists. Popular Odia acronyms such as ୟୁନିସେଫ୍ (UNICEF) and ବିଜେପି (BJP) are used without the abbreviation sign. Technical file format codes like PDF, DOC, and RTF stay in English and are not transliterated.
  - *Source:* "HDR" → *Target:* "HDR" (High Dynamic Range)

## Date And Time

- **International Numerals in Dates and Times, No AM/PM Translation**: Use international numerals (not native Odia numerals) for hardcoded dates and times. Date format is DD/MM/YYYY for long format. Time uses a colon separator (hh:mm:ss). Do not localize AM/PM — keep it in English and match the source capitalization. Do not use a comma between the month and year.
  - *Source:* "29 December 2023" → *Target:* "29 ଡିସେମ୍ବର୍ 2023"
  - *Source:* "10:18:35" → *Target:* "10:18:35"

## Numerals

- **Indian Numbering System for Separators**: Group large numbers using the Indian numbering system for digit grouping (e.g. 10,00,000 for one million). Keep the source's digits as they appear and do not transform the numeral system yourself. For count of objects, use the counter ଟି (for things) or ଜଣ ବ୍ୟକ୍ତି (for people).
  - *Source:* "10,000,000 songs" → *Target:* "1,00,00,000 ଗୀତ"
  - *Source:* "1 person" → *Target:* "1 ଜଣ ବ୍ୟକ୍ତି"
  - *Source:* "5 cards found" → *Target:* "5 ଟି କାର୍ଡ୍ ମିଳିଲା"

## Measurements

- **Electronic Units Stay in English**: Measurement units related to electronics or computers (GB, KB, MB, etc.) are kept in English. For other units, always use the Odia abbreviation dot (.) for short and narrow unit forms. Some units without popular Odia short forms (lb, oz, yd, db, kcal) are kept in English.
  - *Source:* "8 GB" → *Target:* "8 GB"
  - *Source:* "kg" → *Target:* "କି.ଗ୍ରା."
  - *Source:* "cm" → *Target:* "ସେ.ମୀ."

- **No Conversion of Measurements**: Do not convert measurements (e.g., imperial to metric) to local measurements when given in sentences or phrases. For example, do not convert inches to cm. Keep the original measurement values.
  - *Source:* "5\u2033 display" → *Target:* "5\u2033 ଡିସ୍‌ପ୍ଲେ"

- **Spacing Between Number and Unit**: Match the space between the number and the unit of measurement exactly as it appears in the source. If the source has no space, the target should have no space.
  - *Source:* "10KB" → *Target:* "10KB"

- **Abbreviation Dot for Short Units**: Always use the Odia abbreviation symbol (.) for short units (e.g., kg, cm, km, mm, ml, l). Translate these as କି.ଗ୍ରା., ସେ.ମୀ., କି.ମୀ., ମି.ମୀ., ମି.ଲୀ., ଲୀ.
  - *Source:* "10 kg" → *Target:* "10 କି.ଗ୍ରା."

- **Transliteration of Loan Word Units**: Transliterate loan-word unit names using Oxford dictionary pronunciation rules. For example, use ମୀଟର୍, କିଲୋଗ୍ରାମ୍, ସେଣ୍ଟିମୀଟର୍, ପାଉଣ୍ଡ୍, ଆଉନ୍ସ୍, ଫୁଟ୍, ଲୀଟର୍, etc.
  - *Source:* "centimeter" → *Target:* "ସେଣ୍ଟିମୀଟର୍"

- **Units Kept in English**: Abbreviated units that lack popular short forms in Odia and do not have common transliterated full forms (such as dB, kcal) must be kept in English.
  - *Source:* "kcal" → *Target:* "kcal"

## Names And Addresses

- **Use Inclusive Indian Placeholder Names**: Replace English placeholder names with Indian names that do not reveal a specific caste, religion, or community. If the source or the developer's comment indicates the name refers to a specific, real individual (rather than a generic placeholder), keep that person's actual name — transliterating it into Odia script if it appears in Latin — instead of substituting a placeholder.

## Special Characters

- **No Space between Currency Symbol and Amount**: Do not insert a space between the Indian Rupee symbol (₹) and the amount. Write currency amounts directly after the symbol without any whitespace.
  - *Source:* "₹500.45" → *Target:* "₹500.45"

## Diversity And Inclusion

- **Inclusive Language and Fair Representation**: Translate consciously to include everyone. Avoid terms that are violent, oppressive, or ableist (e.g. *kill*, *master*/*slave*, *sanity check*). Do not use color to convey positive or negative qualities. Avoid stereotypes based on gender, ability, or age, and represent diverse backgrounds when content depicts people. Odia is grammatically gender-neutral (see Grammar) — keep phrasing neutral. When referring to people with disabilities, use people-first language. Use inclusive placeholder names that don't reveal caste, religion, or community (see Names And Addresses).

## Variables

- **Reorder Variables Using Positional Indices**: Preserve all variables exactly as they appear in the source. When Odia grammar requires a different word order, number all variables using positional arguments ('n$' after the % sign). Never change the period in numeric format strings like %.1f to a comma — the software handles decimal formatting.
  - *Source:* "Check out the score %1$@ earned on %2$@ playing %3$@" → *Target:* "%2$@ ରେ %3$@ ଖେଳି %1$@ ପାଇଥିବା ସ୍କୋର୍ ଯାଞ୍ଚ କରନ୍ତୁ।"
