import subprocess
from time import sleep
from .exceptions import *


class ScreenCapture(object):
    """Make screenshot/video with settings"""

    def __init__(self):
        self.AVAILABLE_EXTENSIONS = ('png', 'jpg', 'icns', 'gif', 'pict', 'eps')
        self.command = '/opt/local/bin/ffmpeg -f avfoundation -t %s -framerate 10 -video_size 640x480 -i "%s:%s" %s.%s'

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

        if extension in (i for i in self.AVAILABLE_EXTENSIONS):

            sleep(pause if pause is not None else 0.0)
            subprocess.getoutput(cmd=f'screencapture {filename}.{extension}')
            return 'Successful...'

        else:
            raise UnsupportedFormat(
                "Method can make files only with extension ['png', 'jpg', 'icns', 'gif', 'pict']")

    def video_capture(self, record_time, camera_index, microphone_index, filename, extension):
        """
        Capture screen-video.
        :param camera_index: Camera index where will be collected vide0
        :param microphone_index: Microphone index, which used in video
        :param filename: Name of file
        :param extension: File Extension
        :param record_time time of recording
        :return:
        """
        subprocess.getoutput(
            cmd=self.command % (record_time, camera_index, microphone_index, filename, extension))

    @property
    def list_devises(self):
        """
        Return all available devises for recording audio/video.
        :return:
        """
        devises = '[' + str(subprocess.getoutput(
            cmd='/opt/local/bin/ffmpeg -f avfoundation -list_devices true -i ""').split('[', maxsplit=1)[
                                -1])
        return devises.strip().split(': ')[0]

    @property
    def available_extension(self):
        return (self.AVAILABLE_EXTENSIONS)