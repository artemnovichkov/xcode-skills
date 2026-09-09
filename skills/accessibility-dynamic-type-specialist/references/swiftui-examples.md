# SwiftUI Dynamic Text Examples

Each section shows a **Bad** example (with explanation) and a **Good** example.

---

## Text Styles vs Hardcoded Sizes

### Bad

```swift
Text("Hello, World!")
    .font(.system(size: 17))
```

A hardcoded 17pt font. It will not change when the user adjusts their text size.

### Good

```swift
Text("Hello, World!")
    .font(.body)
```

`.body` (and other semantic styles like `.headline`, `.caption`, `.title`, etc.) automatically scale with Dynamic Text. No additional code needed — SwiftUI handles updates automatically.

---

## @ScaledMetric for Spacing and Dimensions

### Bad

```swift
struct ProfileRow: View {
    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: "person.circle")
                .frame(width: 40, height: 40)
            Text("Jane Doe")
                .font(.body)
        }
    }
}
```

The text scales, but the icon stays 40pt and the spacing stays 12pt. At large sizes, the icon looks tiny and the spacing feels cramped.

### Good

```swift
struct ProfileRow: View {
    @ScaledMetric(relativeTo: .body) private var iconSize: CGFloat = 40
    @ScaledMetric(relativeTo: .body) private var spacing: CGFloat = 12

    var body: some View {
        HStack(spacing: spacing) {
            Image(systemName: "person.circle")
                .frame(width: iconSize, height: iconSize)
            Text("Jane Doe")
                .font(.body)
        }
    }
}
```

`@ScaledMetric` scales the value proportionally with the specified text style. The base value (40, 12) applies at the default size and grows/shrinks from there.

---

## @Environment(\.dynamicTypeSize) for Conditional Layouts

### Bad

```swift
struct SettingsRow: View {
    var body: some View {
        HStack {
            Text("Wi-Fi")
                .font(.body)
            Spacer()
            Text("Connected")
                .font(.body)
                .foregroundStyle(.secondary)
        }
    }
}
```

At Accessibility sizes, both labels compete for horizontal space and may truncate.

### Good

```swift
struct SettingsRow: View {
    @Environment(\.dynamicTypeSize) private var dynamicTypeSize

    var body: some View {
        let layout = dynamicTypeSize.isAccessibilitySize
            ? AnyLayout(VStackLayout(alignment: .leading, spacing: 4))
            : AnyLayout(HStackLayout())

        layout {
            Text("Wi-Fi")
                .font(.body)
            if !dynamicTypeSize.isAccessibilitySize {
                Spacer()
            }
            Text("Connected")
                .font(.body)
                .foregroundStyle(.secondary)
        }
    }
}
```

At Accessibility sizes, the layout switches from horizontal to vertical so both labels get the full width. `AnyLayout` provides a smooth transition without duplicating view code.

---

## DynamicTypeSize Ranges with .dynamicTypeSize Modifier

### Bad

```swift
Text("Important notice")
    .font(.body)
    .dynamicTypeSize(.large)
```

Pinning to a single size completely disables Dynamic Text for this view. Users who need large text will not get it.

### Good — Only when truly necessary

```swift
// Limit only the maximum, and only for a specific control that cannot grow further
Text("Tab Label")
    .font(.caption2)
    .dynamicTypeSize(...DynamicTypeSize.accessibility1)
```

If you must limit the range, prefer an open-ended range that still allows scaling. This is appropriate for compact UI like tab labels where you provide Large Content Viewer as an alternative. Avoid using this on body content.

### Best — No clamping at all

```swift
Text("Important notice")
    .font(.body)
```

No modifier needed. Let the text scale to whatever size the user has chosen.

---

## minimumScaleFactor: Usage and Misuse

### Bad

```swift
Text("Welcome back, user!")
    .font(.title)
    .minimumScaleFactor(0.5)
```

