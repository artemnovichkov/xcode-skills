# UIKit VoiceOver Patterns

## Criterion 1 — Missing accessibility labels

### Bad: Image button without label
```swift
let button = UIButton(type: .system)
button.setImage(UIImage(systemName: "trash"), for: .normal)
button.addTarget(self, action: #selector(deleteTapped), for: .touchUpInside)
```
VoiceOver announces: "Button" — no description.

### Good: Image button with label
```swift
let button = UIButton(type: .system)
button.setImage(UIImage(systemName: "trash"), for: .normal)
button.addTarget(self, action: #selector(deleteTapped), for: .touchUpInside)
button.accessibilityLabel = "Delete"
```

### Good: Button with title (auto-labeled)
```swift
let button = UIButton(type: .system)
button.setTitle("Save", for: .normal)
```
VoiceOver announces: "Save, button" — the title provides the label.

### Good: Accessible image view
```swift
let imageView = UIImageView(image: UIImage(named: "userPhoto"))
imageView.isAccessibilityElement = true
imageView.accessibilityLabel = "Profile photo"
```

## Criterion 2 — Non-human-readable labels

### Bad: File path as label
```swift
imageView.accessibilityLabel = "IMG_2847.heic"
```

### Bad: Auto-generated identifier
```swift
cell.accessibilityLabel = "cell_row_\(indexPath.row)"
```

### Good: Human-readable labels
```swift
imageView.accessibilityLabel = "Beach at sunset"
cell.accessibilityLabel = "\(contact.name), \(contact.jobTitle)"
```

## Criterion 3 — Incorrect or missing traits

### Bad: Tappable view with isAccessibilityElement but no button trait
```swift
let cardView = UIView()
cardView.isAccessibilityElement = true
cardView.accessibilityLabel = "View details"
let tap = UITapGestureRecognizer(target: self, action: #selector(cardTapped))
cardView.addGestureRecognizer(tap)
```
VoiceOver does not announce this as a button — the user does not know it is tappable.

### Good: Tappable view with correct traits
```swift
let cardView = UIView()
cardView.isAccessibilityElement = true
cardView.accessibilityLabel = "View details"
cardView.accessibilityTraits = .button
let tap = UITapGestureRecognizer(target: self, action: #selector(cardTapped))
cardView.addGestureRecognizer(tap)
```

### Good: Header label with header trait
```swift
let headerLabel = UILabel()
headerLabel.text = "Recent Items"
headerLabel.font = .preferredFont(forTextStyle: .title2)
headerLabel.accessibilityTraits = .header
```

## Criterion 4 — Inaccessible images

### Bad: UIImageView with meaningful content but no label
```swift
let imageView = UIImageView(image: UIImage(named: "productPhoto"))
imageView.contentMode = .scaleAspectFill
view.addSubview(imageView)
```
`UIImageView` has `isAccessibilityElement = false` by default — it is invisible to VoiceOver.

### Good: UIImageView with label exposed to VoiceOver
```swift
let imageView = UIImageView(image: UIImage(named: "productPhoto"))
imageView.isAccessibilityElement = true
imageView.accessibilityLabel = "Red running shoes"
```

### Good: Decorative image correctly excluded
```swift
let decorativeView = UIImageView(image: UIImage(named: "separator"))
decorativeView.isAccessibilityElement = false
```

## Criterion 5 — Missing isAccessibilityElement

### Bad: Custom interactive view not exposed to VoiceOver
```swift
class RatingView: UIView {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        updateRating(from: touches)
    }
}
```
This view handles touches but is not an accessibility element — VoiceOver users cannot interact with it.

### Good: Custom interactive view exposed to VoiceOver
```swift
class RatingView: UIView {
    override init(frame: CGRect) {
        super.init(frame: frame)
        isAccessibilityElement = true
        accessibilityLabel = "Rating"
        accessibilityTraits = .adjustable
    }

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        updateRating(from: touches)
    }

    override func accessibilityIncrement() { increaseRating() }
    override func accessibilityDecrement() { decreaseRating() }
}
```

### Additional traits (recommendations)

#### Selected state on a segmented control item

```swift
let tab = TabButton()
tab.accessibilityTraits = isSelected ? [.button, .selected] : .button
```

#### Updates-frequently for a live counter

```swift
let timerLabel = UILabel()
timerLabel.font = .monospacedDigitSystemFont(ofSize: 24, weight: .regular)
timerLabel.accessibilityTraits = .updatesFrequently
```

#### Search field for a custom filter input

```swift
let searchTextField = UITextField()
searchTextField.placeholder = "Search items"
searchTextField.accessibilityTraits = .searchField
```

#### Adjustable rating control

```swift
class RatingView: UIView {
    override init(frame: CGRect) {
        super.init(frame: frame)
        isAccessibilityElement = true
        accessibilityLabel = "Rating"
        accessibilityTraits = .adjustable
    }
    override var accessibilityValue: String? {
        get { "\(rating) of 5" } set {}
    }
    override func accessibilityIncrement() { rating = min(rating + 1, 5) }
    override func accessibilityDecrement() { rating = max(rating - 1, 0) }
}
```

## Element grouping (informational)

### Recommendation: Group related elements in a cell
```swift
// Before: VoiceOver focuses on each label separately
let nameLabel = UILabel()
let subtitleLabel = UILabel()
let priceLabel = UILabel()
stackView.addArrangedSubview(nameLabel)
stackView.addArrangedSubview(subtitleLabel)
stackView.addArrangedSubview(priceLabel)

// After: Group into a single accessibility element
stackView.isAccessibilityElement = true
stackView.accessibilityLabel = "\(name), \(subtitle), \(price)"
// Or:
stackView.shouldGroupAccessibilityChildren = true
```

## Custom actions (informational)

### Cell with editing actions but no custom actions

```swift
// Sighted users get swipe-to-delete; VoiceOver users do not
override func tableView(_ tableView: UITableView,
                        trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath)
                        -> UISwipeActionsConfiguration? {
    UISwipeActionsConfiguration(actions: [
        UIContextualAction(style: .destructive, title: "Delete") { _, _, done in
            self.delete(indexPath); done(true)
        }
    ])
}
```

### Same cell, exposed via accessibilityCustomActions

```swift
override func tableView(_ tableView: UITableView,
                        cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = ...
    cell.accessibilityCustomActions = [
        UIAccessibilityCustomAction(name: "Delete") { [weak self] _ in
            self?.delete(indexPath); return true
        }
    ]
    return cell
}
```

## Reading order (informational)

### Override `accessibilityElements` to set reading order

```swift
class HeroCard: UIView {
    let titleLabel = UILabel()
    let subtitleLabel = UILabel()
    let badgeView = UIView()

    override var accessibilityElements: [Any]? {
        get { [badgeView, titleLabel, subtitleLabel] }
        set {}
    }
}
```

