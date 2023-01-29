import subprocess
import sys
from .exceptions import *
from loger import *
from time import sleep
from psutil import process_iter
import os
# ---------------------------------------------------------------------------------------------------------------------|
# INSTALL   || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" OR
# REINSTALL || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"OR
#  sudo apt install ffmpeg / Build dependencies: sudo apt install libunistring-dev libaom-dev libdav1d-dev
# RUN || brew install brightness || brew doctor || brew install blueutil || brew install ffmpeg/port install ffmpeg

__all__ = [
     'ValueBrightnessError', 'LinuxCmd'
]


class ValueBrightnessError(TypeError):
    """
     Value is not type [int].
    """


if sys.platform == 'linux':
     class LinuxCmd(globals):
         class Brightness(object):
             def set_brightness(self, brightness_percent: int):
                 """
                             [LINUX DOCUMENTATION]
                  Automatically set brightness percent [type - int]
                            example: 25; 50; 75; 100(max)
                            :param brightness_percent:
                            :return: Successfully
                  """

                 if not isinstance(brightness_percent, int):
                     raise ValueBrightnessError('Type value of brightness must be ', int)

                 else:
                     if brightness_percent == 100:
                         brightness_percent -= brightness_percent + 1
                         subprocess.getoutput(cmd=f'brightness 1')
                         return 'Successful...'

                     elif isinstance(brightness_percent / 10, float):
                         brightness_percent *= 10
                         subprocess.getoutput(cmd=f'brightness 0.{brightness_percent}')
                         return 'Successful...'
                     else:

                         subprocess.getoutput(cmd=f'brightness 0.{brightness_percent}')
                         return 'Successful...'

         class Switcher(object):
             def unplug_bluetooth(self):
                 """
                 Just unplug bluetooth.
                 :return: Successfully
                 """

                 subprocess.getoutput(cmd='blueutil -p off')
                 return 'Successful...'

             def enable_bluetooth(self):
                 """
                 Just enable bluetooth.
                 :return: Successfully
                 """

                 subprocess.getoutput(cmd='blueutil -p on')
                 return 'Successful...'
         class Creator(object):
             """Create anything"""
             def create_file(self, name, extension):
                 """
                 Create file with setting & extension.
                 :param name: Name of created file
                 :param extension: Extension of created file
                 :return: Successful.
                 """
                 subprocess.getoutput(cmd=str('touch ') + str(name) + str('.') + str(extension))

             def create_folder(self, name):
                    """
                 Create folder.
                 :param name: Name of folder
                 :return: Successful
                 """
                    if name == '':
                         raise NameError('Assign this folder a name!') from None
                    else:
                         subprocess.getoutput(f'mkdir {name}')

         class ScreenCapture(object):
              """Make screenshot/video with settings"""

              def __init__(self):
                   self.AVAILABLE_EXTENSIONS = ('png', 'jpg', 'icns', 'gif', 'pict', 'eps')
                   self.command = 'ffmpeg -f avfoundation -t %s -framerate 10 -video_size 640x480 -i "%s:%s" %s.%s'

              def screenshot(self, filename, extension, pause=None):
                   """
                Method support ['png', 'jpg', 'ico', 'gif', 'pict', 'eps'] formats
                Make screenshot with pause, extensions and filename.
                :param pause: pause for determine screen capture [int, float, None].
                :param filename: Pointed out name of created file(path).
                :param extension: Extensions of created file.
                :return: Successful if created is passed.
                (Available only on Mac-os)
                """
                   """
                |----------------------------------------------|
                |Available extensions for function "screenshot"|
                |----------------------------------------------|
                """

                   if extension in [i for i in self.AVAILABLE_EXTENSIONS]:

                        sleep(pause if pause is not None else 0.0)
                        subprocess.getoutput(cmd=f'scrot ~/Photos/{filename}.{extension}')
                        return 'Successful...'

                   else:
                        """
                        [Format unsupported]
                        """
                        log('Unsupported format', level=3)
                        raise UnsupportedFormat(
                             "Method can make files only with extension ['png', 'jpg', 'icns', 'gif', 'pict']")

              def video_capture(self, record_time, camera_index, microphone_index, filename, extension):
                   """
                   Capture screen-video, click [q] for end video, and save them.
                   :param camera_index: Camera index where will be collected vide0
                   :param microphone_index: Microphone index, which used in video
                   :param filename: Name of file
                   :param extension: File Extension
                   :param record_time time of recording
                   :return:
                   """
                   subprocess.getoutput(
                        cmd=self.command % (record_time, camera_index, microphone_index, filename, extension))
                   if ord('q'):
                        return

              @property
              def list_devises(self):
                   """
                   Return all available devises for recording audio/video.
                   :return:
                   """
                   devises = '[' + str(
                        subprocess.getoutput(
                             cmd='ffmpeg -f avfoundation -list_devices true -i ""').split(
                             '[', maxsplit=1)[-1])
                   return devises.strip()

         class PhotoCapture(object):

              def capture(self, cam_index: int, extension, filename):
                   """
                Method make image trough web-camera
                :param cam_index: index where local camera
                :param extension: extension of created image
                :param filename: name of created file
                :return: Successful...
                """
                   subprocess.getoutput(
                        cmd=f'ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i "{cam_index}" -vframes 1 {filename}.{extension}')
                   return 'Check file is %s.%s' % (filename, extension)

         class AudioRecorder(object):
              """Audio recorder"""

              def __init__(self):
                   """
                Make variable AVAILABLE_EXTENSIONS is global.
                """
                   self.AVAILABLE_EXTENSIONS = (i for i in ('wav', 'mp3'))

              def recorder(self, microphone_index: 0, extension, filename, record_time: int):
                   """

                :param microphone_index: Microphone index
                :param extension: Extension of creates file
                :param filename: Name
                :param record_time: Record time (format minutes)
                :return:
                """
                   if extension in self.AVAILABLE_EXTENSIONS:
                        if os.path.isfile(f'{filename}.{extension}'):
                             raise FileExistsError(f'Please, rename file {filename}.{extension}, him already exist.')
                        else:

                             print('recording...')
                             if subprocess.getstatusoutput(
                                     cmd=f'ffmpeg -f avfoundation -t {record_time} -i ":{microphone_index}"  {filename}.{extension}')[
                                  0] == 1:
                                  raise IndexError

                             return 'Check file is %s.%s' % (filename, extension)



                   else:
                        raise UnsupportedFormat('Method can make files only with extensions (\'wav',
                                                           'mp3\')')

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
                    return bool(application_name in (i.name() for i in self.apps))


         class Switching(object):
              """Switch wi-fi/bluetooth"""

              def unplug_wifi(self):
                   """
                Just unplug wi-fi.
                :return: Successfully
                """
                   sleep(1)
                   subprocess.getoutput(cmd='networksetup -setairportpower en0 off')
                   return 'Successful...'

              def enable_wifi(self):
                   """
                Just enable wi-fi.
                :return: Successfully
                """

                   sleep(1)
                   subprocess.getoutput(cmd='networksetup -setairportpower en0 on')
                   return 'Successful...'

              def unplug_bluetooth(self):
                   """
                Just unplug bluetooth.
                :return: Successfully
                """

                   sleep(1)
                   subprocess.getoutput(cmd='blueutil -p off')
                   return 'Successful...'

              def enable_bluetooth(self):
                   """
                Just enable bluetooth.
                :return: Successfully
                """
                   sleep(1)
                   subprocess.getoutput(cmd='blueutil -p on')
                   return 'Successful...'


else:
    raise NotImplementedError('')
