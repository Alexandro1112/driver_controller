import subprocess
from time import sleep

class Theme:
    def __init__(self):
        self.cmd = 'osascript -e \'tell app "System Events" to tell appearance ' \
                   'preferences to set dark mode to not dark mode\''

    def change_color_mode(self, pause: [int, float, complex]):
        sleep(pause)
        subprocess.getoutput(cmd=self.cmd)

    def current_theme(self):
        """Print current color mode on mac."""
        if not 'Dark' in subprocess.getoutput('defaults find AppleInterfaceStyle'):
            return "Light"
        return subprocess.getoutput('defaults find AppleInterfaceStyle').split(": ")[-1].split()[:2:-1][-1].replace(
            r';', '')