import subprocess
from .exceptions import ValueBrightnessError

class Brightness:
    def set_brightness(self, brightness):
        if type(brightness) != int or type(brightness) != float:
            raise ValueBrightnessError('Brightness must be type:', int, float)
        cmd = 'powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,%s)'
        subprocess.getoutput(cmd=cmd)