# AppKit VoiceOver Patterns

## Criterion 1 — Missing accessibility labels

### Bad: Image button without label
```swift
let button = NSButton()
button.image = NSImage(systemSymbolName: "trash", accessibilityDescription: nil)
button.bezelStyle = .toolbar
button.isBordered = false
button.target = self
button.action = #selector(deleteTapped)
```
VoiceOver announces: "Button" — no description. Note: `accessibilityDescription: nil` on `NSImage` means the image provides no label.

### Good: Image button with label via NSImage
```swift
let button = NSButton()
button.image = NSImage(systemSymbolName: "trash", accessibilityDescription: "Delete")
button.bezelStyle = .toolbar
button.isBordered = false
```
The `accessibilityDescription` on the `NSImage` provides the button's label.

### Good: Image button with explicit label
```swift
let button = NSButton()
button.image = NSImage(systemSymbolName: "trash", accessibilityDescription: nil)
button.setAccessibilityLabel("Delete")
```

### Good: Button with title (auto-labeled)
```swift
let button = NSButton(title: "Save", target: self, action: #selector(saveTapped))
```
VoiceOver announces: "Save, button" — the title provides the label.

## Criterion 2 — Non-human-readable labels

### Bad: Auto-generated identifier as label
```swift
cell.setAccessibilityLabel("cell_id_4f3a2b")
```

### Bad: Variable name as label
```swift
imageView.setAccessibilityLabel("imgHeaderBanner_v2")
```

### Good: Human-readable labels
```swift
cell.setAccessibilityLabel("\(document.title), \(document.dateFormatted)")
imageView.setAccessibilityLabel("Company logo")
```

## Criterion 3 — Incorrect or missing traits (roles in AppKit)

AppKit uses `setAccessibilityRole()` instead of `accessibilityTraits`.

### Bad: Clickable view with no role
```swift
class ClickableCard: NSView {
    override func mouseDown(with event: NSEvent) {
        openDetail()
    }

    init() {
        super.init(frame: .zero)
        setAccessibilityElement(true)
        setAccessibilityLabel("View details")
    }
}
```
VoiceOver does not announce this as a button.

### Good: Clickable view with button role
```swift
class ClickableCard: NSView {
    override func mouseDown(with event: NSEvent) {
        openDetail()
    }

    init() {
        super.init(frame: .zero)
        setAccessibilityElement(true)
        setAccessibilityLabel("View details")
        setAccessibilityRole(.button)
    }
}
```

### Good: Header with heading role
```swift
let header = NSTextField(labelWithString: "Recent Items")
header.font = .preferredFont(forTextStyle: .title2)
if #available(macOS 26.0, *) {
    header.setAccessibilityRole(.headingRole)
}
```
The heading role is available starting in macOS 26. On earlier versions, leave the role unset and rely on the visual styling alone.

## Criterion 4 — Inaccessible images

### Bad: NSImageView with meaningful content but no label
```swift
let imageView = NSImageView()
imageView.image = NSImage(named: "productPhoto")
view.addSubview(imageView)
```
`NSImageView` is not typically an accessibility element by default in AppKit.

### Good: NSImageView with label
```swift
let imageView = NSImageView()
imageView.image = NSImage(named: "productPhoto")
imageView.setAccessibilityElement(true)
imageView.setAccessibilityLabel("Red running shoes")
imageView.setAccessibilityRole(.image)
```

### Good: Decorative image correctly excluded
```swift
let decorativeView = NSImageView()
decorativeView.image = NSImage(named: "separator")
decorativeView.setAccessibilityElement(false)
```

### Good: NSImage with accessibilityDescription
```swift
let image = NSImage(systemSymbolName: "heart.fill", accessibilityDescription: "Favorite")
let imageView = NSImageView()
imageView.image = image
```
The image's `accessibilityDescription` provides the label.

## Criterion 5 — Missing setAccessibilityElement

### Bad: Custom interactive view not exposed to VoiceOver
```swift
class ColorWell: NSView {
    override func mouseDown(with event: NSEvent) {
        showColorPicker()
    }
}
```
This view handles clicks but is not an accessibility element.

### Good: Custom interactive view exposed to VoiceOver
```swift
class ColorWell: NSView {
    override init(frame: NSRect) {
        super.init(frame: frame)
        setAccessibilityElement(true)
        setAccessibilityLabel("Color picker")
        setAccessibilityRole(.button)
    }

    override func mouseDown(with event: NSEvent) {
        showColorPicker()
    }
}
```

### Additional roles (recommendations)

#### Search field subrole

```swift
let searchField = NSTextField()
searchField.placeholderString = "Search items"
searchField.setAccessibilityRole(.textField)
searchField.setAccessibilitySubrole(.searchField)
```
Note: `searchField` is a Subrole (not a Role) on AppKit.

#### Static text role on a non-text container

```swift
container.setAccessibilityRole(.staticText)
container.setAccessibilityValue(combinedText)
```

#### Tab group role for a custom segmented bar

```swift
tabBar.setAccessibilityRole(.tabGroup)
for tab in tabs {
    tab.setAccessibilityRole(.radioButton)
    tab.setAccessibilityValue(tab.isSelected ? 1 : 0)
}
```

#### Announcing a frequently-updating value (AppKit equivalent of UpdatesFrequently)

AppKit has no `accessibilityLiveRegion` setter. To announce updates, post the value-changed notification when the underlying value changes, or post an explicit announcement:

```swift
let scoreLabel = NSTextField(labelWithString: "0")

func updateScore(_ newScore: Int) {
    scoreLabel.stringValue = "\(newScore)"
    NSAccessibility.post(element: scoreLabel, notification: .valueChanged)
}
```

## Element grouping (informational)

### Recommendation: Group related elements
```swift
// Group child elements so VoiceOver reads them together
let container = NSStackView(views: [titleField, subtitleField, dateField])
container.setAccessibilityElement(true)
container.setAccessibilityLabel("\(title), \(subtitle), \(date)")
```

## Custom actions (informational)

### Custom view with hidden alternate actions

```swift
// Sighted users right-click for a menu; VoiceOver users have no path
class RowView: NSView {
    override func rightMouseDown(with event: NSEvent) { showContextMenu() }
}
```

### Same view exposing custom actions

```swift
class RowView: NSView {
    override init(frame: NSRect) {
        super.init(frame: frame)
        setAccessibilityElement(true)
        setAccessibilityCustomActions([
            NSAccessibilityCustomAction(name: "Archive") { [weak self] in
                self?.archive(); return true
            },
            NSAccessibilityCustomAction(name: "Delete") { [weak self] in
                self?.delete(); return true
            }
        ])
    }
}
```

## Reading order (informational)

### Override `accessibilityChildren()` to set reading order

```swift
class HeroCard: NSView {
    override func accessibilityChildren() -> [Any]? {
        [badgeView, titleField, subtitleField]
    }
}
```

