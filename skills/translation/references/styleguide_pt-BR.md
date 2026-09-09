# Brazilian Portuguese (pt-BR) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Brazilian Portuguese uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "Tap \u201CDelete\u201D." → *Target:* "Toque em \u201CApagar\u201D."

## Tone And Voice

- **Smart but Casual Tone**: Write in a neutral, descriptive style that is closer to formal than informal without being stiff or trendy. The translation succeeds when the reader does not feel they are reading a translation — avoid pedantic word-for-word rendering and any cryptic phrasing.

## Addressing Users

- **Use 'você' to Address the User**: Always use the second-person pronoun 'você' when addressing the user directly. Do not use third-person forms. This applies consistently across all Apple software, help, and documentation in Brazilian Portuguese.
  - *Source:* "Any information sent to Apple does not identify you." → *Target:* "As informações enviadas à Apple não identificam você."

- **Reduce Redundant Possessive Pronouns**: English uses possessive pronouns far more than Brazilian Portuguese. When ownership is obvious from context, omit the possessive pronoun. Keep it only where removal creates genuine ambiguity.
  - *Source:* "Turn on your device and connect your device to your computer." → *Target:* "Ligue o dispositivo e conecte-o ao computador."

- **Do Not Translate 'Please'**: 'Por favor' disrupts sentence flow because it requires surrounding commas, and culturally in Brazil its use is reserved for genuine personal favors. Convey politeness through appropriate verb choice rather than adding 'por favor'.
  - *Source:* "Please make more room on this disk." → *Target:* "Libere mais espaço no disco."

## Abbreviations

- **Avoid Abbreviations in Software Strings**: Do not shorten words to make a string fit in the UI. When abbreviation is truly unavoidable, use the first few letters and place a dot after the second or third consonant.

## Acronyms

- **Keep Industry-Standard Acronyms Untranslated**: Do not translate acronyms unless a widely recognized Brazilian Portuguese equivalent exists. Acronyms such as ISO, ANSI, ASCII, and HTML are de facto industry standards and must remain in their English form.
  - *Source:* "RAM" → *Target:* "RAM"

## Grammar

- **Title Case for Software Interface Elements**: Use Title Case for menus, toggles, features, and options. Short prepositions of four letters or fewer (com, de, em, para) are lowercased unless they open the string. Longer prepositions of five or more letters (contra, desde, entre, sobre) remain uppercased.
  - *Source:* "Sensitive Content Warning" → *Target:* "Aviso de Conteúdo Sensível"

- **Infinitive form for Software Interface Elements**: Use Infinitive verb tense for menus, toggles, features, and options.
  - *Source:* "Open File" → *Target:* "Abrir Arquivo"

- **Sentence Case for Software Interface Titles**: For UI titles use Sentence case, but always capitalize UI element and feature names within them.
  - *Source:* "Turn On Dark Mode" → *Target:* "Ative o Modo Escuro"

- **Imperative form for UI titles**: Use Imperative verb tense for UI titles, subtitles, headers, subheaders. Boundary vs. the infinitive rule above: if the string is a label the user acts on (menu item, button, toggle, option), use the infinitive; if it's a prompt telling the user what to do, use the imperative
  - *Source:* "Back Up Your Data" → *Target:* "Faça backup dos dados"

- **Avoid Passive Voice and Gerunds**: Prefer active voice over passive constructions wherever possible. Gerund forms common in English should be rephrased in Brazilian Portuguese by restructuring the sentence or converting the verb to a noun.
  - *Source:* "The requested operation could not be completed." → *Target:* "Não foi possível concluir a operação solicitada."

## Punctuation

- **Use Curly Quotation Marks in Software Strings**: In software strings, curly quotation marks are mandatory. Straight quotes are reserved for code contexts only. Use quotation marks sparingly — add them only where they improve clarity.

- **No Comma Before 'e', 'ou', or 'nem'**: Unlike English, Brazilian Portuguese usually does not place a comma before the copulative conjunctions 'e', 'ou', and 'nem'. Remove any such comma that appears in the source.
  - *Source:* "%@, and %@" → *Target:* "%@ e %@"

- **Lowercase After Colons in Running Text**: Unlike English, Brazilian Portuguese does not capitalize the word following a colon in running text. Use lowercase after colons in warnings, notes, and similar constructions unless the surrounding context uses Title Case for a separate UI reason.
  - *Source:* "Warning: This action cannot be undone." → *Target:* "Aviso: esta ação não poderá ser desfeita."

- **Use the Ellipsis Character — Never Three Separate Dots**: Always insert the single ellipsis character (…) rather than using three consecutive periods. The single character provides correct spacing and proper rendering by accessibility tools.

