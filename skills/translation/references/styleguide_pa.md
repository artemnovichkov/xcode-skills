# Punjabi (pa) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Punjabi uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting UI feature names, and the curly apostrophe ’ (\u2019). Note that the Chhut Marodi shortened form uses a **straight apostrophe** (U+0027), not a curly one — see Punctuation.
  - *Source:* "Tap \u201CEdit\u201D to change your note." → *Target:* "ਆਪਣਾ ਨੋਟ ਬਦਲਣ ਲਈ \u201Cਸੋਧ ਕਰੋ\u201D 'ਤੇ ਟੈਪ ਕਰੋ।"

## Tone And Voice

- **Smart but Casual Register**: Use a written colloquial style that is a fine balance between spoken and written Punjabi, closer to formal than informal but never stiff or archaic. Follow the register of national newspapers. Avoid old or obscure vocabulary wherever a more current word exists.
  - *Source:* "Sign in with your account" → *Target:* "ਆਪਣੇ ਖਾਤੇ ਨਾਲ ਸਾਈਨ ਇਨ ਕਰੋ"

- **Prefer Punjabi but Prioritize Clarity**: Use native Punjabi or well-integrated loan words when clearly understood by urban Punjabi speakers. When no natural equivalent exists or the Punjabi term is archaic, transliterate the English term. The guiding principle is the reader's ease of understanding, not word origin.
  - *Source:* "Installation" → *Target:* "ਇੰਸਟਾਲੇਸ਼ਨ"

- **Use Gurmukhi Script**: All Punjabi text must be written in Gurmukhi. Transliterated English words must also be rendered in Gurmukhi using British/Indian English pronunciation as reference, not American English.
  - *Source:* "Default / Folder / Phone" → *Target:* "ਡਿਫ਼ੌਲਟ / ਫ਼ੋਲਡਰ / ਫ਼ੋਨ"

## Addressing Users

- **Use the Honorific Second Person (ਤੁਸੀਂ)**: Always address the user with ਤੁਸੀਂ and formal verb forms (ਗਏ, ਕਰੋ). Never use informal ਤੂੰ or informal verb forms (ਗਈ). Apply this uniformly across all strings, with no exceptions.
  - *Source:* "You have not gone home." → *Target:* "ਤੁਸੀਂ ਘਰ ਨਹੀਂ ਗਏ" (not: ਤੂੰ ਘਰ ਨਹੀਂ ਗਈ)

## Abbreviations

- **Avoid Abbreviations in Software Strings**: Do not abbreviate words in software translations unless all other approaches have been exhausted. Sensitive abbreviations like SOS must remain in English.
  - *Source:* "North" (abbreviated) → *Target:* "ਉ." (from ਉੱਤਰ)

## Acronyms

- **Retain English Acronyms; Transliterate Well-Known Ones**: Do not translate technical acronyms unless a widely recognized Punjabi equivalent exists. Popular acronyms like UNESCO and FIFA are transliterated into Gurmukhi without the abbreviation period.
  - *Source:* "UNESCO / FIFA" → *Target:* "ਯੂਨੈਸਕੋ / ਫ਼ੀਫ਼ਾ"

## Date And Time

- **Date and Time Format**: Use international numerals in hardcoded dates and times. Preferred date format: 17 ਮਾਰਚ 2022 (correspondence) and DD/MM/YYYY (long). Use colon as time separator with no surrounding spaces. Do not localize AM/PM.
  - *Source:* "March 17, 2022 / 7:15 AM" → *Target:* "17 ਮਾਰਚ 2022 / 7:15 AM"

## Measurements

- **Do Not Convert Measurement Units**: Retain the measurement system from the source. Electronics and computing units (GB, MB, KB, Hz, dB) must remain in English. Keep numeric values as the source's digits. Use international numerals for all numeric values.
  - *Source:* "8 GB / 1080p" → *Target:* "8 GB / 1080p"

