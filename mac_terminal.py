# /opt/anaconda3/bin/python
# Copyright (c) 2022-2023 Aleksandr Bosov. All rights reserved.
# The library is designed for Mac-OS, performs technical
# functions such as disabling Wi-Fi, Bluetooth, sends ,
# notifications: text, sound, recording audio, working with screen brightness,
# control devises and much more.
# ---------------------------------------------------------------------------------------------------------------------|
# INSTALL  || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" OR
# REINSTALL (if need)|| /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# LIB - INSTALLER || brew install brightness || brew doctor || brew install blueutil || brew install ffmpeg ||
# pip install loger || pip install shutup || pip install psutil
# Installations this dependencies will be automatic if you use git-repository.
# ---------------------------------------------------------------------------------------------------------------------|
#  Any files which use code already installed in
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
from time import sleep

# for get list applications
from psutil import process_iter
# Constants
from .CONSTANTS import *

# Log-alerts
from loger import *

"""
|---------------------|
|individual exceptions|
|---------------------|
"""


class UseLinuxTerminal(FileNotFoundError):
    """
    Linux version already working.
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


class LinuxWhileNotSupport(NotImplementedError):
    """
    TODO:
    make linux version library in a future.
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


__all__ = ['PasswordManager',  'WifiValueError', 'WifiNameConnectError',
            'ValueBrightnessError', 'InvalidExtension', 'Sound', 'AppSystem',  'Open',
           'Clicker', 'LOWER', 'UPPER', 'SystemConfig', 'OutputListsDevises', 'Brightness', 'Switching', 'Notifier', 'Connector'
            ,'Creator', "VoiceOver",'ScreenCapture', 'PhotoCapture', "AudioRecorder", 'UnsupportedFormat', 'CONSTANT_SOUNDS'
]


class UPPER:
    """
    Upper text register for press() method
    """

    UPPER = 'upper'


class LOWER:
    """
    Lower text register for press() method
    """
    LOWER = 'lower'


