# European Portuguese (pt-PT) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: European Portuguese uses curly double quotation marks “ (\u201C) and ” (\u201D) for quoting, and the curly apostrophe ’ (\u2019).
  - *Source:* "Tap \u201CDelete\u201D." → *Target:* "Toque em \u201CApagar\u201D."

## Tone And Voice

- **Smart but Casual Register**: The overall tone should lean towards formal rather than informal, but must never feel stiff or stilted. Use neutral, descriptive language and avoid trendy or colloquial expressions. Prefer Portuguese terminology over English borrowings whenever a natural, widely understood equivalent exists.
  - *Source:* "Sign in with your account." → *Target:* "Inicie sessão com a sua conta."

## Addressing Users

- **Formal Third-Person Address — Avoid Explicit 'você'**: Use the formal third-person singular verb form to address the user. Never write the explicit pronoun 'você' — it is implied by the verb form. Avoid exclusive masculine pronouns and overuse of 'seu/sua'; restructure sentences to use gender-neutral or impersonal constructions instead. Use an informal register only when the source string's tone is distinctly casual, or when the developer's instructions call for an informal voice (e.g. a social or youth-oriented app).
  - *Source:* "To help us serve you better, …" → *Target:* "Para ajudar a melhorar a qualidade do serviço, …" (not 'servi-lo')

- **Avoid Overuse of Possessive Pronouns**: English uses possessive pronouns far more frequently than Portuguese. Replace 'your X' with the definite article whenever the owner is obvious or irrelevant to the meaning.
  - *Source:* "Shut down your computer." → *Target:* "Desligue o computador."

## Abbreviations

- **Avoid Abbreviations in Software; Non-Breaking Space in Two-Word Abbreviations**: Do not use abbreviations in software strings unless a string is too long and no other solution exists. When a common two-word Portuguese abbreviation is used, separate its parts with a non-breaking space. Common mappings: 'e.g.' → 'por ex.', 'etc.' → 'etc.', 'page' → 'pág.'.
  - *Source:* "e.g. / etc." → *Target:* "por ex. / etc."

## Acronyms

- **Retain English Acronyms; No Plural Form in Portuguese**: Do not translate acronyms unless a standard industrial Portuguese equivalent exists. Acronyms in Portuguese do not take a plural form — never add 's' to make one plural. If the source already provides a spelled-out expansion, translate it; do not add one the source lacks.
  - *Source:* "Multiple CDs" → *Target:* "Vários CD" (no plural 's' on acronym)

## Date And Time

- **Follow European Portuguese Date and Time Format**: Use the system locale standard for date and time in software strings. When displaying actual time, use the 24-hour format. Write dates with the weekday spelled out in full. Keep 'AM' and 'PM' in English only when the string is itself a 12-hour time-format label (the actual text being displayed).
  - *Source:* "Monday, September 6, 2013 / 4 PM" → *Target:* "Segunda‑feira, 6 de setembro de 2013 / 16:00"

## Measurements

- **Do Not Convert Units; Add Non-Breaking Space Before Unit Symbol**: Do not convert measurement units. In instructional text where localization is meaningful (e.g., distance to a device), convert to metric. Always add a non-breaking space between a numeric value and its unit symbol when space is available. Exception: no space before the percent sign.
  - *Source:* "2 GB / 34 km / 50%" → *Target:* "2 GB / 34 km / 50%"
  - *Source:* "Your modem should be no further than 35 feet from your computer." → *Target:* "O modem não deve estar a mais de 10 m do computador."

## Numerals

- **European Portuguese Number Format**: Use a comma as the decimal separator and a space as the thousands separator for numbers with five or more digits. Numbers with exactly four digits need no separator. Ordinal numbers follow a period with a superscripted 'º' or 'ª' matching the gender of the noun. Version numbers retain a period.
  - *Source:* "3.5 kg / 25,000 songs / 2,350 files / 1st / 2nd (feminine) / Version 2.0" → *Target:* "3,5 kg / 25 000 músicas / 2350 ficheiros / 1.º / 2.ª / Versão 2.0"