- **Localize Common Physical Units with Abbreviation Sign**: Common metric units km and kg are rendered as Punjabi abbreviations: ਕਿ.ਮੀ. for km and ਕਿ.ਗ੍ਰਾ. for kg. Always place a space between the number and the unit.
  - *Source:* "5 km / 10 kg" → *Target:* "5 ਕਿ.ਮੀ. / 10 ਕਿ.ਗ੍ਰਾ."

## Addresses

- **Use Generic Punjabi Sample Names**: Replace English placeholder names with generic Punjabi names that do not reveal caste or sect. Use diverse names. If the source or the developer's comment indicates the name refers to a specific, real individual (rather than a generic placeholder), keep that person's actual name — transliterating it into Gurmukhi script if it appears in Latin — instead of substituting a placeholder.

- **Indian Address Format and PIN Code**: Format addresses using Indian structure: Name, Building/Plot, Street, Locality, City, State-PIN Code (e.g. ਅਮਨਦੀਪ ਸਿੰਘ / ਮਕਾਨ ਨੰ. 1234 / ਮੋਹਾਲੀ, ਪੰਜਾਬ-140055). PIN codes are 6 digits with no spaces in international numerals. Non-Indian addresses remain in English.

## Numerals

- **Use Indian Numbering System for Digit Grouping**: Apply the Indian numbering system for grouping large numbers (10,00,000 not 1,000,000). Keep the source's digits as they are — do not convert them to native Gurmukhi numerals yourself, as whether digits ultimately display as international or native is a user setting the translation can't see.
  - *Source:* "1,000,000 songs" → *Target:* "10,00,000 ਗਾਣੇ"

- **Ordinal Numbers**: Spell out the first four ordinals: ਪਹਿਲਾ, ਦੂਜਾ, ਤੀਜਾ, ਚੌਥਾ. From 5th onward, append ਵਾਂ to the numeral (5ਵਾਂ, 6ਵਾਂ, etc.).
  - *Source:* "1st / 5th" → *Target:* "ਪਹਿਲਾ / 5ਵਾਂ"

## Special Characters

- **Use Dandi as the Punjabi Full Stop**: Sentences end with Dandi (।) not a Latin full stop. Do not add Dandi if the source string does not end with a period, as the string may be concatenated programmatically.
  - *Source:* "Please try again later." → *Target:* "ਕਿਰਪਾ ਕਰਕੇ ਬਾਅਦ ਵਿੱਚ ਦੁਬਾਰਾ ਕੋਸ਼ਿਸ਼ ਕਰੋ।"

- **Always Use Nuqta for Correct Pronunciation**: Use nuqta for all six Punjabi consonants that carry it: ਸ਼, ਖ਼, ਗ਼, ਜ਼, ਫ਼, ਲ਼. Use ਫ਼ for English f sound and ਜ਼ for z sound.
  - *Source:* "File / Default / Folder / Zone" → *Target:* "ਫ਼ਾਈਲ / ਡਿਫ਼ੌਲਟ / ਫ਼ੋਲਡਰ / ਜ਼ੋਨ"

- **Currency Symbol: No Space After Rupee Sign**: Do not place a space between the Indian Rupee symbol and the numeral (₹500.45, not ₹ 500.45). When writing in full, use ਰੁਪਏ as a standalone word after the numeral, e.g. ਪੰਜਾਹ ਰੁਪਏ.
  - *Source:* "500.45 rs./500.45 rupees" → *Target:* "₹500.45/ ਪੰਜਾਹ ਰੁਪਏ"

## Orthography

- **Correct Unicode Sequences for Nuqta Consonants**: For ਸ਼ encode the precomposed character U+0A36. For ਖ਼, ਗ਼, ਜ਼, ਫ਼ encode base consonant + combining Nuqta (U+0A3C) — these are Composition Exclusions and have no single precomposed form.
  - *Source:* "File / Zone / Evening" → *Target:* "ਫ਼ਾਈਲ / ਜ਼ੋਨ / ਸ਼ਾਮ"

