import subprocess
import AppKit
import pathlib


class Notifier(object):
    """Send different alerts"""
    def send_text_alert(self, button, message, icon):
        alert = AppKit.NSAlert.alloc().init()
        if isinstance(button, tuple):
            for i in button:
                alert.setMessageText_(i)
                alert.addButtonWithTitle_(i)
        else:
            alert.addButtonWithTitle_(str(button))
        alert.setInformativeText_(message)

        alert.setShowsHelp_(1)
        alert.setAlertStyle_(1)

        alert.startSpeaking_(0)
        alert.showsSuppressionButton()
        img = AppKit.NSImage.alloc().initWithContentsOfFile_(icon)

        alert.setIcon_(img)

        return alert.runModal() - 1000

    def send_warning_alert(self, labeltext, button1: [int, float, str], button2: [int, float, str]):
        if (type(button1) == int or float or str) and (type(button2) == int or float or str):

            cmd = 'osascript -e \'tell application (path to frontmost ' \
                  f'application as text) to display dialog "{labeltext}" ' \
                  f'buttons {repr(button1), repr(button2)} with icon stop\''
            return subprocess.getoutput(cmd=cmd).split(':')[-1]
        else:
            raise TypeError

    def send_lateral_message(self, label, activate: [None, str], subtitle, text, file_icon: str,
                             sound: [None], content_img=None):
        """
        >>> import driver_controller
        >>> driver_controller.MacCmd().Notifier().send_lateral_message(
        >>> label='Label of message',
        >>> activate='Safari',
        >>> subtitle='Subtitle of message',
        >>> text='Text of message',
        >>> file_icon='icon_.png',
        >>> sound=driver_controller.CONSTANTS.SOUNDS_PING_SOUND,
        >>> content_img='icon_.png')
      Make Lateral message with:
      :param label: Main title on message
      :param content_img: Image which local in center
      :param subtitle: Subtitle of message
      :param text: Description of message
      :param file_icon: Icon in message (Path to image)
      (must local in project-folder) Point out [None]
      if you don't want used icon
      :param activate: application, which open when you click by notify.
      :return: Successful.
      """

        if len(str(file_icon).split()) > 1 or len(str(content_img).split()) > 1:
            fullpath = str(pathlib.Path(str(file_icon)).cwd()) + '/' + repr(str(file_icon))
            content = str(pathlib.Path(str(content_img)).cwd()) + '/' + repr(str(content_img))
            commands = f"terminal-notifier -title '%s' -subtitle '%s' -message '%s' -appIcon %s -contentIm" \
                       f"age '{content}' -activate 'com.apple.{activate if activate is not None else ''}'" % (
                           label, subtitle, text, fullpath)
            commands2 = f'afplay /System/Library/Sounds/{sound if sound is not None else ""}.aiff'


        else:
            fullpath = str(pathlib.Path(str(file_icon)).cwd()) + '/' + str(file_icon)
            content2 = str(pathlib.Path(str(file_icon)).cwd()) + '/' + str(file_icon)
            commands = f"terminal-notifier -title '%s' -subtitle '%s' -message '%s' -appIcon %s -contentIma" \
                       f"ge '{content2}' -activate 'com.apple.{activate}'" % (
                           label, subtitle, text, fullpath)
            commands2 = f'afplay /System/Library/Sounds/{sound if sound is not None else ""}.aiff'

        subprocess.getoutput(cmd=commands)
        subprocess.getstatusoutput(cmd=commands2)

    def send_entry_alert(self, title, button1, button2, entr_text=''):
        """
        :param title: Title of entry
        :param button1: button in alert
        :param entr_text: placeholder-text
        :param button2: button-2
        :return:
        """
        cmd = """
               a=$(osascript -e 'try
               tell app "SystemUIServer"
               set answer to text returned of (display dialog "" default answer "%s" with title "%s"
               buttons {"%s", "%s"})
               end
               end
               activate app (path to frontmost application as text)
               answer' | tr '\r' ' ')
               [[ -z "$a" ]] && exit
               """ % (entr_text, title, button1, button2)
        return subprocess.getoutput(cmd=cmd)