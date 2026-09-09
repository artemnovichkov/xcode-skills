# Gujarati (gu) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Gujarati uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting — not straight ASCII quotes.

## Tone And Voice

- **Smart but Casual Register**: Use a written colloquial style that balances spoken and written Gujarati — neither too conversational nor overly complex. Follow the register found in national newspapers like Gujarat Samachar and Sandesh. Avoid Sanskritized vocabulary unless it is in everyday use.
  - *Source:* "Sign in with your Apple account" → *Target:* "તમારા Apple અકાઉંટ દ્વારા સાઇન ઇન કરો"

- **Prefer Gujarati Over English, but Prioritize Clarity**: Use native Gujarati terms when they are well-understood by urban and semi-urban speakers. If the Gujarati equivalent is archaic, artificial, or unfamiliar to the average reader, use a transliteration of the English term instead. The guiding principle is the reader's ease of understanding, not word origin.
  - *Source:* "Installation" → *Target:* "ઇંસ્ટૉલેશન" (transliteration preferred over an archaic Gujarati coinage)

- **Do Not Translate “Please”**: Gujarati encodes politeness through formal verb endings (e.g., કરો). Do not add 'કૃપા કરીને' as a literal translation of the English word 'please'.
  - *Source:* "Please sign in with your Apple ID." → *Target:* "તમારા Apple ID દ્વારા સાઇન ઇન કરો."

## Addressing Users

- **Use Honorific Second Person (તમે)**: Always address the user with the honorific pronoun તમે/તમને/તમારું and use the corresponding formal verb ending (e.g., કરો, આપો) rather than the informal forms (તું/કર). Gujarati encodes politeness through verb endings, so do not add 'કૃપા કરીને' as a literal translation of English 'please'.
  - *Source:* "To see menu text in your preferred language, change your iPhone language in Settings." → *Target:* "તમારી પસંદગીની ભાષામાં મેન્યૂ ટેક્સ્ટ જોવા માટે સેટિંગ્સમાં તમારી iPhone ભાષા બદલો."

- **Same Formality for Adults and Minors**: In Gujarati and Indian convention, children are addressed with the same formal register as adults. Use તમે (not તું) and formal verb forms (કરો, not કર) regardless of whether the user is an adult or a child.

## Abbreviations

- **Avoid Abbreviations; Use Gujarati Abbreviation Sign When Necessary**: Do not abbreviate strings in software unless rewording is not possible. When an abbreviation is unavoidable, use the Gujarati abbreviation sign (૰) after the first syllable of the abbreviated word.
  - *Source:* "Doctor" (abbreviated) → *Target:* "ડૉ૰"

## Acronyms

- **Retain English Acronyms Unless a Common Gujarati Equivalent Exists**: Do not translate acronyms unless there is a widely used Gujarati equivalent. The bracketed expansion may be translated if it is a familiar phrase in Gujarati. Well-known Gujarati acronyms such as ઇસરો (ISRO) are written without the abbreviation sign.
  - *Source:* "HDR" (High Dynamic Range) → *Target:* "HDR" (retain as-is; translate expansion only if widely known)

## Date And Time

- **Date and Time Format**: Use international numerals in hardcoded dates and times. The preferred date format is DD/MM/YYYY for long form and DD/MM/YY for short form. Do not use a comma between month and year. Use a colon (:) as the time separator with no surrounding spaces, and retain AM/PM in English following source capitalization.
  - *Source:* "March 17, 2022" → *Target:* "17 માર્ચ 2022"
  - *Source:* "7:15 AM" → *Target:* "7:15 AM"

- **Month Short Forms**: Use specific short forms for months with the abbreviation sign: જાન૰, ફેબ૰, માર્ચ, એપ્રિલ, મે, જૂન, જુલાઈ, ઑગ૰, સપ્ટ૰, ઑક્ટ૰, નવ૰, ડિસ૰.
  - *Source:* "Jan / Feb / Oct" → *Target:* "જાન૰ / ફેબ૰ / ઑક્ટ૰"

## Measurements

- **Do Not Convert Measurement Units**: Retain the original unit system from the English source — do not convert imperial to metric or vice versa. For electronics and computing units (GB, KB, 1080p, 5G), keep the unit in English. Add a space between the numeral and the unit, following the US source style.
  - *Source:* "8 GB" → *Target:* "8 GB"

