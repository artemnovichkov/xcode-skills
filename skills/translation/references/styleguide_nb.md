# Norwegian Bokmål (nb) — Software String Localization Style Guide

- **End-weight sentence structure**: Norwegian strongly prefers end-weight — place the main verb/action early and the longer clause at the end. E.g., "To start downloading, press OK." becomes "Trykk på OK for å starte nedlastingen." (not "Hvis du vil starte nedlastingen, trykker du på OK."). Use the formal subject "det" to shift heavy subjects to the end: "Det ble ikke funnet noen dokumenter som oppfyller søkekriteriene."

- **Omit "your" and "this"**: Literal translation of "your" is rarely idiomatic in Norwegian. Use the definite form of the noun instead: "Your software has been updated." becomes "Programvaren har blitt oppdatert." (not "Programvaren din har blitt oppdatert."). Similarly, omit "denne/dette" when the referent is obvious, especially before variables where the gender is unknown.

- **Double angle quotation marks**: Use Norwegian-style guillemets for quotes: «  and ». Do not use quotation marks around app names, company names, or person names. Do add them around account names and Apple IDs («appleseed@icloud.com») and song titles («Yesterday»). When in doubt, omit quotes around variables.

- **Product name inflection**: Single-word device names can be inflected with definite "-en": "iPhonen", "MacBooken". Multi-word names append "-enheten" for iOS devices ("iPod touch-enheten") or "-maskinen" for Macs ("Mac mini-maskinen"). Apple TV follows acronym rules: "Apple TV-en". Avoid inflecting when possible by rewriting.

- **Acronym compounding with non-breaking hyphen**: Use a non-breaking hyphen when inflecting acronyms — "ID-en", "TV-er" (not "IDen" or "ID'en"). This keeps the compound on one line. Avoid placing hyphens next to + characters: rewrite "Fitness+-økt" as "økt i Fitness+".

- **"Angi" vs. "oppgi"**: Use "angi" when the user is setting something new (creating a password: "Angi et passord for kontoen.") and "oppgi" when the user is providing something already established (entering an existing password: "Oppgi passordet for kontoen.").

- **"Or" often becomes "og"**: When English uses "or" after "any" (which maps to Norwegian "alle" + plural), translate "or" as "og": "Keynote accepts any QuickTime or iCloud file type." becomes "Keynote godtar alle QuickTime- og iCloud-filtyper." Use common sense to preserve correct meaning.

- **"May/might" as "kanskje"**: Prefer the adverb "kanskje" over subordinate clause constructions for better flow. E.g., "You may have to restart your computer." becomes "Du må kanskje starte datamaskinen på nytt." (not "Det kan hende du må starte datamaskinen på nytt.").

- **Inflected neuter plurals**: For neuter words where Bokmål allows uninflected plural, prefer the inflected form: "flere programmer" (not "flere program"), "flere kameraer" (not "flere kamera"). For foreign-origin neuter words, mark plural explicitly: "et album, flere albumer". Use Latin plural for Latin words: "et forum, flere fora". Exception: use "kontoer" (not "konti") for Account.

- **Time colon, space thousands, decimal comma**: Per CLDR, the time separator is a colon ("kl. 14:00"). Norwegian uses space as the thousands separator and comma as the decimal separator ("1 000 000", "3,5 km"). Insert non-breaking spaces between numbers and units ("2 GB").

- **Ellipsis always in software**: Always use the pre-composed ellipsis character instead of three periods, regardless of source. In software, skip the space before the ellipsis due to space constraints ("Arkiver som…").

- **Inclusive pronoun "hen"**: For singular "they" referring to a person of unspecified gender, do not translate as "he or she". Instead, rewrite using "person" or "vedkommende", or use the gender-neutral third-person pronoun "hen". Use diverse person names from multiple cultural backgrounds common in Norway, including Sami and immigrant-community names.

- **AI as "KI"**: The acronym AI is translated as "KI" (kunstig intelligens) in Norwegian — one of the few translated acronyms. Most other IT acronyms remain in English.
