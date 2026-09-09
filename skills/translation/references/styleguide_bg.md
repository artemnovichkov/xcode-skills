# Bulgarian (bg) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Bulgarian uses curly double quotation marks „ (\u201E) and “ (\u201C) for quoting — not straight ASCII quotes.

## Tone And Voice

- **Smart but Neutral Style**: Bulgarian text should feel professional yet approachable — closer to formal than informal, but never stiff. Avoid trendy slang or colloquialisms. Prefer genuine Bulgarian terminology over English loan words wherever a clear Bulgarian equivalent exists.
  - *Source:* "ringtone" → *Target:* "тон на звънене"

- **Prefer Bulgarian Over Transliteration**: Use established Bulgarian terms rather than transliterating English words into Cyrillic. Transliteration is only acceptable when a transliterated form is already widely recognized in Bulgarian technical usage.
  - *Source:* "ringtone" → *Target:* "тон на звънене" (not "ринг тон")
  - *Source:* "file" → *Target:* "файл"

## Addressing Users

- **T/V Distinction (Вие vs. ти)**: Bulgarian distinguishes formal/polite second-person plural (Вие, Вас, Вашия) from informal singular (ти, теб, твоя). Default to the polite plural Вие form when the device addresses the user (notifications, messages, instructions). Reduce explicit Вие/Вас pronouns where Bulgarian style makes them unnecessary — verb endings already encode person and number. Use the informal singular ти form only for: strings exclusively directed at children, strings explicitly framed as friend/family interaction, and strings representing the user instructing the device (Siri voice commands, voice input).
  - *Source:* "Your settings have been saved." → *Target:* "Настройките са запазени."
  - *Source:* "You can share this with your friends." → *Target:* "Можеш да споделиш това с приятелите си."
  - *Source:* "Send an email" (Siri command) → *Target:* "Изпрати имейл"

- **Gender-Neutral User References**: Avoid gender-biased translations. Use потребител as a gender-neutral reference when a pronoun or gendered noun would otherwise be required.
  - *Source:* "He/She can change the settings." → *Target:* "Потребителят може да промени настройките."

## Abbreviations

- **Avoid Abbreviations in UI Strings**: Do not shorten words through abbreviations to fit space constraints — instead reword the string. Only use Вкл. and Изкл. for on/off UI toggles, and и др. only when space does not allow и други.
  - *Source:* "On / Off" → *Target:* "Вкл. / Изкл."

- **Day-of-Week Abbreviations**: When space is very tight use single capitalized Cyrillic letters for days of the week. When slightly more space is available use the two-letter capitalized abbreviation forms. Note that the single-letter forms are positional only — П covers both Понеделник and Петък, С covers both Сряда and Събота — so they only disambiguate within an ordered weekday row.
  - *Source:* "Mon Tue Wed Thu Fri Sat Sun" (single-letter form) → *Target:* "П В С Ч П С Н"
  - *Source:* "Mon Tue Wed Thu Fri Sat Sun" (two-letter form) → *Target:* "Пн Вт Ср Чт Пт Сб Нд"

## Acronyms

- **Do Not Translate Acronyms Unless Standardized**: Keep technical acronyms (CD-ROM, RAM, ISO, etc.) in their original form. Never use periods within acronyms in Bulgarian. Only translate an acronym when a standard industrial Bulgarian equivalent exists in technical dictionaries.
  - *Source:* "RAM (random access memory)" → *Target:* "RAM (памет с произволен достъп)"
  - *Source:* "HTTPS" → *Target:* "HTTPS" (keep as-is, do not transliterate)

## Grammar

- **Gender Agreement for Foreign Product Names**: Bulgarian has three grammatical genders. When space is constrained, derive masculine gender from the zero ending of foreign product names. When space allows, prepend a Bulgarian determiner noun to clarify the intended gender.
  - *Source:* "Apple TV is on." → *Target:* "Apple TV е включен."
  - *Source:* "iCloud is active." → *Target:* "Услугата iCloud е активна." (with determiner noun when space allows)

- **Imperative for User Instructions**: All user-facing step-by-step instructions must be written in the imperative mood. This applies to software steps, setup guides, and how-to documentation.
  - *Source:* "Install XYZ." → *Target:* "Инсталирайте XYZ."
  - *Source:* "Select File > Duplicate." → *Target:* "Изберете меню Файл > Дублирай."

- **Undo/Redo Strings Use Lowercase Noun Phrase**: Undo (Отмени) and Redo (Отново) menu commands are followed by a lowercase noun phrase in Bulgarian, unlike English which repeats the capitalized command verb. The actual menu command and its undo/redo counterpart may therefore be translated differently.
  - *Source:* "Undo Edit Photo" → *Target:* "Отмени редактиране на снимка"
  - *Source:* "Redo Edit Photo" → *Target:* "Отново редактиране на снимка"

- **Tooltip Types — Hint vs. Prompt**: Hint tooltips (no clause of purpose) use present tense third person. Prompt or instruction tooltips (with a clause of purpose such as to, in order to) use the imperative.
  - *Source:* "Remove a XYZ settings file" (hint tooltip) → *Target:* "Изтрива файла с параметри XYZ"
  - *Source:* "Press and hold to create a new project" (prompt tooltip) → *Target:* "Натиснете и задръжте, за да създадете нов проект."

## Date And Time

