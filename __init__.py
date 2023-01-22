from .info import *
from.CONSTANTS import *
# ---------------------- #

from sys import platform

__all__ = ['platform']


if platform == 'linux':
    from .linux_terminal import *

else:

    from .mac_terminal import *

# -------------------------- #

