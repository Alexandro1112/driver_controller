from .info import *
from.CONSTANTS import *
from .exceptions import *
# ---------------------- #
# Initialize scripts 

from sys import platform

__all__ = ['platform']


if platform == 'linux':

    from ._linux_engine import *

elif platform == 'darwin':

    from ._mac_engine import *

elif platform == 'win32':

    from ._windows_engine import *

else:
    raise OSError()


if __name__ == '__main__':
    pass


# -------------------------- #

