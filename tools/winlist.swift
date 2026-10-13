import CoreGraphics
let opts = CGWindowListOption(arrayLiteral: .optionAll)
if let wins = CGWindowListCopyWindowInfo(opts, kCGNullWindowID) as? [[String: Any]] {
  for w in wins {
    let owner = w[kCGWindowOwnerName as String] as? String ?? ""
    let layer = w[kCGWindowLayer as String] as? Int ?? -1
    if owner.contains("Resolve") && layer == 0 {
      let id = w[kCGWindowNumber as String] as? Int ?? 0
      let b = w[kCGWindowBounds as String] as? [String: Any] ?? [:]
      let name = w[kCGWindowName as String] as? String ?? ""
      print(id, owner, "|", name, "|", b["Width"] ?? 0, "x", b["Height"] ?? 0)
    }
  }
}