This lets the system shrink the text down to 50% of its rendered size to fit. When a user has chosen large text, shrinking it defeats the purpose. The text may end up smaller than it would be without Dynamic Text.

### Good — Rare legitimate use

```swift
// Only appropriate for fixed-size UI like a clock widget face
Text(timeString)
    .font(.system(.largeTitle, design: .rounded))
    .minimumScaleFactor(0.8)
    .lineLimit(1)
```

`minimumScaleFactor` is acceptable in very constrained, fixed-size containers (like widgets or complications) where scrolling is not possible. Even then, keep the factor high (0.8+) so text does not shrink excessively.

### Best — Use proper layout instead

```swift
ScrollView {
    Text("Welcome back, user!")
        .font(.title)
}
```

If content might overflow, use a `ScrollView` instead of shrinking text.

---

## ScrollView for Large Content at Accessibility Sizes

### Bad

```swift
struct DetailView: View {
    var body: some View {
        VStack(spacing: 16) {
            Text("Title")
                .font(.largeTitle)
            Text("A long description that explains the feature in detail...")
                .font(.body)
            Image("hero")
                .resizable()
                .aspectRatio(contentMode: .fit)
            Button("Get Started") { /* ... */ }
                .font(.headline)
        }
        .padding()
    }
}
```

At Accessibility sizes, this content will overflow the screen. The bottom content will be cut off with no way to reach it.

### Good

```swift
struct DetailView: View {
    var body: some View {
        ScrollView {
            VStack(spacing: 16) {
                Text("Title")
                    .font(.largeTitle)
                Text("A long description that explains the feature in detail...")
                    .font(.body)
                Image("hero")
                    .resizable()
                    .aspectRatio(contentMode: .fit)
                Button("Get Started") { /* ... */ }
                    .font(.headline)
            }
            .padding()
        }
    }
}
```

Wrapping in `ScrollView` ensures all content is reachable at every text size. This is the most common fix for Accessibility size issues.

---

## Scaled Images Alongside Text

### Bad

```swift
Label("Favorites", systemImage: "star.fill")
    .font(.body)
// The SF Symbol scales automatically, but what about custom images?

HStack {
    Image("custom-icon")
        .frame(width: 24, height: 24)
    Text("Custom Item")
        .font(.body)
}
```

The custom image stays at 24pt while the text scales. At large sizes, the icon is disproportionately small.

### Good

```swift
struct IconRow: View {
    @ScaledMetric(relativeTo: .body) private var iconSize: CGFloat = 24

    var body: some View {
        HStack {
            Image("custom-icon")
                .resizable()
                .frame(width: iconSize, height: iconSize)
            Text("Custom Item")
                .font(.body)
        }
    }
}
```

`@ScaledMetric` keeps the custom image proportional to the text. SF Symbols scale automatically when used with `Label` or when given a `.font()` modifier, so this pattern is mainly needed for custom/raster images.

---

## ViewThatFits for Adaptive Layouts (iOS 16+)

`ViewThatFits` is one of the most important tools for Large Text support in SwiftUI. It evaluates its child views in order and displays the **first** one that fits within the available space. Unlike checking `dynamicTypeSize.isAccessibilitySize`, it responds to the **actual rendered size** of content, which means it adapts correctly across all device sizes, orientations, and text sizes — not just at the Accessibility threshold.

### How it works

```swift
ViewThatFits(in: axes) {
    firstChoice   // Tried first — used if it fits
    secondChoice  // Tried if firstChoice doesn't fit
    thirdChoice   // Last resort
}
```

- **`in` parameter (axes)**: Controls which axes SwiftUI checks for fit.
  - `.horizontal` — only checks if the view fits horizontally
  - `.vertical` — only checks if the view fits vertically
  - Default (no parameter) — checks both axes
- SwiftUI proposes the **available space** to each child view in order. The first child whose ideal size fits within that space is displayed. The others are never rendered.

### Bad — Fixed horizontal layout

