import subprocess
import sys
from warnings import filterwarnings
from shutup import please
from time import sleep


__all__ = [
    'set_max_brightness', 'devise_battery', 'connect_wifi_network', 'get_list_wifi_network', 'set_min_brightness',
    'set_brightness', 'get_list_bluetooth_device', 'macos_version', 'enable_bluetooth', 'enable_wifi', 'unplug_wifi',
    'unplug_bluetooth', 'send_voice_notify', 'show_password_wifi', 'WifiValueError', 'WifiNameConnectError', 
    'ValueBrightnessError'
]


class WifiNameConnectError(NameError):
    pass


class ValueBrightnessError(ValueError, TypeError):
    pass


class WifiValueError(ValueError, BaseException):
    pass


if sys.platform == 'darwin' or sys.platform == 'linux':

    def get_list_wifi_network():
        networks = subprocess.getoutput('/System/Library/PrivateFrameworks/Apple80211.'
                                        'framework/Versions/A/Resources/airport scan')
        return networks.replace('SSID BSSID             RSSI CHANNEL HT CC SECURITY (auth/unicast/group)', '')

    def get_list_bluetooth_device():
        bluetooth = subprocess.getoutput('system_profiler SPBluetoothDataType')
        return bluetooth.split(
            'Bluetooth:')[0].capitalize()

    def connect_wifi_network(wifi_network=None, password=None) -> str:

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
        sleep(1)
        subprocess.getoutput('networksetup -setairportpower en0 off')
        return 'Successful...'

    def enable_wifi():
        sleep(1)
        subprocess.getoutput('networksetup -setairportpower en0 on')
        return 'Successful...'

    def unplug_bluetooth():
        sleep(1)
        subprocess.getoutput('blueutil -p off')
        return 'Successful...'

    def enable_bluetooth():
        sleep(1)
        subprocess.getoutput('blueutil -p on')
        return 'Successful...'

    def set_brightness(brightness_percent: int):

        if not isinstance(brightness_percent, int):
            raise ValueBrightnessError('Type value of brightness must be ')

        else:

            subprocess.getoutput(f'brightness .{brightness_percent}')
            return 'Successful...'

    def set_max_brightness():
        subprocess.getoutput('brightness -v 1')
        return 'Successful...'

    def set_min_brightness():
        subprocess.getoutput('brightness -v 0')
        return 'Successful...'

    def devise_battery():
        return f'Battery percent: {str(subprocess.getoutput("pmset -g batt").split()[7].replace(";",r""))}'

    def macos_version():
        return f'Version your Mac os devise: {subprocess.getoutput("sw_vers -productVersion")}'

    def send_voice_notify(text=None):
        subprocess.getoutput(f'say {text}')
        return 'Successful...'

    def show_password_wifi(name_wifi_network=None):

        password = subprocess.getoutput(f'security find-generic-password -wa {name_wifi_network}')
        if name_wifi_network in subprocess.getoutput('/System/Library/PrivateFrameworks/Apple80211.'
                                                     'framework/Versions/A/Resources/airport scan'):
    
            return password.strip()
        return WifiValueError(f'Wifi network {name_wifi_network} is not found.')

else:
    raise NotImplementedError('This module is unsupported Windows OS, only Mac Osx or Linux Os!')
