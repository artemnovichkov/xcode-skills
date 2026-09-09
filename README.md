# Xcode Skills

Agent skills bundled with **Xcode 27**, packaged as a Claude Code plugin so you can use them outside Xcode.

## Install

### Any agent — `npx skills`

Works for Codex, Cursor, Cline, Amp, Claude Code and ~70 more. Project scope by default, `-g` for global:

```bash
npx skills add artemnovichkov/xcode-skills          # pick interactively
npx skills add artemnovichkov/xcode-skills --all -g # install all, globally
```

Installs to `.agents/skills/`, then links into each detected agent's own directory.

### Claude Code plugin

```
/plugin marketplace add artemnovichkov/xcode-skills
/plugin install xcode-skills@xcode-skills
```

The plugin also registers Xcode's `mcpbridge` MCP server (`xcrun mcpbridge`). It requires Xcode 27
installed; `device-interaction`, `translation` and `translation-coordinator` depend on it. The other
skills work without it.

### Manual

```bash
git clone https://github.com/artemnovichkov/xcode-skills.git
cp -R xcode-skills/skills/* ~/.agents/skills/   # Codex, and most other agents
cp -R xcode-skills/skills/* ~/.claude/skills/   # Claude Code
```

In Codex run `/skills` or type `$` to invoke one explicitly; otherwise they trigger on description match.

## Skills

| Skill | What it does |
| --- | --- |
| `swiftui-specialist` | SwiftUI best practices and performance: `@Animatable`, `@Observable` invalidation, `ForEach`/`List` identity, Environment/`@Entry`, localization, soft-deprecated APIs. |
| `swiftui-whats-new-27` | New SwiftUI APIs in the 2027 releases: `@State` as a macro, `@ContentBuilder`, `reorderable()`, `AsyncImage` caching, swipe actions outside `List`, toolbar overflow, item-binding alerts. |
| `app-intents-specialist` | App Intents correctness: execution model, entities and queries, `AppEnum`, parameters and summaries, dependencies, results and errors, donation, localization, shortcut phrases. |
| `app-intents-whats-new-27` | App Intents in iOS 26/27: `supportedModes`, `SnippetIntent`, `UndoableIntent`, Visual Intelligence, Spotlight properties, syncable entities, `@AppIntent(schema:)`, `AppIntentsTesting`. |
| `building-document-based-swiftui-applications` | The new `Document` protocol: `DocumentGroup`, readers/writers, `FileWrapper`, packages, progress, undo, migration off `FileDocument`. |
| `uikit-app-modernization` | Replaces legacy shared-state UIKit APIs (`mainScreen`, `interfaceOrientation`, app lifecycle) with scene-aware equivalents. |
| `modernize-tests` | Swift Testing adoption and XCTest migration. |
| `adopt-c-bounds-safety` | The C `-fbounds-safety` extension: pointer annotations, adoption strategy, build settings, runtime debugging. |
| `audit-xcode-security-settings` | Audits and progressively enables security build settings, analyzer checkers, and Enhanced Security. |
| `accessibility-voiceover-specialist` | Audits views against Apple's VoiceOver nutrition label: labels, traits, images, custom controls. |
| `accessibility-dynamic-type-specialist` | Audits text scaling: text styles, `UIFontMetrics`, layout adaptation at accessibility sizes. |
| `accessibility-sufficient-contrast-specialist` | Audits color contrast against WCAG 2.1 ratios for the Sufficient Contrast nutrition label. |
| `translation-coordinator` | Coordinates translating a project or its `.xcstrings` catalogs: prepares languages, fetches untranslated strings, delegates, verifies. |
| `translation` | Translates individual strings or small batches in String Catalogs. |
| `device-interaction` | Verifies app behavior on device/simulator via screenshots, UI hierarchy, touch input, and tvOS Siri Remote control. |

## Note

Content is Apple's, extracted verbatim from Xcode 27. This repo only repackages it for installation. Beta material — expect it to change in later seeds.
