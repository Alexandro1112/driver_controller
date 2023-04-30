import subprocess
from .exceptions import *
class Password:
    def show_password_wifi(self, name_wifi_network):
        if subprocess.getstatusoutput(cmd=f'netsh wlan show profile name={name_wifi_network} key=clear')[
            0] == 1:
            raise WifiValueError(f'Can not find wifi-network {repr(name_wifi_network)}')
        else:
            password = subprocess.getoutput(
                cmd=f'netsh wlan show profile name={name_wifi_network} key=clear')
            return password.strip()