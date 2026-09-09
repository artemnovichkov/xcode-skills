# Russian (ru) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Russian uses guillemets « (\u00AB) and » (\u00BB) as the primary quotation marks, curly double quotes „ (\u201E) opening and “ (\u201C) closing for a nested quotation inside guillemets, and the curly apostrophe ’ (\u2019).
  - *Source:* "Click the \u201CHome\u201D button" → *Target:* "Нажмите кнопку \u00ABДомой\u00BB"

## Tone And Voice

- **Smart but Casual Tone**: The overall tone should feel intelligent yet approachable — closer to formal than informal, but never stiff or bureaucratic. Avoid trendy slang and keep a neutral, descriptive style. Some English terms that do not translate well may be left in English rather than forced into Russian.
  - *Source:* "HTTPS, True Tone, iTunes Match" → *Target:* "HTTPS, True Tone, iTunes Match" (technical names — do not localize)

## Addressing Users

- **Formal Address with Capitalized Вы**: Address a single user with the capitalized pronoun «Вы» and its forms (Вам, Вас, Ваш) in the machine-to-human dialog. This capitalization was specifically approved by the Russian Academy of Sciences.
  - *Source:* "Your changes will be lost." → *Target:* "Ваши изменения будут потеряны."

- **Minimize Use of Вы and Ваш**: Do not carry over English possessive pronouns mechanically. Omit «Вы» where it adds nothing, prefer «свой» over «Ваш» when the reflexive form is grammatically valid, and try to avoid repeating «Вы» multiple times in the same sentence.
  - *Source:* "You can manipulate clips using various tapping gestures." → *Target:* "Для работы с клипами можно использовать различные жесты касания."

- **Omit "Please" in Instructions**: English commands routinely include "please", but the Russian formal imperative already conveys sufficient politeness. Drop «пожалуйста» from instructional strings unless context strongly requires it.
  - *Source:* "Please restart your computer." → *Target:* "Перезагрузите компьютер."

