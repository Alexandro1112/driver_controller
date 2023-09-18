
# ---------------------- #
# Initialize scripts 

from sys import platform


if platform == 'linux':

    from ._linux_engine import LinuxCmd

elif platform == 'darwin':

    from ._mac_engine import MacCmd # The project frozen until unknown time from July 4 2023 - ???

elif platform == 'win32':

    from ._windows_engine import WindowsCmd

else:
    raise OSError()


if __name__ == '__main__':
    pass


# -------------------------- #

