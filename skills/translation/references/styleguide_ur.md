# Urdu (ur) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Urdu uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "Go to \u201CVisited Places\u201D" → *Target:* "\u201Cوزٹ کی گئی جگہیں\u201D پر جائیں"

## Tone And Voice

- **Smart-Casual, Colloquial Urdu**: The tone is smart but casual — leaning toward formal without being stiff. Write natural, everyday Urdu that reads smoothly on the page. Avoid trendy slang and overly archaic forms; use Urdu as much as possible while keeping text easy to read.

- **Neutral Variant, No Regional Dialect**: Use contemporary, standard Urdu that is not tied to a specific regional dialect or local variety.

## Addressing Users

- **Formal You — آپ and Formal Verb Forms**: Always address the user with the formal pronoun آپ and formal verb forms (کریں/چاہتے ہیں style). Never use the informal تو/تم or their verb forms. This applies equally when addressing children; there is no reduction in formality for younger audiences.
  - *Source:* "Are you sure you want to delete it?" → *Target:* "کیا آپ واقعی اسے حذف کرنا چاہتے ہیں؟"
  - *Source:* "Would you like to cancel?" → *Target:* "کیا آپ منسوخ کرنا چاہتے ہیں؟"
  - *Source:* "Unlock your iPhone." → *Target:* "اپنا iPhone اَنلاک کریں۔"

- **Roles and Common Nouns Translated in Singular**: Common nouns and roles that refer to the user, such as user, person, administrator, member, are translated in the singular. Keep them gender-neutral wherever the grammar allows it (for example, by choosing a construction that avoids a gendered verb or adjective); when Urdu grammar forces a gendered form and no natural neutral wording exists, use the conventional masculine. Do not pluralize these when the source addresses a single user.
  - *Source:* "The user can change this setting at any time." → *Target:* "صارف کسی بھی وقت یہ سیٹنگ تبدیل کر سکتا ہے۔"

## Abbreviations

- **Avoid Abbreviations**: Do not use truncated/shortened abbreviations (where letters are dropped from a word, e.g. Dr. for Doctor, Sept. for September, approx. for approximately) in translations unless absolutely no other option exists. Expand instead. This is distinct from acronyms (HDR, MB, GB, PDF), which ARE retained — see the acronyms rule.
  - *Source:* "Dr." → *Target:* "ڈاکٹر" (expand; do not abbreviate)

## Acronyms

- **Keep Acronyms in English**: Do not translate acronyms unless a very common localized equivalent exists. Popular Urdu acronyms (یونیسکو, ناسا) are written without a full stop. If the source itself provides the expanded form, translate the expansion; do not add an expansion the source lacks.
  - *Source:* "HDR" → *Target:* "HDR" (do not translate)

## Date And Time

- **Date and Time Formats**: Use day → month → year order (DD/MM/YYYY). Use international numerals in hardcoded dates and times; never use native Urdu numerals. Do not put a comma between the month and the year. Keep AM/PM in English, following the source’s capitalization.
  - *Source:* "17/03/2022" → *Target:* "17/03/2022"

- **o’clock and Time Preposition**: Translate o’clock as بجے. Use a colon as the time separator, with no space before or after it. If بجے is present, do not add the preposition پر after the time.
  - *Source:* "10:18:35" → *Target:* "10:18:35" (colon separator; international numerals)
  - *Source:* "10 o\u2019clock" → *Target:* "10 بجے" (no پر after time when بجے present)

## Measurements

- **Do Not Convert Measurement Units**: Never convert imperial to metric or vice versa. Unit abbreviations stay in English to avoid truncation. CLDR exceptions apply (e.g. millimeters = ملی میٹر; unit plurals written singular, kilocalories = کلو کیلوری).
  - *Source:* "10 KB" → *Target:* "10 KB" (follow source spacing)
  - *Source:* "6 ft" → *Target:* "6 ft" (do not convert to metric)

- **Preserve Source Order in Measurements and Math Expressions**: Mathematical expressions and measurements always follow the source order. Keep the number and unit in the same sequence as the source — 8 GB, not GB 8. Do not reorder operands, operators, or number-unit pairs to fit Urdu word order. Numerals and Latin unit symbols render LTR within the RTL line; use BiDi markers if needed for correct display (see RTL rule).
  - *Source:* "8 GB" → *Target:* "8 GB" (not GB 8)

## Names And Addresses