- **Bullet Points: Full Stop for Sentences, None for Enumerations**: Add a full stop to bullet-point items that are grammatically complete sentences, even if the source omits it. Items that are enumerations (noun phrases or fragments) require no punctuation.
  - *Source:* "• Music and podcasts you enjoy" → *Target:* "• Músicas e podcasts que você curte" (no full stop — enumeration)
  - *Source:* "• O app Mensagens podia ser encerrado inesperadamente" → *Target:* "• O app Mensagens podia ser encerrado inesperadamente."

## Measurements

- **Do Not Convert Measurements; Always Space Before Unit Symbols**: Do not convert imperial units to metric or vice versa. Never use a double quote as an abbreviation for inch. Always insert a space between a number and its unit symbol; unit abbreviations never take a trailing period.
  - *Source:* "2GB" → *Target:* "2 GB"

## Numerals

- **Comma as Decimal Separator; Period as Thousands Separator**: Brazilian Portuguese uses a comma for decimals and a period for thousands — the reverse of English. Apply this in all content. Do not manually change the period inside printf-style format specifiers such as %.1f; the software handles decimal conversion internally.
  - *Source:* "45.5" → *Target:* "45,5"
  - *Source:* "1,000,000 songs" → *Target:* "1.000.000 músicas"

## Special Characters

- **Replace Ampersand with 'e' in Regular Text**: Do not use the ampersand (&) in Brazilian Portuguese text. Replace it with the conjunction 'e'. The ampersand is acceptable only in established industry-standard expressions such as 'Plug&Play'.
  - *Source:* "Mac & PC" → *Target:* "Mac e PC"

## Interface Elements

- **Prefix App Names with 'o app' to Resolve Gender Agreement**: Because 'app' is masculine in Portuguese while some app names are feminine (e.g. Casa, Notas, Música), use the prefix 'o app' when needed to avoid gender agreement errors. Exceptions include iWork apps (Pages, Numbers, Keynote), Ajustes, and apps with already-masculine names (Mail, FaceTime, Diário).
  - *Source:* "Click here to open in Bolsa." → *Target:* "Clique aqui para abrir no app Bolsa."
  - *Source:* "Click here to open in Maps." → *Target:* "Clique aqui para abrir no app Mapas."

- **Keyboard Shortcuts: Use Space + Plus Sign Between Keys**: Separate modifier keys with a space, a plus sign, and another space rather than a hyphen.
  - *Source:* "Command-Q" → *Target:* "Command + Q"

- **Do Not Translate Physical Keyboard Key Names**: All key names printed on a physical Apple keyboard must remain untranslated and should be in uppercase. The only exceptions are iOS/iPadOS software keyboard keys: 'Retorno', 'Espaço', and 'Ir'.
  - *Source:* "Caps Lock, Shift, Control, Option, Command" → *Target:* "Caps Lock, Shift, Control, Option, Command"
  - *Source:* "Return (iOS software keyboard)" → *Target:* "Retorno"

## Trademarks And Product Names

- **Never Translate Trademarks or Marketing Slogans**: Keep trademarks, product names, and marketing slogans in their original form — do not translate or transliterate them.
  - *Source:* "Designed by Apple in California" → *Target:* "Designed by Apple in California"

## Variables

- **Preserve Variables Exactly; Add Positional Indices When Reordering**: Never alter or omit variable format specifiers. If Brazilian Portuguese word order requires a different variable sequence, add positional indices (%1$@, %2$@, etc.) to every variable in the string — including variables whose position does not change. Do not change the period inside numeric format specifiers such as %.1f.
  - *Source:* "Meeting scheduled for %1$@ %2$@." → *Target:* "Reunião agendada para %2$@ de %1$@."

## Diversity And Inclusion

- **Avoid Gendered Assumptions; Prefer Gender-Neutral Rephrasing**: Avoid assuming the user's gender and do not use the 'o(a)' workaround. Where a gendered form would otherwise be needed, reword to a gender-neutral construction.
  - *Source:* "You will be notified." → *Target:* "Você receberá uma notificação." (instead of "Você será notificado.")
- **Put People First When Referring to Disability**: Use people-first language — refer to individuals as people before mentioning any disability, and focus on what people can do, not on what they can't.
  - *Source:* "a wheelchair-bound person" → *Target:* "uma pessoa em cadeira de rodas"

## Terminology

- **Use Apple-Specific Terminology Over Generic PC Translations**: Many common terms have an Apple-specific Brazilian Portuguese translation that differs from the generic PC industry term. Reuse the established Apple form as it appears in previously-translated strings.
  - *Source:* "Settings" → *Target:* "Ajustes" (not Configurações)
  - *Source:* "Delete" → *Target:* "Apagar" (not Excluir)
  - *Source:* "Full screen" → *Target:* "Tela cheia" (not Tela inteira)
  - *Source:* "Enable/Disable" → *Target:* "Ativar/Desativar" (not Habilitar/Desabilitar)
  - *Source:* "Tab" → *Target:* "Aba" (not Guia)
