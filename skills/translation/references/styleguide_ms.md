# Malay (ms) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual Tone**: Malay translations should feel smart but casual, leaning closer to formal than informal without being stiff or overly trendy. Avoid literal word-for-word rendering of English and aim for natural-sounding Malay.
  - *Source:* "When words aren't enough, you can turn an iMessage conversation into a FaceTime video call" → *Target:* "Apabila kata-kata tidak mencukupi, anda boleh menukar perbualan iMessage menjadi panggilan video FaceTime"

## Addressing Users

- **Address Users as 'anda'**: All user-facing text must address the user with the formal 'anda'. Casual forms such as 'awak', 'kamu' or 'engkau' are only acceptable in advertisements with spoken dialogue and should be avoided.
  - *Source:* "you" → *Target:* "anda"

## Abbreviations

- **Avoid Abbreviations**: Do not shorten words through abbreviations in software. If a string is too long due to UI constraints, work around it by restructuring the phrase rather than inventing abbreviated forms.
  - *Source:* "20 MB daripada 1 GB" → *Target:* "20 MB / 1 GB (layout fix) — not '20 MB drp 1 GB'"

## Acronyms

- **Do Not Translate Industry Acronyms**: Standard technology acronyms (HD, SD, Wi-Fi, WLAN, CD, RAM) are kept as-is. When the source pairs an acronym with a spelled-out form, translate that form; don't add an expansion the source doesn't have.
  - *Source:* "Wireless Local Area Network (WLAN)" → *Target:* "Rangkaian Kawasan Setempat Wayarles (WLAN)"

## Date And Time

- **Malaysian Date and Time Format**: Use the Malaysian date order (day month year) and localized day/month names. Replace AM/PM with PG (pagi) and PTG (petang).
  - *Source:* "January 20, 2016" → *Target:* "20 Januari 2016"
  - *Source:* "AM / PM" → *Target:* "PG / PTG"

## Measurements

- **Use Metric Units with a Space**: Do not convert imperial measurements. Always insert a space between the numeric value and the unit. Temperature and currency symbols have no space; distance units do.
  - *Source:* "20 km" → *Target:* "20 km"
  - *Source:* "34°C" → *Target:* "34°C"

## Names And Addresses

- **Malaysian Address Format**: Sample names follow the source (John Doe stays as John Doe). Addresses follow Malaysian conventions: unit number and street, then postcode and city, then state and country. The Malaysian postcode (Poskod) is a 5-digit number. Example format: `25, Jalan 12/E, Taman Ria, 47300 Petaling Jaya, Selangor Darul Ehsan, Malaysia`.

## Numerals

- **Numeral Formatting**: Use a comma as the thousands separator and a full stop as the decimal separator. Always place a zero before the decimal point. Numbers below 10 may be written out in words, though digits are acceptable when the source uses them.
  - *Source:* "1,000,000 songs" → *Target:* "1,000,000 lagu"
  - *Source:* "0.09 seconds" → *Target:* "0.09 saat"

## Punctuation

- **Follow Source Punctuation**: Malay punctuation generally mirrors the source. Use the single ellipsis character (…) rather than three periods. Do not add a comma before 'dan' in a list—'dan' alone replaces ', and'.
  - *Source:* "Building Services Menu…" → *Target:* "Membina Menu Perkhidmatan…"
  - *Source:* ", and" → *Target:* "dan"

## Grammar

- **Correct Use of 'ialah' vs 'adalah'**: Use 'ialah' when 'is' links a subject to a noun. Use ‘adalah' when it links to an adjective. 'adalah' must never be followed by a verb.
  - *Source:* "A simple passcode is a %@ digit number." → *Target:* "Kod laluan yang ringkas ialah nombor %@ digit."
  - *Source:* "Argument %1$d of %2$@ is invalid." → *Target:* "Argumen %1$d daripada %2$@ adalah tidak sah."

