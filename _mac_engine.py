# /opt/anaconda3/bin/python
##############################################################################
# Copyright (c) 2022-2023 Aleksandr Bosov. All rights reserved.              #
# The library is designed for Mac-OS, performs technical                     #
# functions such as disabling Wi-Fi, Bluetooth, sends ,                      #
# notifications: text, sound, recording audio, working with scree brightness #
# control devises and much more, pair to bluetooth.                          #
##############################################################################
# |---------------------------------------------------------------------------------------------------------------------|
#                                                   ||PYTHON-INSTALLATION||
# If you cloned this repository trough github,
# dependencies commands such as [blueutil, brew, brightness, ffmpeg, terminal-notifier]
# successful installed. Dont forget about commands:
# I COMMAND - [ pip3 install loger ]
# II COMMAND = [ pip3 install plyer ]
# III COMMAND = [ pip3 install sounddevice ]
# IIII COMMAND = [ pip3 install -U pyobjc ]
# If code not working, though git submodules
# exist in git-hub repository: complete few commands:
# INSTALL || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" OR
# REINSTALL (if need)|| /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# LIB - INSTALLER || brew install brightness || brew doctor || brew install blueutil ||
# 'brew install ffmpeg' OR 'sudo port install ffmpeg' || if "command port not founded: then:
#                                               ||PORT-INSTALLATION ||
# I COMMAND - [export PATH=/opt/local/bin:/opt/local/sbin:$PATH]
# II COMMAND - [export DISPLAY=:0.0]
# III COMMAND - [port](Successful installed port)
# |---------------------------------------------------------------------------------------------------------------------|
#  Any files which already installed in
#  OS Mac in System files, if they not exist - code will not working.
#  /System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/ ||
#  /System/Library/Sounds/Pop.aiff  ||
#  /System/Library/Sounds/Blow.aiff ||
#  /System/Library/Sounds/Glass.aiff ||
#  /System/Library/Sounds/Funk.aiff  ||
#  /System/Library/Sounds/Submarine.aiff ||
#  /System/Library/Sounds/Sosumi.aiff ||
# How check this?
# Finder -> Go -> Go to folder -> /System/
# input the file-path which I wrote.
# TESTED BY Mac Os Big Sur 11.4.7(+), Mac os Catalina(+) 10.15.7, Mac Os High Mojave(confirm osascript) 10.13
# TODO: Make more classes
#                                            Finally, run code.

import warnings


import mutagen.mp3
# Os
import os

# for full paths
import pathlib

# all process
import subprocess

# check platform OS
import sys

# Unplug warnings, unexpected errors
from unittest.mock import Mock

# pause for methods
from time import (sleep, ctime)

# Parse xml
from xml.etree import ElementTree

# Constants
from .CONSTANTS import KeyHexType
# Platform
import platform

from warnings import simplefilter
# Exceptions for methods
from .exceptions import *

try:
     # WARNING: Any mac-os not support this config-file.
     import _sysconfigdata__darwin_darwin as dar
except:
     dar = None

try:
     import CoreLocation

     import SystemConfiguration
     import pyperclip

     # Mouse-click
     import Quartz
     import Quartz.CoreGraphics

     # Play sound
     import Foundation

     # for get list applications
     from psutil import process_iter

     # Sound-devises
     from sounddevice import query_devices
     # Screen size
     import AppKit

     import CoreWLAN

     # Session beetwen bridge objcetive-c
     from objc._framework import infoForFramework
     import objc
     import objc._objc

     import CoreFoundation

     # Unplug warnings, unexpected errors
     from shutup import please

     from PIL import Image
except:
     assert 'Installing Quartz, psutil, loger, pyobjc, AppKit, sounddevice pillow'

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

     IOKit = Foundation.NSBundle.bundleWithIdentifier_('com.apple.framework.IOKit')

     functions = [('IOServiceGetMatchingService', b'II@'),
                  ('IOServiceMatching', b'@*'),
                  ("IODisplayGetFloatParameter", b'iII@o^f'),
                  ("IODisplayGetIntegerRangeParameter", b'I'),
                  ('IORegistryEntryCreateCFProperties', b'IIo^@@I'),
                  ('IOPSCopyPowerSourcesByType', b'@I'),
                  ('IODisplaySetFloatParameter', b'iII@f'),
                  ("IOHIDGetActivityState", b'IBi')
                  ]



     variables = [
       ("kIODisplayNoProductName", b"I"),
       ("kIOMasterPortDefault", b"I"),
       ("kIODisplayOverscanKey", b"*"),
       ("kDisplayVendorID", b"*"),
       ("kDisplayProductID", b"*"),
       ("kDisplaySerialNumber", b"*"),
     ]


     objc._objc.loadBundleFunctions(iokitBundle, iokit, functions)
     objc._objc.loadBundleFunctions(IOKit, globals(), functions)
     objc._objc.loadBundleVariables(iokitBundle, globals(), variables)

     for var in variables:
       key = "{}".format(var[0])
       if key in globals():
           iokit[key] = globals()[key]

     iokit["kDisplayBrightness"] = CoreFoundation.CFSTR("brightness")
     iokit["kDisplayUnderscan"] = CoreFoundation.CFSTR("pscn")