- **Correct Encoding of Independent Vowels and Dependent Vowel Signs**: Encode each independent vowel as its single Unicode codepoint, never constructed from two characters (encode ਆ as U+0A06, not ਅ+ਾ; encode ਇ as U+0A07, not ੲ+ਿ). Dependent vowel signs must always follow the consonant, never precede it (ਕਿ = ਕ+ਿ, not ਿ+ਕ). Do not use ZWJ or ZWNJ to construct vowel characters.

- **Conjuncts: Only Three Used in Modern Gurmukhi**: In modern Punjabi only three subjoined pairin forms are used: ਸ੍ਵ, ਸ੍ਰ, ਸ੍ਹ. Additional conjuncts appear only in traditional Gurbani texts. All conjuncts must be formed using Consonant + Halant + Consonant (e.g. ਕ੍ਰ = ਕ+੍+ਰ and ੜ੍ਹ = ੜ+੍+ਹ).

## Punctuation

- **Comma and Colon Usage**: Do not place a comma before ਅਤੇ (and) or ਜਾਂ (or) in a list. Use colons to introduce lists or explanations. No spaces before or after a slash in ratios or paths.
  - *Source:* "Do task one, two, and three." → *Target:* "ਕੰਮ ਇੱਕ, ਦੋ ਅਤੇ ਤਿੰਨ ਕਰੋ।" (no comma before ਅਤੇ)

- **Chhut Marodi: Apostrophe for Shortened Words**: Chhut Marodi shortens words: ਇਸ ਵਿੱਚ becomes ਇਸ 'ਚ and ਇਸ ਉੱਤੇ becomes ਇਸ 'ਤੇ. Always use a straight apostrophe (U+0027) for the shortened form, not the right single quotation mark ’ (\u2019).
  - *Source:* "ਇਸ ਵਿੱਚ / ਇਸ ਉੱਤੇ" → *Target:* "ਇਸ 'ਚ / ਇਸ 'ਤੇ"

## Grammar

- **Passive Voice and Gender Neutrality: When and How**: Use passive voice in only two cases: (1) when the string has no explicit subject, e.g. system status messages like updating or adding; (2) when an intransitive verb would directly reveal the user's gender (e.g. ਗਿਆ vs ਗਈ) — in this case either use passive voice or rephrase to avoid the gendered form altogether. Do not use passive voice as a general gender-neutrality strategy. Past transitive constructions (ਨੇ + verb) are already gender-neutral because the verb agrees with the object, not the subject. Prefer natural active voice wherever possible.
  - *Source:* "updating / %@ did this / %@ went home" → *Target:* "ਅੱਪਡੇਟ ਕੀਤਾ ਜਾ ਰਿਹਾ ਹੈ (passive, no subject) / %@ ਨੇ ਇਹ ਕੀਤਾ (active, gender not visible) / %@ ਵੱਲੋਂ ਇਹ ਕੀਤਾ ਗਿਆ (passive, gender hidden)"

- **Apply Oblique Case Before Postpositions**: Punjabi nouns and pronouns change to oblique case when followed by a postposition. Every noun before ਵਿੱਚ, ਨੂੰ, ਤੋਂ etc. must be in the correct oblique form.
  - *Source:* "Your account includes subscriber podcasts." → *Target:* "ਤੁਹਾਡੇ ਖਾਤੇ ਵਿੱਚ ਸਬਸਕ੍ਰਾਈਬਰ ਪੌਡਕਾਸਟ ਸ਼ਾਮਲ ਹਨ।" (ਖਾਤੇ not ਖਾਤਾ)

