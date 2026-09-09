# Korean (ko) — Software String Localization Style Guide

## Escaping Curly Quotes And Apostrophes

- **Escape every curly glyph inside a string**: Korean uses curly double quotation marks “ (\u201C) and ” (\u201D) for dialogue and direct quotes, and curly single quotation marks ‘ (\u2018) and ’ (\u2019) for UI element references or emphasis.
  - *Source:* "Tap \u201CPrivacy\u201D." → *Target:* "\u2018개인정보 보호\u2019를 탭하십시오."

## Tone And Voice

- **Smart but Casual; Verb Ending Based on Sentence Function**: Choose the verb ending based on the sentence's function. For descriptive sentences (stating facts), use the formal declarative form ~ㅂ니다 (합쇼체). For imperative sentences (instructing the user), use the standard polite imperative ~세요 (해요체) or ~하십시오. 해요체 is preferred for navigation UI such as Maps and VoiceOver navigation, and for friendly contexts like 'What's New' onboarding screens and Apple Watch achievement notifications. 하십시오체 is preferred in highly formal legal disclaimers or system warnings where an authoritative tone is required.
  - *Source:* "Start enjoying these features today." → *Target:* "지금 바로 이 기능을 즐겨 보세요."

## Addressing Users

- **Addressing 'You/Your' as 사용자**: Render 'user', 'you', and 'your' as 사용자 in standard software strings. 사용자 may be omitted when context makes the subject obvious. Use 여러분 for a warmer, more personal tone in marketing-style text. Do not use 당신 as a pronoun for the user. Exception: when 'you/your' is addressed from the perspective of another user (not this app)—for example, in a message a user is composing to send to someone else—당신 is acceptable.
  - *Source:* "This %@ account has already been added to your Apple Watch." → *Target:* "이 %@ 계정이 이미 사용자의 Apple Watch에 추가되어 있습니다."
  - *Source:* "You're added as my Account Recovery contact." → *Target:* "당신을 제 계정 복구 연락처로 추가했습니다."

## Abbreviations

- **Keep English Abbreviations Unless a Korean Form Is Standard**: Do not create Korean abbreviations for UI strings. Keep familiar English abbreviations unchanged. If the source provides an explanation, translate it; do not add one the source doesn't include. A small number of abbreviations have required Korean forms, such as AM/PM → 오전/오후 and US → 미국.
  - *Source:* "AM/PM" → *Target:* "오전/오후"
  - *Source:* "US" → *Target:* "미국"

## Acronyms

- **Handle Acronyms**: Do not translate acronyms unless there is a standard localized equivalent. If the source spells out the acronym (e.g. the full phrase in parentheses), translate that; do not add an expansion the source doesn't provide.
  - *Source:* "DRM (Digital Right Management)" → *Target:* "DRM (디지털 저작권 관리)"

## Date And Time

- **Korean Date and Time Format**: Add Korean date units and adjust word order to match the system standard. Express time with Korean AM/PM (오전/오후) before the numeral. Dates follow the YYYY년 MM월 DD일 pattern.
  - *Source:* "4:44 PM" → *Target:* "오후 4:44"
  - *Source:* "2010/6/14" → *Target:* "2010년 6월 14일"

## Measurements