if sys.platform == 'darwin' and int(platform.mac_ver()[0].split('.')[0]) > 8 and \
        int(sys.version.split(' | ')[0].split('.')[0]) >= 3 and \
        int(sys.version.split(' | ')[0].split('.')[1]) >= 7:  # Mac version from 10.6 until 10.8 not support.
     class MacCmd:
          """Class with subclasees."""

          class OutputListsDevises(object):
               """ Return output devises """

               def __init__(self):
                    self.bluetooth = subprocess.getoutput(cmd='system_profiler SPBluetoothDataType')
                    self.devises = query_devices()

               def get_list_wifi_networks(self):
                    """ Function output all wi-fi networks,
                    which available for your devise."""
                    if 'loadBundle' in dir(objc):
                         pass
                    else:
                         raise AttributeError

                    wifi = []
                    wifi2 = []

                    bundle_path = '/System/Library/Frameworks/CoreWLAN.framework'

                    dir(objc._objc.loadBundle(infoForFramework(bundle_path)[1], bundle_path=bundle_path,
                                              module_globals=globals()))

                    response = CoreWLAN.CWInterface.interface()
                    r = response.scanForNetworksWithName_includeHidden_error_(None, True, None)

                    for i in range(1, len(str(r).split('>')), 2):
                         wifi.append(str(r).split('>')[i].split(',')[0] + ']')

                    for items in wifi:
                         wifi2.append(items.strip().replace('ssid', '').replace('[', '').replace(']', '').replace('=',
                                                                                                                  '').strip())

                    yield set(sorted(wifi2))

               def get_list_bluetooth_device(self):
                    """ Function output all bluetooth devise(s),
                  which available for your devise."""

                    return self.bluetooth.split('Bluetooth:')[0] if not self.bluetooth.split('Bluetooth:')[0].strip() == \
                                                                        '' else None

               def get_list_cameras(self):

                    self.resp, _ = subprocess.Popen(
                         "system_profiler -xml SPCameraDataType",
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         close_fds=False
                    ).communicate()

                    last_text = None
                    cameras = []

                    for node in ElementTree.fromstring(self.resp).iterfind("./array/dict/array/dict/*"):
                         if last_text == "_name":
                              cameras.append(node.text)
                         last_text = node.text

                    return cameras

               def get_list_audio_devises(self):
                    """
                 Return all audio
                 connectable devises.
                 :return: devises
                 (Available only on Mac-os)
                 """

                    return self.devises

          class BlueTooth(object):
               def __init__(self):
                    self.bluetooth = subprocess.getoutput(cmd='system_profiler SPBluetoothDataType')
                    objc._objc.loadBundle('IOBluetooth', globals(),
                                          bundle_path=u'/System/Library/Frameworks/IOBluetooth.framework')
                    devices = IOBluetoothDevice  # Ignore error.IOBluetoothDevice not objective-class,
                                                                   # and when i packing him in objc.loadBundle i
                                                                   # got error, tied with subcridiable.
                    address = devices.recentDevices_(0)

                    for Query_Devises in address:
                         self.device = Query_Devises

               def get_paired_devices(self):
                    return (self.device.getNameOrAddress())

               def get_all_address(self):
                    """[0] or [1]"""
                    ADDRESID = subprocess.getoutput(cmd='system_profiler SPBluetoothDataType | grep Address').split('Address')[1:]
                    ADDRESID = set(ADDRESID)
                    for ID in ADDRESID:
                         yield ID.rstrip().replace(':', '').lstrip()
               def pair_to_devise(self, address, duration_pair):
                    try:
                         device = IOBluetoothDevice.withAddressString_(address)
                         device.openConnection()
                         device.openConnection_withPageTimeout_authenticationRequired_(None, duration_pair, False)
                    except AttributeError:
                         raise BluetoothConnectionError(f'Can not connect to devise, with address {repr(address)}')
          class Wifi(object):
               """Connect to wi-fi networks/ Data about wifi."""

               def __init__(self):
                    import CoreWLAN
                    self.interface = CoreWLAN.CWInterface.interfaceWithName_("en0")

                    self.speed = subprocess.getoutput(cmd='airport -I | grep maxRate')
                    self.last_speed = subprocess.getoutput(cmd='airport -I | grep lastTxRate')
                    self.secT = subprocess.getoutput(cmd='airport -I | grep "link auth"')

               @staticmethod
               def connectTo(wifi_network, password):
                    """
                 Auto connect to wi-fi network.
                 :param wifi_network: Wi-fi name, which you would to connect.
                 :param password: Password of this Network.(use hide variable)
                 :return: 'Successful...' if you successfully connect to wi-fi.
                 """

                    objc._objc.loadBundle('CoreWLAN',
                                          bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
                                          module_globals=globals())

                    iface = CoreWLAN.CWInterface.interface()

                    networks, error = iface.scanForNetworksWithName_error_(wifi_network, None)

                    network = networks.anyObject()

                    success_connect, error = iface.associateToNetwork_password_error_(network, password, None)
                    if error:
                         raise WifiNameConnectError(f'Can not connect to wifi network name "{wifi_network}"')

               def Disconnect(self):
                    subprocess.getoutput(cmd='networksetup -setnetworkserviceenabled Wi-Fi off')

               def Connect(self):
                    subprocess.getoutput(cmd='networksetup -setnetworkserviceenabled Wi-Fi on')

               def connectToMacAddress(self):
                    """Connect to wi-fi which used your Mac.
                    (Actually connect to Your Mac address, start host Apmode.)"""
                    self.interface.startHostAPMode_(None)

               def NetworkNoise(self):
                    """Noise of current connected wi-fi network."""
                    return int(self.interface.noise())

               def Bssid(self):
                    ps = subprocess.getoutput(cmd='airport -I | grep BSSID').strip(' ')
                    return ps

               def InfoNetwork(self):
                    """Ruturn a lot of data about current wifi network"""
                    return str(self.interface.ipMonitor()).strip().split('>')[1]

               def TransmitRate(self):
                    return self.interface.transmitRate()

               def ChannelGhz(self):
                    """Ghz type channel.It is 2Ghz or 5Ghz."""
                    if str(self.interface.wlanChannel()).split('>')[-1].split(',')[0].strip() == 'None':
                         raise ConnectionRefusedError('Enable wi-fi, please.').with_traceback()
                    return str(self.interface.wlanChannel()).split('>')[-1].split(',')[0].strip()

               def RssiChannelValue(self):
                    return self.interface.aggregateRSSI()

               def _get_speed_by_current_network(self):  # Deleted method.
                    raise NotImplementedError(
                         f'{repr(self._get_speed_by_current_network.__name__)} '
                         f'Deleted method. Because it already not support.')

               def Get_maxSpeed(self):
                    return subprocess.getoutput(cmd='airport -I | grep maxRate').strip()

               def get_last_speed_by_current_network(self):
                    return self.last_speed.strip().split(':')[-1]

               def IsEnable(self):
                    return not subprocess.getoutput(cmd='airport -I | grep SSID').split(':')[-1].strip() == ''

               def isUsedProxy(self):
                    """
                    :return: [False] if proxy/VPN not used, [True] is Using.
                    """
                    return self.interface.isProxy()

               def wifiChannel(self):
                    """Return Wi-fi channel """
                    return self.interface.channel()

               def UnplugWifi(self):
                    """Unplug wi-fi"""
                    self.interface.setPower_error_(None, None)

               def SecurityType(self):
                    """Return security type of current wi-fi network"""
                    return self.secT.split(':')[-1]

               def get_info(self, ssid):
                    return str(CoreWLAN.CWInterface.interfaceWithName_("en0").scanForNetworksWithName_error_(ssid, None)).split('[')[1].split(', ')[:4]

               def GetCounrtyCodeByCurrentWifi(self):
                    return self.interface.countryCodeInternal()

               def SetupDefaultDnsDommains(self, dns_address):
                    """Change DNS setting of wi-fi network.
                    :param dns_address address which available to confirm, default DNS settings."""
                    if dns_address != (i for i in ('8.8.8.8', '8.8.4.4')):
                         command = subprocess.getoutput(f'networksetup -setdnsservers Wi-Fi {dns_address}')

                    else:

                         store = SystemConfiguration.SCDynamicStoreCreate(None, 'Safari', None, None)
                         primaryif = SystemConfiguration.SCDynamicStoreCopyValue(store, 'State:/Network/Global/IPv4')[
                              'PrimaryInterface']

                         preferences = SystemConfiguration.SCPreferencesCreateWithAuthorization(None, 'Safari', None,
                                                                                                SystemConfiguration.SFAuthorization.authorization().authorizationRef())
                         SystemConfiguration.SCPreferencesLock(preferences, True)

                         # Get list of network services
                         networkSet = SystemConfiguration.SCNetworkSetCopyCurrent(preferences)
                         networkSetServices = SystemConfiguration.SCNetworkSetCopyServices(networkSet)

                         for networkServiceIndex in networkSetServices:
                              interface = SystemConfiguration.SCNetworkServiceGetInterface(networkServiceIndex)
                              if primaryif != SystemConfiguration.SCNetworkInterfaceGetBSDName(interface):
                                   continue

                              # Load currently configured DNS servers
                              networkProtocol = SystemConfiguration.SCNetworkServiceCopyProtocol(networkServiceIndex,
                                                                                                 SystemConfiguration.kSCNetworkProtocolTypeDNS)
                              DNSDict = SystemConfiguration.SCNetworkProtocolGetConfiguration(networkProtocol) or {}
                              DNSDict[SystemConfiguration.kSCPropNetDNSServerAddresses] = ['192.168.23.12', '8.8.4.4']
                              SystemConfiguration.SCNetworkProtocolSetConfiguration(networkServiceIndex, DNSDict)

                              tuple_confirm = (
                                   SystemConfiguration.SCPreferencesUnlock(preferences),
                                   SystemConfiguration.SCPreferencesCommitChanges(preferences),
                                   SystemConfiguration.SCPreferencesApplyChanges(preferences))
                              if not any(tuple_confirm):
                                   raise warnings.warn('Setup dns setting did not confirmation.')
                              else:
                                   return 'Successful'

          class Switching(object):
               """Switch wi-fi/bluetooth"""

               def unplug_wifi(self):
                    """
                    Just unplug wi-fi.
                    :return: Successfully
                    """
                    sleep(1)
                    subprocess.getoutput(cmd='networksetup -setairportpower en0 off')
                    return 'Successful...'

               def enable_wifi(self):
                    """
                 Just enable wi-fi.
                 :return: Successfully
                 """

                    sleep(1)
                    subprocess.getoutput(cmd='networksetup -setairportpower en0 on')
                    return 'Successful...'

               def unplug_bluetooth(self):
                    """
                 Just unplug bluetooth.
                 :return: Successfully
                 """

                    sleep(1)
                    subprocess.getoutput(cmd='osascript -e \'tell application '
                                             '"System Events" to tell process'
                                             ' "SystemUIServer" to tell (menu '
                                             'bar item 1 of menu bar 1 whose '
                                             'description is "bluetooth") to '
                                             '{click, click (menu item 2 of menu 1)}\'')
                    return 'Successful...'

               def enable_bluetooth(self):
                    """
                 Just enable bluetooth.
                 :return: Successfully
                 """
                    sleep(1)
                    subprocess.getoutput(cmd='osascript -e \'tell application "System Events" '
                                             'to tell process "SystemUIServer" to tell '
                                             '(menu bar item 1 of menu bar 1 whose description '
                                             'is "bluetooth") to {click, click (menu item 2 of menu 1)}\'')
                    return 'Successful...'

          class Brightness(object):
               """Set brightness"""

               def __init__(self):
                    global iokit
                    simplefilter("ignore")
                    init()
                    iokit = dict(iokit)
                    simplefilter("default")
                    self.s = iokit['IOHIDGetActivityState'](Quartz.CGDisplayIOServicePort(Quartz.CGMainDisplayID()), 1
                                                            )
                    self.get_cur_brightness_per = iokit["IODisplayGetFloatParameter"](Quartz.CGDisplayIOServicePort(Quartz.CGMainDisplayID()),
                                                                                      1,
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

                    try:
                         brightness_error = iokit["IODisplaySetFloatParameter"](Quartz.CGDisplayIOServicePort(Quartz.CGMainDisplayID()),
                                                                                1,iokit["kDisplayBrightness"], brightness_percent)
                         please()
                         if brightness_error != 0:
                             raise Exception('Error code = {}'.format(brightness_error))
                         elif brightness_error == -536870201:
                             raise ScreenErrorIndex( # 2077751737 - Main
                                   f'The screen index is incorrectly specified. use the default index -'
                                   f' {Quartz.CGMainDisplayID().__format__("-")}')
                         else:
                             pass # No errors.
                    except ValueError:
                              raise ValueBrightnessError('Type value of brightness must be ', float)

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

          class SystemConfig(object):
               """Data about mac"""
               simplefilter('ignore')
               init()
               simplefilter("default")



               def __init__(self):
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
                    self.size = subprocess.getoutput(cmd='system_profiler SPDisplaysDataType | grep Resolution').strip().split(":")[1].split(' ')
                    self.mem_size = subprocess.getoutput(cmd='sysctl -a | grep \'^hw\.m\'')
                    self.processor = subprocess.getoutput(cmd='sysctl -n machdep.cpu.brand_string')
                    del self.size[0], self.size[-1]
                    self.num = 'system_profiler SPHardwareDataType | grep x"Serial Number (system)"'
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

          class VoiceOver(object):
               """Voiceover text"""

               def text_voiceover(self, voice, text):
                    """
                 Send voice notify with text,
                 which you point out.
                 :param text: Text
                 :param voice: voicem which will be voiceover text, all voices local in "voices.txt"
                 :example: say -v ALex -i Hi! I am alex
                 :return: voice with point outed text
                 ALL AVAILABLE Voices(probably few unavailable on your devises)
                 """

                    if text is None:
                         raise NameError
                    else:
                         if subprocess.getstatusoutput(cmd=f'say -v {voice} -i {text}')[0] == 1:
                              raise NameError(f'Voice {repr(voice)} is unsupported on your devise.')
                         else:
                              subprocess.getoutput(cmd=f'say -v {voice} -i {text}')

          class PasswordManager(object):
               def show_password_wifi(self, name_wifi_network):
                    password = subprocess.getoutput(cmd=f'security find-generic-password -wa {name_wifi_network}')
                    if name_wifi_network in subprocess.getoutput(cmd='/System/Library/PrivateFrameworks/Apple80211.'
                                                                     'framework/Versions/A/Resources/airport scan') or \
                            subprocess.getstatusoutput(cmd=f'security find-generic-password -wa {name_wifi_network}')[
                                 0] == 0:
                         return password.strip()
                    else:
                         raise ValueError(f'Can not find wifi-network {repr(name_wifi_network)} in key chains.')

          class Notifier(object):
               """Send different alerts"""

               def send_text_alert(self, text, title=''):
                    """
                 Make alert with point out text,
                 which displayed at the center of
                 screen.
                 :param text message in alert
                 (Available only on Mac-os)
                 """

                    cmd = f'osascript -e \'tell app "System Events" to display dialog "{text}" with title "%s"\'' % title
                    subprocess.getoutput(cmd=cmd)

               def send_warning_alert(self, labeltext, button1: [int, float, str], button2: [int, float, str]):
                    if (type(button1) == int or float or str) and (type(button2) == int or float or str):

                         cmd = 'osascript -e \'tell application (path to frontmost ' \
                               f'application as text) to display dialog "{labeltext}" ' \
                               f'buttons {repr(button1), repr(button2)} with icon stop\''
                         return subprocess.getoutput(cmd=cmd).split(':')[-1]
                    else:
                         raise TypeError

               def send_lateral_message(self, label, activate: [None, str], subtitle, text, file_icon: str,
                                        sound: [None], content_img=None):
                    """
                    >>> import driver_controller
                    >>> driver_controller.MacCmd().Notifier().send_lateral_message(
                    >>> label='Label of message',
                    >>> activate='Safari',
                    >>> subtitle='Subtitle of message',
                    >>> text='Text of message',
                    >>> file_icon='icon_.png',
                    >>> sound=driver_controller.CONSTANTS.SOUNDS_PING_SOUND,
                    >>> content_img='icon_.png')
                  Make Lateral message with:
                  :param label: Main title on message
                  :param content_img: Image which local in center
                  :param subtitle: Subtitle of message
                  :param text: Description of message
                  :param file_icon: Icon in message (Path to image)
                  (must local in project-folder) Point out [None]
                  if you don't want used icon
                  :param activate: application, which open when you click by notify.
                  :return: Successful.
                  """

                    if len(str(file_icon).split()) > 1 or len(str(content_img).split()) > 1:
                         fullpath = str(pathlib.Path(str(file_icon)).cwd()) + '/' + repr(str(file_icon))
                         content = str(pathlib.Path(str(content_img)).cwd()) + '/' + repr(str(content_img))
                         commands = f"terminal-notifier -title '%s' -subtitle '%s' -message '%s' -appIcon %s -contentIm" \
                                    f"age '{content}' -activate 'com.apple.{activate if activate is not None else ''}'" % (
                                         label, subtitle, text, fullpath)
                         commands2 = f'afplay /System/Library/Sounds/{sound if sound is not None else ""}.aiff'


                    else:
                         fullpath = str(pathlib.Path(str(file_icon)).cwd()) + '/' + str(file_icon)
                         content2 = str(pathlib.Path(str(file_icon)).cwd()) + '/' + str(file_icon)
                         commands = f"terminal-notifier -title '%s' -subtitle '%s' -message '%s' -appIcon %s -contentIma" \
                                    f"ge '{content2}' -activate 'com.apple.{activate}'" % (
                                         label, subtitle, text, fullpath)
                         commands2 = f'afplay /System/Library/Sounds/{sound if sound is not None else ""}.aiff'

                    subprocess.getoutput(cmd=commands)
                    subprocess.getstatusoutput(cmd=commands2)

               def send_entry_alert(self, title, button1, button2, entr_text=''):
                    """
                    :param title: Title of entry
                    :param button1: button in alert
                    :param entr_text: placeholder-text
                    :param button2: button-2
                    :return:
                    """
                    cmd = """
                         a=$(osascript -e 'try
                         tell app "SystemUIServer"
                         set answer to text returned of (display dialog "" default answer "%s" with title "%s"
                         buttons {"%s", "%s"})
                         end
                         end
                         activate app (path to frontmost application as text)
                         answer' | tr '\r' ' ')
                         [[ -z "$a" ]] && exit
                         """ % (entr_text, title, button1, button2)
                    return subprocess.getoutput(cmd=cmd)

          class Creator(object):
               """Create something."""

               def create_file(self, name, extension):
                    """
                    Create file with setting & extension.
                    :param name: Name of created file
                    :param extension: Extension of created file
                    :return: Successful.
                    """
                    if name != '':
                         subprocess.getoutput(cmd=str('touch ') + str(name) + str('.') + str(extension))
                    else:
                         raise NameError from None

               def create_folder(self, name):
                    """
                 Create folder.
                 :param name: Name of folder
                 :return: Successful
                 """
                    if name == '':
                         raise NameError('Assign this folder a name!') from None
                    else:
                         subprocess.getoutput(cmd=f'mkdir {name}')

          class ScreenCapture(object):
               """Make screenshot/video with settings"""

               def __init__(self):
                    self.AVAILABLE_EXTENSIONS = ('png', 'jpg', 'icns', 'gif', 'pict', 'eps')
                    self.command = '/opt/local/bin/ffmpeg -f avfoundation -t %s -framerate 10 -video_size 640x480 -i "%s:%s" %s.%s'

               def screenshot(self, filename, extension, pause=None):
                    """
                 Method support ['png', 'jpg', 'ico', 'gif', 'pict', 'eps'] formats
                 Make screenshot with pause, extensions and filename.
                 :param pause: pause for determine screen capture [int, float, None].
                 :param filename: Pointed out name of created file(path).
                 :param extension: Extensions of created file.
                 :return: Successful if created is passed.
                 (Available only on Mac-os)
                 """

                    if extension in (i for i in self.AVAILABLE_EXTENSIONS):

                         sleep(pause if pause is not None else 0.0)
                         subprocess.getoutput(cmd=f'screencapture {filename}.{extension}')
                         return 'Successful...'

                    else:
                         """
                         [Format unsupported]
                         """

                         raise UnsupportedFormat(
                              "Method can make files only with extension ['png', 'jpg', 'icns', 'gif', 'pict']")

               def video_capture(self, record_time, camera_index, microphone_index, filename, extension):
                    """
                    Capture screen-video.
                    :param camera_index: Camera index where will be collected vide0
                    :param microphone_index: Microphone index, which used in video
                    :param filename: Name of file
                    :param extension: File Extension
                    :param record_time time of recording
                    :return:
                    """
                    subprocess.getoutput(
                         cmd=self.command % (record_time, camera_index, microphone_index, filename, extension))

               @property
               def list_devises(self):
                    """
                    Return all available devises for recording audio/video.
                    :return:
                    """
                    devises = '[' + str(subprocess.getoutput(
                         cmd='/opt/local/bin/ffmpeg -f avfoundation -list_devices true -i ""').split('[', maxsplit=1)[
                                             -1])
                    return devises.strip().split(': ')[0]

               @property
               def available_extension(self):
                    return (self.AVAILABLE_EXTENSIONS)

          class PhotoCapture(object):

               def capture(self, cam_index: int, extension, filename):
                    """
                 Method make image trough web-camera
                 :param cam_index: index where local camera
                 :param extension: extension of created image
                 :param filename: name of created file
                 :return: Successful...
                 """
                    subprocess.getoutput(
                         cmd=f'/opt/local/bin/ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i "{cam_index}" -vframes 1 {filename}.{extension}')
                    return 'Check file is %s.%s' % (filename, extension)

          class AudioRecorder(object):
               """Audio recorder"""

               def __init__(self):
                    """
                 Make variable AVAILABLE_EXTENSIONS is global.
                 """
                    self.AVAILABLE_EXTENSIONS = (i for i in ('wav', 'mp3'))

               def recorder(self, microphone_index, extension, filename: str, record_time: int):
                    """
                 :param microphone_index: Microphone index
                 :param extension: Extension of creates file
                 :param filename: Name
                 :param record_time: Record time (format minutes)
                 :return:
                 """
                    if extension in self.AVAILABLE_EXTENSIONS:
                         if os.path.isfile(f'{filename}.{extension}'):
                              raise FileExistsError(
                                   f'Please, rename file {filename}.{extension},because him already exist.')
                         else:

                              print('recording...')
                              if subprocess.getstatusoutput(
                                      cmd=f'/opt/local/bin/ffmpeg -f avfoundation -t {record_time} -i ":{microphone_index}"  {filename}.{extension}')[
                                   0] == 1:
                                   raise IndexError

                              return 'Check file is %s.%s' % (filename, extension)



                    else:
                         raise UnsupportedFormat('Method can make files only with extensions (\'wav', 'mp3\')')

          class AppSystem(object):
               def __init__(self):
                    self.apps = process_iter()

               def is_exist(self, application_name):
                    """
                 Check of existing of app({application_name})
                 :param application_name: APP name
                 :return: [True] if application
                 exist on your devise, [False] - if no.
                 """
                    return application_name in (i.name() for i in self.apps)

               def close_app(self, application_name):
                    """
                 Close app.
                 :param application_name:
                 Name of App which will
                 be close.
                 :return: [None]
                 """
                    subprocess.getoutput(cmd=f'pkill {application_name}')
                    return 'Successful...'

               def close_all_app(self):
                    for apps in AppKit.NSWorkspace.sharedWorkspace().runningApplications():
                         apps.terminate()

               def current_opened_app(self, pause):
                    sleep(pause)
                    activeAppName = AppKit.NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
                    return activeAppName

               def isopened(self, application_name):
                    """Returns a boolean value depending on whether the application is open."""
                    return AppKit.NSWorkspace.sharedWorkspace().openFile_withApplication_andDeactivate_(None,
                                                                                                        f'{application_name}',
                                                                                                        None)

               def get_size_icon_by_app(self, application_name):
                    activeAppName = AppKit.NSWorkspace.sharedWorkspace().iconForFile_(
                         f'/Applications/{application_name}')
                    size = str(activeAppName).split(' ')[2] + str(activeAppName).split(' ')[3]
                    return size

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

          class Open(object):

               def application(self, application_name):
                    """
                 Open application by his name.
                 :param path_app: Path to Application
                 (begin from /Applications/{path_app}.app)
                 EXAMPLE [/Applications/Finder.app]
                 :return: Successful if successful opened app.
                 """
                    boolean = AppKit.NSWorkspace.sharedWorkspace().launchApplication_(
                         application_name
                    )
                    if not boolean:
                         raise ApplicationNotExist(f'Application {application_name} not exist.')

               def url(self, url, browser='Safari'):
                    """
                    Open url in main browser
                    DEFAULT BROWSER: Safari.
                    :param url: 'url'
                    :return: None
                    :param url: 
                    :return: 
                    """  # SAFARI - DEFAULT MAIN BROWSER, CHANGE YOUR
                    cmd = f'open /Applications/{browser}.app {url}'  # Select your main browser
                    return subprocess.getoutput(cmd=cmd)

               def open_spotlight(self):
                    """Open spotlight menu."""
                    MacCmd().Mouse().move_click(1212, 13)

               def open_file(self, path):
                    AppKit.NSWorkspace.sharedWorkspace().openFile_(
                         path)

               def open_file_in_app(self, app_name, file):
                    open_objc = AppKit.NSWorkspace.sharedWorkspace().openFile_withApplication_(file, app_name)

                    if open_objc is False:
                         raise OpenPossibilityError \
                              (f'Can not open file {file}, because application {app_name} not support format this files.')

          class Sound(object):
               """
             class Voice add more available
             voices & effects(which beforehand
             installed in Mac-os by path /System/Library/Sounds/)
             (Available only on Mac-os). And play other sounds.
             """

               def __init__(self):
                    self.sound1 = '/System/Library/Sounds/Pop.aiff',
                    self.sound2 = '/System/Library/Sounds/Blow.aiff',
                    self.sound3 = '/System/Library/Sounds/Glass.aiff',
                    self.sound4 = '/System/Library/Sounds/Funk.aiff',
                    self.sound5 = '/System/Library/Sounds/Submarine.aiff',
                    self.sound6 = '/System/Library/Sounds/Sosumi.aiff'

               @staticmethod
               def pop_sound(iters: int):
                    """
                 Pop voice-notify.
                 :param iters How mane
                 iterations(repeats) of sound.
                 (Available only on Mac-os)
                 """

                    subprocess.getoutput(
                         cmd='for i in {1..%s}; do afplay /System/Library/Sounds/Pop.aiff -v 10; done' % iters)

               @staticmethod
               def blow_sound(iters: int):
                    """Blow voice-notify.
                 :param iters How mane
                 iterations(repeats) of sound.
                 (Available only on Mac-os)
                 """
                    subprocess.getoutput(
                         cmd='for i in {1..%s}; do afplay /System/Library/Sounds/Blow.aiff -v 10; done' % iters)

               @staticmethod
               def glass_sound(iters: int):
                    """
                 Glass voice-notify.
                 :param iters How mane
                 iterations(repeats) of sound.
                 (Available only on Mac-os)
                 """
                    subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                             '/System/Library/Sounds/Glass.aiff -v 10; done' % iters)

               @staticmethod
               def funk_sound(iters: int):
                    """
                 Funk voice-notify.
                 :param iters How many
                 iters(repeats) of sound.
                 (Available only on Mac-os)
                 """
                    subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                             '/System/Library/Sounds/Funk.aiff -v 10; done' % iters)

               @staticmethod
               def submarine_sound(iters: int):
                    """
                 Submarine voice-notify.
                 :param iters How many
                 iterations(repeats) of sound.
                 (Available only on Mac-os)
                 """
                    subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                             '/System/Library/Sounds/Submarine.aiff -v 10; done' % iters)

               @staticmethod
               def morse_sound(iters: int):
                    """
                 Submarine voice-notify.
                 :param iters How many
                 iterations(repeats) of sound.
                 (Available only on Mac-os)
                 """
                    subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                             '/System/Library/Sounds/Morse.aiff -v 10; done' % iters)

               @staticmethod
               def ping_sound(iters: int):
                    """
                 Ping voice-notify.
                 :param iters How mane
                 iterations(repeats) of sound.
                 (Available only on Mac-os)
                 """
                    subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                             '/System/Library/Sounds/Ping.aiff -v 10; done' % iters)

               @staticmethod
               def sosumi_sound(iters: int):
                    """
                 Sosumi voice-notify.
                 :param iters How mane
                 iterations(repeats) of sound.
                 (Available only on Mac-os)
                 """
                    subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                             '/System/Library/Sounds/Sosumi.aiff -v 10; done' % iters)

               def playSoundByName(self, soundfile):
                    absolute_path =  str(pathlib.Path(soundfile).cwd()) + str('/') + soundfile
                    url = Foundation.NSURL.URLWithString_(
                         absolute_path
                         )

                    duration_Start = AppKit.NSSound.alloc().initWithContentsOfURL_byReference_(url, True)
                    try:
                         duration_Start.play()
                         sleep(float(duration_Start.duration()))

                    except AttributeError:
                         raise PathError(f'No sound name {url}, or it not support')

               def sound_length(self, file):
                    return mutagen.mp3.MP3(file).info.length

          class AppConfigure(object):
               """App-settings"""

               def get_full_path_by_app_name(self, app):
                    return AppKit.NSWorkspace.sharedWorkspace().fullPathForApplication_(app)

               def get_app_size(self, app_name):
                    """
                    Return size of app by him name.
                    :param app_name: App name, which exist in /Applications/<NAME>.app
                    :return: Size in megabytes/gigabytes
                    """
                    path = f'du -sh {self.get_full_path_by_app_name(app_name)}'
                    if app_name not in (i.name() for i in process_iter()):
                         raise ApplicationNameError
                    else:
                         return subprocess.getoutput(cmd=path).split()[0]

          class FileConfig(object):

               def get_date_create_file(self, path):
                    """
                    Return time, when file was used.
                    :param path:
                    :return:
                    """
                    return ctime(os.stat(path).st_birthtime)

               def get_file_size(self, path):

                    """
                    Return size of file.
                    :param path: Path to file
                    :return:
                    """

                    return subprocess.getoutput(f'du -sh {path}').split('\t')[0].strip()

               def extension(self, path):
                    return str(path).split('.')[-1]

               def name(self, path):
                    """:return Name by path"""
                    return path.split('/', maxsplit=3)[-1].split('.')[0]

               def get_files_in_folder(self, path: str):
                    """Return all files in folder"""
                    if not os.path.exists(path=path):
                         raise FileExistsError
                    if path == subprocess.getoutput(cmd=f'ls {path}'):
                         return None
                    return subprocess.getoutput(cmd=f'ls {path}')

               def get_folder_size(self, path):
                    """Return all files in folder"""
                    if os.path.exists(path=path):

                         return subprocess.getoutput(cmd=f'du -sh {path}').split()
                    else:
                         raise FileExistsError(f'No file name {path}')

          class Volume(object):
               def __init__(self):

                    self.volume = 'osascript -e "set Volume %s"'
                    self.max_volume = 'osascript -e "set Volume 10"'
                    self.min_volume = 'osascript -e "set Volume 0"'

                    self.muted = subprocess.getoutput(cmd='osascript -e \'get volume settings\'')
                    self.input_volume = subprocess.getoutput(cmd='osascript -e \'get volume settings\'').split(' ')[
                         3].replace(',', '')
                    self.output_volume = subprocess.getoutput(cmd='osascript -e \'get volume settings\'').split(' ')[
                         1].replace(',', '')
                    self.alert_vol = subprocess.getoutput(cmd='osascript -e \'get volume settings\'').split(' ')[
                         5].replace(
                         ',', '')

               def set_volume(self, volume):
                    """Set volume by value."""

                    subprocess.getoutput(cmd=self.volume % volume)
                    if subprocess.getstatusoutput(cmd=self.volume % volume)[0] == 1:
                         raise ValueError
                    else:
                         return 'Successful...'

               def set_max_volume(self):
                    subprocess.getoutput(cmd=self.max_volume)
                    return 'Successful...'

               def set_min_volume(self):
                    subprocess.getoutput(cmd=self.min_volume)
                    return 'Successful...'

               @property
               def get_output_volume_percent(self):
                    """
                    Return output volume percent
                    :return:
                    """

                    return self.output_volume

               @property
               def get_input_volume_percent(self):
                    """
                    Return input volume percent
                    :return:
                    """
                    return self.input_volume

               @property
               def get_alert_volume(self):
                    return self.alert_vol

               def ismuted(self):
                    return self.muted.split(', ')[-1].split(':')[-1].capitalize()

               def increase_volume(self):
                    def doKey(down):
                         # NSEvent.h script
                         NSSystemDefined = 14
                         eventInit = Quartz.NSEvent.otherEventthType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                              NSSystemDefined,
                              (0, 0),
                              0xa00 if down else 0xb00,
                              0,
                              0,
                              0,
                              8,
                              (0 << 16) | ((0xa if down else 0xb) << 8),
                              -1
                         )
                         cev = eventInit.CGEvent()
                         Quartz.CGEventPost(0, cev)

                    doKey(True)
                    doKey(False)

               def decrease_volume(self):
                    def doKey(down):
                         # NSEvent.h script
                         NSSystemDefined = 14
                         eventInit = Quartz.NSEvent.otherEventthType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                              NSSystemDefined,
                              (0, 0),
                              0xa00 if down else 0xb00,  # F11/F12 KEY
                              0,
                              0,
                              0,
                              8,
                              (1 << 16) | ((0xa if down else 0xb) << 8),  # data1
                              -1  # data2
                         )
                         cev = eventInit.CGEvent()
                         Quartz.CGEventPost(0, cev)

                    doKey(True)
                    doKey(False)

          class WebCameraCapture(object):
               """Collect data in camera"""

               def __init__(self):
                    self.cmd = '/opt/local/bin/ffmpeg -f avfoundation -t %s -framerate 30 -i "%s" -target pal-vcd ./%s.%s'
                    self.devises = '[' + str(subprocess.getoutput(
                         cmd='/opt/local/bin/ffmpeg -f avfoundation -list_devices true -i ""').split('[', maxsplit=1)[
                                                  -1])

               def webcam_capture(self, record_time: int, camera_index, filename, extension):
                    """
                    Record video in webcam
                    :param record_time: Recording time(seconds)
                    :param camera_index: Camera index
                    :param filename: Name of created file
                    :param extension: Extension of file
                    :return: [None]
                    """

                    subprocess.getoutput(cmd=self.cmd % (record_time, camera_index, filename, extension))
                    if os.path.isfile(f'{filename}.{extension}'):
                         raise FileExistsError(f'Please, rename file {filename}.{extension}, because it already exist.')
                    else:
                         return 'Check file is %s.%s' % (filename, extension)

               @property
               def list_devises(self):
                    """
                    Return all available devises for recording audio/video.
                    :return: Devises
                    """

                    return '[' + str(self.devises.strip().split('[', maxsplit=1)[-1].split(': ')[0])

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


          class Theme:
               def __init__(self):
                    self.cmd = 'osascript -e \'tell app "System Events" to tell appearance ' \
                               'preferences to set dark mode to not dark mode\''

               def change_color_mode(self, pause: [int, float, complex]):
                    sleep(pause)
                    subprocess.getoutput(cmd=self.cmd)

               def current_theme(self):
                    """Print current color mode on mac."""
                    if not 'Dark' in subprocess.getoutput('defaults find AppleInterfaceStyle'):
                         return "Light"
                    return subprocess.getoutput('defaults find AppleInterfaceStyle').split(": ")[-1].split()[:2:-1][-1].replace(r';', '')

          class Buffer:
               def copyText(self, text):
                    init = AppKit.NSStringPboardType

                    pb = AppKit.NSPasteboard.generalPasteboard()
                    pb.declareTypes_owner_([init], None)

                    newStrIng = AppKit.NSString.stringthString_(text)
                    newData = newStrIng.nsstring().dataUsingEncoding_(AppKit.NSUTF8StringEncoding)
                    pb.setData_forType_(newData, init)

               def paste(self):
                    return pyperclip.paste()

          class Illumination:
               def increase_illumination(self):
                    def doKey(down):
                         NSSystemDefined = 14

                         DECODE_TO_INT_KEY_F6 = 21

                         ev = Quartz.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                              NSSystemDefined,
                              (0, 0),
                              0xa00 if down else 0xb00,
                              0,
                              0,
                              0,
                              8,
                              (DECODE_TO_INT_KEY_F6 << 16) | ((0xa if down else 0xb) << 8),
                              -1
                         )
                         cev = ev.CGEvent()
                         Quartz.CGEventPost(0, cev)

                    doKey(True)
                    doKey(False)

               def decrease_illumination(self):
                    def doKey(down):
                         # NSEvent.h
                         NSSystemDefined = 14

                         DECODE_TO_INT_KEY_F5 = 22

                         ev = Quartz.NSEvent.otherEventthType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                              NSSystemDefined,  # type
                              (0, 0),  # location
                              0xa00 if down else 0xb00,  # flags
                              0,  # timestamp
                              0,  # window
                              0,  # ctx
                              8,  # subtype
                              (DECODE_TO_INT_KEY_F5 << 16) | ((0xa if down else 0xb) << 8),  # data1
                              -1  # data2
                         )
                         cev = ev.CGEvent()
                         Quartz.CGEventPost(0, cev)

                    doKey(True)
                    doKey(False)

           class BackGroundScreen:
               def current_background_image(self):
                    Id = Quartz.NSScreen.mainScreen()
                    boolean = AppKit.NSWorkspace.sharedWorkspace().desktopImageURLForScreen_(Id)
                    return boolean

               def set_backgroud(self, filename: str, stretch_img_by_screen_size: bool, image_bg_color='white', ):
                    try:
                         if image_bg_color == 'green':
                              file_url = Foundation.NSURL.fileURLthPath_(filename)
                              config = {
                                   AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                                   AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                                not True else AppKit.YES,
                                   AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.greenColor()
                              }
                         elif image_bg_color == 'red':
                              file_url = Foundation.NSURL.fileURLthPath_(filename)
                              config = {
                                   AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                                   AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size
                                                                                                is not True else AppKit.YES,
                                   AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.redColor()
                              }
                         elif image_bg_color == 'blue':
                              file_url = Foundation.NSURL.fileURLthPath_(filename)
                              config = {
                                   AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                                   AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                                not True else AppKit.YES,
                                   AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.blueColor()
                              }
                         elif image_bg_color == 'yellow':
                              file_url = Foundation.NSURL.fileURLWithPath_(filename)
                              config = {
                                   AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                                   AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                                not True else AppKit.YES,
                                   AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.yellowColor()
                              }
                         elif image_bg_color == 'white':
                              file_url = Foundation.NSURL.fileURLWithPath_(filename)
                              config = {
                                   AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                                   AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                                not True else AppKit.YES,
                                   AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.whiteColor()
                              }
                         elif image_bg_color == 'black':
                              file_url = Foundation.NSURL.fileURLWithPath_(filename)
                              config = {
                                   AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                                   AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                                True else AppKit.YES,
                                   AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.blackColor()
                              }
                         elif image_bg_color != (i for i in ('black', 'white', 'yellow', 'blue', 'red', 'green')):
                              raise RgbValueError(f'No color {image_bg_color} for background.')

                         ws__ = AppKit.NSWorkspace.sharedWorkspace()
                         for screens in AppKit.NSScreen.screens():
                              ws__.setDesktopImageURL_forScreen_options_error_(
                                   file_url, screens, config, None)
                    except Exception:
                         raise UnsupportedFormat(f'Image not support format {repr(str(filename).split(".")[-1])}.')


else:
     raise SystemError('Use python version more [3.7] and mac version [10.9] an more.')

if __name__ == '__main__':
     exit('Welcome to driver_controller!')
