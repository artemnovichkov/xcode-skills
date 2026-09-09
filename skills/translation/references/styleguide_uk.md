# Ukrainian (uk) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual Tone**: Write in a neutral, descriptive style that is closer to formal than informal, but never stiff or overly hip. Use clear and concise language — short, direct text is absorbed quickly. Avoid literal translations; the text should read naturally in Ukrainian as if it were never translated.
  - *Source:* "We recommend" → *Target:* "Рекомендуємо (not Ми рекомендуємо)"

## Abbreviations

- **Avoid Abbreviations in Software; Use Ukrainian Equivalents**: Do not abbreviate words to fit a UI string. When a commonly used Ukrainian abbreviation exists for an English one, use it. Graphical abbreviations formed by truncation require a period; contractions do not.
  - *Source:* "for example / e.g." → *Target:* "наприклад / напр."
  - *Source:* "University" → *Target:* "ун-т"

## Acronyms

- **Keep Acronyms in Source Form; Hyphenate Compound Uses**: Do not translate acronyms unless a very common Ukrainian equivalent exists. Use hyphens when an acronym modifies a noun (DVD-плеєр, USB-пристрій, URL-адреса). Acronyms are always written in all caps regardless of the capitalization of the spelled-out form.
  - *Source:* "DVD player" → *Target:* "DVD-плеєр"
  - *Source:* "USB device" → *Target:* "USB-пристрій"

## Date And Time

- **Ukrainian Date Format — Day Month Year with "р."**: Use day-month-year ordering with the abbreviation "р." for рік. The full format is "d MMMM y р." (e.g. 1 лютого 2017 р.) and the short format is DD.MM.YY. Time uses a 24-hour clock with a colon separator. For ISO-style dates, follow the source format exactly.
  - *Source:* "February 1, 2017" → *Target:* "1 лютого 2017 р."
  - *Source:* "02/01/17" → *Target:* "01.02.17"

## Names And Addresses

- **Ukrainian Sample Names and Address Format**: Use Ukrainian sample names instead of English defaults. Sample addresses should be translated into a Ukrainian format (street name with вул., city, postal code, Ukraine).
  - *Source:* "John Doe" → *Target:* "Андрій Петренко"
  - *Source:* "Jane Doe" → *Target:* "Оксана Петренко"
  - *Source:* "1 Infinite Loop, Springfield" → *Target:* "вул. Лугова, 23, Черкаси"

## Punctuation

- **Ukrainian Comma Rules — Common Mistakes to Avoid**: Do not place a comma before "як" or "ніж" in constructions like "(не) більше ніж". Do not split the complex expressions "перш ніж", "після того як", "тому що", "для того щоб" with a comma when the subordinate clause precedes the main clause. Do not use a comma after "наприклад" when it means "а саме".
  - *Source:* "Перш ніж надсилати повідомлення, заповніть це поле." → *Target:* "Перш ніж надсилати повідомлення, заповніть це поле. (no comma inside "Перш ніж")"

- **Ellipsis**: Use single character ellipsis, not three periods.
  - *Source:* "..." → *Target:* "…"

- **Non-breaking spaces between number and unit**: Add non-breaking space between the number and unit of measure.
  - *Source:* "4 GB" → *Target:* "4 ГБ"
  - *Source:* "%g km" → *Target:* "%g км"

- **Non-breaking space for percent sign**: Add non-breaking space between number and percent sign.
  - *Source:* "90%" → *Target:* "90 %"
  - *Source:* "Downloading, %d%%" → *Target:* "Викачування, %d %%"

- **En-dash**: Use en-dash (–) to indicate a range of numeric values.
  - *Source:* "The meeting time is 6-8 pm." → *Target:* "Зустріч о 18:00–20:00."

- **Apostrophe**: Use modifier letter apostrophe as the Ukrainian apostrophe in all instances.
  - *Source:* "Subject ID" → *Target:* "Ідентифікатор субʼєкта"
  - *Source:* "Requested name: %@" → *Target:* "Запитане імʼя: %@"