- **Localize Common Physical Units with Abbreviation Sign**: Common metric units like km, cm, kg, and mg are localized using Gujarati abbreviations with the abbreviation sign: કિ૰મી૰, સે૰મી૰, કિ૰ગ્રા૰, and મિ૰ગ્રા૰ respectively.
  - *Source:* "5 km" → *Target:* "5 કિ૰મી૰"

## Addresses

- **Indian Address Format**: Format addresses in the standard Indian structure: Name, Building/Plot/Floor, Street/Road, Locality, City/Town, State – PIN Code. PIN codes are 6 digits with no spaces, written using international numerals. Addresses of locations outside India (e.g., Apple headquarters) should be left in English.
  - *Source:* "158-A, Lakshmi Society, Alkapuri, Vadodara, Gujarat 390007" → *Target:* "રમેશ કુમાર,
158-A, લક્ષ્મી સોસાયટી
અલકાપુરી
વડોદરા, ગુજરાત- 390007"

## Numerals

- **Use Indian Numbering System for Separators**: Apply the Indian numbering system for digit grouping (e.g., 10,00,000 rather than 1,000,000).
  - *Source:* "1,000,000 songs" → *Target:* "10,00,000 ગીત"

- **Ordinal Numbers in Gujarati**: Spell out ordinal numbers using full Gujarati inflected forms. The forms agree with the grammatical gender and number of the noun they modify. Avoid the numeric shorthand style (1લો, 2જો) as it is not standard Gujarati.
  - *Source:* "First / Second / Third" → *Target:* "પહેલો/પહેલી/પહેલું · બીજો/બીજી/બીજું · ત્રીજો/ત્રીજી/ત્રીજું"

## Special Characters

- **Anuswara Over Chandrabindu for Nasalization**: Gujarati uses anuswara (a dot above the character) to mark nasalization, not chandrabindu. Use the half consonant (pancham varna) instead of anuswara only in the specific cases where anuswara creates an ambiguous chandrabindu appearance, or when the sound ન/મ is followed by ય.
  - *Source:* "sample / content" → *Target:* "સૅમ્પલ / કૉન્ટેંટ" (not: સૅંપલ / કૉંટેંટ)

- **Use Correct Vowels ઍ and ઑ for English Transliterations**: Use ઍ (near-open front unrounded) for the English short 'a' sound (as in 'app', 'flag') and ઑ (open back rounded) for the English short 'o' sound (as in 'install', 'ball'). These are distinct from the standard Gujarati vowels એ and ઓ and must be applied consistently in transliterated English words.
  - *Source:* "app / install / doctor / camera" → *Target:* "ઍપ / ઇંસ્ટૉલ / ડૉક્ટર / કૅમેરા"

- **Transliterating Short and Long 'i'**: When transliterating English words, use the short 'i' matra (િ) for short 'i/e' sounds (e.g., Device -> ડિવાઇસ). Use the long 'i' matra (ી) for long 'i/ee' sounds (e.g., Sheet -> શીટ).
  - *Source:* "Device / Sheet" → *Target:* "ડિવાઇસ / શીટ"

- **Transliterating Short and Long 'u'**: When transliterating English words, use the short 'u' matra (ુ) for short 'u' sounds (e.g., Account -> અકાઉંટ). Use the long 'u' matra (ૂ) for long 'u/oo' sounds (e.g., Tool -> ટૂલ).
  - *Source:* "Account / Tool" → *Target:* "અકાઉંટ / ટૂલ"

- **Transliterating ‘Ja’, ‘Za’, and 'Fa' Sounds**: Map the English 'J' sound to 'જ'. Map the 'Z' sound to 'ઝ' (e.g., Noise -> નૉઇઝ). Map the 'F' sound to 'ફ' (e.g., San Francisco -> સાન ફ્રાંસિસ્કો). Do not use Nuqtas (subscript dots) for any of these sounds.
  - *Source:* "Noise / San Francisco" → *Target:* "નૉઇઝ / સાન ફ્રાંસિસ્કો"

- **Transcribing English Plural Sounds**: Always prefer the singular form of English transliterations (e.g., devices, features). If you must transliterate a plural English word, transcribe the final sound phonetically: use 'સ' if it ends in an /s/ sound (e.g., Apps -> ઍપ્સ), and use 'ઝ' if it ends in a /z/ sound (e.g., News -> ન્યૂઝ).
  - *Source:* "Apps / News" → *Target:* "ઍપ્સ / ન્યૂઝ"