- **Use Inclusive Caste-Neutral Names as Placeholders**: Replace generic English placeholders with inclusive, caste/religion/sect-neutral names. A generic placeholder should be replaced with a locally-appropriate name; a specific, real individual named in the source or developer comment (any nationality) keeps that person's actual name, transliterated into Urdu script if it is in Latin letters.

- **Indian Address Format and PIN Codes**: Format addresses per the Department of Post, Government of India conventions. Addresses outside India stay in English. PIN codes are six digits in international numerals (e.g. 226010, not native ۲۲۶۰۱۰) with no space between digits. A typical Indian address lists the recipient name, then house/plot/floor number, street, locality, city with the six-digit PIN, and state — for example: جاوید احمد، 134-B، ورنداون انکلیو، گومتی نگر، لکھنئو 226010، اتر پردیش.

## Numerals

- **Indian Numbering System for Separators**: The standard for Urdu numerals is international (Western Arabic). Use the Indian numbering system for separators (10,00,000 not 1,000,000). Keep the digits as international (Western) numerals; only the grouping separators follow the Indian system.
  - *Source:* "1,000,000 songs" → *Target:* "10,00,000 گانے"

- **Ordinal Numbers**: Write 1st through 9th as Urdu words (پہلا، دوسرا … نواں). From 10th onward, append واں to the numeral (10واں، 11واں), including variable-driven ordinals whose value isn't known at translation time (%d واں).
  - *Source:* "10th" → *Target:* "10واں"

## Special Characters

- **Right-to-Left Display and BiDi Markup**: Urdu is RTL but numerals and Latin words render LTR, creating bidirectional issues. When an Urdu string contains an untranslated English name, variable, or number, use the Unicode RLM (U+200F) or FSI/PDI markers (U+2068/U+2069) for correct directionality. Text layout auto-detects direction for most strings (the Unicode bidi algorithm); add explicit BiDi markers only when a Latin or numeric run inside Urdu text would otherwise render in the wrong position (for example an embedded English product name or a measurement mid-sentence). Do not add markers to purely uni-directional text.
  - *Source:* "The disk capacity must be minimum of 10 MB for this." → *Target:* "اس کے لیے ڈسک کی گنجائش کم از کم \u206810 MB\u2069 ہونی چاہیے۔"

- **Urdu Full Stop vs English Period**: Urdu uses its own full stop ۔ (U+06D4), not the English period. Never use the English period to end Urdu sentences or as an abbreviation marker.
  - *Source:* "Photo saved." → *Target:* "تصویر محفوظ ہو گئی۔"

- **Curly Quotes for Ambiguous Category Labels**: When a category/feature label inside a sentence creates grammatical ambiguity — a change in grammatical number, oblique case, or a verb/participial ending — wrap the label in double curly quotes. Mandatory for suffixed-plural labels before postpositions and labels with verb endings. Quotes are not needed for stable broken-plural labels that read naturally (ترجیحی اطلاعات میں دیکھیں).
  - *Source:* "Go to Visited Places" → *Target:* "\u201Cوزٹ کی گئی جگہیں\u201D پر جائیں" (quotes for suffixed-plural label before postposition)

- **Double Curly Quotes and App Name Formatting**: Use double curly quotes as the default quotation style; straight quotes only for HTML code. Do not quote app names; instead place ایپ AFTER the app name.
  - *Source:* "Open the \u2018Files\u2019 app" → *Target:* "فائل ایپ کھولیں" (app name before ایپ, no quotes)

## Grammar

- **No Articles — Avoid Translating a/an as ایک**: Urdu has no articles. Do not translate a/an as ایک (one) — it sounds awkward and implies a specific quantity. Omit the article; add ایک only when the source genuinely means one.
  - *Source:* "Create a Passcode." → *Target:* "پاس کوڈ بنائیں۔" (not ایک پاس کوڈ)

- **Plurals Follow Standard Urdu Rules**: Pluralization follows standard Urdu grammar per authoritative references. Commonly used transliterated loan words take standard Urdu plurals. Uncommon/new transliterated terms use the singular everywhere, letting sentence context convey plurality.
  - *Source:* "Admin/Admins" → *Target:* "ایڈمن" (uncommon term — singular for both)
  - *Source:* "Car/Cars" → *Target:* "کار/کاریں" (commonly-used loan word — takes the standard plural)

