---
name: ios-dynamic-text
description: >
  Guide for correctly implementing Dynamic Text support on iOS.
  Covers UIKit and SwiftUI patterns, common mistakes, Large Content Viewer,
  and testing checklists. Use when helping developers add or fix Dynamic Text support.
user-invocable: true
---

# Dynamic Text Implementation Guide

## What is Dynamic Text

Dynamic Text is an iOS accessibility feature that lets users choose their preferred text size in Settings > Accessibility > Display & Text Size > Larger Text. Apps that support Dynamic Text automatically adjust their text and layout to the user's chosen size. There are 7 standard sizes (from xSmall to xxxLarge) and 5 additional Accessibility sizes (from AX1 to AX5) for users who need even larger text.

## Core Principles

1. **Zero visual change at default size.** Dynamic Text changes must not alter the appearance or layout for users at the default text size (Large). The app should look exactly the same as before your changes when the user has not changed their text size setting. Layout adaptations (e.g., switching from horizontal to vertical) should only activate at non-default sizes.
2. **Use text styles, not point sizes.** Always base fonts on system text styles (`.body`, `.headline`, `.caption1`, etc.) rather than hardcoded point sizes. This is the single most impactful rule.
3. **Never clamp or cap font sizes.** Respect the full range of Dynamic Text sizes including the five Accessibility sizes. Users who enable Accessibility sizes need them.
4. **Test at every size.** Verify layout at both the smallest (xSmall) and largest (AX5) sizes. Most bugs appear at the extremes.
5. **Scroll, don't truncate.** When content grows beyond the screen at large sizes, wrap it in a scroll view. Truncation defeats the purpose of Dynamic Text.
6. **Scale non-text elements too.** Icons, spacing, and padding next to text should scale proportionally so the UI feels balanced at all sizes.

## UIKit Implementation Guide

### Key APIs

| API | Purpose |
|-----|---------|
| `UIFont.preferredFont(forTextStyle:)` | Get a system font that tracks Dynamic Text |
| `adjustsFontForContentSizeCategory = true` | Opt a label/text view into automatic resizing |
| `UIFontMetrics(forTextStyle:)` | Scale custom fonts to match a text style's behavior |
| `UIContentSizeCategoryDidChange` notification | React to size changes at runtime |
| `traitCollectionDidChange(_:)` | Detect content size category changes via trait collection |
| `UILabel.numberOfLines = 0` | Allow labels to wrap instead of truncate |

### Patterns

- **Always** set `adjustsFontForContentSizeCategory = true` on `UILabel`, `UITextField`, and `UITextView`. Without it, the font will not update when the user changes their text size.
- Use `UIFontMetrics` to scale custom fonts. Do not apply a hardcoded point size to a custom font.
- Use Auto Layout with constraints that reference the text's intrinsic content size. Avoid fixed-height constraints on text containers.
- For table views and collection views, use self-sizing cells (`UITableView.automaticDimension` for row height).

See [uikit-examples.md](./uikit-examples.md) for complete code examples with good and bad patterns.

## SwiftUI Implementation Guide

### Key APIs

| API | Purpose |
|-----|---------|
| `.font(.body)` and other `Font.TextStyle` values | Apply a system text style that tracks Dynamic Text |
| `@ScaledMetric` | Scale a numeric value (spacing, icon size) with Dynamic Text |
| `@Environment(\.dynamicTypeSize)` | Read the current Dynamic Text size for conditional layout |
| `.dynamicTypeSize(...:)` modifier | Clamp Dynamic Text range (use sparingly) |
| `ViewThatFits` (iOS 16+) | Automatically pick the first layout variant that fits the available space |
| `ScrollView` | Allow content to scroll at large sizes |

### Patterns