## Punctuation

- **Space Before Colon to Avoid Confusion with Visarga**: Add a space before a colon (:) to prevent visual confusion with the Gujarati visarga (ઃ). This space should be omitted when the colon follows an English word or a number.
  - *Source:* "Settings:" → *Target:* "સેટિંગ્સ :"

- **Use Curly Double Quotes for UI Feature Names**: Use curly double quotes “ (\u201C) and ” (\u201D) around UI feature or app names within a sentence when the name creates grammatical ambiguity — for example, when it changes the grammatical number or requires an oblique case form. Minimize the use of quotes wherever the sentence can flow naturally without them.
  - *Source:* "To add files into the folder, click Add button." → *Target:* "ફોલ્ડરમાં ફાઇલ ઉમેરવા માટે \u201Cઉમેરો\u201D બટન પર ક્લિક કરો."

- **No Double Spaces**: Even if the English source uses double spaces between sentences, Gujarati must always use a single space after a period.
  - *Source:* "Sentence one.  Sentence two." → *Target:* "Sentence one. Sentence two."

- **Terminal Punctuation Mirroring**: Do not add terminal punctuation (like a full stop) at the end of a string if it is not present in the English source. Mirror the source punctuation exactly.
  - *Source:* "A list to remove the places from" → *Target:* "સ્થળોને કાઢી નાખવા માટેની સૂચી"

## Grammar

- **Attach Postpositions Directly to the Noun**: Postpositions in Gujarati must be written with no space between them and the noun they follow. A gap between a noun and its postposition is a grammatical error.
  - *Source:* "in Settings" → *Target:* "સેટિંગ્સમાં" (not: સેટિંગ્સ માં)

- **Prefer Passive Voice When the Subject Is Absent**: Use the passive voice when the string contains an action but no explicit subject (e.g., standalone gerunds, or sentences where 'who is doing the action' cannot be determined from the string). This style produces more natural and unambiguous Gujarati.
  - *Source:* "updating…" → *Target:* "અપડેટ થઈ રહ્યું છે…"
  - *Source:* "Displays photos while locked." → *Target:* "લૉક થવા પર ફોટો બતાવવામાં આવશે."

- **Instrumental 'With' (દ્વારા vs સાથે)**: When 'with' means 'using a device or tool' (e.g., 'Control with iPhone'), translate it using 'દ્વારા' (by/using). Do not use 'સાથે' (along with) or 'વડે'.
  - *Source:* "Control %@ with Your iPad" → *Target:* "તમારા iPad દ્વારા %@ને કંટ્રોલ કરો"

- **Variable Subjects with Active Verbs**: If a variable represents a user name performing an action, use the passive voice (e.g., '%@ દ્વારા... ઉપયોગ કરવામાં આવ્યો') instead of the active voice ('%@ એ... ઉપયોગ કર્યો') to avoid grammatical errors when the name is resolved.
  - *Source:* "%1$@ used %2$@ for %3$@ over the past day." → *Target:* "%1$@ દ્વારા ગયા દિવસે %3$@ માટે %2$@નો ઉપયોગ કરવામાં આવ્યો."

- **Directional Adverbs vs. Gendered Adjectives**: When referring to directions like 'right and left', use the adverbial forms 'જમણે' and 'ડાબે'. Do not use the feminine adjective forms 'જમણી' and 'ડાબી' unless modifying a specific feminine noun.
  - *Source:* "Slowly rotate your head right and left" → *Target:* "ધીમે ધીમે તમારું માથું જમણે અને ડાબે ફેરવો"

- **Parallel Construction in Lists**: List items must match the flow of the source parent phrase and generally use the imperative form (કરો). Ensure parallel construction across all items in a list.
  - *Source:* "• Update your contact information" → *Target:* "• તમારા સંપર્ક સંબંધિત માહિતી અપડેટ કરો"

- **Avoid Hanging Phrases**: Do not leave incomplete prepositional phrases in Gujarati. Translate the complete context or intent rather than doing a literal word-for-word translation that leaves a dangling postposition (not: ના માટે દરેક લાઇડને ચલાવો).
  - *Source:* "Play each slide for" → *Target:* "પ્રતિ સ્લાઇડ અંતરાલ"
  - *Source:* "Use Date from" → *Target:* "નીચેમાંથી એક તારીખ"

