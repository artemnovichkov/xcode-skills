# UIKit Dynamic Text Examples

Each section shows a **Bad** example (with explanation) and a **Good** example.

---

## System Fonts: Preferred Font vs Hardcoded Size

### Bad

```swift
let label = UILabel()
label.font = UIFont.systemFont(ofSize: 17)
```

This creates a fixed 17pt font. It will never change when the user adjusts their text size in Settings.

### Good

```swift
let label = UILabel()
label.font = UIFont.preferredFont(forTextStyle: .body)
label.adjustsFontForContentSizeCategory = true
```

`preferredFont(forTextStyle:)` returns a font scaled to the user's current text size. Setting `adjustsFontForContentSizeCategory` ensures the label updates automatically when the size changes.

---

## The adjustsFontForContentSizeCategory Property

### Bad

```swift
let label = UILabel()
label.font = UIFont.preferredFont(forTextStyle: .headline)
// Missing adjustsFontForContentSizeCategory!
```

The label gets the correct font at launch, but if the user changes their text size while the app is running (via Control Center or Settings), the label will not update.

### Good

```swift
let label = UILabel()
label.font = UIFont.preferredFont(forTextStyle: .headline)
label.adjustsFontForContentSizeCategory = true
```

Now the label automatically updates its font when the content size category changes. This works on `UILabel`, `UITextField`, and `UITextView`.

---

## Custom Fonts with UIFontMetrics

### Bad

```swift
let label = UILabel()
label.font = UIFont(name: "Avenir-Medium", size: 17)
```

Custom font at a hardcoded size. Does not scale with Dynamic Text at all.

### Good

```swift
let baseFont = UIFont(name: "Avenir-Medium", size: 17)!
let metrics = UIFontMetrics(forTextStyle: .body)
let label = UILabel()
label.font = metrics.scaledFont(for: baseFont)
label.adjustsFontForContentSizeCategory = true
```

`UIFontMetrics` scales the custom font proportionally to how `.body` would scale. The base size (17) is used at the default content size category; it grows and shrinks from there.

---

## Responding to Content Size Category Changes

### Bad

```swift
// Setting font once in viewDidLoad and never updating it
override func viewDidLoad() {
    super.viewDidLoad()
    customView.titleFont = UIFont.preferredFont(forTextStyle: .title1)
}
```

If your custom view does not use `adjustsFontForContentSizeCategory` internally, the font will go stale.

### Good — Using traitCollectionDidChange

```swift
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)
    if traitCollection.preferredContentSizeCategory != previousTraitCollection?.preferredContentSizeCategory {
        customView.titleFont = UIFont.preferredFont(forTextStyle: .title1)
    }
}
```

### Good — Using NotificationCenter (iOS 10+)

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    updateFonts()
    NotificationCenter.default.addObserver(
        self,
        selector: #selector(updateFonts),
        name: UIContentSizeCategory.didChangeNotification,
        object: nil
    )
}

@objc private func updateFonts() {
    customView.titleFont = UIFont.preferredFont(forTextStyle: .title1)
}
```

### Good — Using UITraitChangeHandler (iOS 17+)

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    registerForTraitChanges([UITraitPreferredContentSizeCategory.self]) { (self: Self, _) in
        self.customView.titleFont = UIFont.preferredFont(forTextStyle: .title1)
    }
}
```

The `registerForTraitChanges` API is the modern replacement for `traitCollectionDidChange` and avoids the deprecated method.

---

## Auto Layout Constraints That Adapt

### Bad

```swift
label.heightAnchor.constraint(equalToConstant: 44).isActive = true
```

A fixed height will clip text at large Dynamic Text sizes.

### Good

```swift
// Let the label determine its own height from its content
label.numberOfLines = 0
label.setContentHuggingPriority(.required, for: .vertical)

// If you need a minimum height, use greaterThanOrEqualTo:
label.heightAnchor.constraint(greaterThanOrEqualToConstant: 44).isActive = true
```

Using `numberOfLines = 0` lets the label wrap. The `greaterThanOrEqualTo` constraint ensures a minimum tap target while allowing the label to grow.

---

## Self-Sizing Table View Cells

### Bad

```swift
tableView.rowHeight = 60
```

Fixed row height. Cells will clip their content at large text sizes.

### Good

