import CoreLocation
from warnings import simplefilter
import CoreWLAN
import subprocess
from time import sleep
import objc
import Quartz
import Foundation
import _sysconfigdata__darwin_darwin as dar


iokit = None
def init():
    global iokit
    iokit = {}

    iokitBundle = objc.initFrameworkWrapper(
        "IOKit",
        frameworkIdentifier="com.apple.iokit",
        frameworkPath=objc.pathForFramework("/System/Library/Frameworks/IOKit.framework"),
        globals=globals()
    )

    # The IOKit functions to be retrieved
    functions = [
        ("IOServiceGetMatchingServices", b"iI@o^I"),
        ('IODisplayGetIntegerRangeParameter', b"II^{__CFString=}^i^ii"),
        ('IOHIDDeviceActivate', b'^{__IOHIDDevice=}v'),
        ('IODisplayCreateInfoDictionary', b'II^{__CFDictionary=}')

    ]
    objc._objc.loadBundleFunctions(iokitBundle, iokit, functions)

class SystemConfig(object):
    """Data about mac"""
    simplefilter('ignore')

    simplefilter("default")

    def __init__(self):
        global iokit
        manager = CoreLocation.CLLocationManager.alloc().init()
        manager.delegate()
        manager.startUpdatingLocation()
        while CoreLocation.CLLocationManager.authorizationStatus() != 3 or manager.location() is None:
            sleep(0.01)
        coord = manager.location().coordinate()
        self.lat = coord.latitude
        self.lon = coord.longitude
        self.percent = iokit['IOPSCopyPowerSourcesByType'](0)[0]['Current Capacity']  # ignore: noqa 401
        self.vers = subprocess.getoutput(cmd="sw_vers -productVersion")
        self.net = CoreWLAN.CWInterface.interfaceWithName_("en0")
        self.size = iokit['IODisplayCreateInfoDictionary'](Quartz.CGDisplayIOServicePort(Quartz.CGMainDisplayID()), 0)[
                        'resolution-preview-width'] * 10, \
                    iokit['IODisplayCreateInfoDictionary'](Quartz.CGDisplayIOServicePort(Quartz.CGMainDisplayID()), 0)[
                        'resolution-preview-height'] * 10
        self.mem_size = subprocess.getoutput(cmd='sysctl -a | grep \'^hw\.m\'')
        self.processor = subprocess.getoutput(cmd='sysctl -n machdep.cpu.brand_string')
        self.num = 'system_profiler SPHardwareDataType | grep x "Serial Number (system)"'
        self.disk_mem = 'diskutil list | grep GUID_partition_scheme'  # Diskutil not found: https://superuser.com/questions/213088/diskutil-command-not-found-in-os-x-terminal
        self.video_crd_nm = subprocess.getoutput(
            cmd='system_profiler SPDisplaysDataType | grep "Chipset Model"')  # system profiler: command not found https://github.com/jlhonora/lsusb/issues/12?ysclid=ldu37f5jk9865312203
        self.temp = subprocess.getoutput(
            cmd='sysctl machdep.xcpm.cpu_thermal_level sysctl machdep.xcpm.gpu_thermal_level')

        self.name = Foundation.NSUserName()

    @property
    def devise_battery(self):
        """
     Return battery percent of
     computer at current time.
     :return: Battery percent [str]
     """
        return f'Battery percent: {self.percent}'

    @property
    def macos_version(self):
        """
     Function.
     :return: Version your devise.
     """
        return self.vers

    @property
    def current_connected_wifi_network(self):
        """
     Return current wi-fi network.
     :return: Current wi-fi network,
     which you connect to.
     (Available only on Mac-os)
     """

        return self.net.ssidData().decode('ascii')

    @property
    def screen_size(self):
        """
       Screen size of your mac-book.
       :return: screen size
       """

        return self.size

    @property
    def get_processor_name(self):
        """
     Return current processor name
     :return: Processor mark
     """
        return self.processor

    @property
    def memory_size(self):
        return int(self.mem_size.split(': ')[-1]) / pow(1024, 3)

    @property
    def get_mac_serial_number(self):
        return subprocess.getoutput(cmd=self.num).strip().split(': ')[-1]

    @property
    def get_disk_memory(self):
        """Return disk meomory."""
        return subprocess.getoutput(cmd=self.disk_mem).replace('*', '').split()[2] + 'Gb'

    @property
    def get_video_card_name(self):
        """Return vide card name"""
        return self.video_crd_nm.strip().split(':')[-1]

    def sensor_temperature(self):
        return round(int(self.temp.split('\n')[0].split(':')[-1]))

    @property
    def mac_name(self):
        return self.name

    @property
    def darwin_version(self):
        if dar is None:
            return ""
        return dar.build_time_vars['BUILD_GNU_TYPE']

    def mac_location(self):
        """Return mac location from geolocation-service. Enable this functions for python.
        System Preferences -> Security and Privacy -> allow geolocation services for python.
        More info: https://howtoenable.net/how-to-enable-geolocation-on-mac/"""

        return (self.lat, self.lon)

    def mac_address(self):
        """Return mac address in format  XX:XX:XX:XX:XX:XX(not show him)"""
        return self.net.hardwareAddress().split()[-1]