- **Use 24-Hour Time Format**: Convert 12-hour AM/PM times to the 24-hour system wherever possible. Only keep AM/PM notation when the string explicitly relates to the American time format distinction as a selectable display option.
  - *Source:* "4:00 PM" → *Target:* "16:00"

## Numerals

- **Decimal Comma and Non-Breaking Space Thousands Separator**: Bulgarian uses a comma as the decimal separator and a non-breaking space as the thousands separator. Version numbers are an exception and keep the period as separator. Remove the v prefix from version strings and replace it with the word версия.
  - *Source:* "11,234.50 kg" → *Target:* "11 234,50 kg"
  - *Source:* "Requires OS X v10.8.2." → *Target:* "Необходима e версия OS X 10.8.2."

## Measurements

- **Do Not Convert Units; Use Latin SI Symbols**: Never convert measurement units (e.g. inches to centimetres). Bulgaria follows the SI system, which uses Latin-character unit symbols — do not use Cyrillic equivalents. Use a non-breaking space between the numerical value and the unit symbol; exceptions are the percent and degree signs.
  - *Source:* "2.5 GB" → *Target:* "2,5 GB"
  - *Source:* "0.45" → *Target:* "0,45"

## Addresses

- **Bulgarian Address Format**: Format addresses following Bulgarian Post conventions — recipient name, street and number, 4-digit postal code, and city on separate lines.

## Punctuation

- **Bulgarian Quotation Marks**: Use „ (\u201E) as the opening quotation mark and “ (\u201C) as the closing quotation mark. Do not use quotation marks around app names, UI navigation paths, button names, or variables representing a person's name or email address. Add quotes around UI elements only when they genuinely aid readability.
  - *Source:* "Click \u201CDone\u201D." → *Target:* "Щракнете върху Готово." (no quotes around button name)
  - *Source:* "Select Messages > Settings > iMessage." → *Target:* "Изберете Съобщения > Настройки > iMessage" (no quotes in path)

- **Spacing After Punctuation**: Use a space after full stops, commas, semicolons and other punctuation marks unless otherwise required by source.

## Special Characters

- **Replace**: The # symbol to denote numbers or positions is not used in Bulgarian text — replace it with № followed by a non-breaking space. The `&` symbol should be translated as и in regular text. Keep `&` only when it is part of a trademark or product name (e.g. Plug&Play), with no spaces around it.
  - *Source:* "Track #5" → *Target:* "Запис №\u00A05" (use \u00A0 between № and the digit)
  - *Source:* "Cut & Paste" → *Target:* "Изрязване и поставяне"
  - *Source:* "Plug&Play" → *Target:* "Plug&Play"

## Interface Elements

- **Window Titles Must Be Nouns**: Bulgarian window titles must be nouns, not verbs. English often reuses the verb form of a button as the title of the resulting screen — this is not acceptable in Bulgarian.
  - *Source:* "Edit Photo" (window title) → *Target:* "Редактиране на снимка"

- **Buttons and Commands — Imperative Verbs for Actions; Fixed Forms for Dismissive Buttons**: Action and command labels (Copy, Paste, Delete, Save, Send, Open) are translated as 2nd-person singular imperative verbs. Dialog-closing and dismissive buttons (Cancel, OK, Yes, No, Done, Next) follow established fixed-form conventions and are usually nouns or short non-verbal forms. Menu items that trigger an action follow the imperative pattern; items that open submenus are usually nouns. Option and checkbox labels can be nouns or verbs as long as they agree grammatically with the surrounding context.
  - *Source:* "Copy" (command) → *Target:* "Копирай"
  - *Source:* "Paste" (command) → *Target:* "Постави"
  - *Source:* "Save" (command) → *Target:* "Запази"
  - *Source:* "Cancel" (button) → *Target:* "Отказ"
  - *Source:* "Done" (button) → *Target:* "Готово"
  - *Source:* "Next" (button) → *Target:* "Напред"

## Trademarks And Product Names

- **Do Not Translate or Transliterate Trademarks**: Apple trademarks, product names, and marketing terms must remain in English exactly as provided. Use non-breaking spaces within multi-word trademarks such as iPod touch to prevent awkward line breaks. For long compound names such as Apple Pro Display XDR, do not place a non-breaking space after Apple to avoid mid-word wrapping.
  - *Source:* "iPod touch" → *Target:* "iPod touch" (use a non-breaking space between iPod and touch)
  - *Source:* "True Tone, iTunes Match" → *Target:* "True Tone, iTunes Match" (keep as-is, do not transliterate)

## Variables

- **Preserve Variables Exactly as in the Source**: Variables such as %@, %.1f, and %1$s must not be modified in any way — they are substituted at runtime and any alteration will break the substitution. Do not convert a period to a comma inside a numeric format specifier like %.1f GB; decimal formatting is handled by the software.
  - *Source:* "%.1f GB available" → *Target:* "%.1f GB свободно"

## Diminutives

- **Diminutives**: Diminutives should be generally avoided, as they represent stylistic connotations not appropriate in technical translation.

## Genders

- **Gender - Use Determiner words**: Bulgarian has three genders. For clear reference, in descriptive texts, it is possible to preposition the product name with a determiner word.
  - *Source:* "iTunes is open" → *Target:* "Приложението iTunes е стартирано"

- **Derive Masculine Gender from the Zero Ending**: In cases with space constraints and to simplify the text, derive and use the masculine gender from the zero ending of the foreign word.
  - *Source:* "iTunes is open, iPhone is turned on" → *Target:* "iTunes е стартиран, iPhone е включен"
