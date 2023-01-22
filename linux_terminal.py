import subprocess
import sys

# ---------------------------------------------------------------------------------------------------------------------|
# INSTALL   || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" OR
# REINSTALL || /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# RUN || brew install brightness || brew doctor || brew install blueutil

__all__ = [
     'Switcher', 'Brightness',  'ValueBrightnessError'
]


class ValueBrightnessError(TypeError):
    """
     Value is not type [int].
    """


if sys.platform == 'linux':
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


else:
    raise NotImplementedError