- **Vowel Mapping and Vowel Drop Rule**: Map English vowels as follows: short 'i' → ਿ◌ (ਡਿਵਾਈਸ), long 'i' → ◌ੀ (ਸ਼ੀਟ), short 'u' → ◌ੁ (ਅਕਾਊਂਟ), long 'u' → ◌ੂ (ਟੂਲ), long 'O' → ◌ੋ (ਨੋਟ), 'aw/ou' → ◌ੌ (ਮੌਮ), 'ay' → ◌ੇ (ਡੇਟ), 'ae/a' → ◌ੈ (ਐਪ). Vowel Drop Rule: When English words enter Punjabi through everyday use, unstressed vowels are dropped or shifted to match Punjabi phonology. Always follow how the word is actually spoken in Punjabi, not how it is spelled in English.
  - *Source:* "Content / Comment / Call / America" → *Target:* "ਕੰਟੈਂਟ (not ਕੌਂਟੈਂਟ) / ਕਮੈਂਟ (not ਕੌਮੈਂਟ) / ਕਾਲ (not ਕੌਲ) / ਅਮਰੀਕਾ (not ਅਮੈਰਿਕਾ)"

- **Mapping S/Sh, J/Z and F Sounds**: For 'S' sound use ਸ (ਸੋਰਸ). For 'Sh' sound use ਸ਼ with Nuqta (ਸ਼ੀਟ). For 'J' sound use ਜ. For 'Z' sound use ਜ਼ with Nuqta (ਜ਼ਿਊਰਿਖ). For 'F' sound use ਫ਼ with Nuqta (ਫ਼ਾਈਲ). Nuqta is mandatory for all three — ਜ਼, ਫ਼, ਸ਼ must never be written without it.
  - *Source:* "Source / Sheet / Zone / File / Zurich" → *Target:* "ਸੋਰਸ / ਸ਼ੀਟ / ਜ਼ੋਨ / ਫ਼ਾਈਲ / ਜ਼ਿਊਰਿਖ"

- **English Plural Sounds and Nasal Sounds (Bindi and Tippi)**: For English plurals, transcribe the final sound phonetically only: if it ends in /s/ sound use ਸ (ਨੋਟਸ); if it ends in /z/ sound use ਜ਼ (ਵਿੰਗਜ਼). For nasal sounds: use Tippi (ੰ) when the nasal sound is followed by a consonant within the same word (ਵਾਸ਼ਿੰਗਟਨ, ਲੰਡਨ); use Bindi (ਂ) when the nasal sound nasalizes a vowel (ਫ਼ਰਾਂਸ, ਸੈਨ ਫ਼ਰਾਂਸਿਸਕੋ).
  - *Source:* "Notes / Wings / Washington / France" → *Target:* "ਨੋਟਸ / ਵਿੰਗਜ਼ / ਵਾਸ਼ਿੰਗਟਨ / ਫ਼ਰਾਂਸ"

- **Consonant Clusters and Halant Rules**: For English transliteration, only two subjoined forms are used: ੍ਰ (half Ra) and ੍ਹ (half Ha). Do not apply Halant to any other consonant. Rule 1: 'r' cluster + short vowel → use Halant ੍ਰ (ਸਟ੍ਰਿੰਗ, ਸਟ੍ਰੈਂਥ). Rule 2: 'r' cluster + long vowel → use full ਰ (ਸਕਰੀਨ, ਗਰਾਊਂਡ). Exception to Rule 2: if the word has an established standardized Punjabi spelling, always prefer that over the rule (ਗ੍ਰੀਨ not ਗਰੀਨ). Rule 3: Punjabi proper nouns never use Halant regardless of cluster (ਗਰੇਵਾਲ, ਸ਼ਰਮਾ)
  - *Source:* "String / Screen / Green / Grewal" → *Target:* "ਸਟ੍ਰਿੰਗ (Rule 1) / ਸਕਰੀਨ (Rule 2) / ਗ੍ਰੀਨ (Exception) / ਗਰੇਵਾਲ (Rule 3)"

- **Transliteration Pronunciation Standard**: Use ODE (Oxford Dictionary of English) as the reference for standard pronunciation when mapping English sounds to Gurmukhi. Always base transliteration on how the word is actually pronounced, not how it is spelled in English.
  - *Source:* "File / Zone / America" → *Target:* "ਫ਼ਾਈਲ / ਜ਼ੋਨ / ਅਮਰੀਕਾ"

