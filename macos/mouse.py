import Quartz.CoreGraphics
import time


class MouseController:
    def move_mouse(self, x, y):
        move_event = Quartz.NSEvent.mouseEventWithType_location_modifierFlags_timestamp_windowNumber_context_eventNumber_clickCount_pressure_(
            Quartz.NSEventTypeMouseMoved,
            Quartz.NSPoint(x, y),
            0,
            Quartz.CGEventGetTimestamp(Quartz.CGEventCreate(None)),
            0,
            None,
            0,
            0,
            0.5
        )

        Quartz.CGEventPost(Quartz.kCGHIDEventTap, move_event.CGEvent())

    def click_mouse(self, x, y):

        self.move_mouse(x, y)
        time.sleep(0.1)

        down_event = Quartz.NSEvent.mouseEventWithType_location_modifierFlags_timestamp_windowNumber_context_eventNumber_clickCount_pressure_(
            Quartz.NSEventTypeLeftMouseDown,
            Quartz.NSPoint(x, y),
            0,
            Quartz.CGEventGetTimestamp(Quartz.CGEventCreate(None)),
            0,
            None,
            0,
            0,
            0.5
        )
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, down_event.CGEvent())

        up_event = Quartz.NSEvent.mouseEventWithType_location_modifierFlags_timestamp_windowNumber_context_eventNumber_clickCount_pressure_(
            Quartz.NSEventTypeLeftMouseUp,
            Quartz.NSPoint(x, y),
            0,
            Quartz.CGEventGetTimestamp(Quartz.CGEventCreate(None)),
            0,
            None,
            0,
            0,
            0.5
        )
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, up_event.CGEvent())

    def scroll_mouse(self, to):
        scroll_event = Quartz.CGEventCreateScrollWheelEvent(None, 
                                                            0, 
                                                            Quartz.CoreGraphics.kCGScrollEventUnitLine,
                                                            to)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, scroll_event)

    def location(self):
        return Quartz.NSEvent.mouseLocation()

