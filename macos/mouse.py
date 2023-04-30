from unittest.mock import Mock
import AppKit
import Quartz
from .exceptions import *


class Mouse(object):
    """Mouse events"""

    def __init__(self):
        try:
            location = AppKit.NSEvent.mouseLocation()
            self.position = (round(location.x), round(Quartz.CGDisplayPixelsHigh(0) - round(location.y)))

        except AttributeError:
            return

    @classmethod
    def EventInitScript(cls, ev, x, y, button):

        """Initalizate mouse objc x: x-pos, y:y-pos"""
        mouseEvent = Quartz.CGEventCreateMouseEvent(None,
                                                    ev, (x, y), button)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouseEvent)

    call = Mock(side_effect=EventInitScript)
    if call.called:
        raise CallError()

    def ClickEventInitScript(self, x, y, type):

        """Click initalizate function"""
        theEvent = Quartz.CoreGraphics.CGEventCreateMouseEvent(
            None,
            type,
            (x, y),
            Quartz.CoreGraphics.kCGMouseButtonLeft)
        Quartz.CoreGraphics.CGEventPost(Quartz.CoreGraphics.kCGHIDEventTap, theEvent)

    @classmethod
    def mouse_move(cls, x, y):
        """Move mouse in pointed out possition."""
        cls.EventInitScript(Quartz.kCGEventMouseMoved, x, y, 0)

    @classmethod
    def mouse_click(cls, x, y):
        """Click mouse in current position."""
        cls.EventInitScript(Quartz.CoreGraphics.kCGEventLeftMouseDown, x, y, button=2)
        cls.EventInitScript(Quartz.CoreGraphics.kCGEventLeftMouseUp, x, y, button=2)

    @classmethod
    def move_click(cls, x, y):
        """Make click and mouse-move."""
        theEvent = Quartz.CoreGraphics.CGEventCreateMouseEvent(None, 1, (x, y),
                                                               Quartz.CoreGraphics.kCGMouseButtonLeft)
        Quartz.CoreGraphics.CGEventPost(Quartz.CoreGraphics.kCGHIDEventTap, theEvent)

    def scrolling(self, turnover: int):
        scrollWheelEvent = Quartz.CGEventCreateScrollWheelEvent(
            None,
            Quartz.kCGScrollPhaseBegan,
            1,
            15 if turnover >= 0 else -15)
        Quartz.CGEventPost(Quartz.kCGHIDEventTap, scrollWheelEvent)

    @property
    def mouse_position(self):
        """Return mouse position"""
        return self.position[0], self.position[1]
