import subprocess
from AVFoundation import *

import objc
import CoreWLAN


class OutputListsDevises(object):
    """ Return output devises """

    def get_list_wifi_networks(self):
        """ Function output all wi-fi networks,
        which available for your devise."""
        if 'loadBundle' in dir(objc):
            pass
        else:
            raise AttributeError
        bundle_path = '/System/Library/Frameworks/CoreWLAN.framework'
        objc._objc.loadBundle(objc.infoForFramework(bundle_path)[1], bundle_path=bundle_path,
                                  module_globals=globals())

        response = CoreWLAN.CWInterface.interface()
        r = response.scanForNetworksWithName_includeHidden_error_(None, True, None)
        for networks in r[0]:
            yield networks.ssid()

    def get_list_bluetooth_device(self):
        """ Function output all bluetooth devise(s),
      which available for your devise."""

        return None  # Not manage yet.

    def get_list_cameras(self):
        devices = AVCaptureDevice.devicesWithMediaType_('Video')
        list_devices = []
        for device in devices:
            list_devices.append(device.localizedName())
            yield list_devices[-1]

    def get_list_audio_devises(self):
        """
     Return all audio
     connectable devises.
     :return: devises

     """

        devices = AVCaptureDevice.devicesWithMediaType_('Audio')
        list_devices = []
        for device in devices:
            list_devices.append(device.localizedName())
            yield list_devices[-1]


