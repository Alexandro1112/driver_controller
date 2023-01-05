# Copyright (c) 2022 Aleksandr Bosov. All rights reserved.

import subprocess
import sys
from warnings import filterwarnings
from shutup import please
from time import sleep


"""
individual exceptions
"""


class LinuxWhileNotSupport(NotImplementedError):
    """
    TODO:
    make linux version in a future
    """


class WifiNameConnectError(NameError):
     """
     Password or SSID of Network is not right.
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
    'ValueBrightnessError', 'send_text_alert'
]


if sys.platform == 'darwin':

    def get_list_wifi_network():
        """ Function output all wi-fi networks devise(s),
         which available to your devise"""
        networks = subprocess.getoutput('/System/Library/PrivateFrameworks/Apple80211.'
                                        'framework/Versions/A/Resources/airport scan')
        return networks.replace('SSID BSSID             RSSI CHANNEL HT CC SECURITY (auth/unicast/group)', '')

    def get_list_bluetooth_device():
        """ Function output all bluetooth devise(s),
         which available to your devise"""

        bluetooth = subprocess.getoutput('system_profiler SPBluetoothDataType')

        return bluetooth.split('Bluetooth:')[0].capitalize()

    def connect_wifi_network(wifi_network=None, password=None):
        """
        Auto connect to wi-fi network.

        :param wifi_network: Wi-fi name, which you would to connect.
        :param password: Password of this Network.
        :return: 'Successful...' if you successfully connect to wi-fi.
        """

        name_error = f'Failed to join network {wifi_network}.' \
                     'Error: -3924  The operation couldn’t be completed. ' \
                     '(com.apple.wifi.apple80211API.error error -3924.)'
        password_error = f'Could not find network {wifi_network}.'
        please()

        connect_GADGET = subprocess.getoutput(f'networksetup -setairportnetwork en0 {wifi_network} {password}')
        if connect_GADGET == name_error or connect_GADGET == password_error:
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
        subprocess.getoutput('networksetup -setairportpower en0 off')
        return 'Successful...'

    def enable_wifi():
        """
        Just enable wi-fi.
        :return: Successfully
        """

        sleep(1)
        subprocess.getoutput('networksetup -setairportpower en0 on')
        return 'Successful...'

    def unplug_bluetooth():
        """
        Just unplug bluetooth.
        :return: Successfully
        """

        sleep(1)
        subprocess.getoutput('blueutil -p off')
        return 'Successful...'


    def enable_bluetooth():
        """
        Just enable bluetooth.
        :return: Successfully
        """
        sleep(1)
        subprocess.getoutput('blueutil -p on')
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
            subprocess.getoutput(f'brightness .{brightness_percent}')
            return 'Successful...'

    def set_max_brightness():
        """
        Set max brightness of screen equal one hundred
        :return: Successfully
        """
        subprocess.getoutput('brightness -v 1')
        return 'Successful...'


    def set_min_brightness():
        """
        Set min brightness of screen equal zero
        :return: Successfully
        """

        subprocess.getoutput('brightness -v 0')
        return 'Successful...'

    def devise_battery():
        """
        Output battery percent of computer.
        :return: Battery percent
        """

        return f'Battery percent: {str(subprocess.getoutput("pmset -g batt").split()[7].replace(";",r""))}'

    def macos_version():
        """
        Function.
        :return: Version your devise.
        """
        return f'Version your Mac os devise: {subprocess.getoutput("sw_vers -productVersion")}'

    def send_voice_notify(text=None):
        """
        Send voice notify with text, which you point out.
        :param text:
        :return:
        """
        if text is None:
            return NameError

        subprocess.getoutput(f'say {text}')
        return 'Successful...'

    def show_password_wifi(name_wifi_network=None):
        """
        [!!DANGEROUS!!] Function return password
        of saved wi-fi network
        trough util "bunch of keys".
        (Must be Administrator)
        (Available only on Mac-os)
        :param name_wifi_network:
        :return: password
        """

        password = subprocess.getoutput(f'security find-generic-password -wa {name_wifi_network}')
        if name_wifi_network in subprocess.getoutput('/System/Library/PrivateFrameworks/Apple80211.'
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

elif sys.platform == 'win32':
    raise NotImplementedError('This module is unsupported Windows OS, only Mac Osx or Linux Os!')
else:
    raise LinuxWhileNotSupport('Linux is not supported since the creation of the library')