if sys.platform == 'darwin':

    class OutputListsDevises(object):
        """ Return output devises """

        def get_list_wifi_networks(self):
            """ Function output all wi-fi networks,
                  which available for your devise."""
            self.scan_cmd = subprocess.Popen(['airport', '-s'], stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
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
                print(self.networks.split())

        def get_list_bluetooth_device(self):
            """ Function output all bluetooth devise(s),
             which available for your devise."""
            self.bluetooth = subprocess.getoutput(cmd='system_profiler SPBluetoothDataType')

            return self.bluetooth.split('Bluetooth:')[0].capitalize()

        def get_list_audio_devises(self):
            """
            Return all audio
            connectable devises.
            :return: devises
            (Available only on Mac-os)
            """
            self.devises = subprocess.getoutput(cmd='system_profiler SPAudioDataType')

            return self.devises

    class Connector(object):
        def connect_wifi_network(self, wifi_network, password):
            """
            Auto connect to wi-fi network.

            :param wifi_network: Wi-fi name, which you would to connect.
            :param password: Password of this Network.(use hide variable)
            :return: 'Successful...' if you successfully connect to wi-fi.
            """
            please()

            connect_GADGET = subprocess.getoutput(cmd=f'networksetup -setairportnetwork en0 {wifi_network} {password}')
            if connect_GADGET.strip() != '':
                filterwarnings('ignore', category=DeprecationWarning)
                raise WifiNameConnectError(f'Could not find network {wifi_network}')

            else:
                log(f'You successful connected to wifi network {wifi_network}', level=4)


    class Switching(object):
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


    class SystemConfig(object):
        def __init__(self):

            self.percent = subprocess.getoutput(cmd="pmset -g batt").split()[7].replace(";", r"")
            self.vers = subprocess.getoutput(cmd="sw_vers -productVersion")
            airport = pathlib.Path("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport")

            self.network = subprocess.getoutput(cmd=f"{airport} -I | awk '/ SSID/ {{print substr($0, index($0, $2))}}'").capitalize()
            self.size = subprocess.getoutput('system_profiler SPDisplaysDataType | grep Resolution').strip().split(":")[1].split(' ')
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

    class VoiceOver(object):
        def text_voiceover(self, text=None):
            """
            Send voice notify with text,
            which you point out.
            :param text:
            :return: voice with point outed text
            """

            if text is None:
                raise NameError
            subprocess.getoutput(cmd=f'say {text}')


    class PasswordManager(object):
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

            password = subprocess.getoutput(f'security find-generic-password -wa {name_wifi_network}')
            if name_wifi_network in subprocess.getoutput(cmd='/System/Library/PrivateFrameworks/Apple80211.'
                                                             'framework/Versions/A/Resources/airport scan'):
                return password.strip()
            raise WifiValueError(f'Wifi network {name_wifi_network} is not found.')

    class Notifier(object):
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
            cmd = 'osascript -e \'tell application (path to frontmost ' \
                 f'application as text) to display dialog "{labeltext}" ' \
                 f'buttons {repr(buttons1), repr(button2)} with icon stop\''
            subprocess.getoutput(cmd=cmd)

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
        def __init__(self):
            self.AVAILABLE_EXTENSIONS = ('png', 'jpg', 'icns', 'gif', 'pict', 'eps')

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

                sleep(pause if pause is not None else 0)
                subprocess.getoutput(cmd=f'screencapture {filename}.{extension}')
                return 'Successful...'

            else:
                """
                [Format unsupported]
                """
                log('Unsupported format', level=3)
                raise UnsupportedFormat(
                   "Method can make files only with extension ['png', 'jpg', 'icns', 'gif', 'pict']")

    class PhotoCapture(object):

         def capture(self, cam_index: int, extension, filename):
             """
              Method make image trough web-camera
             :param cam_index: index where local camera
             :param extension: extension of created image
             :param filename: name of created file
             :return:
             """
             subprocess.getoutput(cmd=f'ffmpeg -f avfoundation -video_size {1280}x{720}'
                                      f' -framerate 30 -i "{cam_index}" -vframes 1 {filename}.{extension}')
             return 'Successful...'


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
             :param record_time: Record time (Mean seconds)
             :return:
             """
             if extension in self.AVAILABLE_EXTENSIONS:
                 print('recording...')
                 subprocess.getoutput(cmd=f'ffmpeg -f avfoundation -i ":{microphone_index}" -t {record_time} {filename}.{extension}')
                 return 'Successful...'

             else:
                  raise UnsupportedFormat('Method can make files only with extensions (\'wav', 'mp3\')')
    class AppSystem(object):
       def is_exist(self, application_name):
           """
           Check of existing of app({application_name})
           :param application_name: APP name
           :return: [True] if application
           exist on your devise, [False] - if no.
           """
           return bool(application_name in (i.name() for i in process_iter()))

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
       def press(self, button, register: [LOWER, UPPER]):
           if register == 'upper':

                subprocess.getoutput(cmd='osascript -e \'tell application '
                                         '"System Events" to keystroke "%s" using {shift down}\'' % str(button).upper())
                return 'Successful...'
           elif register == 'lower':
                subprocess.getoutput(cmd='osascript -e \'tell application '
                                         '"System Events" to keystroke "%s" using {shift down}\'' % str(button).lower())
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
            """                       # SAFARI - DEFAULT MAIN
            cmd = f'open /Applications/Safari.app {url}' # Select your main browser
            subprocess.getoutput(cmd=cmd)
            subprocess.getstatusoutput(cmd=cmd)
            log('Successful...', log=4)


    class Sound(object):
        """
        class Voice add more available
        voices & effects(which beforehand
        installed in Mac-os.)
        """

        def __init__(self, sound: bool):
            if sound is not True:
                raise ConfirmationError('Argument "sound" must be [True]')
            else:
                sound += True

        @staticmethod
        def pop_sound(iters: int):
            """
            Pop voice-notify.
            :param iters How mane
            iterations(repeats) of sound.
            (Available only on Mac-os)
            """

            subprocess.getoutput(cmd='for i in {1..%s}; do afplay /System/Library/Sounds/Pop.aiff -v 10; done' % iters)


        @staticmethod
        def blow_sound(iters: int):
            """Blow voice-notify.
            :param iters How mane
            iterations(repeats) of sound.
            (Available only on Mac-os)
            """
            subprocess.getoutput(cmd='for i in {1..%s}; do afplay /System/Library/Sounds/Blow.aiff -v 10; done' % iters)


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



elif sys.platform == 'win32':
     raise OSError



if __name__ == '__main__':
    exit(1)

