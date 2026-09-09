# Japanese (ja) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual Tone**: Write in a tone that is closer to formal than informal, but never stiff or overly academic. Avoid trendy slang; use a neutral, descriptive style. Prefer Japanese terminology where possible, even when users commonly say the English word.
  - *Source:* "You may have to reinstall some of the applications you transfer." → *Target:* "転送するアプリケーションによっては、再インストールが必要なものもあります。"

- **Translation of 'Try again'**: When translating the common UI instruction "Try again", use "やり直してみてください". Do not use "やり直してください" or "もう一度お試しください", as "やり直してみてください" better conveys the intended nuance.
  - *Source:* "Try again later." → *Target:* "あとでやり直してみてください。"

## Addressing Users

- **Omit 'You' / 'Your' When Context Is Clear**: In Japanese it is natural to drop the subject. Omit 'you' and 'your' unless the sentence must explicitly distinguish one user from another. When disambiguation is needed, use ユーザ（の）, あなた（の）, 自分(の), or この.
  - *Source:* "Enter your password" → *Target:* "パスワードを入力してください"
  - *Source:* "on your iPhone" → *Target:* "iPhone上"
  - *Source:* "This iPhone is linked to your Apple Account so no one else can use it" → *Target:* "このiPhoneはあなたのApple Accountに関連付けられているため、ほかの人は使用できません。"

- **Minimize and Localize Pronoun Usage**: Directly translating English pronouns often results in unnatural text. Omit pronouns if context is clear. For third-person (he/she/they), avoid 彼/彼女; use descriptive nouns like ユーザ, 連絡先, この人, or the person's name. For first-person (I/we), avoid casual terms like 僕/俺; if strictly necessary, use the standard 私 or 私たち.
  - *Source:* "You should change the passwords and passkeys for accounts you no longer want them to have access to." → *Target:* "この人にアクセスして欲しくないアカウントのパスワードとパスキーを変更する必要があります。"

## Special Characters

- **No-Break Space for Specific Apple Product Names**: Always use NO-BREAK SPACE within the following terms to prevent them from wrapping across two lines: Apple ID, Apple Account, Face ID, Touch ID, Optic ID, Apple TV, Apple Pay, Apple Cash, Apple Card, iTunes U, Vision Pro.
  - *Source:* "Set up Apple Pay" → *Target:* "Apple Payを設定"

- **Conditional No-Break Space for Other Apple Terms**: For store names (e.g., App Store), Apple service names (e.g., Apple Music), and other Apple product names (e.g., Apple Watch), follow the English source text. If the source uses a NO-BREAK SPACE, use it in the translation. If the source uses a regular space, use a regular space. Exception: You may use a NO-BREAK SPACE if a regular space would cause an awkward line break.
  - *Source:* "Open the App Store" → *Target:* "App Storeを開く"

## Grammar

- **Conjunctions: 'and' and 'or'**: Use 'と' as the default translation of 'and' between nouns. Use 'および' in formal enumerations or with three or more items. For 'or', prefer 'または'; use 'あるいは' when the conjunction is nested. Do not use 'もしくは'.
  - *Source:* "Display & Brightness" → *Target:* "画面表示と明るさ"
  - *Source:* "Forgot Apple Account or Password?" → *Target:* "Apple Accountまたはパスワードをお忘れですか?"
  - *Source:* "Restoring ringtones, media, and files" → *Target:* "着信音、メディア、およびファイルを復元中"

- **Avoid Inanimate Subjects (無生物主語)**: Inanimate subject is to be avoided. Omit the inanimate subject or rephrase.
  - *Source:* "iPhone can help during an Emergency" → *Target:* "緊急時にiPhoneが役に立ちます"

## Numerals

- **Arabic Numerals; Respect Thousand Separators from Source**: Use single-byte Arabic numerals. Add or omit the thousand separator (,) based on whether the English source uses it. Use Japanese numerals only when the number is part of a fixed idiom or set phrase.
  - *Source:* "1,000,000 songs" → *Target:* "1,000,000曲"
  - *Source:* "1000 Mbps/Half Duplex" → *Target:* "1000 Mbps/半二重"

## Names And Addresses

- **Honorific Suffix さん After Person-Name Variables**: Add the honorific suffix 'さん' directly after any variable that will be replaced by a person's name at runtime. Do not add it after variables that represent device names, email addresses, or phone numbers. If a variable could represent either a name or an email, prefer adding さん.
  - *Source:* "Received item from %1$@." → *Target:* "%1$@さんから1項目を受信しました。"

## Measurements

- **Unit Handling: Spell Out or Keep Per Context**: Do not convert imperial measurements to metric. For abbreviated units, keep them as-is. Translate fully spelled-out units into Japanese (e.g., 'inch' → インチ). Exception: time abbreviations such as 'h', 'm', 's' should be translated to 時間, 分, 秒 unless space is constrained.
  - *Source:* "h" → *Target:* "時間"
  - *Source:* "inch" → *Target:* "インチ"