```swift
tableView.rowHeight = UITableView.automaticDimension
tableView.estimatedRowHeight = 60
```

With `automaticDimension`, the table view uses Auto Layout to calculate each cell's height based on its content. The estimated height is only for scroll bar sizing.

Inside the cell, ensure labels use `numberOfLines = 0` and constraints pin to the cell's `contentView` margins.

---

## Handling Accessibility Sizes with Scrolling

### Bad

```swift
// A stack view with lots of content but no scroll view
let stackView = UIStackView(arrangedSubviews: [titleLabel, subtitleLabel, descriptionLabel, imageView, actionButton])
stackView.axis = .vertical
view.addSubview(stackView)
// stackView pinned to view edges...
```

At Accessibility sizes, this content will overflow the screen. The user cannot scroll to see everything.

### Good

```swift
let scrollView = UIScrollView()
view.addSubview(scrollView)
scrollView.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    scrollView.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor),
    scrollView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
    scrollView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
    scrollView.bottomAnchor.constraint(equalTo: view.bottomAnchor)
])

let stackView = UIStackView(arrangedSubviews: [titleLabel, subtitleLabel, descriptionLabel, imageView, actionButton])
stackView.axis = .vertical
stackView.spacing = 16
scrollView.addSubview(stackView)
stackView.translatesAutoresizingMaskIntoConstraints = false
NSLayoutConstraint.activate([
    stackView.topAnchor.constraint(equalTo: scrollView.contentLayoutGuide.topAnchor, constant: 16),
    stackView.leadingAnchor.constraint(equalTo: scrollView.frameLayoutGuide.leadingAnchor, constant: 16),
    stackView.trailingAnchor.constraint(equalTo: scrollView.frameLayoutGuide.trailingAnchor, constant: -16),
    stackView.bottomAnchor.constraint(equalTo: scrollView.contentLayoutGuide.bottomAnchor, constant: -16)
])
```

The scroll view ensures all content is reachable at any text size.

---

## Image Scaling with Dynamic Text

### Bad

```swift
let imageView = UIImageView(image: UIImage(systemName: "star.fill"))
imageView.widthAnchor.constraint(equalToConstant: 24).isActive = true
imageView.heightAnchor.constraint(equalToConstant: 24).isActive = true
```

Fixed image size next to text that scales. At large text sizes, the icon will look tiny and out of proportion.

### Good

```swift
let imageView = UIImageView(image: UIImage(systemName: "star.fill"))

// Scale the image size with the body text style
let scaledSize = UIFontMetrics.default.scaledValue(for: 24)
imageView.widthAnchor.constraint(equalToConstant: scaledSize).isActive = true
imageView.heightAnchor.constraint(equalToConstant: scaledSize).isActive = true

// For SF Symbols, you can also use preferredSymbolConfiguration:
imageView.preferredSymbolConfiguration = UIImage.SymbolConfiguration(textStyle: .body)
```

`UIFontMetrics.default.scaledValue(for:)` scales a numeric value the same way the default text style scales. For SF Symbols, `SymbolConfiguration(textStyle:)` is even simpler and keeps the symbol in sync with nearby text.

---

## Switching Layout at Accessibility Sizes

### Bad

```swift
// Always horizontal, even at very large text sizes
let stackView = UIStackView(arrangedSubviews: [iconView, titleLabel])
stackView.axis = .horizontal
```

At Accessibility sizes, a horizontal layout may cause text to be severely compressed or truncated.

### Good

```swift
let stackView = UIStackView(arrangedSubviews: [iconView, titleLabel])

// Switch to vertical layout at Accessibility sizes
let isAccessibilitySize = traitCollection.preferredContentSizeCategory.isAccessibilityCategory
stackView.axis = isAccessibilitySize ? .vertical : .horizontal

// Update when the size changes (iOS 17+):
registerForTraitChanges([UITraitPreferredContentSizeCategory.self]) { (self: Self, _) in
    let isAccessibilitySize = self.traitCollection.preferredContentSizeCategory.isAccessibilityCategory
    self.stackView.axis = isAccessibilitySize ? .vertical : .horizontal
}
```

`isAccessibilityCategory` returns `true` for the five largest sizes (AX1–AX5). This is a clean way to adapt layout for users who need the most space.


---

# UIKit Large Text Anti-Patterns