- **Rule for Headings and subheadings**: Headings that begin with verb can be localized as imperative in Gujarati. Sub headings and topic titles that begin with verb can be localized in a manner of 'to do so and so'.
  - *Source:* "Personalize your iPhone" (heading) → *Target:* "તમારો iPhone પર્સનલાઇઝ કરો"
  - *Source:* "Adjust the volume" (subheading) → *Target:* "વૉલ્યૂમ ઍડજસ્ટ કરવા માટે"

## Interface Elements

- **Avoid Double Pluralization**: Do not mark plural on a noun when plurality is already expressed by a preceding number or by verb agreement. Adding a Gujarati plural suffix (e.g., -ઓ) in addition to a numeric indicator creates redundant marking.
  - *Source:* "5 folders were deleted." → *Target:* "5 ફોલ્ડર ડિલીટ કરવામાં આવ્યાં હતાં." (not: 5 ફોલ્ડરો)

- **Buttons Use Imperative Form with Helping Verb**: Translate button labels in the imperative (command) form and always include the appropriate helping verb (કરો, આપો, etc.) so the label functions as a verb phrase rather than a bare noun.
  - *Source:* "Edit / Cancel / Reply" → *Target:* "સંપાદિત કરો / રદ કરો / જવાબ આપો"

- **App Names: Singular Proper Nouns**: Localized app names are treated as singular proper nouns even when the English name is plural. Exceptions are app names that are transliterated (Notes, Settings, Photos, Stocks remain plural in transliteration).
  - *Source:* "Reminders / Maps / Books" → *Target:* "રિમાઇન્ડર / નકશો / પુસ્તક"

- **App and Category Names Default Singularization**: The default grammatical posture for app names and category labels in Gujarati is the uninflected (singular or number-neutral) base form. Drop the English plural marker ('s' or 'es') whether translating or transliterating.
  - *Source:* "Apps / Albums / Artists" → *Target:* "ઍપ / ઍલ્બમ / કલાકાર"

- **Lexicalized Plurals for Specific Containers**: Retain the English plural marker ('s') in transliteration only when necessary to shift a single instance noun into a collective repository or system hub.
  - *Source:* "Photos / Notes / Settings" → *Target:* "ફોટોસ / નોટ્સ / સેટિંગ્સ"

- **Native Pluralization for Human Relationships**: While inanimate objects and broad classes remain singular, nouns representing specific personal human relationships must use the native Gujarati plural suffix ('-ઓ') when acting as a category label.
  - *Source:* "Friends" → *Target:* "મિત્રો"

- **Contextual Plurality Avoidance**: When a category label is used in a sentence as a common noun, apply double pluralization avoidance. If a number is present, keep the noun singular. If no number is present but plurality is needed, use a quantifying modifier (e.g., 'તમામ') instead of forcing an English '-s'.
  - *Source:* "Delete 5 folders" → *Target:* "5 ફોલ્ડર ડિલીટ કરો"

- **Retain Frozen Plurals in Sentences**: When referring to a UI feature that is a frozen lexicalized plural (e.g., સેટિંગ્સ, ફોટોસ), it must retain its exact pluralized form in all sentence contexts. Do not strip the '-s' as it is part of the root's identity.
  - *Source:* "Open Settings to change your password." → *Target:* "તમારો પાસવર્ડ બદલવા માટે સેટિંગ્સ ખોલો."

- **URL Tags with 'See'**: For strings commencing with the verb 'See' followed by a URL tag, place 'જુઓ :' at the start of the string followed by the tag to avoid unnatural verb repetition.
  - *Source:* "See <g>Customize controls</g>." → *Target:* "જુઓ : <g>કંટ્રોલ કસ્ટમાઇઝ કરો</g>."

- **Callout Bar Formatting Exceptions**: Unlike standard buttons, formatting options in callout bars (Bold, Italic, Underline, Strikethrough) must be localized as nouns without helping verbs.
  - *Source:* "Bold / Italic / Underline" → *Target:* "બોલ્ડ / ઇટૅલિક / અંડરલાઇન"

## Spelling

- **Transliteration Pronunciation Standard**: Sound out the English word based strictly on the Standard Oxford Dictionary of English (ODE) pronunciation when transliterating into Gujarati.

