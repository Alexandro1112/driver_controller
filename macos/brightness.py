import warnings
from time import sleep
from warnings import simplefilter
from .exceptions import ValueBrightnessError, ScreenWarning
import subprocess
import Foundation
import Quartz
from ColorSync import *


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
            raise ScreenWarning('No has access to IOKit and display ID.')
        return self.get_cur_brightness_per[-1]

    def set_color_profile(self, profile_path):

        graphics_path = f'file://{profile_path}'
        display_uuid = CGDisplayCreateUUIDFromDisplayID(Quartz.CGMainDisplayID())
        fullURL = Foundation.CFURLCreateWithString(objc.NULL, graphics_path, objc.NULL)
        config_new = NSDictionary({kColorSyncDeviceDefaultProfileID: fullURL})
        success = ColorSyncDeviceSetCustomProfiles(kColorSyncDisplayDeviceClass, display_uuid, config_new)
        if not success:
            raise ImportError(f'Can not import color profile named {profile_path}, or it not support.')

    def get_color_profile(self):
        display_uuid = CGDisplayCreateUUIDFromDisplayID(Quartz.CGMainDisplayID())
        colorInfo = ColorSyncDeviceCopyDeviceInfo(kColorSyncDisplayDeviceClass, display_uuid)
        return dict(dict(colorInfo['FactoryProfiles'])['1'])['DeviceProfileURL']
