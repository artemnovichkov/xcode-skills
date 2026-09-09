# English (en) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: English uses the curly apostrophe ’ (\u2019) for contractions and possessives, and curly double quotation marks “ (\u201C) and ” (\u201D) for quoting — not straight ASCII quotes.

## Tone And Voice

- **Smart but casual**: Render the target in a tone that is "smart but casual" — closer to formal than informal, but never stiff or academic. Use a neutral, descriptive style and avoid trendy slang, regardless of how formal or casual the source register is.

- **Use contractions**: English UI text reads naturally with common contractions, even when the source language has no equivalent. Contract be-verbs and auxiliaries with "not" ("don’t" (\u2019), "isn’t" (\u2019), "can’t" (\u2019)) and with personal pronouns ("you’re" (\u2019), "it’s" (\u2019), "they’re" (\u2019)). Don’t contract nouns or proper nouns ("The computer isn’t working" (\u2019), not "The computer’s not working" (\u2019)). Avoid awkward contractions ("could’ve" (\u2019), "it’ll" (\u2019), "how’re" (\u2019)).

- **Don’t translate idioms literally**: Don’t carry a source-language idiom or colloquial expression across word for word. Use plain, simple sentence structures so the result reads naturally.

## Addressing The User

- **Address the user as "you"; never first person**: Translate the user as "you", collapsing any formal/informal (T–V) distinction the source language makes — English has only one form. Don’t render the source’s first-person "we"/"I" (common when the source refers to the maker); rewrite in terms of the reader or the product. Use "recommended", not "we recommend".

- **Omit "please"**: Drop "please" from instructions even when the source includes a politeness marker. "Enter your password", not "Please enter your password".

- **Prefer present tense**: Use the present tense wherever it suffices, even if the source uses future or another tense. In conditionals use the present ("If the parameter is true, playback stops", not "…will stop"). Reserve the future tense for things genuinely yet to come (e.g. a product not yet available).

## Grammar And Usage

- **Possessives**: Form the possessive of a singular noun — including one ending in s — with an apostrophe and s ("the device’s connector" (\u2019), "the boss’s husband" (\u2019)); a plural noun ending in s takes only an apostrophe ("the students’ curriculum" (\u2019)). When a name precedes a `%@` person variable, prefer "%@’s" (\u2019) over a separate possessive construction. Rewrite to avoid a possessive on any product name ("the features of your MacBook Pro", not "your MacBook Pro’s features" (\u2019)).

- **Serial comma**: Use a serial (Oxford) comma before "and" or "or" in a list of three or more items ("phone calls, text messages, and reminders"), regardless of the source’s list punctuation.

- **Avoid "and/or"**: Rewrite to avoid the construction — "document and app icons", not "document and/or app icons".

- **Avoid abbreviations and Latin shortcuts**: Don’t introduce abbreviations to save space; if a string is too long, make a note about a UI improvement rather than abbreviate. Avoid Latin abbreviations ("for example", not "e.g."; "and so on", not "etc."; "that is", not "i.e."). Keep an acronym as the source uses it; if the source pairs it with a spelled-out form, keep that, and don't add an expansion the source lacks or drop one it has.

## Capitalization

- **Apply English casing by string role, not from the source**: English uses sentence-style (capitalize only the first word — "Skip this backup") and title-style (capitalize each significant word — "Skip This Backup"). Choose the style from the string’s role per English UI convention, not from the source: many source languages capitalize far less or far more than English, so don’t mirror the source’s casing.

- **Title-style rules**: Capitalize the first and last word, and all nouns, pronouns, verbs, adjectives, and adverbs regardless of length ("Is", "Are", "Be"). Capitalize prepositions of five letters or more, and prepositions of any length in a phrasal verb ("Turn On", "Log In"). Don’t capitalize articles ("a", "an", "the"), coordinating conjunctions ("and", "but", "or", "nor", "for", "yet", "so"), the "to" in infinitives, or prepositions of four letters or fewer ("at", "by", "for", "in", "of", "on", "to", "up", "with"). Keep lowercase-initial product names lowercase even at the start ("iPad", "macOS").

## Punctuation

- **Curly quotation marks**: Use English curly quotation marks “ (\u201C) and ” (\u201D), not straight quotes and not the source language’s quotation style (guillemets, low-high quotes, corner brackets, etc.). Straight quotes and primes are only for code and for feet/inches. Put periods and commas inside the quotation marks; put semicolons, colons, question marks, and exclamation points outside unless part of an actual quotation.