- **Quotes**: Use left-pointing double angle quotation mark « and right-pointing double angle quotation mark » as quotation marks. For nested quotes, use straight double quotation marks.
  - *Source:* "Building Services Menu…" → *Target:* "Побудова меню «Сервіси»…"
  - *Source:* "Click the link 'Go to system preferences'" → *Target:* "Натисніть посилання «Перейти в меню "Системні параметри"»."

- **Quotes and > character**: If the sequence of commands is divided by ">" character, avoid using quotes around user interface terms and add non-breaking space before ">".
  - *Source:* "To fix this, open Settings > General and turn off "Sync Library", then turn it back on." → *Target:* "Щоб виправити це, відкрийте Параметри > Загальні та вимкніть параметр «Синхронізувати медіатеку», потім увімкніть його знову."

- **M-dash**: Em dash is used as a dash, except for number ranges. Always add non-breaking space before Em dash.
  - *Source:* "%@ - %@" → *Target:* "%@ — %@"
  - *Source:* "%@-%@" → *Target:* "%@–%@"
  - *Source:* "%@ — Secure AirPrint" → *Target:* "%@ — безпечний AirPrint"

- **Non-breaking hyphen**: Use non-breaking hyphens everywhere where the part of the word is 2 letters or shorter.
  - *Source:* "HD-SD" → *Target:* "HD‑SD"
  - *Source:* "QR Code Detected" → *Target:* "Виявлено QR‑код"

- **Avoid double spacing**: Do not copy double white spaces from the source to translation. Use a single whitespace.
  - *Source:* "Copyright © 2001-2020 Apple. All rights reserved." → *Target:* "© 2001–2020, Apple Inc. Усі права захищено."

- **Non-breaking space in trademarks and DNTs**: Use non-breaking space in trademarks, DNTs, app names, company names.
  - *Source:* "About this Apple Watch:" → *Target:* "Про цей Apple Watch:"

- **No space before degrees character**: Do not put space between a number and degrees character if the scale is not indicated.
  - *Source:* "Latitude: %1$.4f°" → *Target:* "Широта: %1$.4f°"

## Grammar

- **Perfective vs. Imperfective Verbs**: Choose perfective verbs for one-time actions and commands (Copy, Paste, Open, Print) and imperfective for repetitive or continuous actions. Buttons and commands should use perfective infinitives; options and settings may use imperfective forms.
  - *Source:* "Copy (button)" → *Target:* "Скопіювати (perfective)"
  - *Source:* "Allow While Using App" → *Target:* "Дозволяти за використання (imperfective)"

- **Prefer Verbal (Infinitive) Constructions Over Deverbal Nouns**: Ukrainian favors verbs (дієслівність). For command names, checkboxes, button names, links, use the infinitive form rather than deverbal nouns ending in -ння/-ття. Using verbal infinitive constructions improves both readability and idiomatic accuracy.
  - *Source:* "Save as (button/command)" → *Target:* "Зберегти як (not Збереження)"
  - *Source:* "Open" → *Target:* "Відкрити (not Відкриття)"
  - *Source:* "Quit app" → *Target:* "Завершити програму"

## Interface Elements

- **UI Element Translation Patterns**: Buttons and commands use perfective or imperfective infinitive verbs. Status messages in Present Continuous use action nouns or "триває + noun". Messages requiring action should be as short as possible, avoiding gendered forms and direct pronoun addressing. Titles use nouns or imperatives. The OK button is always written in Latin as "OK".
  - *Source:* "Sign in (button)" → *Target:* "Увійти"
  - *Source:* "Downloading…" → *Target:* "Викачування…"
  - *Source:* "Searching…" → *Target:* "Триває пошук…"
  - *Source:* "Export (title)" → *Target:* "Експорт"

## Trademarks And Product Names

- **Do Not Translate or Transliterate Apple Product Name**: Product names must not be translated or transliterated. When an unlocalized product name is used in a sentence, add a descriptive word (програма, функція) to make the sentence sound natural in Ukrainian.
  - *Source:* "Pages has new features." → *Target:* "У програмі Pages з'явилися нові функції."
  - *Source:* "Today Apple announced a new MacBook computer." → *Target:* "Сьогодні Apple анонсувала новий комп'ютер MacBook."

