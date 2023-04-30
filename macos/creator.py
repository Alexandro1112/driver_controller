import subprocess

class Creator(object):
    """Create something."""

    def create_file(self, name, extension):
        """
        Create file with setting & extension.
        :param name: Name of created file
        :param extension: Extension of created file
        :return: Successful.
        """
        if name != '':
            subprocess.getoutput(cmd=str('touch ') + str(name) + str('.') + str(extension))
        else:
            raise NameError from None

    def create_folder(self, name):
        """
     Create folder.
     :param name: Name of folder
     :return: Successful
     """
        if name == '':
            raise NameError('Assign this folder a name!') from None
        else:
            subprocess.getoutput(cmd=f'mkdir {name}')