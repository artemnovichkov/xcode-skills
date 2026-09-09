# Device Variations

Use device variation when a string's wording must change depending on the device the app runs on. Device variation is **optional and rarely needed** — most strings work identically across devices.

## Decision Tree

```
Is the source string already varied by device?
├─ Yes → You MUST vary by device in the target language, using the same device keys.
└─ No → Does the string reference a device-specific interaction or device name?
    ├─ No → Do NOT add device variations. Use simple `translation` or plural variation.
    └─ Yes → Is `supportedDevices` present in context with ≥ 2 device keys?
        ├─ No → Do NOT vary (single-platform app, no meaningful split).
        └─ Yes → Use `variationTranslation` with `topLevelVariation` keyed by device.
```

## When to Vary by Device

### Interaction verbs

When the source string describes a gesture or input method that differs between touch-screen and pointer-based devices

Examples:

| Touch (iPhone, iPad, Apple Watch) | Pointer (Mac) | Notes |
|---|---|---|
| tap | click | Most common form of interaction |
| swipe | scroll | Navigation gesture |
| drag | drag | Same word, but sometimes phrased differently ("drag with your finger" vs. just "drag") |

### Device name references

When the string mentions a specific device or form factor by name:

- "on your **iPhone**" vs. "on your **Mac**"
- "this **Apple Watch**" vs. "this **iPad**"
- "Open App Store on your **Apple TV**" — the sentence structure may change for different devices.

## When NOT to Vary

Do **not** add device variations for:

- Generic labels, settings names, or status text ("Downloading…", "Settings", "Done").
- Error messages that do not reference interaction mode or device name.
- Strings that contain only nouns, numbers, or format specifiers without device-dependent wording.
- Strings where the interaction verb is already device-neutral ("select", "choose", "open", "close").

**Rule of thumb**: if replacing every device key with the same translation would produce a correct result, skip device variation.

## Device-Only Example

**Source**: `"Tap to open"` (app builds for iPhone and Mac)

```json
{
  "variationTranslation": {
    "topLevelVariation": {
      "device.iphone": "Toca para abrir",
      "device.mac": "Haz clic para abrir",
      "device.other": "Pulsa para abrir"
    }
  }
}
```

## Combining Device and Plural Variations

In rare cases, a string can need **both** device variation and plural variation — for example, `"Tap to launch %lld spaceships"` differs by device (tap vs. click) **and** has a countable noun.

### Single Plural Noun

When only one format specifier + countable noun needs pluralization, use compound keys that combine device and plural in `topLevelVariation`. The format is `device.<device_variant>.plural.<plural_case>`. The `device.other` fallback must be a flat string — it cannot be further varied.

**Source**: `"Tap to launch %lld spaceships"` (app builds for iPhone and Mac)

```json
{
  "variationTranslation": {
    "topLevelVariation": {
      "device.iphone.plural.one": "Touchez pour lancer %lld vaisseau spatial",
      "device.iphone.plural.other": "Touchez pour lancer %lld vaisseaux spatiaux",
      "device.mac.plural.one": "Cliquez pour lancer %lld vaisseau spatial",
      "device.mac.plural.other": "Cliquez pour lancer %lld vaisseaux spatiaux",
      "device.other": "Touchez pour lancer %lld vaisseaux spatiaux"
    }
  }
}
```


### Multiple Plural Nouns

When a device-varied string has multiple format specifiers each tied to a countable noun, use `topLevelVariation` keyed by device with `%#@name@` substitution references, and define the plural forms in `substitutions`. If the noun itself changes per device, create separate substitutions per device (e.g., `arg1_iphone`, `arg1_mac`).

**Source**: `"Tap to share with %lld devices and %lld users"` (app builds for iPhone and Mac)

```json
{
  "variationTranslation": {
    "topLevelVariation": {
      "device.iphone": "Tippe, um mit %#@devices@ und %#@users@ zu teilen",
      "device.mac": "Klicke, um mit %#@devices@ und %#@users@ zu teilen",
      "device.other": "Tippe, um mit %lld und %lld zu teilen"
    },
    "substitutions": [
      {
        "name": "devices",
        "argNum": 1,
        "formatSpecifier": "lld",
        "variants": {
          "plural.one": "%arg Gerät",
          "plural.other": "%arg Geräte"
        }
      },
      {
        "name": "users",
        "argNum": 2,
        "formatSpecifier": "lld",
        "variants": {
          "plural.one": "%arg Benutzer",
          "plural.other": "%arg Benutzer"
        }
      }
    ]
  }
}
```

See [references/plural-variations.md](references/plural-variations.md) for more details on plural variation rules and substitution structure.

## Critical Rules

* The `StringCatalogContext` tool will tell you what device keys are available. `device.other` is a fallback for any unknown device.
* When plural variations are required, provide all plural cases from `relevantPluralCases` for every device key **except** `device.other`, which is always a flat fallback string.
* The `device.other` fallback must use plain format specifiers (`%lld`), not substitution references (`%#@name@`). Fallback values cannot be further varied.
