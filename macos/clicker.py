from .CONSTANTS import KeyHexType
import AppKit

class Clicker(object):
    """Click keys"""

    def press(self, key, hotkey: bool):
        """Press key via >>> AppKit"""
        import Quartz
        try:
            if hotkey:
                try:
                    key = KeyHexType[key]
                except KeyError:
                    raise KeyError(f'No special key named {repr(key)}')
            else:
                key = KeyHexType[key]
        except KeyError:
            raise ValueError(
                f'Method {repr(self.press.__name__)} support only 1 letter. Use {repr(self.write.__name__)}.')

        ev = Quartz.CGEventCreateKeyboardEvent(None,
                                               Quartz.CGEventTapLocation(key),
                                               Quartz.CGEventType(100))
        Quartz.CGEventPost(0, ev)

    def write(self, text):
        """Write text"""
        for i in text:
            self.press(key=i, hotkey=False)

    def press_hot_key(self, key):
        import Quartz
        if len(key) > 1:
            try:
                key = KeyHexType[key]
                ev = Quartz.CGEventCreateKeyboardEvent(None,
                                                       Quartz.CGEventTapLocation(key),
                                                       Quartz.CGEventType(100))
                Quartz.CGEventPost(Quartz.kCGHIDEventTap, ev)
            except KeyError:
                raise KeyError('Can not find hot key named {}'.format(repr(key)))