- **Hyphenation in Transliterated Compounds**: Maintain hyphens in specific transliterated compound words as they appear in the source to maintain consistency in spoken and written aesthetics.
  - *Source:* "plug-in / check-in / pop-up" → *Target:* "પ્લગ-ઇન / ચેક-ઇન / પોપ-અપ"

- **Transliteration Spelling Consistency**: Maintain consistent spelling for transliterated terms across the OS, strictly adhering to the approved glossary (e.g., use 'હેપ્ટિક્સ' for Haptics, not 'હૅપ્ટિક્સ').
  - *Source:* "Turn off Music Haptics." → *Target:* "સંગીત હેપ્ટિક્સ બંધ કરો."

## Variables

- **Preserve and Reorder Variables Correctly**: Variables must be kept exactly as they appear in the source. When Gujarati word order requires reordering, number all variables using the n$ indexing format (e.g., %1$@, %2$@) before rearranging. Never alter the variable format or remove a variable from the string.
  - *Source:* "Check out the score %1$@ earned on %2$@ playing %3$@" → *Target:* "%2$@ પર %3$@ રમીને %1$@ના કેટલા સ્કોર થયા તેમ તપાસો"

- **Gender Agreement with Variables**: When a variable represents a person possessing another variable (e.g., a device), attach the correct gendered postposition (ના/ની/નું) directly to the first variable based on the gender of the second variable.
  - *Source:* "%@\u2019s %@" → *Target:* "%@ના/ની/નું %@"

## Diversity And Inclusion

- **Gender-Neutral Language and Fair Representation**: Prefer neuter or gender-neutral phrasing wherever possible. When referring to an unknown user, avoid defaulting to masculine forms by using plural phrasing or structuring sentences that are valid for all genders. Do not use terms that are violent, oppressive, or ableist, and avoid using color metaphors to convey positive or negative qualities.
  - *Source:* "You're becoming a world-building master!" → *Target:* "તમે વિશ્વ નિર્માણના ગુરૂ બની રહ્યાં છો."

- **First-Person Gender Neutrality (Siri/AI)**: When an App or system refers to itself in the first person (e.g., 'I couldn't retrieve'), use a passive construction (e.g., 'મારાથી... કરી શકાયા નથી') to remain gender-neutral. Avoid masculine forms like 'હું... શક્યો'.
  - *Source:* "I couldn\u2019t retrieve the messages from this conversation." → *Target:* "મારાથી આ વાર્તાલાપમાંથી મેસેજ રિટ્રીવ કરી શકાયા નથી."

- **Culturally Adapt Foreign Names to Gujarati Equivalents**: Culturally adapt foreign placeholder names (e.g., Danny, Anthony, Elena) to familiar Gujarati names (e.g., શિવમ, શુભમ, શનાયા) so they resonate with the target locale.
  - *Source:* "Dear Danny" → *Target:* "પ્રિય શિવમ"

## Terminology

- **Exact Word Forms (App vs Application)**: Translate the exact word form used in the source. Do not abbreviate 'Application' to 'ઍપ'; use 'ઍપ્લિકેશન'. Use 'ઍપ' only when the source says 'App'.
  - *Source:* "Application Not Available" → *Target:* "ઍપ્લિકેશન ઉપલબ્ધ નથી"

- **Established Feature Translation vs Transliteration**: Do not fall back to transliterating English feature names if a localized Gujarati term has been used in a previously-translated string.
  - *Source:* "Writing Tools" → *Target:* "લેખનશિલ્પી"

- **Reuse Established Localized Terms**: Reuse the established Gujarati translations for features, apps, and UI elements as they appear in previously-translated strings (e.g., use 'ખોજી' for Find My, not 'શોધો').
  - *Source:* "Find My / Apple Intelligence" → *Target:* "ખોજી / Apple Intelligence"

## Formatting

- **Preserve Line Breaks and Spacing**: Always maintain the exact line breaks (carriage returns) and spacing present in the English source string. Do not merge paragraphs into a single line.
  - *Source:* "Expressive Voices are powered by a new on-device model, currently available in developer preview.
Certain Apple Intelligence features..." → *Target:* "એક્સપ્રેસિવ વૉઇસ નવા ઑન-ડિવાઇસ મૉડલ દ્વારા સંચાલિત છે જે હાલમાં ડેવલપર પ્રિવ્યૂમાં ઉપલબ્ધ છે.
Apple Intelligenceના અમુક ફીચર..."
