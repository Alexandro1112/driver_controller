from time import ctime
import os
import subprocess


class FileConfig(object):

    def get_date_create_file(self, path):
        """
        Return time, when file was used.
        :param path:
        :return:
        """
        return ctime(os.stat(path).st_birthtime)

    def get_file_size(self, path):

        """
        Return size of file.
        :param path: Path to file
        :return:
        """

        return subprocess.getoutput(f'du -sh {path}').split('\t')[0].strip()

    def extension(self, path):
        return str(path).split('.')[-1]

    def name(self, path):
        """:return Name by path"""
        return path.split('/', maxsplit=3)[-1].split('.')[0]

    def get_files_in_folder(self, path: str):
        """Return all files in folder"""
        if not os.path.exists(path=path):
            raise FileExistsError
        if path == subprocess.getoutput(cmd=f'ls {path}'):
            return None
        return subprocess.getoutput(cmd=f'ls {path}')

    def get_folder_size(self, path):
        """Return all files in folder"""
        if os.path.exists(path=path):

            return subprocess.getoutput(cmd=f'du -sh {path}').split()
        else:
            raise FileExistsError(f'No file name {path}')