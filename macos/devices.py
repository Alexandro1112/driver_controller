import subprocess
from xml.etree.ElementTree import ElementTree
from sounddevice import query_devices
import objc
import CoreWLAN


class OutputListsDevises(object):
    """ Return output devises """

    def __init__(self):
        self.bl, _ = subprocess.Popen(
            "system_profiler -xml SPBluetoothDataType",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=False
        ).communicate()

        last_text = None
        cameras = []

        for node in ElementTree.fromstring(self.bl).iterfind("./array/dict/array/dict/*"):
            if last_text == "_name":
                cameras.append(node.text)
            last_text = node.text
        self.devises = query_devices()

    def get_list_wifi_networks(self):
        """ Function output all wi-fi networks,
        which available for your devise."""
        if 'loadBundle' in dir(objc):
            pass
        else:
            raise AttributeError

        wifi = []
        wifi2 = []

        bundle_path = '/System/Library/Frameworks/CoreWLAN.framework'

        dir(objc._objc.loadBundle(objc.infoForFramework(bundle_path)[1], bundle_path=bundle_path,
                                  module_globals=globals()))

        response = CoreWLAN.CWInterface.interface()
        r = response.scanForNetworksWithName_includeHidden_error_(None, True, None)

        for i in range(1, len(str(r).split('>')), 2):
            wifi.append(str(r).split('>')[i].split(',')[0] + ']')

        for items in wifi:
            wifi2.append(items.strip().replace('ssid', '').replace('[', '').replace(']', '').replace('=',
                                                                                                     '').strip())

        yield set(sorted(wifi2))

    def get_list_bluetooth_device(self):
        """ Function output all bluetooth devise(s),
      which available for your devise."""

        return self.bl

    def get_list_cameras(self):

        self.resp, _ = subprocess.Popen(
            "system_profiler -xml SPCameraDataType",
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=False
        ).communicate()

        last_text = None
        cameras = []

        for node in ElementTree.fromstring(self.resp).iterfind("./array/dict/array/dict/*"):
            if last_text == "_name":
                cameras.append(node.text)
            last_text = node.text

        return cameras

    def get_list_audio_devises(self):
        """
     Return all audio
     connectable devises.
     :return: devises
     (Available only on Mac-os)
     """

        return self.devises