These 10 anti-patterns are common UIKit mistakes that undermine Dynamic Text support.

---

## Anti-Pattern 1: Fixed Row Height on UITableView

```swift
// WRONG
tableView.rowHeight = 60
```

**Why it's wrong**: At Accessibility sizes, text content will be clipped to 60pt of height. Some cells might need 200+ points at AX5.

**Fix**:

```swift
// CORRECT
tableView.rowHeight = UITableView.automaticDimension
tableView.estimatedRowHeight = 60
```

Ensure cells use Auto Layout constraints that pin to `contentView` edges, and labels have `numberOfLines = 0`.

---

## Anti-Pattern 2: Intrinsic Content Size Override That Ignores Text

```swift
// WRONG
class FixedHeightLabel: UILabel {
    override var intrinsicContentSize: CGSize {
        return CGSize(width: UIView.noIntrinsicMetric, height: 44)
    }
}
```

**Why it's wrong**: Overriding `intrinsicContentSize` to return a fixed height prevents the label from growing with its text content. At large sizes, text clips.

**Fix**: Don't override `intrinsicContentSize` for text-containing views. If you need a minimum height, use a constraint:

```swift
// CORRECT
label.heightAnchor.constraint(greaterThanOrEqualToConstant: 44).isActive = true
```

---

## Anti-Pattern 3: Using sizeToFit Instead of Auto Layout

```swift
// WRONG
label.text = "Welcome back!"
label.font = .preferredFont(forTextStyle: .title1)
label.sizeToFit()
label.frame = CGRect(x: 16, y: 100, width: view.bounds.width - 32, height: label.frame.height)
```

**Why it's wrong**: `sizeToFit()` calculates size once. When the user changes their text size while the app is open, the frame doesn't update. Manual frame calculations also don't handle rotation or multitasking.

**Fix**: Use Auto Layout.

```swift
// CORRECT
label.font = .preferredFont(forTextStyle: .title1)
label.adjustsFontForContentSizeCategory = true
label.numberOfLines = 0
label.translatesAutoresizingMaskIntoConstraints = false
view.addSubview(label)
NSLayoutConstraint.activate([
    label.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 16),
    label.leadingAnchor.constraint(equalTo: view.layoutMarginsGuide.leadingAnchor),
    label.trailingAnchor.constraint(equalTo: view.layoutMarginsGuide.trailingAnchor),
])
```

---

## Anti-Pattern 4: UIFontMetrics on the Wrong Text Style

```swift
// WRONG
let customFont = UIFont(name: "Avenir-Heavy", size: 34)!
let scaledFont = UIFontMetrics(forTextStyle: .caption2).scaledFont(for: customFont)
titleLabel.font = scaledFont
```

**Why it's wrong**: A 34pt font wrapped in `.caption2` metrics will scale as if it's a caption — barely growing at large sizes. A large-title-sized font using caption scaling creates a broken type hierarchy.

**Fix**: Match the `UIFontMetrics` text style to the role the font plays in your UI.

```swift
// CORRECT
let customFont = UIFont(name: "Avenir-Heavy", size: 34)!
let scaledFont = UIFontMetrics(forTextStyle: .largeTitle).scaledFont(for: customFont)
titleLabel.font = scaledFont
```

---

## Anti-Pattern 5: numberOfLines = 1 on Primary Content Labels

```swift
// WRONG
let titleLabel = UILabel()
titleLabel.font = .preferredFont(forTextStyle: .headline)
titleLabel.adjustsFontForContentSizeCategory = true
titleLabel.numberOfLines = 1  // "Keeps it clean"
```

**Why it's wrong**: At Accessibility sizes, even a short title like "Notifications" might be too wide for the screen. With `numberOfLines = 1`, it truncates with "...". The user cannot read the full text.

**Fix**:

```swift
// CORRECT
titleLabel.numberOfLines = 0  // Allow unlimited wrapping
```

Only use `numberOfLines = 1` for supplementary text (timestamps, preview snippets) where the full content is accessible elsewhere.

---

## Anti-Pattern 6: Hardcoded Content Insets on UIButton

```swift
// WRONG
button.contentEdgeInsets = UIEdgeInsets(top: 8, left: 16, bottom: 8, right: 16)
```

**Why it's wrong**: At AX5, the button text might be 4x its default size, but the padding stays at 8pt/16pt. The text looks jammed against the button edges. The tap target may also be disproportionately small relative to the visible content.

