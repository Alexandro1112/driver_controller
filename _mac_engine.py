# /opt/anaconda3/bin/python
# Copyright (c) 2022-2023 Aleksandr Bosov. All rights reserved.
# The library is designed for Mac-OS, performs technical
# functions such as disabling Wi-Fi, Bluetooth, sends ,
# notifications: text, sound, recording audio, working with screen brightness,
# control devises and much more.Soon be cross-platform.
# |---------------------------------------------------------------------------------------------------------------------|
#                                                   ||PYTHON-INSTALLATION||
# If you cloned this repository trough github, dependencies commands such as [blueutil, brew, brightness]
# successful installed. Dont forget about commands:
# I COMMAND - [ pip3 install loger]
# II COMMAND = [ pip3 install plyer]
# III COMMAND = [ pip3 install sounddevice]
# If code not working, though git submodules exist in git-hub repository: complete few commands:
# INSTALL || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" OR
# REINSTALL (if need)|| /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# LIB - INSTALLER || brew install brightness || brew doctor || brew install blueutil ||
# brew install ffmpeg OR sudo port install ffmpeg || if "command port not founded: then:
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
# TODO: Make more classes
#                                            Finally, run code.

# for full paths
import pathlib
# all process
import subprocess
# check platform OS
import sys
# Unplug warnings, unexpected errors
from warnings import filterwarnings
from shutup import please

# Mouse-click
import Quartz
import Quartz.CoreGraphics

# pause for methods
from time import (sleep, ctime)
# for get list applications
from psutil import process_iter
# Constants
from .CONSTANTS import CONSTANT_SOUNDS
# Log-alerts
from loger import *
# Sound-devises
from sounddevice import query_devices

# Exceptions for methods
from .exceptions import *

import AppKit

# For collecting data in system files
import objc

# Os
import os

__all__ = ['MacCmd', 'CONSTANT_SOUNDS']