## Interface Elements

- **App Name Quoting Rules**: Quote the following translated app names with curly double quotation marks “ (\u201C) and ” (\u201D) because they are common nouns: “カレンダー”, “カメラ”, “時計”, “連絡先”, “ファイル”, “探す”, “ヘルスケア”, “ホーム”, “メール”, “マップ”, “メッセージ”, “ミュージック”, “メモ”, “電話”, “写真”, “ポッドキャスト”, “リマインダー”, “設定”, “ショートカット”, “株価”, “ヒント”, “翻訳”, “天気”. Do not quote DNT names.
  - *Source:* "Video saved to Photos" → *Target:* "ビデオは\u201C写真\u201Dに保存されました"

- **Button and Command Names: Noun Phrase Without する**: For buttons, command names, menu names, and option names, use a noun or noun phrase (O＋を＋V) and omit the trailing 'する'. One exception is '同意する', which must keep する because its counterpart '同意しない' requires it.
  - *Source:* "Delete" → *Target:* "削除"
  - *Source:* "Show All" → *Target:* "すべてを表示"

- **Keyboard Shortcuts: Spell Out Key Names**: Refer to modifier keys using lowercase English letters followed by キー (e.g., commandキー, optionキー), not by their symbols. Use a single-byte '+' to join keys in shortcut combinations.
  - *Source:* "Press Command-Option-F5" → *Target:* "Command+Option+F5キーを押します"

- **Translation of '"%@" would like to xxx'**: When translating strings formatted as '"%@" would like to xxx' (where "%@" is an inanimate subject like an app), use the passive voice structure: "\u201C%@\u201Dから、[action]を求められています。". Do not use active voice structures like "\u201C%@\u201Dが[action]を求めています。"
  - *Source:* "\u201C%@\u201D would like to access your contacts." → *Target:* "\u201C%@\u201Dから、連絡先へのアクセス権を求められています。"

## Variables

- **Preserve Variables and Add Positional Markers When Reordering**: Never alter variable tokens such as %@, %d, or %lu. If multiple variables must be reordered to produce natural Japanese, add positional markers (e.g., %1$@, %2$@) to every variable in the string. Use the %[tt]@ format when a variable holds a Japanese App name such as “探す”  that needs automatic quoting.
  - *Source:* "Leave now: It will take %@ to get to %@ on %@ by car." → *Target:* "今出発: %2$@まで車で%3$@を通って%1$@かかります。"

## Orthography

- **Katakana**: Half-width katakana should never be used.
  - *Source:* "Software Update" → *Target:* "ソフトウェアアップデート"

- **Alphabets**: Full-width Latin letters should not be used.
  - *Source:* "iPhone" → *Target:* "iPhone"

- **Numbers**: Full-width digits should not be used.
  - *Source:* "Your Available Credit may take up to 10 business days to reflect this payment." → *Target:* "このお支払いが利用可能残高に反映されるまでに最大10日間かかる場合があります。"

- **Compound word in katakana**: KATAKANA MIDDLE DOT should not be used when writing a compound word in katakana.
  - *Source:* "Picture in Picture" → *Target:* "ピクチャインピクチャ"

- **Place name in katakana**: When writing a place name in katakana, use KATAKANA MIDDLE DOT as appropriate.
  - *Source:* "Trinidad and Tobago" → *Target:* "トリニダード・トバゴ"

- **Time format**: Use the 24-hour for time format by default. Use a single-byte colon as a separator. If the source uses 12-hour clock, then use it in the target too. Use "午前" for AM and "午後" for PM. "午前" and "午後" should be placed before the time.
  - *Source:* "4:00 am" → *Target:* "午前4:00"

- **Date format**: Use the Japanese standard date format, YYYY/MM/DD.
  - *Source:* "8/14/2025" → *Target:* "2025/8/14"

- **No Space Between English and Japanese**: A space should not be placed between English and Japanese words.
  - *Source:* "Apple Watch cellular plans." → *Target:* "Apple Watchのモバイル通信プラン"

- **Spacing Between Numbers and Units**: A single-byte space between a numeric value (or variable) and a unit should strictly follow the English source text. If the source has a space, include a space in the translation. If the source does not have a space, do not include a space.
  - *Source:* "%@ GB" → *Target:* "%@ GB"
  - *Source:* "%@GB" → *Target:* "%@GB"

## Punctuation

- **Question mark**: The full-width question mark should not be used. Instead, the single-byte one should be used.
  - *Source:* "Are you sure you want to delete %lu items?" → *Target:* "%lu項目を削除してもよろしいですか?"