```swift
HStack {
    Image(systemName: "wifi")
    Text("Wi-Fi")
    Spacer()
    Text("Not Connected")
        .foregroundStyle(.secondary)
}
```

At large text sizes, the two text elements compete for horizontal space and one or both will truncate.

### Good — Horizontal-to-vertical fallback

```swift
ViewThatFits {
    // Try horizontal first
    HStack {
        Label("Wi-Fi", systemImage: "wifi")
        Spacer()
        Text("Not Connected")
            .foregroundStyle(.secondary)
    }

    // Fall back to vertical if horizontal doesn't fit
    VStack(alignment: .leading, spacing: 4) {
        Label("Wi-Fi", systemImage: "wifi")
        Text("Not Connected")
            .foregroundStyle(.secondary)
    }
}
```

At default text sizes, the horizontal layout fits fine. At large text sizes, SwiftUI automatically switches to the vertical layout. No manual size checking needed.

### Good — Progressive text abbreviation

```swift
ViewThatFits {
    Text("Accessibility Inspector")
    Text("AX Inspector")
    Text("AXI")
}
```

This is useful for labels in constrained spaces (toolbars, tab bars, navigation titles). At large text sizes, the shorter labels are used automatically. Pair this with Large Content Viewer so the full text is still available via long-press.

### Good — Switching from grid to list at large sizes

```swift
ViewThatFits(in: .vertical) {
    // Compact 2-column grid at normal sizes
    LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 12) {
        ForEach(items) { item in
            ItemCard(item: item)
        }
    }

    // Single-column list at large sizes
    VStack(spacing: 12) {
        ForEach(items) { item in
            ItemCard(item: item)
        }
    }
}
```

Using `in: .vertical` tells SwiftUI to only check whether the content fits vertically. The grid may overflow vertically at large sizes, triggering the fallback to a single-column stack.

### ViewThatFits vs @Environment(\.dynamicTypeSize)

| | `ViewThatFits` | `@Environment(\.dynamicTypeSize)` |
|---|---|---|
| **Adapts based on** | Actual rendered content size | The text size category setting |
| **Breakpoint** | Automatic — wherever content stops fitting | Manual — you choose (typically `isAccessibilitySize`) |
| **Works across device sizes** | Yes — adapts to iPhone SE vs iPad | No — only responds to text size changes |
| **Available since** | iOS 16 | iOS 15 |

**Prefer `ViewThatFits`** when you want layout to adapt to actual space (most cases). **Use `@Environment(\.dynamicTypeSize)`** when you need to change behavior (not just layout) based on the text size — for example, hiding decorative images at Accessibility sizes to save space, or switching to a simplified view.

### Combining ViewThatFits with ScrollView

```swift
ViewThatFits(in: .vertical) {
    // If everything fits without scrolling, show it directly
    VStack(spacing: 16) {
        headerContent
        bodyContent
        footerContent
    }
    .padding()

    // If it doesn't fit vertically, wrap in a scroll view
    ScrollView {
        VStack(spacing: 16) {
            headerContent
            bodyContent
            footerContent
        }
        .padding()
    }
}
```

This avoids unnecessary scroll views at small text sizes while ensuring content is scrollable at large sizes. Note: extract shared content into computed properties or `@ViewBuilder` methods to avoid duplication.


# Large Text Anti-Patterns

These 10 anti-patterns are common mistakes that undermine Dynamic Text support. Each shows the problematic code, explains why it fails, and provides the correct approach.

---

## Anti-Pattern 1: Using .minimumScaleFactor as a Layout Crutch

```swift
// WRONG
Text("Account Balance: $1,234.56")
    .font(.title)
    .minimumScaleFactor(0.3)
    .lineLimit(1)
```

**Why it's wrong**: At AX5, `.title` might want to render at 60pt+. With `.minimumScaleFactor(0.3)`, the system can shrink it to ~18pt — smaller than `.body` at the default size. The user chose large text and got small text. The `lineLimit(1)` forces the shrinking.