if sys.platform == 'darwin':
     class MacCmd(object):

          class OutputListsDevises(object):
               """ Return output devises """

               def __init__(self):
                    self.bluetooth = subprocess.getoutput(cmd='system_profiler SPBluetoothDataType')
                    self.devises = query_devices()

               def get_list_wifi_networks(self):
                    """ Function output all wi-fi networks,
                       which available for your devise."""

                    wifi = []
                    wifi2 = []
                    bundle_path = '/System/Library/Frameworks/CoreWLAN.framework'
                    objc.loadBundle('CoreWLAN', bundle_path=bundle_path, module_globals=globals())

                    response = CWInterface.interface()
                    r = response.scanForNetworksWithName_includeHidden_error_(None, True, None)
                    for i in range(1, len(str(r).split('>')), 2):
                         wifi.append(str(r).split('>')[i].split(',')[0] + ']')

                    for items in wifi:
                         wifi2.append(items.strip().replace('ssid', '').replace('[', '').replace(']', '').replace('=',
                                                                                                                  '').strip())

                    yield set(wifi2)

               def get_list_bluetooth_device(self):
                    """ Function output all bluetooth devise(s),
                  which available for your devise."""

                    return self.bluetooth.split('Bluetooth:')[0] if not self.bluetooth.split('Bluetooth:')[
                                                                             0].strip() == '' else None

               def get_list_audio_devises(self):
                    """
                 Return all audio
                 connectable devises.
                 :return: devises
                 (Available only on Mac-os)
                 """

                    return self.devises

          class Connector(object):
               """Connect to wi-fi networks"""

               @staticmethod
               def connectTo(wifi_network, password):
                    """
                 Auto connect to wi-fi network.

                 :param wifi_network: Wi-fi name, which you would to connect.
                 :param password: Password of this Network.(use hide variable)
                 :return: 'Successful...' if you successfully connect to wi-fi.
                 """
                    please()

                    connect_GADGET = subprocess.getoutput(
                         cmd=f'networksetup -setairportnetwork en0 {wifi_network} {password}')
                    if connect_GADGET.strip() != '':
                         filterwarnings('ignore', category=DeprecationWarning and FutureWarning and Warning)
                         raise WifiNameConnectError(f'Could not find network {wifi_network}')

                    else:
                         log(f'You successful connected to wifi network {wifi_network}', level=4)
               def disconnect(self):
                    subprocess.getoutput(cmd='networksetup -setnetworkserviceenabled Wi-Fi off')

               def connect(self):
                    subprocess.getoutput(cmd='networksetup -setnetworkserviceenabled Wi-Fi on')

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
                    self.get_cur_brightness_per = subprocess.getoutput(cmd='brightness -l')

               def set_brightness(self, brightness_percent: int):
                    """
                 Automatically set brightness
                 percent [type - int]
                 example: 25; 50; 75; 100(max)
                 :param brightness_percent:
                 :return: Successfully
                 """

                    if not isinstance(brightness_percent, int):
                         raise ValueBrightnessError('Type value of brightness must be ', int)

                    else:
                         if brightness_percent == 100:
                              brightness_percent -= brightness_percent + 1
                              subprocess.getoutput(cmd=f'brightness 1')

                         elif isinstance(brightness_percent / 10, float):
                              brightness_percent *= 10
                              subprocess.getoutput(cmd=f'brightness 0.{brightness_percent}')

                         else:
                              subprocess.getoutput(cmd=f'brightness 0.{brightness_percent}')

               def set_max_brightness(self):
                    """
                 Set max brightness of
                 screen equal one hundred.
                 :return: Successfully
                 """
                    subprocess.getoutput(cmd='brightness -v 1')

               def set_min_brightness(self):
                    """
                 Set min brightness of
                 screen equal zero.
                 :return: Successfully
                 """

                    subprocess.getoutput(cmd='brightness -v 0')

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
                    subprocess.getoutput(cmd="osascript - e'tell application \"finder\" to sleep'")

               @property
               def get_brightness(self):
                    """Get brightness percent"""
                    return round(float(self.get_cur_brightness_per.split(' ')[-1]), ndigits=1)

          class SystemConfig(object):
               """Data about mac"""

               def __init__(self):
                    self.percent = subprocess.getoutput(cmd="pmset -g batt").split()[7].replace(";", r"")
                    self.vers = subprocess.getoutput(cmd="sw_vers -productVersion")
                    airport = pathlib.Path(
                         "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport")
                    self.network = subprocess.getoutput(
                         cmd=f"{airport} -I | awk '/ SSID/ {{print substr($0, index($0, $2))}}'").capitalize()
                    self.size = \
                    subprocess.getoutput(cmd='system_profiler SPDisplaysDataType | grep Resolution').strip().split(":")[
                         1].split(' ')
                    self.mem_size = subprocess.getoutput(cmd='sysctl -a | grep \'^hw\.m\'')
                    self.processor = subprocess.getoutput(cmd='sysctl -n machdep.cpu.brand_string')
                    del self.size[0], self.size[-1]
                    self.num = 'system_profiler SPHardwareDataType | grep "Serial Number (system)"'
                    self.disk_mem = 'diskutil list | grep GUID_partition_scheme'  # Diskutil not found: https://superuser.com/questions/213088/diskutil-command-not-found-in-os-x-terminal
                    self.video_crd_nm = subprocess.getoutput(
                         cmd='system_profiler SPDisplaysDataType | grep "Chipset Model"')  # system profiler: command not found https://github.com/jlhonora/lsusb/issues/12?ysclid=ldu37f5jk9865312203

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

                    return self.network.capitalize()

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
                    return subprocess.getoutput(cmd=self.disk_mem).replace('*', '').split()[2] + 'Gb'


               @property
               def get_video_card_name(self):
                    return self.video_crd_nm.strip().split(':')[-1]

          class VoiceOver(object):
               """Voiceover text"""

               def text_voiceover(self, voice, text=None):
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
               """Paasword-manager"""

               def show_password_wifi(self, name_wifi_network=None):
                    """
                   [!!ATTENTION!!]
                 Function return password
                 of saved wi-fi network
                 trough util "keychain".
                 (Must be Administrator for run this code)
                 (Available only on Mac-os)
                 :param name_wifi_network: Name
                 :return: password of network which saved in KEY CHAINS.
                  """

                    password = subprocess.getoutput(cmd=f'security find-generic-password -wa {name_wifi_network}')
                    if not name_wifi_network in subprocess.getoutput(cmd='/System/Library/PrivateFrameworks/Apple80211.'
                                                                         'framework/Versions/A/Resources/airport scan') or \
                            subprocess.getstatusoutput(cmd=f'security find-generic-password -wa {name_wifi_network}')[
                                 0] == 0:
                         return password.strip()
                    else:
                         raise WifiValueError(f'Can not find wifi-network {repr(name_wifi_network)}')

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

               def send_lateral_message(self, label, subtitle, text, file_icon: [None, str],
                                        sound: [None, CONSTANT_SOUNDS], content_img=None):
                    """
                  Make Lateral message with:
                  :param label: Main title on message
                  :param content_img: Image which local in center
                  :param subtitle: Subtitle of message
                  :param text: Description of message
                  :param file_icon: Icon in message (Path to image)
                  (must local in project-folder) Point out [None]
                  if you don't want used icon
                  :return: Successful.
                  """
                    if len(file_icon.split()) > 1 or len(content_img.split()) > 1:
                         fullpath = str(pathlib.Path(str(file_icon)).cwd()) + '/' + repr(str(file_icon))
                         content = str(pathlib.Path(str(content_img)).cwd()) + '/' + repr(str(content_img))
                         commands = f"terminal-notifier -title '%s' -subtitle '%s' -message '%s' -appIcon %s -contentImage {content}" % (
                              label, subtitle, text, fullpath)
                         commands2 = f'afplay /System/Library/Sounds/{sound if sound is not None else ""}.aiff'
                    else:
                         fullpath = str(pathlib.Path(str(file_icon)).cwd()) + '/' + str(file_icon)
                         content2 = str(pathlib.Path(str(file_icon)).cwd()) + '/' + str(file_icon)
                         commands = f"terminal-notifier -title '%s' -subtitle '%s' -message '%s' -appIcon %s -contentImage {content2}"% (
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
                    set answer to text returned of (display dialog "" default answer "%s" with title "%s" buttons {"%s", "%s"})
                    end
                    end
                    activate app (path to frontmost application as text)
                    answer' | tr '\r' ' ')
                    [[ -z "$a" ]] && exit
                    """ % (entr_text, title, button1, button2)
                    return subprocess.getoutput(cmd=cmd)

          class Creator(object):
               """Create anything"""

               def create_file(self, name, extension):
                    """
                    Create file with setting & extension.
                    :param name: Name of created file
                    :param extension: Extension of created file
                    :return: Successful.
                    """
                    if name == '':
                         subprocess.getoutput(cmd=str('touch ') + str(name) + str('.') + str(extension))

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
                    """
                 |----------------------------------------------|
                 |Available extensions for function "screenshot"|
                 |----------------------------------------------|
                 """

                    if extension in [i for i in self.AVAILABLE_EXTENSIONS]:

                         sleep(pause if pause is not None else 0.0)
                         subprocess.getoutput(cmd=f'screencapture {filename}.{extension}')
                         return 'Successful...'

                    else:
                         """
                         [Format unsupported]
                         """
                         log('Unsupported format', level=3)
                         raise UnsupportedFormat(
                              "Method can make files only with extension ['png', 'jpg', 'icns', 'gif', 'pict']")

               def video_capture(self, record_time, camera_index, microphone_index, filename, extension):
                    """
                    Capture screen-video, click [q] for end video, and save them.
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
                    return self.AVAILABLE_EXTENSIONS

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

               def recorder(self, microphone_index: 0, extension, filename, record_time: int):
                    """

                 :param microphone_index: Microphone index
                 :param extension: Extension of creates file
                 :param filename: Name
                 :param record_time: Record time (format minutes)
                 :return:
                 """
                    if extension in self.AVAILABLE_EXTENSIONS:
                         if os.path.isfile(f'{filename}.{extension}'):
                              raise FileExistsError(f'Please, rename file {filename}.{extension}, him already exist.')
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

          class Clicker(object):
               """Click keys"""
               @staticmethod
               def press(key):
                    subprocess.getoutput(cmd='osascript -e \'tell application '
                                             '"System Events" to keystroke "%s" using {shift down}\'' % str(
                         key).upper())
                    return 'Successful...'

          class Open(object):
               @staticmethod
               def application(path_app):
                    """
                 Open application by his name.
                 :param path_app: Path to Application
                 (begin from /Applications/{path_app}.app)
                 EXAMPLE [/Applications/Finder.app]
                 :return: Successful if successful opened app.
                 """
                    cmd = subprocess.getoutput(cmd=f'open -F -a "{path_app}"')
                    if cmd.strip() != '':
                         raise ApplicationNotExist('Application %s not exist' % path_app)

                    else:
                         return 'Successful...'

               @staticmethod
               def url(url):
                    """
                    Open url in main browser
                    DEFAULT BROWSER: Safari.
                    :param url: 'url'
                    :return: None
                    :param url: 
                    :return: 
                    """  # SAFARI - DEFAULT MAIN BROWSER, CHANGE YOUR
                    cmd = f'open /Applications/Safari.app {url}'  # Select your main browser
                    return subprocess.getoutput(cmd=cmd)
                    # log(log='Successful...', level=4)

          class Sound(object):
               """
             class Voice add more available
             voices & effects(which beforehand
             installed in Mac-os by path /System/Library/Sounds/)
             (Available only on Mac-os)
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

          class AppConfigure(object):
               """App-settings"""

               def get_app_size(self, app_name):
                    """
                    Return size of app by him name.
                    :param app_name: App name, which exist in /Applications/<NAME>.app
                    :return: Size in megabytes/gigabytes
                    """
                    path = f'du -sh /Applications/{app_name}.app'
                    if subprocess.getstatusoutput(cmd=path)[0] == 1:
                         raise ApplicationNameError
                    else:
                         return subprocess.getoutput(cmd=path)

               def get_full_path_by_app_name(self, app):
                    if subprocess.getstatusoutput(
                            cmd=f"osascript -e 'tell application \"System Events\" to POSIX path of (file of process \"{app}\" as alias)'")[
                         0] == 1:
                         raise ApplicationNotExist
                    else:
                         return subprocess.getoutput(
                              cmd=f"osascript -e 'tell application \"System Events\" to POSIX path of (file of process \"{app}\" as alias)'")

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
                    return path.split('/', maxsplit=3)[-1].split('.')[0]

               def get_files_in_folder(self, path: str):
                    """Return all files in folder"""
                    if not os.path.exists(path=path):
                         raise FileExistsError
                    return subprocess.getoutput(cmd=f'ls {path}')

               def get_folder_size(self, path):
                    """Return all files in folder"""
                    if os.path.exists(path=path):

                         return subprocess.getoutput(cmd=f'du -sh {path}').split()
                    else:
                         raise FileExistsError

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

               def set_volume(self, volume):

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

               def ismuted(self):
                    return self.muted.split(', ')[-1].split(':')[-1].capitalize()

               def increase_volume(self):
                    def doKey(down):
                         # NSEvent.h script
                         NSSystemDefined = 14
                         eventInit = Quartz.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
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
                    """set volume in 1 division less"""
                    def doKey(down):
                         # NSEvent.h script
                         NSSystemDefined = 14
                         eventInit = Quartz.NSEvent.otherEventWithType_location_modifierFlags_timestamp_windowNumber_context_subtype_data1_data2_(
                              NSSystemDefined,
                              (0, 0),
                              0xa00 if down else 0xb00,
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


          class WifiSpeed(object):
               def __init__(self):
                    self.speed = subprocess.getoutput(cmd='airport -I | grep maxRate')
                    self.last_speed = subprocess.getoutput(cmd='airport -I | grep lastTxRate')

               def get_speed_by_current_network(self):
                    return self.speed

               def get_last_speed_by_current_network(self):
                    return self.last_speed

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
               def __init__(self, x, y):
                    location = AppKit.NSEvent.mouseLocation()
                    position = (round(location.x), round(Quartz.CGDisplayPixelsHigh(0) - location.y))
                    self.x = position[0]
                    self.y = position[1]



               @classmethod
               def EventInitScript(cls, ev, x, y, button):
                    """Initalizate mouse objc x: x-pos, y:y-pos"""
                    mouseEvent = Quartz.CGEventCreateMouseEvent(None,
                                                                ev, (x, y), button)
                    Quartz.CGEventPost(Quartz.kCGHIDEventTap, mouseEvent)

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
               def super_click(cls, x, y):
                    """Make click and mouse-move."""
                    theEvent = Quartz.CoreGraphics.CGEventCreateMouseEvent(None, 1, (x, y), Quartz.CoreGraphics.kCGMouseButtonLeft)
                    Quartz.CoreGraphics.CGEventPost(Quartz.CoreGraphics.kCGHIDEventTap, theEvent)


               def mouse_position(self):
                    """Return mouse position"""

                    return self.x, self.y



if __name__ == '__main__':
     exit(1)


