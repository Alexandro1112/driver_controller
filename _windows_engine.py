import subprocess

class WindowsCmd(object):
    class Notifier(object):
        def __init__(self):
            self.center_message ='msg * "%s"'
        def send_text_message(self, text):
            subprocess.getoutput(cmd=self.center_message % text)


if __name__  == '__name__':
    exit(0)
