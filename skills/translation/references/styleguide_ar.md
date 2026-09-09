# Arabic (ar) — Software String Localization Style Guide

- **Modern Standard Arabic only**: All translations must use neutral MSA (Modern Standard Arabic) understood across all Arab countries. Translations must not be characterized by any specific country's dialect or regional vocabulary.

- **Gender-neutral imperatives via workarounds**: Avoid gendered imperative forms by using يمكنك / يمكن / يرجى / يجب instead of directly conjugated verbs. E.g., "Enable" → "يمكنك التمكين" (not "مكِّن"). Use masculine imperative only when workarounds would sound unnatural: sequential instructions, direct contextual instructions (e.g., "قرب الكاميرا من وجهك"), or sentences with multiple imperatives. For "please" phrases, consistently use "يرجى".

- **Gender with name variables**: For strings where `%@` represents a person's name, prefer a noun-based construction to avoid gendered verb conjugation. E.g., `%@ liked this photo` → `إعجاب من %@ بهذه الصورة` ✓. When a noun-based workaround is not possible, append `(ت)` to the verb: `انضم(ت) %@ إلى الدردشة` ✓.

- **Avoid "قم بـ" and "لا تقم"**: Never use the auxiliary "قم" construction — use يرجى or the direct verb instead. E.g., "Open the link" → "يرجى فتح الرابط" (not "قم بفتح الرابط"). For negative imperatives, use يجب عدم or لا + verb (not "لا تقم بـ"). For general negation, use "لن" with the original verb (not "لن تقوم بـ").

- **Minimize possessives**: Drop الخاص بك / الخاص بي unless the possessive sense is vital to complete the meaning. "Your" with device names should be removed entirely — "Go to Settings on your iPhone" → "انتقل إلى الإعدادات على iPhone" (not "على الـ iPhone الخاص بك"). Use the pronoun suffix ـك only when it reads naturally (e.g., "جهات اتصالك").

- **Present continuous**: Use يجري (masculine) / تجري (feminine) for ongoing actions on all platforms. E.g., "Syncing" → "تجري المزامنة", "Playing" → "يجري التشغيل".

- **RTL and bidirectional text**: Arabic is RTL. Use Unicode directional markers (LRM/RLM) for strings ending with English words or variables. Keyboard shortcuts remain LTR and are not localized. Multi-key combos are arranged RTL: "Press Command-F5" → "F5-command اضغط على". Always add non-breaking space before the conjunctive "و" when it precedes English text to prevent line-break issues.

- **Numerals**: Use Eastern Arabic numerals (١، ٢، ٣) unless the context is technical (IP addresses, version numbers, MAC addresses). In Technical context, use Western Arabic (1, 2, 3) numerals. Technical ratios, multipliers, and resolutions remain unlocalized (1/3, 16:9, 1x, 1088p). Size units use Arabic abbreviation with dots: غ.ب. for GB, م.ب. for MB — single dot at end of sentence to avoid duplication.

- **Arabic punctuation marks**: Use Arabic comma "،" and Arabic question mark "؟". Arabic percentage sign ٪ is placed after the number. Always use the ellipsis character …  instead of three dots. Do not close nominal phrases or imperative commands with a period.

- **Quotation marks**: Use straight quotes " " only — never curly. Do not enclose UI options in quotation marks unless omitting them would make the context confusing to the reader.

- **Conjunctive "و" over commas**: Always use و or أو to join items, not commas, except in sequential action steps where commas improve readability. E.g., "iPhone و iPad و Mac" (not "iPhone، iPad والـ Mac").

- **No transliteration of product names and Apple terms**: Apple product names and trademarks must remain in their original English form — never transliterate them into Arabic script. Write `iPhone` not `آيفون`, `iCloud` not `آي كلاود`, `App Store` not `آب ستور`, `AirDrop` not `إير دروب`.

- **Product name gender**: Phone and TV are masculine. Watches, displays, speakers, headphones, AirTags, and services are feminine. Apple Vision Pro is feminine unless referred to in the source string as a device or spatial computer (then masculine).

- **Diacritics**: No full vocalization needed — add diacritics only to disambiguate. A shadda must always be accompanied by its vowel mark (شدَّة not شدّة). Tanwin is written on the letter preceding the alif (حاليًا not حالياً).

- **Passive voice by readability**: Choose between تم + verbal noun and the Arabic passive form based on readability. Use "تم استيراد الصور" when the passive verb form is uncommon, but "أُرسِلت الرسالة" when it reads naturally. Exercise judgment when uncertain.
