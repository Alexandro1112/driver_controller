import subprocess
import psutil
import AppKit
from .exceptions import ApplicationNameError


class AppConfigure(object):
    """App-settings"""

    def get_full_path_by_app_name(self, app):
        return AppKit.NSWorkspace.sharedWorkspace().fullPathForApplication_(app)

    def get_app_size(self, app_name):
        """
        Return size of app by him name.
        :param app_name: App name, which exist in /Applications/<NAME>.app
        :return: Size in megabytes/gigabytes
        """
        path = f'du -sh {self.get_full_path_by_app_name(app_name)}'
        if app_name not in (i.name() for i in psutil.process_iter()):
            raise ApplicationNameError
        else:
            return subprocess.getoutput(cmd=path).split()[0]

    def move_app(self, app, x, y, width, height):
        return subprocess.getoutput(cmd="""osascript -e 'tell application "%s"
                                   set bounds of front window to {%s, %s, %s, %s}
                                   end tell'""" % (app, x, y, width, height), encoding='utf-8')

