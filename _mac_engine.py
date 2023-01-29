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
# /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" OR
# /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# LIB - INSTALLER || brew install brightness || brew doctor || brew install blueutil ||
# brew install ffmpeg OR sudo port install ffmpeg || if "command port not found: then:
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
# Finder -> Go -> Go to folder -> /System/...
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

# pause for methods
from time import sleep, ctime
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


# Check existing file, get date file created 

import os

__all__ = ['MacCmd',]

if sys.platform == 'darwin':
     class MacCmd(object):

          class OutputListsDevises(object):
               """ Return output devises """

               def __init__(self):
                    self.scan_cmd = subprocess.Popen(['airport', '-s'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                                     stdin=subprocess.PIPE)
                    self.bluetooth = subprocess.getoutput(cmd='system_profiler SPBluetoothDataType')
                    self.devises = query_devices()

               def get_list_wifi_networks(self):
                    """ Function output all wi-fi networks,
                       which available for your devise."""
                    scan_out, scan_err = self.scan_cmd.communicate()
                    scan_out_data = dict()
                    scan_out_lines = str(scan_out).split("\\n")[1:-1]
                    for each_line in scan_out_lines:
                         split_line = [i for i in each_line.split(' ') if i != '']
                         line_data = {"SSID": split_line[0], "RSSI": split_line[2], "channel": split_line[3],
                                      "HT": (split_line[4] == "Y"), "CC": split_line[5], "security": split_line[6]}
                         scan_out_data[split_line[1]] = line_data
                    names_ = scan_out_data

                    for names in names_.values():
                         self.networks = list(names.values())[0]
                         print(self.networks) if not self.networks.strip() == '' else None

               def get_list_bluetooth_device(self):
                    """ Function output all bluetooth devise(s),
                  which available for your devise."""

                    return self.bluetooth.split('Bluetooth:')[0] if not self.bluetooth.split('Bluetooth:')[0].strip() == '' else None

               def get_list_audio_devises(self):
                    """
                 Return all audio
                 connectable devises.
                 :return: devises
                 (Available only on Mac-os)
                 """

                    return self.devises if not self.devises.strip() == '' else None


          class Connector(object):
               """Connect to wi-fi networks"""

               @staticmethod
               def connect_wifi_network(wifi_network, password):
                    """
                 Auto connect to wi-fi network.

                 :param wifi_network: Wi-fi name, which you would to connect.
                 :param password: Password of this Network.(use hide variable)
                 :return: 'Successful...' if you successfully connect to wi-fi network.
                 """
                    please()

                    connect_GADGET = subprocess.getoutput(
                         cmd=f'networksetup -setairportnetwork en0 {wifi_network} {password}')
                    if connect_GADGET.strip() != '':
                         filterwarnings('ignore', category=DeprecationWarning and FutureWarning)
                         raise WifiNameConnectError(f'Could not find network {wifi_network}')

                    else:
                         log(f'You successful connected to wifi network {wifi_network}', level=4)


          class Switching(object ):
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
                    subprocess.getoutput(cmd='blueutil -p off')
                    return 'Successful...'

               def enable_bluetooth(self):
                    """
                 Just enable bluetooth.
                 :return: Successfully
                 """
                    sleep(1)
                    subprocess.getoutput(cmd='blueutil -p on')
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
               def increase_brightness(self):
                    subprocess.getoutput(cmd="""osascript -e 'tell application "System Events"' -e 'key code 144' -e ' end tell'""")
               def lower_brightness(self):
                    subprocess.getoutput(cmd="""osascript -e 'tell application "System Events"' -e 'key code 145' -e ' end tell'""")


               @property
               def get_brightness(self):
                    return round(float(self.get_cur_brightness_per.split(' ')[-1]), ndigits=2)


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
                    subprocess.getoutput('system_profiler SPDisplaysDataType | grep Resolution').strip().split(":")[1].split(
                         ' ')
                    self.mem_size = subprocess.getoutput(cmd='sysctl -a | grep \'^hw\.m\'')
                    self.processor = subprocess.getoutput(cmd='sysctl -n machdep.cpu.brand_string')
                    del self.size[0], self.size[-1]


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
                    return f'Version your Mac os devise: {self.vers}'

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
                    return 'Memory-size:', int(self.mem_size.split(': ')[-1]) / pow(1024, 3)


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
                              raise NameError(f'Voice {voice} is unsupported on your devise.')
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
                    if  name_wifi_network in subprocess.getoutput(cmd='/System/Library/PrivateFrameworks/Apple80211.'
                                                                     'framework/Versions/A/Resources/airport scan') or subprocess.getstatusoutput(cmd=f'security find-generic-password -wa {name_wifi_network}')[0]!=0:
                         return password.strip()
                    else:
                        raise WifiValueError(f'Can not find wifi-network {repr(name_wifi_network)}')

          class Notifier(object):
               """Send different alerts"""

               def send_text_alert(self, text):
                    """
                 Make alert with point out text,
                 which displayed at the center of
                 screen.
                 :param text message in alert
                 (Available only on Mac-os)
                 """

                    cmd = f'osascript -e \'tell app "System Events" to display dialog "{text}"\''
                    subprocess.getoutput(cmd=cmd)

               def send_warning_alert(self, labeltext, buttons1, button2):
                    cmd = 'osascript -e \'tell application (path to frontmost application as text) to display dialog "%s" buttons {"%s", "%s"} with icon stop\'' % (labeltext, buttons1, button2)
                    return subprocess.getoutput(cmd=cmd)

               def send_lateral_message(self, label, subtitle, text, file_icon: [None, str], sound: [None, CONSTANT_SOUNDS]):
                    """
                  Make Lateral message with:
                  :param label: Main title on message
                  :param subtitle: Subtitle of message
                  :param text: Description of message
                  :param file_icon: Icon in message (Path to image)
                  (must local in project-folder) Point out [None]
                  if you don't want used icon
                  :return: Successful.
                  """

                    fullpath = str(pathlib.Path(str(file_icon)).cwd()) + '/' + str(file_icon)
                    commands = f"terminal-notifier -title '{label}' -subtitle '{subtitle}' -message '{text}' -appIcon {fullpath}"
                    commands2 = f'afplay /System/Library/Sounds/{sound if sound is not None else ""}.aiff'

                    subprocess.getoutput(cmd=commands)
                    subprocess.getstatusoutput(cmd=commands2)


          class Creator(object):
               """Create anything"""

               def create_file(self, name, extension):
                    """
                 Create file with setting & extension.
                 :param name: Name of created file
                 :param extension: Extension of created file
                 :return: Successful.
                 """
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
                         subprocess.getoutput(f'mkdir {name}')


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
                         raise UnsupportedFormat("Method can make files only with extension ['png', 'jpg', 'icns', 'gif', 'pict']")


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
                    if ord('q'):
                         return

               @property
               def list_devises(self):
                    """
                    Return all available devises for recording audio/video.
                    :return:
                    """
                    devises = '[' + str(
                         subprocess.getoutput(cmd='/opt/local/bin/ffmpeg -f avfoundation -list_devices true -i ""').split(
                              '[', maxsplit=1)[-1])
                    return devises.strip()


          class PhotoCapture(object):

               def capture(self, cam_index: int, extension, filename):
                    """
                 Method make image trough web-camera
                 :param cam_index: index where local camera
                 :param extension: extension of created image
                 :param filename: name of created file
                 :return: Successful...
                 """
                    subprocess.getoutput(cmd=f'/opt/local/bin/ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i "{cam_index}" -vframes 1 {filename}.{extension}')
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
                                      cmd=f'/opt/local/bin/ffmpeg -f avfoundation -t {record_time} -i ":{microphone_index}"  {filename}.{extension}')[0] == 1:
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
                    return bool(application_name in (i.name() for i in self.apps))

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
               @staticmethod
               def press(key):
                    subprocess.getoutput(cmd='osascript -e \'tell application '
                                             '"System Events" to keystroke "%s" using {shift down}\'' % str(key).upper())
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
                    """
                    # SAFARI - DEFAULT MAIN BROWSER, CHANGE YOUR
                    cmd = f'open /Applications/Safari.app {url}'  # Select your main browser
                    subprocess.getoutput(cmd=cmd)
                    log('Successful...', log=4)


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
               def __init__(self):
                    self.size = subprocess.getoutput(f'du -sh %')
                    self.time_cr = '%s'


               def get_date_create_file(self, path):
                    """
                    Return time, when file was used.
                    :param path:
                    :return:
                    """
                    return [ ctime(os.stat(self.time_cr % path).st_birthtime) ]

               def get_file_size(self, path):
                    """
                    Return size of file.
                    :param path: Path to file
                    :return:
                    """

                    return [self.size % path]

               @classmethod
               def extension(cls, path):
                    return str(path).split('.')[-1]

               @classmethod
               def name(cls, path):
                    return path.split('/', maxsplit=3)[-1].split('.')[0]


          class Volume(object):
               def __init__(self):

                    self.volume = 'osascript -e "set Volume %s"'
                    self.max_volume = 'osascript -e "set Volume 10"'
                    self.min_volume = 'osascript -e "set Volume 0"'
                    self.input_volume = subprocess.getoutput(cmd='osascript -e \'get volume settings\'').split(' ')[3].replace(',', '')
                    self.output_volume = subprocess.getoutput(cmd='osascript -e \'get volume settings\'').split(' ')[1].replace(',', '')

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




          class WebCameraCapture(object):
               """Collect data in camera"""

               def __init__(self):
                    self.cmd = '/opt/local/bin/ffmpeg -f avfoundation -t %s -framerate 30 -i "%s" -target pal-vcd ./%s.%s'
                    self.devises = '[' + str(subprocess.getoutput(cmd='/opt/local/bin/ffmpeg -f avfoundation -list_devices true -i ""').split('[', maxsplit=1)[-1])


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
                         raise  FileExistsError(f'Please, rename file {filename}.{extension}, him already exist.')
                    else:
                        return 'Check file is %s.%s' % (filename, extension)

               @property
               def list_devises(self):
                    """
                    Return all available devises for recording audio/video.
                    :return: Devises
                    """

                    return self.devises.strip().split(': ')[0]



elif sys.platform == 'win32':
     raise OSError('Windows version will be created soon...')

if __name__ == '__main__':
     exit(0)