- **Passive Voice in Software Descriptions and Hints**: Use passive voice when no subject performs the action in the string — hints, footers, button descriptions, intent explanations. If unsure between active and passive, prefer passive. Use active voice for complete indicative sentences describing features.
  - *Source:* "This will turn off Cellular." → *Target:* "اس سے موبائل نیٹ ورک بند ہو جائے گا۔"
  - *Source:* "Email to be sent" → *Target:* "وہ ای میل جو بھیجا جانا ہے"

- **Imperative Mood for Commands and Buttons**: Use the imperative form for commands, buttons, menu items, and callout bar items. Helping verbs like کریں/دیں must be included so the translation stays an action, not a noun. Translate tooltips in the imperative.
  - *Source:* "Edit" → *Target:* "ترمیم کریں"
  - *Source:* "Delete" → *Target:* "حذف کریں"
  - *Source:* "Answer" → *Target:* "جواب دیں" (not جواب alone)

- **Gender Neutrality via Workaround Constructions**: User-addressed pronouns default to masculine by convention. Where possible, achieve gender neutrality with نے or کی طرف سے, and minimize بذریعہ; limit these workarounds so the sentence does not sound unnatural. Company and brand names must be kept gender-neutral — do not use a slash form or reword them as plural to achieve this.
  - *Source:* "%@ completed 2km run today." → *Target:* "%@ نے آج 2 کلو میٹر کی دوڑ پوری کی۔"

- **Indefinite Pronouns Are Singular**: Indefinite pronouns like someone/somebody/anyone are translated as کوئی in the singular and paired with singular verb forms (کوئی سوال ہے, not کوئی سوالات ہیں). Avoid constructions that incorrectly treat کوئی as plural.
  - *Source:* "If you have any questions, please feel free to ask me." → *Target:* "اگر آپ کے پاس کوئی سوال ہے تو براہ کرم مجھ سے پوچھیں۔"

- **Gender of Transliterated Loan Words**: Assign gender to non-nativized loan words by their closest Urdu translation, or feminine if the transliteration ends in ی (e.g. کنکٹیوِٹی, کیلوری). Common nativized words follow established usage (car/bus fem., truck/station masc.).
  - *Source:* "connectivity" → *Target:* "کنکٹیوِٹی" (feminine — transliteration ends in ی)
  - *Source:* "admin" → *Target:* "ایڈمن" (masculine — by closest Urdu translation)

- **Translate "Cannot" with ہے at the End**: Translate Cannot as نہیں کیا جا سکتا ہے (ending in ہے) to avoid hanging phrases in descriptive/explanatory text.
  - *Source:* "Cannot connect" → *Target:* "کنکٹ نہیں کیا جا سکتا ہے"

- **Transliteration Rules and English Plural Markers**: Transliterated English words do not take English plural markers — drop the -s/-es (ز/س) as it does not integrate into Urdu phonology. The direct case stays in the base singular form (فون، کارڈ، ڈاکٹر، پوڈکاسٹ); only commonly-used words may inflect in the oblique case (اسکول → اسکولوں).
  - *Source:* "Podcasts" → *Target:* "پوڈکاسٹ" (drop English -s; base singular form)

## Terminology

- **Transliteration Preferred for Technical Jargon**: For widely used technical terms and software jargon, use transliteration rather than an artificial/archaic Urdu equivalent. Base transliteration on UK English pronunciation, not American spelling. Keep file formats and acronyms (PDF, RTF, DOC) untouched.
  - *Source:* "Installation" → *Target:* "انسٹالیشن" (transliterated, not an invented Urdu compound)

- **Choose Urdu Over English When Both Are Natural**: When a genuine Urdu word is still common and easy to understand, prefer it over a transliteration. Judge by whether the word would feel natural to an Urdu newspaper reader. Avoid sweeping terminology changes; assess each term individually in context.
  - *Source:* "Photo" → *Target:* "تصویر" (not فوٹو or پکچر)
  - *Source:* "Map" → *Target:* "نقشہ" (not میپ)

- **Hybrid Approach for Technical + Generic Phrases**: Pure translation or pure transliteration is preferred, but a hybrid (translation + transliteration) is acceptable when a phrase mixes technical and generic words (Continuous Scrolling) to preserve natural flow.
  - *Source:* "Continuous Scrolling" → *Target:* "مسلسل اسکرولنگ" (hybrid acceptable)