- **What to quote**: Quote onscreen elements whose names use sentence-style capitalization, including checkbox and option labels ("Select the “Allow repeated calls” checkbox" (\u201C, \u201D)). For title-style element names, quote only if the name could be misread in context. Quote onscreen messages cited in text.

- **No space before punctuation**: Don’t carry over spacing the source language requires before marks like "?", "!", ":", or ";". English closes these up directly against the preceding word.

- **Ellipsis**: Use the ellipsis character (not three periods). When a menu command or button name ends with an ellipsis, drop the ellipsis when referring to it in running text ("Choose File > Print", not "Choose File > Print…").

- **Colons**: In running text, capitalize the first word after a colon only if it begins a complete sentence; in a heading, capitalize it regardless of part of speech. Precede every list with a colon.

- **Ampersand**: Use "&" only when referring to onscreen elements, document tiles, or other items that contain the character ("Privacy & Security settings") in the source string. Otherwise spell out "and". Don’t escape `&` like you have to in HTML.

## Interface Interaction Verbs

- **Choose vs. select**: Use "choose" for menu items and commands; use "select" for objects the user picks among or highlights — icons, files, text, checkboxes, radio buttons ("Select the text, then choose Edit > Copy"). A checkbox or option is selected or unselected — avoid "checked"/"unchecked".

- **Click, tap, press**: Use "click" for the mouse or trackpad, "tap" for touchscreens, and "press" for keys and physical buttons — choose by platform rather than mirroring a single generic source verb. Don’t write "click on" or "tap on", and don’t use "click and drag" — use "click" or "drag".

## Numbers, Units, And Time

- **Spelling out numbers**: Spell out cardinal and ordinal numbers from one through nine ("up to five computers"), and any number that begins a sentence (rephrase to avoid this where possible). Always use a numeral for a number referred to as a number and for a value with a unit ("the number 4 appears", "5 mm").

- **Number grouping and decimals**: Use a comma as the thousands separator, even with four digits ("1,000 songs"), and a period as the decimal separator — converting from the source’s separators where they differ. Don’t alter decimal points inside variables such as "%.1f". Flag any string that hard-codes a grouping or decimal separator.

- **Units of measure**: Insert a space between the number and a unit symbol or abbreviation ("20 GB of memory"). Unit symbols are unaltered in the plural ("lb.", not "lbs."). Hyphenate a spelled-out unit in a compound adjective ("20-yard line"), but not the symbol form ("30 GB capacity"). Where a unit is shown, flag any string that hard-codes a unit instead of using a formatter.

- **Time of day**: Use numerals for times. Include "a.m." and "p.m." in lowercase, with periods, preceded by a space ("10:45 a.m."). Use "noon" and "midnight".

## Names, Variables, And Trademarks

- **Don’t abbreviate or shorten product names**: Write product and service names in full, following their official capitalization. Never abbreviate, shorten, translate, or transliterate them.

- **Don’t use product names as verbs**: "Make a FaceTime call to a friend", not "FaceTime a friend"; "identify a song using Shazam", not "Shazam a song".

- **No plural or possessive trademarks**: Rewrite to avoid plural or possessive forms of trademarked names ("Mac computers", not "Macs"; "the storage on your iPad", not "your iPad’s storage" (\u2019)).

- **Variables and placeholders**: Never alter or translate variable tokens such as %@, %d, or %lu. English word order often differs from the source, so when the natural English sentence reorders variables, add positional markers (%1$@, %2$@) to every variable in the string.

- **Keep multi-word names together**: Don’t break a multi-word trademark (Apple TV, iPad Pro) across lines; use a nonbreaking space to keep it on one line.

## Inclusive Language

- **Gender-neutral by default**: English does not mark grammatical gender, so resolve any gendered agreement in the source into neutral English. Avoid binary gender phrasing when you can reword ("people", not "men and women"), and use singular "they"/"their"/"them" for a person of unspecified gender, or rewrite with a plural noun or by omitting the pronoun.

- **Avoid violent, oppressive, or ableist terms**: Don’t describe technology with terms that are inherently violent ("kill", "hang"), oppressive ("master"/"slave"), or that equate mental health with function ("sanity check"). Avoid attributing human or biological qualities to software or hardware.

- **Don’t encode value in color**: Don’t assign good or bad meaning to colors. Use "deny list"/"allow list" instead of "blacklist"/"whitelist"; use colors only to describe actual colors.

- **Don’t assume the senses**: In instructions, don’t assume the reader can see, hear, or speak. Write "a message appears" or "an alert sound plays", not "you see a message" or "you hear an alert". Avoid idioms with negative associations about disability ("fell on deaf ears", "turned a blind eye").
