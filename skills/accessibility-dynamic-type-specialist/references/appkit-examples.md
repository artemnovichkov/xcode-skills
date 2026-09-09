# AppKit Dynamic Type Examples

Each section shows a **Bad** example (with explanation) and a **Good** example.

---

## System Fonts: Preferred Font vs Hardcoded Size

### Bad

```swift
let textField = NSTextField(labelWithString: "Settings")
textField.font = NSFont.systemFont(ofSize: 13)
```

This creates a fixed 13pt font. It will never change when the user adjusts their text size in System Settings > Accessibility > Display > Text Size.

### Good

```swift
let textField = NSTextField(labelWithString: "Settings")
textField.font = NSFont.preferredFont(forTextStyle: .body)
```

`NSFont.preferredFont(forTextStyle:)` (available since macOS 11) returns a font scaled to the user's current preferred size. When the view redraws, it picks up the new size automatically.

---

## Live Updates on Content Size Changes

### Bad

```swift
let label = NSTextField(labelWithString: "Status")
label.font = NSFont.preferredFont(forTextStyle: .headline)
// Font is set once at init — no mechanism to update when size changes
```

The label gets the correct font at creation time, but if the user changes their text size while the app is running, the label won't update until the view is recreated.

### Good

```swift
class MyViewController: NSViewController {
    let label = NSTextField(labelWithString: "Status")

    override func viewDidLoad() {
        super.viewDidLoad()
        label.font = NSFont.preferredFont(forTextStyle: .headline)

        NSWorkspace.shared.notificationCenter.addObserver(
            self,
            selector: #selector(accessibilityDisplayOptionsDidChange),
            name: NSWorkspace.accessibilityDisplayOptionsDidChangeNotification,
            object: nil
        )
    }

    @objc func accessibilityDisplayOptionsDidChange() {
        label.font = NSFont.preferredFont(forTextStyle: .headline)
    }
}
```

AppKit does not have `adjustsFontForContentSizeCategory`. The closest available signal is `NSWorkspace.accessibilityDisplayOptionsDidChangeNotification`, posted on `NSWorkspace.shared.notificationCenter` when any system accessibility display option changes. Re-apply the preferred font in the handler so the label picks up the new size. Note: this notification fires for many display-option changes (Increase Contrast, Reduce Motion, etc.), not text-size changes alone — but on macOS there is no granular text-size-only notification, so this is the canonical observation point.

---

## Custom Fonts — Manual Scaling

### Bad

```swift
let label = NSTextField(labelWithString: "Welcome")
label.font = NSFont(name: "Avenir-Medium", size: 17)
```

Custom font at a fixed size. No scaling with Dynamic Type.

### Good

```swift
let baseFont = NSFont(name: "Avenir-Medium", size: 17)!
let preferredBody = NSFont.preferredFont(forTextStyle: .body)
let scaleFactor = preferredBody.pointSize / NSFont.systemFontSize
label.font = NSFont(descriptor: baseFont.fontDescriptor, size: baseFont.pointSize * scaleFactor)
```

AppKit does not have `UIFontMetrics`. To scale custom fonts, compute a scale factor by comparing the current preferred body font size to the default system font size, and apply it to the custom font's point size.

---

## NSButton Title Fonts

### Bad

```swift
let button = NSButton(title: "Submit", target: self, action: #selector(submit))
button.font = NSFont.systemFont(ofSize: 14, weight: .semibold)
```

The button title uses a hardcoded font size.

### Good

```swift
let button = NSButton(title: "Submit", target: self, action: #selector(submit))
button.font = NSFont.preferredFont(forTextStyle: .body)
```

Using a preferred font ensures the button title scales with the user's text size preference.

---

## NSTextView with Rich Text

### Bad

```swift
let textView = NSTextView()
let attrs: [NSAttributedString.Key: Any] = [
    .font: NSFont.systemFont(ofSize: 15)
]
textView.textStorage?.setAttributedString(NSAttributedString(string: "Hello", attributes: attrs))
```