**Fix**: Remove both modifiers and allow wrapping.

```swift
// CORRECT
Text("Account Balance: $1,234.56")
    .font(.title)
```

---

## Anti-Pattern 2: Fixed Frame That Clips Text

```swift
// WRONG
Text("Enable Notifications")
    .font(.body)
    .frame(width: 200, height: 44)
```

**Why it's wrong**: At large text sizes, "Enable Notifications" won't fit in 200pt width or 44pt height. The text clips invisibly — the user sees a partial word with no indication there's more.

**Fix**: Use `maxWidth` and `minHeight` instead.

```swift
// CORRECT
Text("Enable Notifications")
    .font(.body)
    .frame(maxWidth: 200, minHeight: 44)
```

---

## Anti-Pattern 3: Hardcoded Spacer Size That Doesn't Scale

```swift
// WRONG
HStack {
    Image(systemName: "star.fill")
        .font(.body)
    Spacer()
        .frame(width: 8)
    Text("Favorites")
        .font(.body)
}
```

**Why it's wrong**: At AX5, the text might be 4x larger but the gap is still 8pt — it looks jammed against the icon. Worse, the total width may exceed the screen because the spacing doesn't adapt.

**Fix**: Use `@ScaledMetric` for the spacing.

```swift
// CORRECT
struct FavoritesRow: View {
    @ScaledMetric(relativeTo: .body) private var spacing: CGFloat = 8

    var body: some View {
        HStack(spacing: spacing) {
            Image(systemName: "star.fill")
                .font(.body)
            Text("Favorites")
                .font(.body)
        }
    }
}
```

---

## Anti-Pattern 4: Applying .dynamicTypeSize to a Whole Screen

```swift
// WRONG
NavigationStack {
    ContentView()
}
.dynamicTypeSize(.large) // "Looks best at this size"
```

**Why it's wrong**: This overrides the user's chosen text size for the entire app. A user who set AX5 will get `.large` — a massive usability failure. This is equivalent to not supporting Dynamic Text at all.

**Fix**: Don't override the user's choice. If specific controls genuinely can't scale (like a tab bar label), clamp only those individual views and provide Large Content Viewer.

```swift
// CORRECT — only clamp specific controls that truly can't scale
TabBarLabel("Home")
    .dynamicTypeSize(...DynamicTypeSize.accessibility1)
    .accessibilityShowsLargeContentViewer {
        Label("Home", systemImage: "house")
    }
```

---

## Anti-Pattern 5: GeometryReader for Text-Size-Dependent Layout

```swift
// WRONG
GeometryReader { geometry in
    if geometry.size.width > 300 {
        HStack { labelContent; valueContent }
    } else {
        VStack { labelContent; valueContent }
    }
}
```

**Why it's wrong**: `GeometryReader` takes up all available space, disrupts the parent layout, and doesn't directly measure text size — it measures container size. It causes layout instability and often produces invisible content (zero height in scroll views).

**Fix**: Use `ViewThatFits` which directly measures whether the child content fits.

```swift
// CORRECT
ViewThatFits(in: .horizontal) {
    HStack { labelContent; valueContent }
    VStack(alignment: .leading) { labelContent; valueContent }
}
```

---

## Anti-Pattern 6: Using .lineLimit(1) on Primary Content

```swift
// WRONG
VStack(alignment: .leading) {
    Text(article.title)
        .font(.headline)
        .lineLimit(1)
    Text(article.body)
        .font(.body)
        .lineLimit(3)
}
```

**Why it's wrong**: At large text sizes, even short titles may need 2+ lines. Clamping to 1 line truncates the title — the user loses context. The 3-line limit on body similarly cuts off content.

**Fix**: Remove line limits on primary content. Only use line limits on supplementary preview text where the full content is accessible elsewhere.

```swift
// CORRECT
VStack(alignment: .leading) {
    Text(article.title)
        .font(.headline)
    Text(article.body)
        .font(.body)
}
```

