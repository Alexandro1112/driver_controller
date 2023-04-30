import subprocess


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
            cmd=f'/opt/local/bin/ffmpeg -f avfoundation -video_size 1280x720 -framerate 30 -i "{cam_index}" -vframes 1 {filename}.{extension}',
            encoding='utf-8')
        return 'Check file is %s.%s' % (filename, extension)