import AppKit
from .exceptions import *
import subprocess


class Open(object):

    def application(self, application_name):
        """
     Open application by his name.
     :param path_app: Path to Application
     (begin from /Applications/{path_app}.app)
     EXAMPLE [/Applications/Finder.app]
     :return: Successful if successful opened app.
     """
        boolean = AppKit.NSWorkspace.sharedWorkspace().launchApplication_(
            application_name
        )
        if not boolean:
            raise ApplicationNotExist(f'Application {application_name} not exist.')

    def url(self, url, browser='Safari'):
        """
        Open url in main browser
        DEFAULT BROWSER: Safari.
        :param url: 'url'
        :return: None
        :param url: 
        :return: 
        """  # SAFARI - DEFAULT MAIN BROWSER, CHANGE YOUR
        cmd = f'open /Applications/{browser}.app {url}'  # Select your main browser
        return subprocess.getoutput(cmd=cmd)

    def open_spotlight(self):
        """Open spotlight menu."""


    def open_file(self, path):
        AppKit.NSWorkspace.sharedWorkspace().openFile_(
            path)

    def open_file_in_app(self, app_name, file):
        open_objc = AppKit.NSWorkspace.sharedWorkspace().openFile_withApplication_(file, app_name)

        if open_objc is False:
            raise OpenPossibilityError \
                (f'Can not open file {file}, because application {app_name} not support format this files.')