---

## Anti-Pattern 7: Fixed Aspect Ratio Container for Mixed Content

```swift
// WRONG
VStack {
    Image("banner")
        .resizable()
        .aspectRatio(16/9, contentMode: .fill)
        .frame(height: 200)
    Text("Welcome to the app! Here's a long description of the features...")
        .font(.body)
        .padding()
}
.frame(height: 350) // Fixed total height
```

**Why it's wrong**: The 200pt image and 350pt total frame leave only 150pt for text. At large sizes, the text is severely clipped. The fixed container prevents any adaptation.

**Fix**: Let the container size itself, make the image proportional, and wrap in a scroll view.

```swift
// CORRECT
ScrollView {
    VStack {
        Image("banner")
            .resizable()
            .aspectRatio(16/9, contentMode: .fill)
            .frame(maxHeight: 200)
            .clipped()
        Text("Welcome to the app! Here's a long description of the features...")
            .font(.body)
            .padding()
    }
}
```

---

## Anti-Pattern 8: Invisible Truncation via ZStack Overlays

```swift
// WRONG
ZStack(alignment: .bottomTrailing) {
    Text(message)
        .font(.body)
        .padding()
    Text(timestamp)
        .font(.caption2)
        .padding(4)
        .background(.regularMaterial, in: Capsule())
}
.frame(height: 80) // Fixed height
```

**Why it's wrong**: The timestamp overlaps the message text at large sizes. The fixed height clips both. The user may not realize content is hidden behind the overlay.

**Fix**: Stack vertically and let the container size itself.

```swift
// CORRECT
VStack(alignment: .trailing, spacing: 8) {
    Text(message)
        .font(.body)
        .frame(maxWidth: .infinity, alignment: .leading)
    Text(timestamp)
        .font(.caption2)
        .foregroundStyle(.secondary)
}
.padding()
```

---

## Anti-Pattern 9: Mixing Custom Point Sizes with System Text Styles

```swift
// WRONG
VStack(alignment: .leading) {
    Text("Section Title")
        .font(.headline)  // Scales with Dynamic Text
    Text("Subtitle info")
        .font(.system(size: 14))  // Fixed at 14pt forever
    Text("Body content here")
        .font(.body)  // Scales with Dynamic Text
}
```

**Why it's wrong**: At AX5, `.headline` might render at 50pt and `.body` at 40pt, but the subtitle is stuck at 14pt. The visual hierarchy is broken — a "subtitle" appears as tiny, nearly invisible text between large elements.

**Fix**: Use semantic text styles consistently.

```swift
// CORRECT
VStack(alignment: .leading) {
    Text("Section Title")
        .font(.headline)
    Text("Subtitle info")
        .font(.subheadline)
    Text("Body content here")
        .font(.body)
}
```

---

## Anti-Pattern 10: Disabling Scroll on Content That Can Overflow

```swift
// WRONG
ScrollView {
    VStack(spacing: 16) {
        ForEach(items) { item in
            ItemView(item: item)
        }
    }
    .padding()
}
.scrollDisabled(true) // "We don't want this to scroll"
```

**Why it's wrong**: The developer disabled scrolling for aesthetic reasons (maybe to prevent scroll bounce at normal sizes). At Accessibility sizes, content overflows the screen and the user is trapped — they can see the top content but cannot reach anything below the fold.

**Fix**: Remove `.scrollDisabled(true)`. If you want to avoid unnecessary scrolling at small sizes, use `ViewThatFits` to conditionally add the `ScrollView`.

```swift
// CORRECT
ViewThatFits(in: .vertical) {
    VStack(spacing: 16) {
        ForEach(items) { item in
            ItemView(item: item)
        }
    }
    .padding()

    ScrollView {
        VStack(spacing: 16) {
            ForEach(items) { item in
                ItemView(item: item)
            }
        }
        .padding()
    }
}
```

---