Hardcoded font size in attributed string attributes.

### Good

```swift
let textView = NSTextView()
let attrs: [NSAttributedString.Key: Any] = [
    .font: NSFont.preferredFont(forTextStyle: .body)
]
textView.textStorage?.setAttributedString(NSAttributedString(string: "Hello", attributes: attrs))
```

Using a preferred font in attributed string attributes ensures the text scales.

---

## Layout Adaptation with NSStackView

### Bad

```swift
let stack = NSStackView(views: [iconView, titleLabel, subtitleLabel])
stack.orientation = .horizontal
// Horizontal layout always, even when text becomes very large
```

At large text sizes, horizontal layouts overflow. Unlike SwiftUI, there is no `ViewThatFits`.

### Good

```swift
let stack = NSStackView(views: [iconView, titleLabel, subtitleLabel])

private let baselineBodyPointSize = NSFont.preferredFont(forTextStyle: .body).pointSize

func updateLayout() {
    let currentBodyPointSize = NSFont.preferredFont(forTextStyle: .body).pointSize
    let scale = currentBodyPointSize / baselineBodyPointSize
    stack.orientation = scale >= 1.4 ? .vertical : .horizontal
}
```

macOS has no equivalent of UIKit's `UIContentSizeCategory`, so there is no published API to query whether the user is at an "accessibility size." Instead, capture a baseline `preferredFont(forTextStyle: .body).pointSize` at launch and compare the current value against it; switch to a vertical layout when the scale factor passes a threshold you choose. Call `updateLayout()` from `viewDidLoad` and from your `accessibilityDisplayOptionsDidChange` handler so the layout responds to live changes.

---

## Fixed Frame Heights

### Bad

```swift
let label = NSTextField(labelWithString: "Description")
label.font = NSFont.preferredFont(forTextStyle: .body)
label.addConstraint(label.heightAnchor.constraint(equalToConstant: 20))
```

The font scales, but the fixed height constraint clips the text at larger sizes.

### Good

```swift
let label = NSTextField(labelWithString: "Description")
label.font = NSFont.preferredFont(forTextStyle: .body)
label.setContentHuggingPriority(.required, for: .vertical)
label.setContentCompressionResistancePriority(.required, for: .vertical)
```

Let Auto Layout determine the height based on the font size. Use content hugging and compression resistance instead of fixed height constraints.

---

## NSTextField vs NSText — Multiline Handling

### Bad

```swift
let label = NSTextField(labelWithString: "A long description that should wrap")
label.font = NSFont.preferredFont(forTextStyle: .body)
label.maximumNumberOfLines = 1
// Truncates at large sizes
```

### Good

```swift
let label = NSTextField(wrappingLabelWithString: "A long description that should wrap")
label.font = NSFont.preferredFont(forTextStyle: .body)
label.maximumNumberOfLines = 0
```

Use `NSTextField(wrappingLabelWithString:)` for multiline labels and set `maximumNumberOfLines = 0` to allow unlimited wrapping. This prevents truncation at larger Dynamic Type sizes.

---

## Text Style Mapping Reference (AppKit)

`NSFont.TextStyle` values available on macOS 11+:

| Text Style | Default Size (approx.) | Use for |
|---|---|---|
| `.largeTitle` | 26pt | Screen titles |
| `.title1` | 22pt | Section headers |
| `.title2` | 17pt | Subsection headers |
| `.title3` | 15pt | Tertiary headers |
| `.headline` | 13pt bold | Emphasized labels |
| `.body` | 13pt | Body text |
| `.callout` | 12pt | Secondary descriptions |
| `.subheadline` | 11pt | Tertiary labels |
| `.footnote` | 10pt | Fine print |
| `.caption1` | 10pt | Captions |
| `.caption2` | 10pt light | Smaller captions |
