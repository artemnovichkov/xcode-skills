# Plural Variations

Use plural variation when a string contains a **format specifier + countable noun**. The context tool provides `relevantPluralCases` for the target locale—always provide all cases.

## Decision Tree

```
Does the string contain a format specifier (%lld, %d, %@, etc.)?
├─ No → Use simple `translation`
└─ Yes → Is there a countable noun tied to that number?
    ├─ No → Use simple `translation` (number is standalone)
    └─ Yes → How many format specifier + noun pairs?
        ├─ One → Use `variationTranslation` with `topLevelVariation`
        └─ Multiple → Use `templateTranslation` with `substitutions`
```

## Translation Types

### Simple Translation

No format specifiers, or format specifiers without countable nouns.

```json
{ "translation": "Willkommen in unserer App" }
```

### Single Noun Variation

One format specifier with one noun that varies by count.

**Source**: `"Order %lld croissants"`

```json
{
  "variationTranslation": {
    "topLevelVariation": {
      "plural.one": "Order %lld croissant",
      "plural.other": "Order %lld croissants"
    }
  }
}
```

If providing an explicit `zero` case does not meaningfully improve the semantics of the translation, you may omit it.

**Critical**: Preserve the exact format specifier (`%lld`, `%1$lld`, etc.) in each variant. Only the noun changes.
**Critical**: Provide the entire variation structure, including any variations that might have translations already. You can only write the entire structure at once, and this overwrites what was there before.

### Multiple Noun Variation

Multiple format specifiers, each with a noun needing pluralization.

**Source**: `"Order %lld apples and %lld oranges"`

```json
{
  "templateTranslation": {
    "template": "Order %#@apples@ and %#@oranges@",
    "substitutions": [
      {
        "name": "apples",
        "argNum": 1,
        "formatSpecifier": "lld",
        "variants": {
          "plural.one": "%arg apple",
          "plural.other": "%arg apples"
        }
      },
      {
        "name": "oranges",
        "argNum": 2,
        "formatSpecifier": "lld",
        "variants": {
          "plural.one": "%arg orange",
          "plural.other": "%arg oranges"
        }
      }
    ]
  }
}
```

**Key points**:
- Template uses `%#@name@` to reference substitutions
- Each substitution needs `argNum` (1-indexed position) and `formatSpecifier` (without %)
- Variants use `%arg` as placeholder for the number

### Device Variations with Plurals

When source has device variations AND each contains nouns needing pluralization, vary by device first, then by plural:

```json
{
  "variationTranslation": {
    "topLevelVariation": {
      "device.iphone": "iPhone users have %#@apps@",
      "device.mac": "Mac users have %#@apps@",
      "device.other": "Users have %lld apps"
    },
    "substitutions": [
      {
        "name": "apps",
        "argNum": 1,
        "formatSpecifier": "lld",
        "variants": {
          "plural.one": "%arg app",
          "plural.other": "%arg apps"
        }
      }
    ]
  }
}
```

## A Number Behind a Non-Numerical Specifier

Sometimes a number reaches the string already formatted — the code formatted it for grouping separators or native digits and interpolated the result — so it arrives as `%@` rather than `%lld`. Plural categories are selected by reading a number, and `%@` is a string, so there is no axis to vary on. No translation repairs this: the string needs a numerical placeholder, which is a change in the source code.

Do two things.

**Translate around it.** Restructure so that no word has to agree with the count. Place the variable after a colon (preferred, shorter) or inside brackets, and keep the counted noun in the form the target locale uses for a standalone label — for many languages, the plural nominative.

- **Source**: `"%@ photos"` → `"Fotografije: %@"`
- **Source**: `"Sending %@ photos to destination."` → `"Slanje fotografija (%@) na odredište."`

Do not build a plural variation over a `%@`, and do not pick the one plural form that fits the most-common count.

**Report it.** Name the key in your final summary and state that it needs a numerical placeholder for correct plural agreement. The restructured string reads acceptably, but it is not the sentence the language would otherwise use. Only a code fix gets that back.

Restructuring is only for the non-numerical case. When the variable is numerical, vary by plural instead, providing every case in `relevantPluralCases` for the target locale.

## When the Source Needs Plural First

If `StringCatalogContext` returned a `sourcePluralCasesToAdd`, the source string might have to be varied by plural, but is not yet. You need to vary the source value by plural first.

Follow this two-step flow — one `StringCatalogEdit` call per step:

1. **Vary the source.** Call `StringCatalogEdit` with `targetLocaleIdentifier` set to the source locale identifier (from `sourceValues.sourceLocaleIdentifier`). Supply a suitable plural variation structure that covers every case in `sourcePluralCasesToAdd`.
2. **Translate the target.** Only after the source edit succeeds, call `StringCatalogEdit` a second time with the real `targetLocaleIdentifier` and a variation/template translation that uses every case in `relevantPluralCases`.

Do not attempt to do both edits in one call, and do not translate the target before the source has been varied.

**Critical**: The `device.other` fallback must be a flat string with plain format specifiers — it cannot reference substitutions or be further varied.

See [references/device-variations.md](references/device-variations.md) for when to add device variations and which device keys to use.

**Critical**: If the string is varied in the source language, you MUST use the same variation technique (i.e. top-level variation vs. substitution) in the target language.

## Plural Cases by Language

Different languages require different plural cases. The context tool tells you which cases to provide.
Always check `relevantPluralCases` from the context tool—it's authoritative for the target locale.
