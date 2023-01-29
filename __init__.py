from .info import *
from.CONSTANTS import *

# ---------------------- #
# Initialize scripts 

from sys import platform

__all__ = ['platform']


if platform == 'linux':

    from ._linux_engine import *

elif platform == 'darwin':

    from ._mac_engine import *

else:

    raise OSError('While, platform support only on ma/Linux os')


    


# -------------------------- #

