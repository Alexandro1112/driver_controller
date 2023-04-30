import subprocess

class Notifier(object):
    def __init__(self):
        self.STOP_ICON = 0x10
        self.WARNING_ICON = 0x30
        self.QUESTION_ICON = 0x20
        self.center_message = 'powershell (New-Object -ComObject Wscript.Shell).Popup("""%s""",0,"""%s""",%s)'

    def send_text_message(self, text, label, icon):

        if icon == 'stop':
            subprocess.getoutput(cmd=self.center_message % (text, label, self.STOP_ICON))
        elif icon == 'warning':
            subprocess.getoutput(cmd=self.center_message % (text, label, self.WARNING_ICON))
        elif icon == 'question':
            subprocess.getoutput(cmd=self.center_message % (text, label, self.QUESTION_ICON))

        else:
            raise ValueError(' ')