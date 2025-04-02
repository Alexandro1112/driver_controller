import subprocess
import Quartz

class Volume(object):
    def __init__(self):

        self.volume = 'osascript -e "set Volume %s"'
        self.max_volume = 'osascript -e "set Volume 10"'
        self.min_volume = 'osascript -e "set Volume 0"'

        self.muted = subprocess.getoutput(cmd='osascript -e \'get volume settings\'')
        self.input_volume = subprocess.getoutput(cmd='osascript -e \'get volume settings\'').split(' ')[
            3].replace(',', '')
        self.output_volume = subprocess.getoutput(cmd='osascript -e \'get volume settings\'').split(' ')[
            1].replace(',', '')
        self.alert_vol = subprocess.getoutput(cmd='osascript -e \'get volume settings\'').split(' ')[
            5].replace(
            ',', '')

    def set_volume(self, volume):
        """Set volume by value."""

        subprocess.getoutput(cmd=self.volume % volume)
        if subprocess.getstatusoutput(cmd=self.volume % volume)[0] == 1:
            raise ValueError
        else:
            return 0

    def set_max_volume(self):
        subprocess.getoutput(cmd=self.max_volume)
        return 0

    def set_min_volume(self):
        subprocess.getoutput(cmd=self.min_volume)
        return 0

    @property
    def get_output_volume_percent(self):
        """
        Return output volume percent
        :return:
        """

        return self.output_volume

    @property
    def get_input_volume_percent(self):
        """
        Return input volume percent
        :return:
        """
        return self.input_volume

    @property
    def get_alert_volume(self):
        return self.alert_vol

    def ismuted(self):
        return self.muted.split(', ')[-1].split(':')[-1].capitalize()

   
