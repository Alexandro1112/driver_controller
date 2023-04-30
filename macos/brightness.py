from time import sleep
from warnings import simplefilter
import Quartz
from .exceptions import *
import subprocess


class Brightness(object):
    """Set brightness"""

    def __init__(self):
        global iokit
        simplefilter("ignore")
        iokit = dict(iokit)
        simplefilter("default")

        self.get_cur_brightness_per = iokit["IODisplayGetFloatParameter"](
            Quartz.CGDisplayIOServicePort(Quartz.CGMainDisplayID()),
            0,
            iokit["kDisplayBrightness"], None)

    def set_brightness(self, brightness_percent: [int, float]):
        """
     Automatically set brightness
     percent [type - float]
     example: 0.25; 0.50; 0.75; 0.1(max)
     :param brightness_percent:
     :return: Successfully.
     P.s: will be show warning:
     /Library/Frameworks/Python.framework/Versions/X.XX/lib/pythonX.XX/site-packages/objc/_bridgesupport.py
     :666: RuntimeWarning: Error parsing BridgeSupport data for IOKit: Invalid array definition in type
     signature: [255{ATASMARTLogEntry}}
     warnings.warn(...). Ignore them.
     """

        success = Quartz.IKMonitorBrightnessController.alloc().setBrightnessOnAllDisplays_(brightness_percent)
        if not success is None:
            raise ValueBrightnessError('Brightness must be type: int, float')

    def set_max_brightness(self):
        """
     Set max brightness of
     screen equal one hundred.
     :return: Successfully
     """
        self.set_brightness(1.0)

    def set_min_brightness(self):
        """
     Set min brightness of
     screen equal zero.
     :return: Successfully
     """

        self.set_brightness(0.0)

    def increase_brightness(self, division):
        """Increase brightness by 1 division"""
        if division >= 1:
            for repeat in range(division + 2):
                subprocess.getoutput(
                    cmd="""osascript -e 'tell application "System Events"' -e 'key code 144' -e ' end tell'""")
        else:
            division = division.imag
        division += 1

    def decrease_brightness(self, division: int):
        if division >= 1:
            for repeat in range(division + 2):
                subprocess.getoutput(
                    cmd="""osascript -e 'tell application "System Events"' -e 'key code 145' -e ' end tell'""")
        else:
            division = division.imag
        division += 1

    def sleep_mac(self, pause: [int, float]):
        """Sleep Mac"""
        sleep(pause)
        subprocess.getoutput(cmd="osascript - e 'tell application \"finder\" to sleep'")

    @property
    def get_brightness(self):
        """Get brightness percent"""
        if self.get_cur_brightness_per[0] != 0:
            raise ScreenWarning('Not support bridge objective-c and python via IOKit.')
        return self.get_cur_brightness_per[-1]