- **Headings: Noun Form by Default, Imperative for Creative Pages**: Headings default to noun/infinitive form (ਬਦਲਣਾ, ਬਣਾਉਣਾ) for standard instructional strings. For creative or promotional strings such as welcome screens and feature highlights, imperative verb form (ਖਿੱਚੋ, ਬਣਾਓ) is acceptable and often preferred. Use judgment based on tone and purpose.
  - *Source:* "Change iPhone Sounds (instructional) / Take your best shot (creative)" → *Target:* "iPhone ਦੀਆਂ ਧੁਨੀਆਂ ਬਦਲਣਾ / ਬਿਹਤਰੀਨ ਤਸਵੀਰਾਂ ਖਿੱਚੋ"

## Interface Elements

- **Buttons Use Imperative Form with Helping Verb**: Translate button labels in imperative form and always include a helping verb (ਕਰੋ, ਦਿਓ) so the label reads as a verb phrase not a bare noun.
  - *Source:* "Edit / Cancel / Cut / Paste" → *Target:* "ਸੋਧ ਕਰੋ / ਰੱਦ ਕਰੋ / ਕੱਟ ਕਰੋ / ਪੇਸਟ ਕਰੋ"

- **Use Curly Quotes Around UI Feature Names When Grammatically Necessary**: Wrap UI feature or app names in double curly quotes only when leaving them unquoted would create grammatical ambiguity. Minimize use of quotes and prefer rephrasing.
  - *Source:* "To add files into the folder, click Add button." → *Target:* "ਫ਼ੋਲਡਰ ਵਿੱਚ ਫ਼ਾਈਲਾਂ ਜੋੜਨ ਲਈ ਜੋੜੋ ਬਟਨ ਤੇ ਕਲਿੱਕ ਕਰੋ।"

- **App Name and Category Label Pluralization Rules**: Plural marking in Punjabi is gender-dependent and governs all app name and category label translations. Three rules apply: (1) Feminine nouns always take the -ਆਂ (aan) suffix: ਫ਼ਾਈਲ → ਫ਼ਾਈਲਾਂ (2) Masculine nouns ending in vowel -ਾ (aa) change to -ੇ (e) in the plural: ਨਕਸ਼ਾ → ਨਕਸ਼ੇ (3) Masculine nouns ending in a consonant have identical Direct Singular and Direct Plural forms and take no plural suffix: ਸੰਪਰਕ, ਕਲਾਕਾਰ
  - *Source:* "Files / Maps / Contacts / Reminders" → *Target:* "ਫ਼ਾਈਲਾਂ (feminine -ਆਂ) / ਨਕਸ਼ੇ (masculine -ਾ → -ੇ) / ਸੰਪਰਕ (masculine consonant, no change) / ਰਿਮਾਈਂਡਰ (masculine consonant, no change)"

## Key Labels

- **Transliterate Physical Keyboard Key Names**: Keyboard shortcuts (cmd+N etc.) are copied as-is. Physical keyboard key names (esc, command, option) are transliterated into Gurmukhi.

## Variables

- **Preserve and Reorder Variables Correctly**: Variables must be kept exactly as in source. When Punjabi word order requires reordering, number all variables using n$ index format (%1$@, %2$@). Never change variable type or remove a variable. Do not change a period to comma inside numeric format specifiers.
  - *Source:* "Check out the score %1$@ earned on %2$@ playing %3$@" → *Target:* "%3$@ ਖੇਡਦੇ ਹੋਏ %2$@ ਤੇ ਹਾਸਲ ਕੀਤੇ ਸਕੋਰ %1$@ ਨੂੰ ਦੇਖੋ।"

## Diversity And Inclusion

- **Inclusive Language and Fair Representation**: Translate consciously to include all users. Prefer neuter or plural phrasing over masculine defaults. Do not use color metaphors for positive or negative qualities.
  - *Source:* "You're becoming a world-building master!" → *Target:* "ਤੁਸੀਂ ਇੱਕ ਵਿਸ਼ਵ-ਨਿਰਮਾਣ ਮਾਹਰ ਬਣ ਰਹੇ ਹੋ!"