- **Informal Address for Casual or Youth-Oriented Strings**: Use the informal singular «ты» and its forms instead of «Вы» only when the source string's tone is distinctly casual, or when the developer's instructions call for an informal, youth-oriented voice (e.g. a kids' or fitness app).
  - *Source:* "You did it!" → *Target:* "У тебя получилось!"

## Abbreviations

- **Avoid Abbreviations in Software Strings**: Do not shorten words through abbreviations when a string is too long; instead, rephrase it. Where commonly accepted Russian abbreviations exist for English ones (e.g. США for USA), use them. Specific approved short forms include Кол-во, Вкл., and Выкл.
  - *Source:* "Qty: %d" → *Target:* "Кол-во: %d"

- **Days of the Week Abbreviations**: Use single capitalized letters (П, В, С, Ч, П, С, В) only when space is extremely tight. Use the two-letter forms (Пн, Вт, Ср, Чт, Пт, Сб, Вс) whenever space permits.

## Acronyms

- **Do Not Translate Acronyms Without Cause**: Leave technical acronyms in English unless a standard Russian industry equivalent exists. If the source provides an expansion, translate it; do not add one the source lacks. Never use periods inside Russian acronyms (e.g. США, not С.Ш.А.).
  - *Source:* "CD-ROM (compact disc read-only memory)" → *Target:* "CD-ROM (компакт-диск с памятью только для чтения)"

## Date And Time

- **Use 24-Hour Time Format**: Convert AM/PM times to 24-hour format (e.g. 16:00). Keep AM/PM in English only when the string itself is the 12-hour time-format label being displayed.
  - *Source:* "4 PM" → *Target:* "16:00"

## Numerals

- **Number Formatting: Space as Thousands Separator, Comma as Decimal**: Use a non-breaking space as the thousands separator and a comma as the decimal separator. Version numbers keep a period and do not take a trailing period. Remove the leading «v» from version strings. Four-digit numbers in running text may use a non-breaking space in numeric tables, except for years and list numbering.
  - *Source:* "11,234.50 kg / OS X v10.8.2" → *Target:* "11 234,50 кг / OS X 10.8.2"

## Measurements

- **Use Russian Unit Symbols per GOST Standards**: Use a non-breaking space between the numeric value and the unit symbol. Percentage and degree signs take a narrow (two-point) space. Symbols raised above the baseline (°, ′, ″) are written without any space. Do not convert imperial measures.
  - *Source:* "2 GB / 30 min / 100 % / 25 °C" → *Target:* "2 ГБ / 30 мин / 100 % / 25 °C" (non-breaking space before ГБ and мин; narrow no-break space before % and °C)

## Names And Addresses

- **Use Locally-Appropriate Names and the Russian Address Format**: Replace English placeholder names with locally-appropriate Russian equivalents. Address lines follow the Russian postal convention: name/company, then street and number, then locality, then region, then «Россия», then the 6-digit postal code. Omit «дом» and «город» for style consistency.

## Special Characters

- **Use # as № and & as и**: Replace the English ordinal symbol # with the Russian № followed by a non-breaking space when it denotes an order number. The ampersand & is not used in Russian text; translate it as «и». The & may remain only when it is part of a trademark or product name with no spaces around it (e.g. Plug&Play).
  - *Source:* "Track #5 / Music & Movies" → *Target:* "Трек № 5 / Музыка и фильмы"

## Punctuation

- **Guillemet Quotation Marks**: Use «guillemets» (double chevrons) as the primary quotation marks. Curly double quotes „ (\u201E) opening and “ (\u201C) closing are reserved for a second level of quotation nested inside guillemets. Use quotation marks with function and button names when the generic (descriptor) word (кнопка, функция) is present, and in UI navigation paths. Do not quote standalone app names or foreign words such as FaceTime.
  - *Source:* "Click the \u201CHome\u201D button / Go to Messages > Settings" → *Target:* "Нажмите кнопку \u00ABДомой\u00BB / Перейдите в \u00ABСообщения\u00BB > \u00ABНастройки\u00BB"

- **Em Dash with Non-Breaking Space**: Use the em dash (—) for parenthetical constructions. Always place a non-breaking space before the spaced em dash to prevent it from wrapping to the next line. Do not use spaces in numeric ranges; use the em dash directly between values.
  - *Source:* "Lightning to USB Cable" → *Target:* "Кабель Lightning — USB"
  - *Source:* "10–100 m" → *Target:* "10—100 м" (no spaces in a numeric range)

- **Full Stops: Follow the Source**: Add or omit a period at the end of a string to match the source.

## Grammar

- **Buttons as Perfective Verbs**: Translate button labels as verbs in the perfective aspect. If space is too tight for the full infinitive form, use the noun form as a fallback. Command names in menus also use the perfective infinitive. Menu bar names use nouns. Window titles and UI alert titles must be nouns in the nominative case.
  - *Source:* "Cancel" (button) / "Copy" (menu command) / "View" (menu name) → *Target:* "Отменить / Скопировать / Вид"

- **Gender Assignment for Foreign Product Names**: Add a Russian descriptor word to clarify grammatical gender when product names are used with verbs or adjectives. Always add «часы» before «Apple Watch» when declension is required. Use «приложение» before an app name when declension is required.
  - *Source:* "Apple TV is on / Apple Watch is on" → *Target:* "Apple TV включен" (short) / "Устройство Apple TV включено" (long) / "Часы Apple Watch включены"

- **Capitalization: Russian Rules Override English Title Case**: Russian capitalizes only proper nouns, the first word of a sentence, and standalone table entries. Do not replicate English title case in translated UI item names. Capitalize concrete UI element names and feature names that are referenced directly; use lowercase for the same terms used in a generic sense.
  - *Source:* "System Preferences / Show All / Location Services" (UI label) vs. "location services" (generic) → *Target:* "Системные настройки / Показать все / Службы геолокации" (UI) / "службы геолокации" (generic)

- **Plural Forms: Four Categories**: Russian requires four plural categories: «one» (numbers ending in 1, e.g. 1, 21), «few» (2–4, 22–24), «many» (5–20, 25+), and «other» (decimal fractions). Always include the variable in the «one» category string even if the source omits it, consistent with the other categories. Parent and child plural strings must agree grammatically.
  - *Source:* "%d icon / %d icons" → *Target:* "one: %d значок / few: %d значка / many: %d значков / other: %d значка"

- **Use Descriptor words in front of Peoples' Names**: When the source clearly marks a variable as a person's name, prepend the generic descriptor "Пользователь" (User): a name inserted at runtime can't be declined for case or gender, so the fixed masculine descriptor noun carries the agreement and the sentence stays grammatical for any name. In messaging or participant contexts, use the descriptor "Участник" (Participant) instead; reuse whichever descriptor already appears in previously-translated strings for consistency.
  - *Source:* "%@ hasn\u2019t started their account recovery yet. / %1$@ and %2$lld others liked %3$@\u2019s location" → *Target:* "Пользователь %@ еще не начал восстановление аккаунта. / Участнику %1$@ и еще %2$lld людям нравится геопозиция участника %3$@"

- **Use Descriptor words in front of Features and Services**: Russian has three genders, but a foreign product name carries none reliably. For clear agreement in descriptive text, prepend a Russian descriptor noun to the product name so verbs and adjectives can inflect — e.g. «Приложение %@ запущено», «Сервис %@ выключен». Under space constraints, drop the descriptor and treat the bare foreign name as masculine, deriving that gender from its zero ending — e.g. «%@ запущен».
  - *Source:* "%@ Disabled / AutoMix is On" → *Target:* "Сервис %@ выключен / Функция AutoMix включена"

- **Use ″ for Inches and “ми” for Miles**: Use the double prime ″ (\u2033) as the abbreviation for inches — there is no universally accepted verbal abbreviation in Russian ("дм" can be confused with decimeters). Inside a delivered string value, write it as its escape \u2033 (and the single prime ′ for feet/minutes as \u2032), like curly quotes. Use “ми” for miles, not "мл”, to avoid confusion with milliliters.

- **Differentiate Translation of "Service"**: Differentiate translations of "Service(s)" by meaning. For a subscription or online service (streaming, cloud, media), translate as "Сервис". For a system or background service, translate as "Служба".
  - *Source:* "Accessory Information Service / This service is not available in your region." → *Target:* "Служба информации об аксессуарах / Этот сервис недоступен в Вашем регионе."

- **Try to Use Gender-Neutral Language**: Prefer a construction that avoids gendered past-tense endings rather than providing multiple gender endings in brackets or with slashes.
  - *Source:* "%@ created a note" → *Target:* "Новая заметка от %@" (noun phrase — avoids the gendered "создал(-а)")

## Interface Elements

- **Tooltips: Infinitive for Hints, Imperative for Prompts**: Distinguish two tooltip types. Static hints describing what a control does should use the infinitive. Instructional prompts that guide the user through an action (typically containing a purpose clause) should use the imperative.
  - *Source:* "Delete the selected item" (hint) / "Touch and hold to add a widget" (prompt) → *Target:* "Удалить выбранный объект" (hint) / "Нажмите и удерживайте, чтобы добавить виджет" (prompt)

- **Undo/Redo Strings Use Lowercase Noun**: In the Edit menu, «Отменить» and «Повторить» are followed by a lowercase noun describing the action, unlike the action command itself which starts with a capital. When «Cancel» and «Undo» both appear in the same UI, translate «Undo» as «Не применять» to avoid duplicate «Отменить» labels.
  - *Source:* "Undo Keyboard Typing / Redo Edit photo" → *Target:* "Отменить ввод с клавиатуры / Повторить редактирование фото"

## Trademarks And Product Names

- **Do Not Translate Trademarks and Product Names**: Trademarks, branded slogans, and product names kept in English must not be translated or transliterated. Within a multi-word product name, join the words with a non-breaking space (U+00A0) — e.g. Apple Watch, iPod touch. For a long name like Apple Pro Display XDR, apply non-breaking spaces only within «Pro Display XDR», not after the company name.
  - *Source:* "Designed by Apple in California" → *Target:* "Designed by Apple in California" (do not translate)

## Variables

- **Preserve Variables Exactly; Reorder with Positional Indices When Needed**: Never alter or omit variable format specifiers (%@, %d, %lld, %1$@). If Russian word order requires a different variable sequence, add positional indices (%1$@, %2$@) to every variable in the string. Do not change the period inside numeric format specifiers such as %.1f.
  - *Source:* "%1$@\u2019s %2$@" → *Target:* "%2$@ (%1$@)"

## Diversity And Inclusion

- **Avoid Harmful, Oppressive, or Ableist Terms**: Do not use terms that are inherently violent (e.g. kill, hang), oppressive (e.g. master/slave), or that equate a disability with a defect. Do not use color to convey positive or negative qualities. When translating about people with disabilities, use people-first language.
  - *Source:* "The blind" → *Target:* "Люди с нарушениями зрения"
- **Represent People Inclusively**: Where Russian grammar allows, avoid binary he/she constructions by rewriting the sentence, using the plural, or omitting the pronoun; where the source uses a singular gender-neutral reference, follow suit (e.g. этот человек). Use gender-agnostic placeholder names (e.g. Саша, Женя).

## General Advice

- **Prefer Natural Russian Over Literal Translation**: The translation succeeds when the reader does not feel like they are reading a translation. Avoid word-for-word renderings of English gerunds and participial phrases; use Russian adverbial participles with clear temporal and logical anchoring. Simplify error messages that contain developer-facing language into clear, user-friendly sentences.
  - *Source:* "The operation couldn\u2019t be completed. (error -50)" → *Target:* "Не удалось выполнить операцию."
