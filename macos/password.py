import subprocess

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
