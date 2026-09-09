# SwiftUI VoiceOver Patterns

## Criterion 1 — Missing accessibility labels

### Bad: Icon-only button without label
```swift
Button {
    viewModel.delete()
} label: {
    Image(systemName: "trash")
}
```
VoiceOver announces: "Button" — no description of what the button does.

### Good: Icon-only button with explicit label
```swift
Button {
    viewModel.delete()
} label: {
    Image(systemName: "trash")
}
.accessibilityLabel("Delete")
```

### Good: Button with text content (auto-labeled)
```swift
Button("Save") {
    viewModel.save()
}
```
VoiceOver announces: "Save, button" — the text content provides the label automatically.

### Good: Button with Label (auto-labeled)
```swift
Button {
    openSettings()
} label: {
    Label("Settings", systemImage: "gear")
}
```
VoiceOver announces: "Settings, button" — the Label's text provides the accessibility label.

### Good: Toggle, Picker, Slider with title (auto-labeled)
```swift
Toggle("Dark Mode", isOn: $isDark)
Picker("Sort by", selection: $sort) { ... }
Slider(value: $volume, in: 0...1, label: { Text("Volume") })
```
The title parameter provides the label automatically.

## Criterion 2 — Non-human-readable labels

### Bad: Programmer identifier as label
```swift
Button {
    submit()
} label: {
    Image(systemName: "paperplane")
}
.accessibilityLabel("btn_submit_v2_final")
```

### Bad: File name as label
```swift
Image("hero_banner")
    .accessibilityLabel("hero_banner.png")
```

### Good: Human-readable labels
```swift
Button { submit() } label: { Image(systemName: "paperplane") }
    .accessibilityLabel("Send message")

Image("hero_banner")
    .accessibilityLabel("Mountain landscape at sunset")
```

## Criterion 3 — Incorrect or missing traits

### Bad: Custom tappable view without button trait
```swift
Text("Show Details")
    .padding()
    .background(.blue)
    .foregroundStyle(.white)
    .cornerRadius(8)
    .onTapGesture { showDetails = true }
```
VoiceOver announces as static text — the user does not know it is tappable.

### Good: Custom tappable view with button trait and label
```swift
Text("Show Details")
    .padding()
    .background(.blue)
    .foregroundStyle(.white)
    .cornerRadius(8)
    .onTapGesture { showDetails = true }
    .accessibilityAddTraits(.isButton)
```

### Bad: Section header without header trait
```swift
Text("Recent Items")
    .font(.title2)
    .bold()
```
VoiceOver will not include this in the headings rotor.

### Good: Section header with header trait
```swift
Text("Recent Items")
    .font(.title2)
    .bold()
    .accessibilityAddTraits(.isHeader)
```

## Criterion 4 — Inaccessible images

### Bad: Meaningful image without label
```swift
Image("userAvatar")
    .resizable()
    .frame(width: 60, height: 60)
    .clipShape(Circle())
```

### Good: Meaningful image with label
```swift
Image("userAvatar")
    .resizable()
    .frame(width: 60, height: 60)
    .clipShape(Circle())
    .accessibilityLabel("Profile photo")
```

### Good: Decorative image correctly excluded
```swift
Image(decorative: "backgroundPattern")
    .resizable()
```

### Good: Decorative image hidden from VoiceOver
```swift
Image("dividerLine")
    .accessibilityHidden(true)
```

### Good: SF Symbol inside a labeled container
```swift
Label("Favorites", systemImage: "heart.fill")
```
The Label provides the text — the SF Symbol does not need its own label.

### Bad: Variable image with unclear intent
```swift
Image(item.imageName)
    .resizable()
    .frame(width: 80, height: 80)
```
Cannot determine if decorative. Should either add `.accessibilityLabel()` or `.accessibilityHidden(true)`.

### Additional traits (recommendations)

#### Selected state in a segmented picker

```swift
ForEach(tabs, id: \.self) { tab in
    Text(tab.title)
        .onTapGesture { selection = tab }
        .accessibilityAddTraits(selection == tab ? [.isButton, .isSelected] : .isButton)
}
```

#### Updates-frequently for a live counter

```swift
Text(timerString)
    .font(.system(.title, design: .monospaced))
    .accessibilityAddTraits(.updatesFrequently)
```

#### Search field for a custom filter input

```swift
TextField("Search items", text: $query)
    .accessibilityAddTraits(.isSearchField)
```

#### Adjustable view with crown / increment+decrement

```swift
Text("\(rating) of 5")
    .accessibilityElement()
    .accessibilityLabel("Rating")
    .accessibilityValue("\(rating) of 5")
    .accessibilityAdjustableAction { direction in
        switch direction {
        case .increment: rating = min(rating + 1, 5)
        case .decrement: rating = max(rating - 1, 0)
        @unknown default: break
        }
    }
```

## Element grouping (informational)

### Recommendation: Combine related elements in a card
```swift
// Before: VoiceOver focuses on each element separately (verbose)
VStack {
    Image("product")
    Text("Widget Pro")
    Text("$9.99")
    Text("In Stock")
}

// After: VoiceOver reads the card as one unit
VStack {
    Image("product")
    Text("Widget Pro")
    Text("$9.99")
    Text("In Stock")
}
.accessibilityElement(children: .combine)
```

## Custom actions (informational)

### List row with swipe actions but no custom action

```swift
// Before — only sighted users can delete
ForEach(items) { item in
    Text(item.title)
        .swipeActions {
            Button("Delete", role: .destructive) { delete(item) }
        }
}
```

### List row with both swipe and custom action

```swift
ForEach(items) { item in
    Text(item.title)
        .swipeActions {
            Button("Delete", role: .destructive) { delete(item) }
        }
        .accessibilityAction(named: "Delete") { delete(item) }
}
```

### Multiple custom actions on a row

```swift
Text(item.title)
    .accessibilityAction(named: "Archive") { archive(item) }
    .accessibilityAction(named: "Pin") { pin(item) }
    .accessibilityAction(named: "Delete") { delete(item) }
```

## Reading order (informational)

### ZStack overlay read last by default

```swift
ZStack {
    MainContent()           // read first by default
    BannerOverlay()         // read second — but visually on top
}
```

### Promote the overlay to read first

```swift
ZStack {
    MainContent()
    BannerOverlay()
        .accessibilitySortPriority(1)
}
```