## Terminology

- **Prefer Ukrainian Terms Over Anglicisms**: Use Ukrainian terminology wherever a native equivalent exists and is commonly used in the industry. Borrow English terms only when no adequate Ukrainian equivalent is available.
  - *Source:* "Link" → *Target:* "Посилання (not Лінк)"
  - *Source:* "Browser" → *Target:* "Оглядач (not Браузер)"
  - *Source:* "User" → *Target:* "Користувач (not Юзер)"
  - *Source:* "Content" → *Target:* "Вміст (not Контент)"

## Variables

- **Preserve Variables Exactly; Reorder with Positional Notation**: Keep all runtime variables unchanged. If Ukrainian word order requires moving a variable, add positional numbering to every variable in the string (%1$@, %2$@). Do not attach Ukrainian grammatical suffixes directly to a variable placeholder, as this will break runtime substitution.
  - *Source:* "%@ %@" → *Target:* "%2$@ — %1$@"

## Diversity And Inclusion

- **People-First Language for Disability; Official Ukrainian Term**: Refer to people with disabilities by describing the person before the condition. The official Ukrainian legal term is "особа з інвалідністю" — not "інвалід".
  - *Source:* "The blind" → *Target:* "Люди з вадами зору / незрячі (context-dependent)"
  - *Source:* "A disabled person" → *Target:* "Особа з інвалідністю"

## General

- **App/Apps**: Software applications are called "програма/програми" in Ukrainian, not "застосунок" or "додаток".
  - *Source:* "All third-party apps must explain why they are requesting access to your Health app data." → *Target:* "Усі сторонні програми повинні пояснювати, чому вони запитують доступ до ваших даних у програмі «Здоровʼя»."
  - *Source:* "Apps Syncing to iCloud Drive" → *Target:* "Програми, які синхронізуються з iCloud Drive"
  - *Source:* "Apply to all apps" → *Target:* "Застосувати до всіх програм"

- **Choose**: Translate Choose as Обрати and its appropriate forms.
  - *Source:* "Choose a file…" → *Target:* "Обрати файл…"
  - *Source:* "Choose a Braille Display" → *Target:* "Оберіть брайль-дисплей"
  - *Source:* "Activate to choose color" → *Target:* "Активуйте, щоб обрати колір"

- **Avoid excessive usage of pronouns**: Omit the word "your" in translation.
  - *Source:* "Turn off your iPhone" → *Target:* "Вимкніть iPhone"
  - *Source:* "Your library has been updated." → *Target:* "Бібліотеку оновлено."

- **Passive predicate forms ending in -но, -то**: It is recommended to use the passive predicate forms ending in -но, -то when the subject is unknown or not important enough to be mentioned in the sentence.
  - *Source:* "Page not loaded" → *Target:* "Сторінку не оновлено"
  - *Source:* "This album has already been created" → *Target:* "Цей альбом уже створено"
  - *Source:* "Invitation accepted" → *Target:* "Запрошення прийнято"

- **Avoid incorrect usage of вимагати for Require**: For translation of "Require" use the word запитувати or потребувати, not вимагати. Вимагати should be used only for persons.
  - *Source:* "Require Password" → *Target:* "Запитувати пароль"
  - *Source:* "This feature requires additional security" → *Target:* "Ця функція потребує додаткових заходів безпеки"

- **Avoid incorrect usage of вимагати for Need**: For translation of "need" use the word потребувати, not вимагати.
  - *Source:* "Event needs reply" → *Target:* "Подія потребує відповіді"
  - *Source:* "Looks like we need a password for this show." → *Target:* "Схоже, для цього шоу потрібен пароль."

- **Time**: Use the 24 hour clock for time format. Use a colon as a separator. If a 12 hour clock must be used, use "дп" for "AM" and "пп" for "PM". Use a leading 0 for times between 00:00 and 09:59.
  - *Source:* "Saturday, May 12 at 2:00 pm" → *Target:* "Субота, 12 травня, 14:00"
  - *Source:* "Today at 3 PM" → *Target:* "Сьогодні о 15:00"

