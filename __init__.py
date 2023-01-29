from .info import *
from.CONSTANTS import *

# ---------------------- #

from sys import platform

__all__ = ['platform']


if platform == 'linux':
    from ._linux_engine import *
else:

    from ._mac_engine import *

# -------------------------- #

