# Simplified Chinese (zh-Hans) — Software String Localization Style Guide

## Tone And Voice

- **Smart but Casual Tone**: The tone should be direct, friendly, and closer to formal than informal, but never stiff or overly rigid. Avoid trendy slang and keep a neutral, descriptive style. Always prioritize capturing the meaning of the message over literal word-for-word translation.
  - *Source:* "To make a great iOS app, you need to learn and do many things." → *Target:* "开发优秀的iOS App，需要大量的学习和实践。"

## Addressing Users

- **Use Informal 你 for All Software**: Address users with the informal 你 across all software. Do not translate every instance of 'you' or 'your' if the Chinese reads naturally without it.
  - *Source:* "You can sign in with your Apple ID." → *Target:* "你可以使用 Apple ID 登录。"

## Abbreviations

- **Localize Common Abbreviations, Keep Technical Ones**: Do not use abbreviations in software unless absolutely necessary. Identifiers like ID, URL, and PPP stay in English. Month, weekday, and time abbreviations (Jan., Sun., AM/PM) should be localized. Watch for context-dependent abbreviations like Min (minutes vs. minimum). The abbreviation vs/vs./v.s. should be kept in English following source punctuation.
  - *Source:* "BCC" → *Target:* "密送"
  - *Source:* "Lakers vs. Chicago" → *Target:* "湖人队 vs. 芝加哥队"
  - *Source:* "Min (for Minimum)" → *Target:* "最小"
  - *Source:* "Min (for Minutes)" → *Target:* "分/分钟"

## Acronyms

- **Retain English Acronyms Unless a Standard Chinese Equivalent Exists**: Keep acronyms in English when their meaning is apparent to users (e.g., SIM). Use Chinese for terms where a well-known standard translation exists (e.g., TV to 电视, HD to 高清). If the source pairs an acronym with a spelled-out form, translate that form; don't add an expansion the source doesn't have.
  - *Source:* "TV" → *Target:* "电视"

## Date And Time

- **Follow System Standard for Date and Time**: Software date and time formats must follow the system locale standard. When a date and weekday appear together in a standalone context (e.g., a status bar), add a space between the two elements.
  - *Source:* "Wednesday, August 28, 2020" → *Target:* "2020年8月28日 星期三"

## Measurements

- **Do Not Convert Measurements**: Do not convert imperial measurements to metric in software strings. Never use the inch symbol as an abbreviation.
  - *Source:* "minimum separation distance of 8 inches (20 cm)" → *Target:* "至少8英寸（20厘米）的距离"

- **Use English Symbols for Technical Units**: For units with long Chinese names, retain the English symbol or abbreviation. Units including KB, MB, GB, Hz, kHz, MHz, dB, kbps, Mbps, Gbps, and others do not need to be localized when they appear as abbreviations.
  - *Source:* "%@ hrs %@ mins (at %@ kB/s)" → *Target:* "%@小时%@分钟（速度：%@ kB/秒）"

## Names And Addresses

- **Reverse Address Order to Follow Chinese Convention**: Chinese addresses go from largest to smallest unit (Country, Province, City, District, Street, Building, Room).
  - *Source:* "19 Sanlitun Road, Chaoyang, Beijing, China" → *Target:* "中国北京市朝阳区三里屯路19号"

## Numerals

- **Use Arabic Numerals for Technical Content**: Technical specifications, dates, currencies, speeds, and product generation numbers use Arabic numerals.
  - *Source:* "Apple TV 3rd Generation" → *Target:* "Apple TV（第3代）"

- **Localize Approximate Numbers in Natural Chinese**: Approximate numbers expressed as a range or estimation in English (e.g., '5 or 6 minutes', 'a few hundred') read more naturally in Chinese using Chinese numerals (五六分钟, 几百). This applies only to approximate quantities; exact numbers with units (e.g., 2 分钟, 5 GB) keep Arabic numerals.
  - *Source:* "5 or 6 minutes" → *Target:* "五六分钟"

## Grammar

- **Use 两 Instead of 二 Before Measure Words**: When the number two is followed by a Chinese measure word (量词), use 两 instead of 二. This is a grammatical rule in Mandarin Chinese.
  - *Source:* "two restaurants" → *Target:* "两家餐馆"

- **Drop Plural -s from English Loan Words in Chinese**: Chinese has no plural inflection. When English terms or acronyms appear in Chinese text, drop the trailing -s or -es and use a Chinese quantity modifier (such as 所有 or 多个) if needed. Do not drop the -s from terms like AirPods, iTunes, or iBooks unless the source itself uses the singular form.
  - *Source:* "All iPads" → *Target:* "所有iPad"
  - *Source:* "CDs, DVDs, and iPods" → *Target:* "CD、DVD和iPod"

