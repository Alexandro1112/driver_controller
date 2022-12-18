import subprocess
import sys
from warnings import filterwarnings
from shutup import please
from time import sleep


class WifiNameConnectError(NameError):
    pass


class ValueBrightnessError(ValueError, TypeError):
    pass


if sys.platform == 'darwin' or sys.platform == 'linux':

    def get_list_wifi_network():
        networks = subprocess.getoutput('/System/Library/PrivateFrameworks/Apple80211.'
                                        'framework/Versions/A/Resources/airport scan')
        return networks.replace('SSID BSSID             RSSI CHANNEL HT CC SECURITY (auth/unicast/group)', '')

    def get_list_bluetooth_device():
        bluetooth = subprocess.getoutput('system_profiler SPBluetoothDataType')
        return bluetooth.split(
            'Bluetooth:')[0]

    def connect_wifi_network(wifi_network=None):
        please()
        connect_GADGET = subprocess.getoutput(f'networksetup -setairportnetwork en0 {wifi_network}')
        if connect_GADGET != f'Could not find network {wifi_network}' or wifi_network is None:

            filterwarnings('ignore')
            filterwarnings('ignore', category=DeprecationWarning)

            filterwarnings('ignore', category=FutureWarning)
            filterwarnings('ignore', category=Warning)
            raise WifiNameConnectError(f'Could not find network {wifi_network}')
        else:
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

    def enable_bluetooth():
        sleep(1)
        subprocess.getoutput('blueutil -p on')

    def set_brightness(brightness_percent: int):

        if not isinstance(brightness_percent, int):
            raise ValueBrightnessError('Type value of brightness must be ')

        else:

            subprocess.getoutput(f'brightness .{brightness_percent}')
            return 'Successful...'

else:
    raise NotImplementedError('This module is unsupported Windows OS, only Mac Osx or Linux Os!')
