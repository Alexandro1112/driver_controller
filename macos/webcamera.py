import subprocess
import os

class WebCameraCapture(object):
    """Collect data in camera"""

    def __init__(self):
        self.cmd = '/opt/local/bin/ffmpeg -f avfoundation -t %s -framerate 30 -i "%s" -target pal-vcd ./%s.%s'
        self.devises = '[' + str(subprocess.getoutput(
            cmd='/opt/local/bin/ffmpeg -f avfoundation -list_devices true -i ""').split('[', maxsplit=1)[
                                     -1])

    def webcam_capture(self, record_time: int, camera_index, filename, extension):
        """
        Record video in webcam
        :param record_time: Recording time(seconds)
        :param camera_index: Camera index
        :param filename: Name of created file
        :param extension: Extension of file
        :return: [None]
        """

        subprocess.getoutput(cmd=self.cmd % (record_time, camera_index, filename, extension))
        if os.path.isfile(f'{filename}.{extension}'):
            raise FileExistsError(f'Please, rename file {filename}.{extension}, because it already exist.')
        else:
            return 'Check file is %s.%s' % (filename, extension)

    @property
    def list_devises(self):
        """
        Return all available devises for recording audio/video.
        :return: Devises
        """

        return '[' + str(self.devises.strip().split('[', maxsplit=1)[-1].split(': ')[0])