- **Question mark spacing**: When QUESTION MARK is followed by another text, a space should be placed after the mark.
  - *Source:* "Are you sure you want to continue? All media, data, and settings will be erased." → *Target:* "続けてもよろしいですか? すべてのメディア、データ、および設定を消去します。この操作は取り消せません。"

- **Exclamation mark**: The full-width exclamation mark should not be used. Instead, the single-byte one should be used.
  - *Source:* "That marks 1000 Fitness+ mindful cooldowns. Amazing!" → *Target:* "これはFitness+のマインドフルクールダウン1000回の記録です。すごいです!"

- **Exclamation mark spacing**: When EXCLAMATION MARK is followed by another text, a space should be placed after the mark.
  - *Source:* "Nice job getting on the bike yesterday! Well done, %@." → *Target:* "昨日はサイクリングをがんばりましたね! よくできました、%@さん。"

- **Comma**: Except for a thousands separator, an ideographic comma should be used.
  - *Source:* "If you have multiple calling apps, you can change the default." → *Target:* "複数の通話アプリがある場合は、デフォルトを変更できます。"

- **Full stop**: Except for a decimal separator, an ideographic full stop should be used.
  - *Source:* "A request to get the car power level status for the user." → *Target:* "ユーザが車の充電状態を取得するためのリクエスト。"

- **Colon**: The full-width colon should not be used. Instead, the single-byte one should be used. When followed by text, place a single-byte space after the colon.
  - *Source:* "Replacement:" → *Target:* "置き換え:"
  - *Source:* "Arriving: %@" → *Target:* "到着: %@"

- **Parenthesis**: FULLWIDTH LEFT and RIGHT PARENTHESIS are to be used.
  - *Source:* "Shanghainese (China mainland)" → *Target:* "上海語（中国本土）"

- **Parenthesis Exception: Hardware Model Names**: While full-width parentheses are the standard, you must use half-width (single-byte) parentheses ( ) when translating hardware model names (e.g., Mac models) to prevent UI layout issues.
  - *Source:* "MacBook Air (13-inch, M5)" → *Target:* "MacBook Air (13インチ、M5)"

- **Ellipsis**: HORIZONTAL ELLIPSIS is always to be used. MIDLINE HORIZONTAL ELLIPSIS should not be used. Do not use three single-byte dots.
  - *Source:* "..." → *Target:* "…"

- **Double quotation marks**: Use curly quotes in general, i.e. LEFT/RIGHT DOUBLE QUOTATION MARK (\u201C and \u201D). Double quotation marks are typically used to refer to UI elements such as an app name, a menu item, and a button label.
  - *Source:* "Double-tap to open Settings" → *Target:* “\u201C設定\u201Dを開くにはダブルタップします"

- **Right double quotation mark spacing**: When RIGHT DOUBLE QUOTATION MARK is followed by another single-byte character, then a single-byte space should be placed after the quotation mark.
  - *Source:* "Are you sure you want to remove the selected messages from the \u201C%1$@\u201D POP server?" → *Target:* "選択したメッセージを\u201C%1$@\u201D POPサーバから削除してもよろしいですか?"

- **Greater-than sign**: When the Greater-Than Sign is used to explain the steps of UI navigation, use FULLWIDTH GREATER-THAN SIGN.
  - *Source:* "Additional Outgoing Mail Servers can be configured for Mail accounts in Settings > Apps > Mail > Accounts." → *Target:* "\u201C設定\u201D＞\u201Cアプリ\u201D＞\u201Cメール\u201D＞\u201Cアカウント\u201Dで、追加の送信用メールサーバを構成することができます。"

- **Slash sign**: Use a half-width/single-byte sign. FULLWIDTH SOLIDUS should not be used.
  - *Source:* "Parent/Guardian" → *Target:* "親/保護者"

- **Wave dash**: Use a WAVE DASH to indicate a range of values.
  - *Source:* "40-49 dB" → *Target:* "40〜49 dB"

- **Corner brackets**: LEFT CORNER BRACKET and RIGHT CORNER BRACKET should not be used in general. Instead, LEFT DOUBLE QUOTATION MARK (\u201C) and RIGHT DOUBLE QUOTATION MARK (\u201D) should be used.
  - *Source:* ""Tags" is supported in Landmarks 2.0 and later." → *Target:* "\u201Cタグ\u201DはLandmarks 2.0以降に対応しています。"

- **Corner brackets Exception: Tapbacks and Accessibility**: While double curly quotation marks (“ ”) are the standard for quoting UI elements in software, you must use corner brackets (「 」) as an exception when translating Messages Tapback reactions (e.g., 「ハート」).
  - *Source:* "You loved this" → *Target:* "あなたはこれに「ハート」と応答"

## Terminology

- **Press and hold Terminology**: "Press and hold", "Press & hold" and "Long press" should be translated as "長押し（する）" for consistency.
  - *Source:* "Press and hold the power button" → *Target:* "電源ボタンを長押しします"
