"""

Individual exceptions for driver_controller

"""


try:
    exc = ExceptionGroup
except NameError:
    exc = ReferenceError


class ApplicationNameError(NameError):
    """
     App with pointed out name not exist.
    """


class ApplicationNotExist(SystemError):
    """
    Application, which you point outed is not exist
    """


class UnsupportedFormat(FileExistsError):
    """
    Method screenshot support only ['png', 'jpg', 'ico', 'gif', 'pict'] formats.
    """


class ConfirmationError(TypeError):
    """
    If confirmation is [False].
    """


class InvalidExtension(NameError):
    """
    No extension specified.
    """


class WifiNameConnectError(NameError):
    """
    Password or SSID/Wi-fi name of Network is not right.
    """


class ValueBrightnessError(ValueError, TypeError):
    """
    Value is not type [int].
    """


class WifiValueError(ValueError, BaseException):
    """
    There is no wi-fi network in util "bunch keys".
    """


class ExtensionError(ValueError):
    pass


class PathError(FileNotFoundError):
    pass


class CallError(exc):
    pass


class RgbValueError(ValueError):
    """No available color for bg"""
    pass


class OpenPossibilityError(FileExistsError):
    """Can not open file in that app."""


class ScreenErrorIndex(IndexError):
    """Screen ID not exist."""
    
    
class ScreenWarning(Warning):
    """Not support bridge with objective-c and python via IOKit."""


class BluetoothConnectionError(ConnectionRefusedError):
    """Specify not right address to pair."""
    
# END FILE