## Cultural Adaptation

- **Politeness**: Avoid translating and including "Please" or similar polite imperatives from the source text. It is rarely used or needed in Ukrainian.
  - *Source:* "Please activate the account in Settings" → *Target:* "Активуйте обліковий запис у Параметрах"
  - *Source:* "Please click again" → *Target:* "Клацніть ще раз"
  - *Source:* "Please Sign In Again" → *Target:* "Увійдіть ще раз"

- **Formality**: Always address the user with "ви", not "ти".
  - *Source:* "Looks like you're listening on another device." → *Target:* "Схоже, що ви прослуховуєте це на іншому пристрої."
  - *Source:* "What do you want to hear?" → *Target:* "Що ви хочете послухати?"
  - *Source:* "Welcome to iTunes Match" → *Target:* "Вас вітає iTunes Match"

- **Avoid excessive usage of pronouns**: Sometimes "ви" may be omitted after the first reference or in clauses that follow imperative constructions.
  - *Source:* "Do you want to keep your subscription for this app?" → *Target:* "Хочете зберегти підписку на цю програму?"
  - *Source:* "Hear more of what's happening around you." → *Target:* "Почуйте світ навколо."

- **Non-personal sentences**: Direct addressing of the user should be replaced by a non-personal or non-gendered sentence.
  - *Source:* "How do you want to change it?" → *Target:* "Як саме слід змінити це?"
  - *Source:* "Four Things You Should Know" → *Target:* "Чотири речі, які варто знати"
  - *Source:* "You must log in to the proxy server." → *Target:* "Потрібно авторизуватися на проксі-сервері."

- **Are you sure you want to**: Translate the phrase "Are you sure you want to" as "Справді".
  - *Source:* "Are you sure you want to continue?" → *Target:* "Справді продовжити?"
  - *Source:* "Are you sure you want to quit?" → *Target:* "Справді завершити?"

- **Gender neutrality**: Use gender-neutral language and constructs. Try to rewrite any sentence to exclude pronouns or binary representations of gender.
  - *Source:* "Messages you send will be delivered when %@ comes online." → *Target:* "%@ отримає ці повідомлення, коли зʼявиться в мережі."

- **Present tense workaround for gender neutrality**: Translate the past tense phrases with variables that represent user name in present tense.
  - *Source:* "%@ invited you to chat." → *Target:* "%@ запрошує вас у чат."
  - *Source:* "%@ shared this document." → *Target:* "%@ поширює цей документ."
  - *Source:* "%@ completed a workout." → *Target:* "%@ завершує тренування."

- **Plural forms with s**: Plural forms for DNTs with 's' should be reproduced in translation. Use the appropriate descriptive word and full form with 's' ending.
  - *Source:* "Clean your AirPod" → *Target:* "Очистьте навушник AirPods"
  - *Source:* "Left AirPod" → *Target:* "Лівий навушник AirPods"

- **OK button**: OK is used globally in UI in the form of a button as OK (not O.k. or ОК in Cyrillic) and should be written in Latin letters.
  - *Source:* "OK" → *Target:* "OK"
  - *Source:* "Ok" → *Target:* "OK"
  - *Source:* "O.K." → *Target:* "OK"

## Orthography

- **Separator for decimal numbers**: Use comma as a separator for decimal numbers.
  - *Source:* "2.5 cm" → *Target:* "2,5 см"
  - *Source:* "iPad Pro (10.5-inch)" → *Target:* "iPad Pro (10,5 дюйма)"

- **Version numbers**: Although commas normally should be used as the separator for decimals, periods are instead used for software versions.
  - *Source:* "version 2.5" → *Target:* "версія 2.5"
  - *Source:* "iOS version 9.0 or later is required." → *Target:* "Потрібна iOS 9.0 або новішої версії."

- **Ampersand character**: Use the conjunction "і" or "та" or "й" instead of the character &.
  - *Source:* "Privacy & Security" → *Target:* "Приватність і безпека"
  - *Source:* "Documents & Data" → *Target:* "Документи й дані"