- **Correct Use of Prepositions: 'di', 'ke', 'dari', 'daripada'**: di' precedes place nouns and is written separately. ke' indicates movement toward a location. dari' refers to a place, direction, or time origin. 'daripada' indicates a human or abstract source, and is used when removing something from a location.
  - *Source:* "iTunes Radio is not currently available in Malaysia." → *Target:* "iTunes Radio tidak tersedia di Malaysia pada masa ini."
  - *Source:* "Message from John" → *Target:* "Mesej daripada John"
  - *Source:* "Delete the files from the folder" → *Target:* "Padamkan fail daripada folder"

- **No Plural Repetition with Numerals**: When a numeral is present, do not use the Malay reduplication plural form (e.g. ‘elemen-elemen'). The numeral itself already conveys plurality.
  - *Source:* "5 elements" → *Target:* "5 elemen"

- **Use 'ia' for Abstract Entities, Not 'mereka'**: 'Mereka' refers to people. For abstract or artificial entities such as files, apps, or processes, use 'ia' or rephrase using 'ini'/'itu' to avoid using any pronoun.
  - *Source:* "The files could not be moved to the trash because they were not found" → *Target:* "Fail tidak dapat dialihkan ke sampah kerana ia tidak ditemui"

## Interface Elements

- **Sentence Capitalisation for Multi-Word UI Terms**: When a translated button or UI label becomes two or more words as a result of translation, use Sentence Caps (capitalise the first word only).
  - *Source:* "Update" → *Target:* "Kemas Kini"
  - *Source:* "Unavailable" → *Target:* "Tidak Tersedia"

- **Use Grammatically Complete Command Names**: Command names must be grammatically complete and should include full suffixes (e.g. '-kan'). Avoid dropping suffixes for brevity unless it is a documented UI space workaround. E.g. 'Tunjukkan' is correct, 'Tunjuk' only is incorrect for UI (generally)
  - *Source:* "Show All Contacts" → *Target:* "Tunjukkan Semua Kenalan"

## Terminology

- **Prefer Malay Terminology Over English Loanwords**: Use established Malay terms whenever possible, even if users in conversation might default to English. Unnecessary transliterations of terms that already have accepted Malay equivalents should be avoided. Perihalan and not Deskripsi
  - *Source:* "Group Description" → *Target:* "Perihalan Kumpulan"

## Diversity And Inclusion

- **Avoid Violent or Oppressive Technical Terms**: Do not use terms like 'matikan' (kill/turn off) for abstract entities such as apps or functions—reserve it for physical devices. Use 'nyahaktifkan' for disabling abstract features, and 'senyap' or 'redam' instead of 'bisu' for muting.
  - *Source:* "Find My iPad has been turned off." → *Target:* "Cari iPad Saya telah dinyahaktifkan."
  - *Source:* "Accessory is powered off." → *Target:* "Aksesori telah dimatikan."

## Variables

- **Preserve and Reorder Variables for Grammar**: Never alter variable tokens (e.g. %@, %1$@, %d). You may reorder numbered variables to match Malay word order, but the variable syntax itself must not be changed. Do not convert a decimal period inside a numeric variable format.
  - *Source:* "%@ %@ (first Monday)" → *Target:* "%2$@ %1$@ (Isnin pertama)"

## General Advice

- **Contextual Translation Over Literal Translation**: Always read surrounding strings to understand context before translating. Question-word translations such as 'what', 'when', 'where', and 'how' carry different Malay equivalents depending on whether they appear in a question or in a descriptive heading. E.g. what - perihal instead of apakah, when - masa instead of bila, where - tempat instead of di mana, how - cara instead of bagaimana when it's not an interrogative sentence
  - *Source:* "What is Location Services (heading, not a question)" → *Target:* "Perihal Perkhidmatan Lokasi"

- **Avoid Hanging Sentences**: Translations must be grammatically complete. Do not produce 'ayat tergantung' (hanging sentences) where a phrase is left without a proper grammatical ending. E.g.: What would you like to use? —> Apakah yang anda mahu gunakan? Instead of Yang anda mahu gunakan?
  - *Source:* "What would you like to use?" → *Target:* "Apakah yang anda mahu gunakan?"
