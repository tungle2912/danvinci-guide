import CoreGraphics
import Foundation
import AppKit
func requireResolveFrontmost() {
    guard NSWorkspace.shared.frontmostApplication?.bundleIdentifier == "com.blackmagic-design.DaVinciResolve" else {
        FileHandle.standardError.write("Resolve không ở trên cùng, bỏ qua\n".data(using: .utf8)!)
        exit(1)
    }
}
let a = CommandLine.arguments
let from = CGPoint(x: Double(a[1])!, y: Double(a[2])!)
let to = CGPoint(x: Double(a[3])!, y: Double(a[4])!)
requireResolveFrontmost()
let src = CGEventSource(stateID: .hidSystemState)
func post(_ type: CGEventType, _ p: CGPoint) {
    CGEvent(mouseEventSource: src, mouseType: type, mouseCursorPosition: p, mouseButton: .left)?.post(tap: .cghidEventTap)
}
post(.mouseMoved, from)
usleep(100000)
post(.leftMouseDown, from)
usleep(150000)
let steps = 30
for i in 1...steps {
    let t = Double(i) / Double(steps)
    post(.leftMouseDragged, CGPoint(x: from.x + (to.x - from.x) * t, y: from.y + (to.y - from.y) * t))
    usleep(20000)
}
usleep(200000)
requireResolveFrontmost()
post(.leftMouseUp, to)
