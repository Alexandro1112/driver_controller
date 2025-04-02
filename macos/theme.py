import subprocess
from time import sleep
from AppKit import NSUserDefaults

class Theme:
    def __init__(self):
        self.cmd = 'osascript -e \'tell app "System Events" to tell appearance ' \
                   'preferences to set dark mode to not dark mode\''

    def change_color_mode(self):
        subprocess.getoutput(self.cmd)

    def current_theme(self):
        """Print current color mode on mac."""
        return NSUserDefaults.standardUserDefaults().stringForKey_(u"AppleInterfaceStyle")