- **Convert Passive Voice to Active Where Natural**: Passive constructions can be rendered with 被, 由, 让, 受, etc., but it is often better to identify the logical subject and rewrite as an active sentence. Only use 被 when it genuinely improves clarity.
  - *Source:* "When an open log is updated:" → *Target:* "更新打开的日志时："

- **Add Measure Words After Number Variables**: When a placeholder variable represents a number, always insert the appropriate Chinese measure word (量词) between the variable and the following noun. The correct measure word depends on context.
  - *Source:* "%d podcasts" → *Target:* "%d个播客"

## Special Characters

- **Localize & Only with Chinese Text**: The ampersand used alongside untranslated English text should be kept as-is. When it connects localized Chinese terms, translate it as 与.
  - *Source:* "Terms & Conditions" → *Target:* "条款与条件"

## Punctuation

- **Use Full-Width Chinese Punctuation**: Convert half-width punctuation to full-width Chinese equivalents where applicable: commas (，), periods (。), semicolons (；), colons (：). Use the caesura sign 、 to separate list items. Colons stay half-width in time and IP address contexts. When text consists entirely of Latin characters, keep half-width punctuation (e.g., parentheses around English-only content). No punctuation mark (except opening brackets) should appear at the start of a line.
  - *Source:* "#1# album, #%li# songs" → *Target:* "#1#张专辑，#%li#首歌曲"
  - *Source:* "Choose an iPad, iPhone or iPod touch:" → *Target:* "请选择iPad、iPhone或iPod touch："

- **Ellipsis Must Be a Single Unicode Character**: Always use the ellipsis character rather than three separate periods.
  - *Source:* "Add To…" → *Target:* "添加到…"

## Interface Elements

- **Enclose UI Element Names in Quotation Marks When Referenced**: When button names, command names, menu names, and option names are quoted in software strings, enclose the translation in Chinese curly double quotation marks “ (\u201C) and ” (\u201D), not straight ASCII quotes. Do not add quotation marks inside menus unless the source includes them.
  - *Source:* "Tap \u201CAdd To\u201D to save the photo." → *Target:* "轻点\u201C添加到\u201D以保存照片。"
  - *Source:* "Choose File > Save." → *Target:* "选取\u201C文件\u201D>\u201C保存\u201D。"

## Trademarks And Product Names

- **Do Not Translate Apple Trademarks and Product Names**: Trademarks, trademarked slogans, and Apple product names must remain in English. The word Apple itself is DNT; however, the Apple menu item (the menu in the upper-left corner) should be translated as 苹果菜单.
  - *Source:* "Sign in with Apple" → *Target:* "通过Apple登录"

- **Foreign Company and Service Names Generally Stay in English**: Names of overseas companies, services, and brands generally remain in English in zh-Hans content. When a well-established Chinese name exists and is more familiar to local users, the localized form may be used at your discretion.
  - *Source:* "Search in Google" → *Target:* "Google搜索"
  - *Source:* "Currency data provided by Yahoo Finance" → *Target:* "货币数据由Yahoo Finance提供"

- **App and Service Localization**: Apple app and service name localization is highly context-dependent. (1) App names (the system app/icon on the device) are often fully localized: Maps → 地图, Books → 图书, Music → 音乐. (2) Service names (Apple's branded service offering) generally stay in English: Apple Music, Apple TV+, Apple Pay. (3) The same English string can take different translations depending on whether it refers to the app or the service.
  - *Source:* "Subscribe to Apple Music." → *Target:* "订阅Apple Music。"
  - *Source:* "Open Music to play your library." → *Target:* "打开\u201C音乐\u201D播放你的资料库。"
  - *Source:* "Maps" → *Target:* "地图"
  - *Source:* "Books" → *Target:* "\u201C图书\u201DApp"

## Variables

- **Preserve Variable Format and Count Exactly**: Keep every runtime variable (%@, %d, %1$@, etc.) in the translation with the same format as the source. Never change %@ to %e or similar. Variables may be reordered but must then be numbered (e.g., %1$@, %2$@). The count of variables must match the source exactly.
  - *Source:* ""%d or more"" → *Target:* ""%d个或更多""

## Diversity And Inclusion

- **Use People-First Language for Disability**: Describe people with disabilities as people first. Prefer 残障 over 残疾, and avoid 残废 or 残缺. Do not use terms like 受害者 or language that frames disability as inspiring or tragic. Use 非残障人士 or 健全人 for people without disabilities; never use 正常人, 一般人, or 普通人.
  - *Source:* "The blind" → *Target:* "视障人士 / 有视觉障碍的人"