- **Always** use semantic text styles (`.font(.body)`, `.font(.headline)`, etc.) instead of `.font(.system(size:))`.
- Use `@ScaledMetric` to scale spacing, padding, and icon dimensions alongside text.
- Use `@Environment(\.dynamicTypeSize)` to switch between horizontal and vertical layouts when text is large.
- Use `ViewThatFits` (iOS 16+) to let SwiftUI automatically select from multiple layout variants based on available space. This is the preferred approach for adaptive layouts because it responds to actual content size, not just the text size setting.
- Avoid `.minimumScaleFactor` as a substitute for proper Dynamic Text support. It shrinks text, which is the opposite of what the user wants.

See [swiftui-examples.md](./swiftui-examples.md) for complete code examples with good and bad patterns.

## Common Mistakes

| Mistake | Why it's wrong | Fix |
|---------|---------------|-----|
| Hardcoded font size (`UIFont.systemFont(ofSize: 17)`) | Does not respond to Dynamic Text | Use `UIFont.preferredFont(forTextStyle: .body)` |
| Missing `adjustsFontForContentSizeCategory` | Font is set correctly at launch but never updates | Set property to `true` |
| Fixed-height constraints on labels | Text clips at large sizes | Use intrinsic content size or `>= height` constraints |
| Using `.minimumScaleFactor` to "handle" large text | Shrinks text instead of growing it | Remove it; use proper layout that accommodates large text |
| Truncating text at Accessibility sizes | User cannot read the content | Allow wrapping (`numberOfLines = 0`) and add scroll views |
| Not scaling icons/images with text | Small icons next to large text look broken | Use `UIFontMetrics.default.scaledValue(for:)` or `@ScaledMetric` |
| Custom font without `UIFontMetrics` | Custom font stays fixed while system text scales | Wrap in `UIFontMetrics(forTextStyle:).scaledFont(for:)` |

## Large Content Viewer

Some UI elements cannot practically scale their text — tab bar items, toolbar buttons, segmented controls, and similar compact controls. For these, iOS provides **Large Content Viewer**: when a user with Accessibility sizes enabled long-presses a control, a large HUD appears showing the control's icon and title.

### UIKit

```swift
// UIBarButtonItem and UITabBarItem support this automatically.
// For custom views, adopt UILargeContentViewerItem:
class CustomToolbarButton: UIButton, UILargeContentViewerItem {
    var largeContentTitle: String? { return accessibilityLabel }
    var largeContentImage: UIImage? { return image(for: .normal) }
    var scalesLargeContentImage: Bool { return true }
    var showsLargeContentViewer: Bool { return true }
}

// Add the interaction to the parent view:
let interaction = UILargeContentViewerInteraction()
toolbar.addInteraction(interaction)
```

### SwiftUI

```swift
Button(action: { /* ... */ }) {
    Label("Favorites", systemImage: "star.fill")
}
.accessibilityShowsLargeContentViewer {
    Label("Favorites", systemImage: "star.fill")
}
```

## Info.plist Configuration

No specific `Info.plist` keys are required to enable Dynamic Text. However, be aware of:

- **`UISupportsLargeTextUserActivity`**: Not a real key. Sometimes hallucinated by LLMs. Do not add it.
- The system automatically provides Dynamic Text support when you use the correct APIs. There is no opt-in flag.

## Testing Checklist

- [ ] Set text size to **xSmall** — verify nothing looks oversized or wastes space
- [ ] Set text size to **AX5** (the largest) — verify all text is readable, not truncated, and the screen scrolls if needed
- [ ] Change text size **while the app is running** — verify labels update without restarting the app
- [ ] Check that **custom fonts** scale (not just system fonts)
- [ ] Verify **icons and spacing** scale proportionally with text
- [ ] Check that **table/collection view cells** resize correctly
- [ ] Test **landscape orientation** at large sizes — layouts may need to adapt
- [ ] Verify **Large Content Viewer** works on toolbar/tab bar items at Accessibility sizes
- [ ] Confirm no **fixed-size containers** clip text at large sizes
- [ ] Run Accessibility Inspector's audit — it flags missing Dynamic Text support