- **Color Names — Three-Tier Approach**: Standard colors (Red, Green, Blue) take direct Urdu equivalents. Coined/marketing color names (Midnight Black, Rose Gold) are transliterated consistently. Proprietary/brand color names (Bleu Pastel, Orange Mangue) stay in English where a developer comment says not to localize.
  - *Source:* "Midnight Black" → *Target:* "مڈنائٹ بلیک" (transliterate)
  - *Source:* "Red" → *Target:* "سرخ" (translate)
  - *Source:* "Bleu Pastel" → *Target:* "Bleu Pastel" (keep English)

## Interface Elements

- **Category and Feature Label Pluralization**: For category/feature labels use a split approach: transliterated labels stay singular with English plural markers dropped (Devices = ڈیوائس, Utilities = یوٹیلٹی); translated labels keep the plural, strongly preferring stable broken plurals/جمع مکسر (Messages = پیغامات, Suggestions = تجاویز, Notifications = اطلاعات, Items = اشیا). Broken plurals are preferred because they do not inflect before postpositions and avoid oblique-case friction.
  - *Source:* "Devices" → *Target:* "ڈیوائس" (transliterated, singular)
  - *Source:* "Suggestions" → *Target:* "تجاویز" (translated, broken plural)

- **Heading and Title Verbs (UI)**: Promotional or label headings use the imperative (Make = بنائیں). Welcome-screen headings should be creative, short, and formal.
  - *Source:* "Make" → *Target:* "بنائیں"

## Variables

- **Preserve and Reorder Variables Correctly**: Keep all variables exactly as in the source. When Urdu word order differs, number every variable using the n$@ format (%1$@, %2$@) so runtime substitution stays correct. Never change a period to a comma inside a numeric format variable like %.1f.
  - *Source:* "On %@ at %@." → *Target:* "%2$@ کو %1$@ پر۔" (reordered with numbered variables)

## General Advice

- **Modern Urdu Spelling Conventions**: Follow modern Urdu spelling: write compound words separately (اس لیے not اسلیے), apply declension (امالہ) so ہ or ا at word endings change to ے when grammatically required, and write words as they sound rather than older joined forms.
  - *Source:* "By this way" → *Target:* "اس طریقے سے" (correct — declension ہ→ے after postposition)

## Diversity And Inclusion

- **Inclusive Language**: Avoid translations that tie occupations to caste names. For disability, lead with the person before the condition (people-first), unless the specific community prefers identity-first.
  - *Source:* "The blind" → *Target:* "نابینا افراد / وہ افراد جو بینائی سے محروم ہیں"

## Compounds And Hyphens

- **No Hyphens in Transliterated Compounds**: When transliterating compound terms do not use a hyphen even if the source has one (against standard Urdu). Source inconsistencies like sign-in/sign in are written consistently without a hyphen.
  - *Source:* "sign-in / sign in" → *Target:* "سائن اِن" (without hyphen)

## Slashes

- **No Space Around Slashes**: Slashes can express a part of a whole. Do not put a space before or after a slash, unless the source itself has spaces around it.
  - *Source:* "3 out of 5 pages" → *Target:* "5/3 صفحہ"

## Currency

- **No Space After Indian Rupee Symbol**: Do not insert a space after the Indian Rupee symbol ₹. Correct: ₹500.45; Incorrect: ₹ 500.45.

## Software

- **Software String Integrity (Spaces, Periods, Returns)**: Preserve leading and trailing spaces (needed for concatenation). Do not use double spaces between sentences. Do not add a period if the source has none. Keep carriage returns/line breaks.
  - *Source:* "Updating… " → *Target:* "اپڈیٹ کیا جا رہا ہے… " (preserve trailing space, no added period)

- **App Names — Singular Form; Some Names Not Translated**: Translate/transliterate app names in the singular using the most appropriate variant. Do not translate trademarked product names; keep them in their original form, or as the developer's comment directs.
  - *Source:* "iTunes" → *Target:* "iTunes" (do not translate)
  - *Source:* "Photos" → *Target:* "تصویر" (singular)

## Emoji

- **Emoji Translation Conventions**: Avoid prepositions/helping words in emoji names unless necessary. Singular and plural emoji-count strings keep the same noun form (the count refers to multiple emoji, not multiple objects). Avoid tying a depicted feature to a specific religion/region (no اسلام/مسلم for a hijab emoji).
  - *Source:* "%d black cat emoji" → *Target:* "%d کالی بلی ایموجی" (no prepositions; same form sing./plural)
