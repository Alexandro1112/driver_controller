from .info import *

# ---------------------- #

from sys import platform

if platform == 'linux':
    from .linux_terminal import *

else:

    from .mac_terminal import *

# -------------------------- #

