# Copyright (c) 2023 Aleksandr Bosov. All rights reserved.
# The library is designed for Mac-OS, performs technical functions
# such as disabling Wi-Fi, Bluetooth, sends notifications: text,
# sound, working with screen brightness, and much more.

import subprocess
import sys
from warnings import filterwarnings
from shutup import please
from time import sleep


"""
individual exceptions
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


__all__ = [
    'set_max_brightness', 'devise_battery', 'connect_wifi_network', 'get_list_wifi_network', 'set_min_brightness',
    'set_brightness', 'get_list_bluetooth_device', 'macos_version', 'enable_bluetooth', 'enable_wifi', 'unplug_wifi',
    'unplug_bluetooth', 'send_voice_notify', 'show_password_wifi', 'WifiValueError', 'WifiNameConnectError',
    'ValueBrightnessError', 'send_text_alert', 'create_file', 'InvalidExtension', 'LinuxWhileNotSupport', 'Voice',
    'send_lateral_message'
]


if sys.platform == 'darwin':

    def get_list_wifi_network():
        """ Function output all wi-fi networks,
         which available for your devise."""
        networks = subprocess.getoutput(cmd='/System/Library/PrivateFrameworks/Apple80211.'
                                        'framework/Versions/A/Resources/airport scan')
        return networks.replace('SSID BSSID             RSSI CHANNEL HT CC SECURITY (auth/unicast/group)', '')

    def get_list_bluetooth_device():
        """ Function output all bluetooth devise(s),
         which available to your devise."""

        bluetooth = subprocess.getoutput(cmd='system_profiler SPBluetoothDataType')

        return bluetooth.split('Bluetooth:')[0].capitalize()

    def connect_wifi_network(wifi_network=None, password=None):
        """
        Auto connect to wi-fi network.

        :param wifi_network: Wi-fi name, which you would to connect.
        :param password: Password of this Network.(Not show him in global project(use hide variable))
        :return: 'Successful...' if you successfully connect to wi-fi.
        """
        please()

        connect_GADGET = subprocess.getoutput(cmd=f'networksetup -setairportnetwork en0 {wifi_network} {password}')
        if connect_GADGET.strip() != '':
            filterwarnings('ignore')
            filterwarnings('ignore', category=DeprecationWarning)

            filterwarnings('ignore', category=FutureWarning)
            filterwarnings('ignore', category=Warning)
            raise WifiNameConnectError(f'Could not find network {wifi_network}')

        return f'You successful connected to wifi network {wifi_network}'

    def unplug_wifi():
        """
        Just unplug wi-fi.
        :return: Successfully
        """
        sleep(1)
        subprocess.getoutput(cmd='networksetup -setairportpower en0 off')
        return 'Successful...'

    def enable_wifi():
        """
        Just enable wi-fi.
        :return: Successfully
        """

        sleep(1)
        subprocess.getoutput(cmd='networksetup -setairportpower en0 on')
        return 'Successful...'

    def unplug_bluetooth():
        """
        Just unplug bluetooth.
        :return: Successfully
        """

        sleep(1)
        subprocess.getoutput(cmd='blueutil -p off')
        return 'Successful...'


    def enable_bluetooth():
        """
        Just enable bluetooth.
        :return: Successfully
        """
        sleep(1)
        subprocess.getoutput(cmd='blueutil -p on')
        return 'Successful...'

    def set_brightness(brightness_percent: int):
        """
        Automatically set brightness percent [type - int]
        :param brightness_percent:
        :return: Successfully
        """

        if not isinstance(brightness_percent, int):
            raise ValueBrightnessError('Type value of brightness must be ', int)

        else:
            subprocess.getoutput(cmd=f'brightness .{brightness_percent}')
            return 'Successful...'

    def set_max_brightness():
        """
        Set max brightness of screen equal one hundred
        :return: Successfully
        """
        subprocess.getoutput(cmd='brightness -v 1')
        return 'Successful...'


    def set_min_brightness():
        """
        Set min brightness of screen equal zero
        :return: Successfully
        """

        subprocess.getoutput(cmd='brightness -v 0')
        return 'Successful...'

    def devise_battery():
        """
        Return battery percent of
        computer at current time.
        :return: Battery percent
        """

        return f'Battery percent: {str(subprocess.getoutput(cmd="pmset -g batt").split()[7].replace(";",r"%"))}'

    def macos_version():
        """
        Function.
        :return: Version your devise.
        """
        return f'Version your Mac os devise: {subprocess.getoutput(cmd="sw_vers -productVersion")}'

    def send_voice_notify(text=None):
        """
        Send voice notify with text, which you point out.
        :param text:
        :return: voice
        """
        if text is None:
            return NameError

        subprocess.getoutput(cmd=f'say {text}')
        return 'Successful...'

    def show_password_wifi(name_wifi_network=None):
        """
             [!!DANGEROUS!!]
        Function return password
        of saved wi-fi network
        trough util "bunch of keys".
        (Must be Administrator for run this code)
        (Available only on Mac-os)
        :param name_wifi_network:
        :return: password of network
        """

        password = subprocess.getoutput(f'security find-generic-password -wa {name_wifi_network}')
        if name_wifi_network in subprocess.getoutput(cmd='/System/Library/PrivateFrameworks/Apple80211.'
                                                     'framework/Versions/A/Resources/airport scan'):
            return password.strip()
        return WifiValueError(f'Wifi network {name_wifi_network} is not found.')

    def send_text_alert(text):
        """Make alert with point out text. """

        part1 = "osascript -e 'tell app "
        part2 = '"System Events" to display dialog "'
        part3 = '"'
        part4 = "'"
        subprocess.getoutput(str(part1) + str(part2) + str(text) + str(part3) + str(part4))
        return 'Successful...'

    def create_file(name, extension):
        """
        Create file with setting & extension.
        :param name: Name of created file
        :param extension: Extension of created file
        :return: Successful.
        """
        subprocess.getoutput(cmd=str('touch ') + str(name) + str('.') + str(extension))

        return 'Successful...'

    def send_lateral_message(label, subtitle, text):
        """
        Make Lateral message.
        :param label: Main title on message
        :param subtitle: Subtitle of message
        :param text: Description of message
        :return: Successful
        """
        command = f"terminal-notifier -title '{label}' -subtitle '{subtitle}' -message '{text}'" \
            f" -open https://myserver.local.net/stat_log.html -group 0 -execute `terminal-notifier -remove 0`"

        subprocess.getoutput(cmd=command)
        return 'Successful...'

    def create_folder(name):
        """
        Create folder.
        :param name: Name of folder
        :return: Successful
        """
        subprocess.getoutput(f'mkdir {name}')
        return 'Successful...'

    class Voice(object):
        """
        class Voice add more available
        voices & effects(which beforehand
        installed in Mac-os.)
        """

        def __init__(self: None, voice: bool):
            if voice is not True:
                raise ConfirmationError('Argument voice must be [True]')
            else:
                return

        @staticmethod
        def pop():
            """Pop voice-notify."""
            subprocess.getoutput(cmd=str('for i in {1..1}; do afplay /System/Library/Sounds/Pop.aiff -v 10; done'))

        @staticmethod
        def blow():
            """Blow voice-notify."""
            subprocess.getoutput(cmd=str('for i in {1..1}; do afplay /System/Library/Sounds/Blow.aiff -v 10; done'))

        @staticmethod
        def glass():
            """Glass voice-notify."""
            subprocess.getoutput(cmd=str('for i in {1..1}; do afplay /System/Library/Sounds/Glass.aiff -v 10; done'))

        @staticmethod
        def funk():
            """Funk voice-notify."""
            subprocess.getoutput(cmd=str('for i in {1..1}; do afplay /System/Library/Sounds/Funk.aiff -v 10; done'))


elif sys.platform == 'win32':
    raise NotImplementedError('Windows is unsupported platform, only Mac Osx or Linux Os!')

else:
    raise LinuxWhileNotSupport('Linux is not supported since the creation of the library')
