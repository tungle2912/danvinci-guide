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
let p = CGPoint(x: Double(a[1])!, y: Double(a[2])!)
let right = a.count > 3 && a[3] == "right"
let down: CGEventType = right ? .rightMouseDown : .leftMouseDown
let up: CGEventType = right ? .rightMouseUp : .leftMouseUp
let button: CGMouseButton = right ? .right : .left
requireResolveFrontmost()
let src = CGEventSource(stateID: .hidSystemState)
CGEvent(mouseEventSource: src, mouseType: .mouseMoved, mouseCursorPosition: p, mouseButton: button)?.post(tap: .cghidEventTap)
usleep(80000)
CGEvent(mouseEventSource: src, mouseType: down, mouseCursorPosition: p, mouseButton: button)?.post(tap: .cghidEventTap)
usleep(60000)
CGEvent(mouseEventSource: src, mouseType: up, mouseCursorPosition: p, mouseButton: button)?.post(tap: .cghidEventTap)
