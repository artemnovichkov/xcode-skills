# Platform-Specific VoiceOver Considerations

This doc captures behaviors that vary across Apple platforms and are not adequately
covered by the per-framework patterns. Read this in addition to the SwiftUI/UIKit/
AppKit references when auditing code targeting these platforms.

## iOS

Default platform. The patterns in `uikit-patterns.md` and `swiftui-patterns.md`
apply directly. No iOS-specific quirks affect the five hard FAIL criteria.

## iPadOS

Uses UIKit / SwiftUI identically to iOS for VoiceOver. Two iPad-specific
traits worth noting on hover-affordance views:

- `.accessibilityRespondsToUserInteraction` — set when a non-control view
  becomes tappable through a pointer/keyboard.
- Pointer hover does not change VoiceOver behavior; do not gate accessibility
  on pointer presence.

## macOS

Uses AppKit / SwiftUI. Key differences from iOS captured in
`appkit-patterns.md`:

- AppKit uses `setAccessibilityRole()` instead of `accessibilityTraits`.
- Standard NSControls are accessible by default; custom NSViews are not.
- VoiceOver on macOS uses different gestures (VO+arrow keys, VO+Space).
  Code does not change because of this; just be aware that "tappable" on
  macOS means "clickable / VO-Space-activatable".

## tvOS

Uses UIKit + SwiftUI. The focus engine drives navigation, but VoiceOver
still operates as a separate layer.

- A view that is `.focusable(true)` is not automatically a VoiceOver
  element. If a custom focusable view handles `pressesBegan` or a
  `UITapGestureRecognizer`, it still needs `isAccessibilityElement = true`
  + `accessibilityLabel` + `.button` trait, exactly like iOS.
- SwiftUI: `Button { ... } label: { ... }` is auto-accessible. A
  `.focusable()` modifier with `.onTapGesture` is **not** — apply
  `.accessibilityLabel` and `.accessibilityAddTraits(.isButton)`.

## watchOS

Uses SwiftUI. Two watchOS-specific accessibility surfaces:

- **Digital Crown / adjustable values** — Slider-like custom views must
  attach `.accessibilityAdjustableAction { direction in ... }`. The Crown
  maps to VoiceOver increment/decrement when this is set; the adjustable
  role is implicit, no separate trait is required in SwiftUI.
- **Limited screen real estate makes grouping more important** — the
  Recommendations section of the audit should call out cards/rows that
  would benefit from `.accessibilityElement(children: .combine)` more
  aggressively on watchOS.

## visionOS

Uses SwiftUI primarily, plus UIKit for catalysed apps. visionOS-specific
notes:

- Eye + pinch input does not change accessibility-element requirements.
  A view that is tappable via pinch must still have a label and the
  button trait if it is custom.
- Spatial containers (`RealityView`, `Model3D`) need explicit
  `.accessibilityLabel` — the system cannot describe 3D content.
- `.accessibilityRotor` is fully supported and especially useful in
  spatial UIs where focus order is hard to predict.

## How to use this doc during an audit

1. Identify the deployment platforms from the file's imports
   (`import WatchKit`, `import UIKit` + tvOS-specific symbols, etc.) or
   from the surrounding project context.
2. Apply the framework patterns first.
3. Layer on platform-specific behavior from this doc only when the file
   targets a non-default platform.
4. Platform behavior never changes the five hard FAIL criteria — it only
   adds context for recommendations and trait selection.
