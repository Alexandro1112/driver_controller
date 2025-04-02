import subprocess
from time import sleep
import AppKit
from psutil import process_iter


class AppSystem(object):
    def __init__(self):
        self.apps = process_iter()

    def is_exist(self, application_name):
        """
     Check of existing of app({application_name})
     :param application_name: APP name
     :return: [True] if application
     exist on your devise, [False] - if no.
     """
        return application_name in (i.name() for i in self.apps)

    def close_app(self, application_name):
        """
     Close app.
     :param application_name:
     Name of App which will
     be close.
     :return: [None]
     """
        subprocess.getoutput(cmd=f'pkill {application_name}')
        

    def close_all_app(self):
        for apps in AppKit.NSWorkspace.sharedWorkspace().runningApplications():
            apps.terminate()

    def current_opened_app(self, pause):
        sleep(pause)
        activeAppName = AppKit.NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        return activeAppName

    def isopened(self, application_name):
        """Returns a boolean value depending on whether the application is open."""
        return AppKit.NSWorkspace.sharedWorkspace().openFile_withApplication_andDeactivate_(None,
                                                                                            f'{application_name}',
                                                                                            None)

    def get_size_icon_by_app(self, application_name):
        activeAppName = AppKit.NSWorkspace.sharedWorkspace().iconForFile_(
            f'/Applications/{application_name}')
        size = str(activeAppName).split(' ')[2] + str(activeAppName).split(' ')[3]
        return size