- **Inch Localization for Product Names vs. Display Size**: When 'inch' appears as part of a product name (e.g., iPad Pro 13-inch), remove it from the Korean translation. When it describes display size in a spec or marketing context, convert the figure to centimeters and replace 'inch' with 'cm' (this matches Apple's shipped Korean specs, which express display sizes in cm, e.g. 33.0cm).
  - *Source:* "iPad Pro 13-inch" → *Target:* "iPad Pro 13"
  - *Source:* "13-inch (diagonal)" → *Target:* "33.0cm(대각선)"

## Names And Addresses

- **Use Street Name Address Format (도로명주소)**: A Korean address follows the street name address format (도로명주소) introduced in 2014, not the older parcel number format (지번주소): city/province, district, then road name and building number, with an optional legal dong in parentheses (e.g. "서울특별시 강남구 영동대로 517 (삼성동)"). Korean postal codes consist of 5 digits with no spaces. Foreign addresses are kept as-is.

## Numerals

- **Arabic Numerals Are Not Translated; Spell Out Korean Numerals When Required**: Do not translate Arabic numerals (1 stays 1). When numbers are written out as words in the source (one, two, three), you are allowed to localize them into Korean spoken-number form (하나, 둘, 셋) or Sino-Korean form (일, 이, 삼) as appropriate to the context.
  - *Source:* "You\u2019ll see your Year in Review as soon as you have at least 1 book marked as finished." → *Target:* "최소 1권의 책을 읽기 완료로 표시하면 \u2018한 해 돌아보기\u2019를 확인할 수 있습니다."

## Special Characters

- **Always Use the Ellipsis Character, Not Three Periods**: Use the single ellipsis character (…, typed Option-;) everywhere. Three individual periods are not equivalent visually or functionally and should not be used. Unify any inconsistent source usage to the ellipsis character.
  - *Source:* "Loading..." → *Target:* "로드 중…"

## Grammar

- **DNT Terms: Use Singular Capitalized Form for Software Feature Names**: When a software feature-name DNT (e.g., 'Live Photo/Live Photos') appears in both singular and plural forms in the source, use the singular capitalized form consistently in translation.
  - *Source:* "Save %@ Live Photos" → *Target:* "%@장의 Live Photo 저장"

- **DNT Terms: Follow the Singular/Plural Forms in the Source for Hardware DNT Terms**: If a hardware DNT appears in both singular and plural forms, follow the form used in the source (e.g., AirPod/AirPods).
  - *Source:* "Select your AirPods" → *Target:* "AirPods 선택"

- **DNT Terms: Keep Plural Form for DNT Terms in Plural Forms in All Instances**: If a DNT only has plural form, keep this Plural form in all instances, e.g. iTunes Extras, iTunes, AirTunes, iBooks, Beats, Apple Ads, etc.

- **Proper Korean Suffixes After DNT Terms**: Attach Korean grammatical suffixes to DNT terms based on the Korean phonetic pronunciation of the transliteration. For example, 'HomeKit' is pronounced 홈키트, so the correct forms are HomeKit가, HomeKit는, HomeKit를, HomeKit로.
  - *Source:* "CarPlay.app uses homekit for dashboard features" → *Target:* "CarPlay.app은 대시보드 기능에 HomeKit를 사용합니다."

- **Proper Korean Suffixes After DNT Terms (Plural)**: Phonetic pronunciation of hardware DNT terms in plural form should follow the singular form. Make sure it’s followed by the correct postpositional particles (e.g. Both “AirPod” and “AirPods” will be pronounced “에어팟”)
  - *Source:* "Adjust the duration required to press and hold on your AirPods." → *Target:* "AirPods을 길게 누를 때 필요한 시간을 조절합니다."

## Capitalization

- **DNT Terms: Match the Source if DNT Terms in All Caps**: If a DNT term is all caps in the source, keep all caps in translation.
  - *Source:* "DIGITAL CROWN" → *Target:* "DIGITAL CROWN"

- **DNT Terms: Use Capitalized Form Consistently**: Use capitalized form consistently, if a DNT term is used inconsistently in the source.
  - *Source:* "wifi / wi-fi / Wifi / WiFi / Wi-Fi" → *Target:* "Wi-Fi"

## Punctuation

- **Using a Non-breaking Space for DNT with Two or More Words**: DNT terms comprised of two or more words should stay together for better readability. To this end, add a non-breaking space as necessary between words in DNT terms.
  - *Source:* "Apple Watch" → *Target:* "Apple Watch" (non-breaking space between the words)

- **Period Use with Korean Sentences**: Add a period when the Korean translation ends with a complete verb form (~다, ~시오). Omit the period when the translation ends with a noun or noun-form suffix (~하기, ~ㅁ), even if the English sentence had a period.
  - *Source:* "Please Try Again" → *Target:* "다시 시도하십시오."

- **Do Not Use Semicolons in Korean**: Korean does not use semicolons. Replace a source semicolon with a period, a comma, or omit it entirely, choosing the approach that produces the most natural Korean sentence.
  - *Source:* "Only the table you're currently in is affected; other tables will still use the setting." → *Target:* "현재 사용 중인 표에만 적용됩니다. 다른 표는 기존 설정을 계속 사용합니다."

- **Colon at End of a Complete Sentence Becomes a Period**: If a Korean sentence ends with a complete verb and the source ends in a colon, replace the colon with a period in the translation. A colon may be kept if the sentence ends in a noun or noun-form suffix.
  - *Source:* "Please refer to the Apple support page: www.apple.com/compatibility" → *Target:* "Apple 지원 페이지(www.apple.com/compatibility)를 참조하십시오."

- **Korean Quotation Mark Style: Curly Quotes**: Use curly double quotation marks for dialogue and direct quotes, and curly single quotation marks for UI element references or emphasis. Never use straight typewriter quotes.
  - *Source:* "You can review this information by going to Settings on your iOS device, tapping Privacy, tapping Analytics and looking under Analytics Data." → *Target:* "관련 정보는 iOS 기기에서 설정으로 이동하여 \u2018개인정보 보호\u2019, \u2018분석\u2019을 차례로 탭한 다음 \u2018분석 데이터\u2019에서 확인할 수 있습니다."

- **No Space Before the Honorific Suffix 님**: Although standard Korean grammar places a space before 님, do not insert one in translations. This prevents text clipping and orphan-character issues and is standard practice in the Korean IT industry.
  - *Source:* "%@ has joined this chat." → *Target:* "%@님이 이 대화방에 들어왔습니다."

## Interface Elements

- **Button and Menu Names: Change Verbs to Noun Form**: When a button, menu item, command, or option name contains a verb, convert it to the corresponding Korean verbal nouns (Sino-Korean or derived nouns, gerund form) in the translation when applicable.
  - *Source:* "Add" → *Target:* "추가"
  - *Source:* "Open" → *Target:* "열기"
  - *Source:* "Don't use" → *Target:* "사용 안 함"

- **Tooltip Style: ~합니다. with Full Stop**: Tooltips should use the ~합니다 verb form and end with a full stop, even if the source does not. Keep the translation clear and brief. Look for the cue from the engineering comment mentioning “tooltip”.
  - *Source:* "Show contents in grid view" → *Target:* "목차를 격자 보기로 표시합니다."

## Variables

- **Variable Orders**: When the source string contains two identical variables (%@ %@) and the order needs to change in the target language, the variables can be changed to %1$@ and %2$@ to indicate the original variable order.
  - *Source:* "%@ near %@" → *Target:* "%2$@ 근처의 %1$@"

## General Advice

- **Age References: Do Not Use 만 Prefix**: As of June 2023, Korean officially adopted the international age counting system, so do not add the 만 prefix before age numbers in translations. Translate ages directly without 만, and remove 만 from any existing strings that previously used it for international age clarification.
  - *Source:* "The Blood Oxygen app is available for users age 18 and above." → *Target:* "혈중 산소 앱은 18세 이상의 사용자를 대상으로 합니다."

## Diversity And Inclusion

- **Avoid Violent, Oppressive, and Ableist Language**: Do not translate technology terms using inherently violent words (kill, hang) or terms describing oppressive relationships (master/slave). Avoid 제거 when referring to a person; use 삭제 instead. Korean has no gendered pronouns by default—avoid imported gendered forms like 그녀 where gender-neutral language suffices.
  - *Source:* "Remove Yourself?" → *Target:* "사용자 본인을 삭제하겠습니까?"

## Terminology

- **Application vs. App Terminology**: 'Application(s)' should be translated as 응용 프로그램. 'App(s)' should always be translated as 앱 in singular form. The term 'OK' translates as 확인 (not 승인 as in earlier usage), 'Document' as 문서 (not 도큐멘트), and 'Passkey' as 패스키 (not 암호키).
  - *Source:* "App" → *Target:* "앱"
  - *Source:* "Application" → *Target:* "응용 프로그램"

## Translation Style

- **Use Active Voice and Direct Sentence Structure**: Prefer active voice over passive voice when context allows and meaning is preserved—it makes the actor of the action clear and the sentence more direct. For call-to-action sentences, prefer Object > Verb structure that presents the action directly (e.g., '이 팁을 활용하여 보세요') over indirect framing (e.g., '저장을 위해 이 팁을 보세요').
  - *Source:* "Face ID will be required to open this app." → *Target:* "이 앱을 열려면 Face ID가 필요합니다."

## Standardized Translations

- **Welcome Translations**: Use the standardized translation for 'Welcome' based on context: '~ 시작하기' for software menus/titles and '~의 사용을 환영합니다.' for phrases.
  - *Source:* "Welcome to Game Center" → *Target:* "Game Center 시작하기"
