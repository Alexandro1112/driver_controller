import subprocess
from .exceptions import *
import sys

# Windows version lib.
# Currently, no dependencies for classes.

if sys.platform.lower() == 'win32':
     class WindowsCmd(object):
          class Notifier(object):
               def __init__(self):
                    self.STOP_ICON = 0x10
                    self.WARNING_ICON = 0x30
                    self.QUESTION_ICON = 0x20
                    self.center_message = 'powershell (New-Object -ComObject Wscript.Shell).Popup("""%s""",0,"""%s""",%s)'

               def send_text_message(self, text, label, icon):
                   
                   if icon == 'stop':
                       subprocess.getoutput(cmd=self.center_message % (text, label, self.STOP_ICON))
                   elif icon == 'warning':
                       subprocess.getoutput(cmd=self.center_message % (text, label, self.WARNING_ICON))
                   elif icon == 'question':
                       subprocess.getoutput(cmd=self.center_message % (text, label, self.QUESTION_ICON))
                   
                   else:
                       raise ValueError( ' ' )

          class Password:
               def show_password_wifi(self, name_wifi_network):

                    if subprocess.getstatusoutput(cmd=f'netsh wlan show profile name={name_wifi_network} key=clear')[
                         0] == 1:
                         raise WifiValueError(f'Can not find wifi-network {repr(name_wifi_network)}')
                    else:
                         password = subprocess.getoutput(
                              cmd=f'netsh wlan show profile name={name_wifi_network} key=clear')
                         return password.strip()


          class Brightness:
              def set_brightness(self, brightness):
                  if type(brightness) != int or type(brightness) != float:
                        raise ValueBrightnessError('Brightness must be type:', int, float)
                  cmd = 'powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,%s)'
                  subprocess.getoutput(cmd=cmd)
else:
     raise OSError("")

if __name__ == '__name__':
     exit(0)