**Fix**: Scale insets with `UIFontMetrics`.

```swift
// CORRECT
let metrics = UIFontMetrics(forTextStyle: .body)
var config = UIButton.Configuration.filled()
config.contentInsets = NSDirectionalEdgeInsets(
    top: metrics.scaledValue(for: 8),
    leading: metrics.scaledValue(for: 16),
    bottom: metrics.scaledValue(for: 8),
    trailing: metrics.scaledValue(for: 16)
)
button.configuration = config
```

---

## Anti-Pattern 7: Using preferredFont Without adjustsFontForContentSizeCategory

```swift
// WRONG
override func viewDidLoad() {
    super.viewDidLoad()
    titleLabel.font = .preferredFont(forTextStyle: .title1)
    bodyLabel.font = .preferredFont(forTextStyle: .body)
    // Missing: adjustsFontForContentSizeCategory on both labels
}
```

**Why it's wrong**: The fonts are correct at launch time, but when the user changes their text size via Control Center (without leaving the app), the labels don't update. This is one of the most common bugs: it looks correct during development but fails in real use.

**Fix**: Always pair `preferredFont` with `adjustsFontForContentSizeCategory`:

```swift
// CORRECT
titleLabel.font = .preferredFont(forTextStyle: .title1)
titleLabel.adjustsFontForContentSizeCategory = true
bodyLabel.font = .preferredFont(forTextStyle: .body)
bodyLabel.adjustsFontForContentSizeCategory = true
```

---

## Anti-Pattern 8: Mixing System and Custom Fonts Without UIFontMetrics

```swift
// WRONG
titleLabel.font = .preferredFont(forTextStyle: .headline)  // Scales
titleLabel.adjustsFontForContentSizeCategory = true

subtitleLabel.font = UIFont(name: "Georgia", size: 15)  // Doesn't scale
```

**Why it's wrong**: At AX5, the headline might render at 50pt, but Georgia stays at 15pt. The subtitle becomes nearly invisible next to the title. The visual hierarchy is destroyed.

**Fix**: Scale the custom font with `UIFontMetrics`.

```swift
// CORRECT
subtitleLabel.font = UIFontMetrics(forTextStyle: .subheadline)
    .scaledFont(for: UIFont(name: "Georgia", size: 15)!)
subtitleLabel.adjustsFontForContentSizeCategory = true
```

---

## Anti-Pattern 9: Fixed-Size Container View for Dynamic Content

```swift
// WRONG
class TooltipView: UIView {
    override var intrinsicContentSize: CGSize {
        CGSize(width: 250, height: 100)
    }

    // Contains a label with dynamic text...
}
```

**Why it's wrong**: The tooltip is always 250x100pt. At large text sizes, the label's text overflows this box and either clips or overlaps other content.

**Fix**: Let the view size itself based on content, with a maximum width constraint.

```swift
// CORRECT
class TooltipView: UIView {
    override init(frame: CGRect) {
        super.init(frame: frame)
        // Use Auto Layout, no intrinsicContentSize override
        widthAnchor.constraint(lessThanOrEqualToConstant: 300).isActive = true
        // Pin label to edges with padding...
    }
}
```

---

## Anti-Pattern 10: Ignoring isAccessibilityCategory for Layout Decisions

```swift
// WRONG — always horizontal, truncates at large sizes
let stack = UIStackView(arrangedSubviews: [iconView, label, detailLabel])
stack.axis = .horizontal
stack.spacing = 8
```

**Why it's wrong**: At Accessibility sizes, three views fighting for horizontal space results in severely compressed text. `iconView` and `detailLabel` take their share, leaving `label` with too little width.

**Fix**: Check `isAccessibilityCategory` and adapt.

```swift
// CORRECT
let stack = UIStackView(arrangedSubviews: [iconView, label, detailLabel])
stack.spacing = 8

func updateAxis() {
    let isAccessibility = traitCollection.preferredContentSizeCategory.isAccessibilityCategory
    stack.axis = isAccessibility ? .vertical : .horizontal
    stack.alignment = isAccessibility ? .leading : .center
}

updateAxis()
registerForTraitChanges([UITraitPreferredContentSizeCategory.self]) { (self: Self, _) in
    self.updateAxis()
}
```

---