## Addresses

- **Use Locally-Appropriate Placeholder Names and Portuguese Address Format**: Replace English placeholder names with locally-appropriate Portuguese names. For sample addresses, use the European Portuguese format with postcode (NNNN-NNN) preceding the city name. Example format: `Rua da Ponte Direita, n.º 3, r/c esq., 1600-123 Cidade`.

## Special Characters

- **Use the Single Ellipsis Character**: Always use the single ellipsis character (…) instead of three individual dots. The single character counts as one character for space calculations and is interpreted correctly by assistive technologies.
  - *Source:* "Loading..." → *Target:* "A carregar…" (single ellipsis character)

- **Non-Breaking Hyphen and Non-Breaking Space in Product Names**: Use non-breaking hyphens in hyphenated words such as 'palavra‑passe' and clitic pronoun forms to prevent translineation errors. Use non-breaking spaces within multi-word product or service names (Apple TV, iPod touch, or the app's own multi-word names) and before UI path arrows (>).
  - *Source:* "password / Apple TV / Settings > General" → *Target:* "palavra‑passe / Apple TV / Definições > Geral"

- **Keyboard Keys — Capitalized; Plus Sign for Shortcuts**: Translate keyboard key names using the established Portuguese forms, capitalizing each key name regardless of source capitalization. In shortcut lists, join keys with a plus sign (+). In running prose, use 'mantenha premida a tecla X' constructions.
  - *Source:* "Command-Option-click" → *Target:* "Comando + Opção + clique"
  - *Source:* "Hold the Option key while dragging…" → *Target:* "Mantenha premida a tecla Opção enquanto arrasta…"

## Grammar

- **Avoid Incorrect Use of 'seu/sua' for Non-Possessive Reference**: 'Seu' and 'sua' indicate possession and should only be used when something genuinely belongs to a grammatical person. When referring back to a previously mentioned noun without implying ownership, use 'respetivo/respetiva' instead.
  - *Source:* "The XYZ Update fixes issues. Its installation is recommended." → *Target:* "A Atualização do XYZ corrige problemas. A respetiva instalação é recomendada." (not: a sua instalação)

- **Prepositions Are Idiomatic — Do Not Translate Literally**: Prepositions must follow Portuguese grammar rules rather than mirror the source. In particular, 'for' often maps to 'a' rather than 'para', and 'to' in directive contexts depends on the governing verb. Restructuring the target sentence significantly is often necessary and correct.
  - *Source:* "recommended for all users / restore iPod to factory settings" → *Target:* "recomendado a todos os utilizadores / restaurar o iPod com as definições de fábrica"

- **Capitalization: Sentence Case Only**: In Portuguese, only the initial letter of a sentence is capitalized as a general rule. Exceptions are app and utility names (Utilitário de Discos, Definições do Sistema) and names of legal documents (Política de Privacidade, Termos e Condições). Section headings and common nouns are not capitalized.
  - *Source:* "Read Before You Install " → *Target:* "Ler antes de instalar"

## Punctuation

- **Use Curly Quotation Marks; Period Outside Closing Quote**: Use curly (typographic) quotation marks, as in the source. The period always goes outside the closing quotation mark. Do not use double periods when an abbreviation ends a sentence.
  - *Source:* "The field includes the word \u201Cbundle.\u201D" → *Target:* "O campo inclui a palavra \u201Cpacote\u201D." (period outside closing quote)

- **Em-Dash Replaced by En-Dash**: The em-dash (—) is used only in Portuguese literature to introduce dialogue. Replace it with an en-dash (–) preceded by a non-breaking space and followed by a regular space. Never substitute a plain hyphen where a non-breaking hyphen should be used.
  - *Source:* "Settings — Overview" → *Target:* "Definições – Visão geral"

- **UI References — Quotation Marks**: Use quotation marks around a UI item name only where intelligibility could otherwise be compromised. App and utility names are always capitalized and do not require quotation marks. Quotation marks are also not needed when specifying a UI path.
  - *Source:* "Tap Delete." → *Target:* "Toque em \u201CApagar\u201D."
  - *Source:* "Settings > General > Accessibility" → *Target:* "Definições > Geral > Acessibilidade" (no quotes in UI path)

## Interface Elements

- **Button Labels and Command Names — Infinitive Form**: Translate button labels and menu command names using the infinitive form of the verb. Option names (checkboxes, radio buttons) also use the infinitive, begin with an uppercase letter, and never end with a full stop. Menu names that are nouns should remain as nouns.
  - *Source:* "Open Recent / Print / Cancel / File" → *Target:* "Abrir documento recente / Imprimir / Cancelar / Ficheiro"

- **Tooltips — Sentence Style, Infinitive, Closing Full Stop**: Tooltips should be well-formed Portuguese sentences beginning with an uppercase letter and ending with a full stop, regardless of whether the source has one. Use the infinitive form. Purely descriptive single-word or phrase tooltips do not require a full stop.
  - *Source:* "Create a new file." → *Target:* "Criar um novo ficheiro."
  - *Source:* "Color picker" → *Target:* "Seletor de cores" (no full stop — descriptive)

- **Undo/Redo strings**: Strings that appear under Edit (menu bar) and refer to actions that can be undone (or redone). When translating these strings, the infinitive is used and the first letter of the action to undo/redo should be capitalized.
  - *Source:* "Undo Hide Location / Redo Hide Location" → *Target:* "Desfazer Ocultar localização / Refazer Ocultar localização"

## Variables

- **Preserve and Reorder Variables Correctly**: Variables must be kept exactly as in the source. Never add a new variable to a translation. When reordering is required, use positional notation (%2$@ %1$@). Do not change a period to a comma inside a numeric format specifier (e.g., %.1f GB) — the decimal separator is handled by the software. In plural-variant strings, variables may be added or removed for grammatical reasons.
  - *Source:* "%.1f GB" → *Target:* "%.1f GB" (do not change period to comma)

## Diversity And Inclusion

- **Prefer Gender-Neutral Phrasing**: Prefer gender-neutral phrasing wherever possible; when a gendered form would otherwise be needed, reword to avoid it.
  - *Source:* "Welcome" → *Target:* "Boas-vindas" (gender-neutral, instead of "Bem-vindo/Bem-vinda")
- **Put People First When Referring to Disability**: Use people-first language — refer to individuals as people before mentioning any disability, and focus on what people can do, not on what they can't.
  - *Source:* "person in a wheelchair" → *Target:* "pessoa que usa cadeira de rodas"

## Style

- **Standardized translations**: Standardized translations are somewhat similar to established terminology. Certain sentences will always be translated consistently the same way. The usage of consistent translations for repetitive text phrases is recommended.
  - *Source:* "More Info / Learn More / Make sure that … " → *Target:* "Informação adicional / Saiba mais / Certifique‑se de que…"

- **What’s New, Welcome and Store texts**: These texts should be clear and concise. Addressing the user directly should be avoided. In these types of files, bulleted lists are normally used to list items (e.g. new features, bug fixes) without a specific order. In this case, bullet point items should be treated as “standalone” items and begin with an uppercase letter and end with a full stop, regardless of whether they are preceded by an introductory sentence ending or not in a colon “:”. When an introductory sentence ending in a colon and each subsequent bullet point item form a grammatical unit, each item should begin with a lowercase letter and end with a semi-colon “;”. A full stop is used only on the last item of the list.
  - *Source:* "This update adds the following features:
• Introduces support for AirPods Pro" → *Target:* "Esta atualização inclui as seguintes melhorias:
• Suporte para AirPods Pro."
  - *Source:* "This update:
• Addresses an issue that could prevent a device from ringing or vibrating for an incoming call
• Resolves an issue where notifications may not be received on Apple Watch" → *Target:* "Esta atualização:
• resolve um problema que podia impedir um dispositivo de tocar ou vibrar ao receber uma chamada;
• resolve um problema que podia fazer com que não fossem recebidas notificações no Apple Watch."

