# Hebrew (he) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual Register**: The tone should be closer to formal than informal, but never stiff or stilted. Avoid trendy slang and maintain a neutral, descriptive style. Strive for translations that sound as if they were originally written in Hebrew, not translated from English.

- **Prefer Native Hebrew Terms**: Use native Hebrew vocabulary as much as possible, unless the term is unnatural or foreign to typical users. There is no one-to-one mapping between English and Hebrew; choose the most natural Hebrew equivalent used by a similar audience rather than a more literal but uncommon option.
  - *Source:* "load / retrieve" → *Target:* "לטעון (for both — לאחזר is too uncommon)"
  - *Source:* "program / software" → *Target:* "תוכנה (for both — תוכנית is rarely used in this context)"

## Addressing Users

- **Use Gender-Neutral Forms When Addressing the User**: Because it is often ambiguous whether a string addresses the user or instructs the device, and because Hebrew grammatical gender is pervasive, default to gender-neutral constructions. Preferred strategies include present-tense participle verbs, second-person past-tense homographs, modal forms (באפשרותך, ניתן, יש ל-), and gerunds. Avoid hybrid slash forms (י/הקש) as they are not truly inclusive and are not read correctly by VoiceOver.
  - *Source:* "Save" → *Target:* "שמירה (gerund) or לשמור באפשרותך (modal)"

## Abbreviations

- **Avoid Abbreviations; Reword Instead**: Abbreviations should be a last resort when a string is too long. Preferred fixes are rewording the translation for conciseness or filing a localizability bug. When abbreviation is unavoidable, use the geresh (׳) as the standard abbreviation marker, as is conventional in Hebrew writing.
  - *Source:* "by / number (abbreviated)" → *Target:* "ע״י / מס׳"

## Acronyms

- **Use Hebrew Equivalents for Acronyms When They Exist**: If a common Hebrew equivalent term exists for an English acronym, use it freely — there is no requirement to retain the English form unless it is on a DNT list provided by the user. When an acronym concept can be translated but has no Hebrew acronym counterpart, keep the English acronym; if the source pairs it with a spelled-out form, translate that form and place the translated term first, with the English acronym in parentheses (the opposite of the English order) — don't add an expansion the source doesn't have, or drop one it does.
  - *Source:* "RAM" → *Target:* "זיכרון"
  - *Source:* "HDR (High Dynamic Range)" → *Target:* "תחום דינמי רחב (HDR)"

## Date And Time

- **Date Format and Range Orientation**: Use the period (.) as the date separator and place the day before the month. Do not use a leading zero for hours or day numbers. For date and time ranges, place the earlier value on the right side (per Hebrew right-to-left convention). Use an en-dash (–) rather than a hyphen for ranges, as it behaves better in bidirectional text.
  - *Source:* "9/13/2013–9/15/2013" → *Target:* "13.9.2013–15.9.2013"

## Measurements

- **Do Not Convert Measurement Units**: Keep the unit system from the source; do not convert inches to centimeters or vice versa. Do not use the gershayim character (״) as an abbreviation for inches — it is reserved for abbreviations and quotations in Hebrew.

## Names And Addresses

- **Use Israeli Sample Names and Realistic Address Mix**: Replace generic placeholders (John/Jane Doe) with ישראל/ישראלה ישראלי. When multiple sample names are needed, include a realistic mix that reflects Israel's diverse population — include minority names and names representing a range of genders. City names in sample addresses should be fictional.
  - *Source:* "John Doe / Jane Doe" → *Target:* "ישראל ישראלי / ישראלה ישראלי"

## Numerals

- **Write 1 and 2 as Words; Handle Plural Forms Carefully**: In Hebrew, the numbers 1 and 2 are written as words when they count a noun. The word for '1' follows its noun; '2' and all higher numbers precede it.
  - *Source:* "1 book / 2 books / 30 days" → *Target:* "ספר אחד / שני ספרים / 30 ספרים"

## Grammar

- **Always Use the Definite Article (ה-) in Hebrew**: Hebrew does not drop the definite article in short UI strings. Add the article where it is grammatically required. Note that in construct-state compounds, the definite article attaches to the last noun in the chain. Prefixed prepositions and articles before non-Hebrew words or numbers require a hyphen (non-breaking when possible) between the prefix and the word.
  - *Source:* "File not found" → *Target:* "הקובץ לא נמצא (not: קובץ לא נמצא)"
  - *Source:* "the iPhone" → *Target:* "ה-iPhone (hyphen, no spaces)"

- **Gerunds for Menu and Command Names**: Menu names should be translated as nouns or gerunds (e.g., קובץ, שיתוף, הוספה). Command names inside menus or action buttons should also use gerund forms. Avoid infinitive-only forms, which can seem grammatically incomplete and create ambiguity about who is performing the action.
  - *Source:* "Edit (menu name)" → *Target:* "עריכה"
  - *Source:* "Print / Install" → *Target:* "הדפסה / התקנה"

- **No Comma Before Final List Item**: Hebrew rarely uses a serial comma before the last item in a list. Omit the comma unless the list items are so long or syntactically complex that the comma is needed to delimit the final item clearly.
  - *Source:* "iPhone, iPad, iPod touch" → *Target:* "ה-iPhone, ה-iPad וה-iPod touch"

- **Spell Out 'Your' Using Definite Article When Possible**: English uses possessives like 'your' where Hebrew often uses the definite article instead. Avoid translating 'your' as שלך unless extra emphasis on the user's ownership is necessary for the context.
  - *Source:* "Turn off your device" → *Target:* "יש לכבות את המכשיר (no need for שלך)"

- **Use Plene (Fuller) Spelling**: The Hebrew Language Academy recommends the 'fuller' spelling (כתיב מלא) as it is easier to read and leaves less ambiguity. Adopt fuller spellings in all new translations.
  - *Source:* "was (female)" → *Target:* "הייתה (preferred over היתה)"

## Punctuation

- **Use Geresh and Gershayim for Quotation Marks**: Hebrew uses exclusively the geresh (׳) for embedded quotations and the gershayim (״) for primary quotations and abbreviations. Do not use English curly quotes, straight quotes, or any other quotation characters. Punctuation marks (periods, commas) go outside the closing quotation mark in Hebrew.
  - *Source:* "Choose File > Quit." → *Target:* ".יש לבחור ״קובץ״ < ״סיום״"

- **Hyphen vs. En-Dash: Connecting vs. Separating**: A hyphen (מקף) connects elements with no surrounding spaces (e.g., ה-iPhone, דו-משמעות). An en-dash (קו מפריד) separates syntactic units and requires spaces on both sides. Do not use the upper makaf — it is inaccessible on standard keyboards. Use non-breaking hyphens whenever the following element might wrap to a new line.
  - *Source:* "the 19th century / iPhone settings" → *Target:* "המאה ה-19 / הגדרות ה-iPhone"

## Interface Elements

- **Device Type Names Must Be Definite; English App Names Are Not**: Hebrew device type names (iPhone, iPad, Apple Watch) in a possessive or modified context take the definite article via a hyphen prefix. English application names that are not translated do not take the definite article. Translated generic app names (Calculator, Camera) use regular nouns and are definite when required.
  - *Source:* "iPhone Settings / Finder Settings" → *Target:* "הגדרות ה-iPhone / הגדרות Finder"

- **Wrap Translated App Names in Gershayim Within Sentences**: When a translated compound or specialized app name is mentioned within running text, enclose it in gershayim (״…״) to distinguish it from surrounding text — Hebrew has no capital letters to perform this function. Generic app names that directly describe the function (Calculator, Camera) do not require quotes.
  - *Source:* "Quit Calendar" → *Target:* "סיום ״לוח שנה״"

- **Mirror Left/Right References for RTL UI**: Because Hebrew UI elements are mirrored for right-to-left display, occurrences of 'right' in source strings that describe on-screen position should generally be translated as 'left' and vice versa. Exercise discretion since not all UI surfaces are mirrored.
  - *Source:* "Swipe from the left" → *Target:* "החלקה מהצד הימני (mirrored to right)"

## Variables

- **Spell Out One and Two variants in a Plural Structure**: Plural strings allow modifying numbering variables. For Hebrew, remove the number "one" and "two" in most cases, and instead write the numbers in words. When the string contains more than one variable, only the first variable is allowed to be removed. The remaining variables should be numbered.
  - *Source:* "Add %lu item to \u201C%@\u201D" → *Target:* "הוספת שני פריטים אל ״%2$@״"

- **Reorder Variables Using Numbered Indices**: When Hebrew word order requires reordering, add n$ numbering to all variables (e.g., %1$@ %2$@) before rearranging. When a prefix such as ה- or a preposition precedes a variable that may receive a non-Hebrew value, insert a non-breaking hyphen between the prefix and the variable.
  - *Source:* "%@ reacted %@ to an audio message" → *Target:* "תגובה של %2$@ נוספה על ידי %1$@ להודעת שמע"

## General Advice

- **Keep Translations Concise**: Hebrew speakers favor directness, and Hebrew translations are often significantly shorter than their English equivalents. Aim to convey meaning in as few words as possible while maintaining clarity. Double spaces used in English before a new sentence should be reduced to a single space in Hebrew.

## Diversity And Inclusion

- **People-First Language for Disability**: When referring to people with disabilities, describe the person before the disability. Avoid noun forms that reduce a person to their disability (e.g., עיוורים). Use full phrases such as אנשים עם עיוורון or אנשים עם לקות ראייה instead.
  - *Source:* "the blind" → *Target:* "אנשים עם עיוורון או לקות ראייה"

- **Use Diverse and Inclusive Example Names**: When sample names are required, include names representing a variety of ethnicities and genders found in Israel's diverse population. Prefer gender-neutral names (טל, אור) where appropriate, and include minority names alongside common ones. Ensure a mix of ages is represented.
  - *Source:* "John / Jane Doe (multiple names)" → *Target:* "Examples: דימה, מוחמד, פנטה, נביל, רבקה, מיה"
