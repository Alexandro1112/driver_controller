import subprocess
import CoreWLAN
from .exceptions import *
import SystemConfiguration
import warnings


class Wifi(object):
    """Connect to wi-fi networks/ Data about wifi."""

    def __init__(self):
        import CoreWLAN
        self.interface = CoreWLAN.CWInterface.interfaceWithName_("en0")

        self.speed = subprocess.getoutput(cmd='airport -I | grep maxRate')
        self.last_speed = subprocess.getoutput(cmd='airport -I | grep lastTxRate')
        self.secT = subprocess.getoutput(cmd='airport -I | grep "link auth"')

    @staticmethod
    def connectTo(wifi_network, password):
        """
     Auto connect to wi-fi network.
     :param wifi_network: Wi-fi name, which you would to connect.
     :param password: Password of this Network.(use hide variable)
     :return: 'Successful...' if you successfully connect to wi-fi.
     """

        iface = CoreWLAN.CWInterface.interface()

        networks, error = iface.scanForNetworksWithName_error_(wifi_network, None)

        network = networks.anyObject()

        success_connect, error = iface.associateToNetwork_password_error_(network, password, None)
        if error:
            raise WifiNameConnectError(f'Can not connect to wifi network name "{wifi_network}"')

    def Disconnect(self):
        subprocess.getoutput(cmd='networksetup -setnetworkserviceenabled Wi-Fi off')

    def Connect(self):
        subprocess.getoutput(cmd='networksetup -setnetworkserviceenabled Wi-Fi on')

    def connectToMacAddress(self):
        """Connect to wi-fi which used your Mac.
        (Actually connect to Your Mac address, start host Apmode.)"""
        self.interface.startHostAPMode_(None)

    def NetworkNoise(self):
        """Noise of current connected wi-fi network."""
        return int(self.interface.noise())

    def Bssid(self):
        ps = subprocess.getoutput(cmd='airport -I | grep BSSID').strip(' ')
        return ps

    def InfoNetwork(self):
        """Ruturn a lot of data about current wifi network"""
        return str(self.interface.ipMonitor()).strip().split('>')[1]

    def TransmitRate(self):
        return self.interface.transmitRate()

    def ChannelGhz(self):
        """Ghz type channel.It is 2Ghz or 5Ghz."""
        if str(self.interface.wlanChannel()).split('>')[-1].split(',')[0].strip() == 'None':
            return None
        return str(self.interface.wlanChannel()).split('>')[-1].split(',')[0].strip()

    def RssiChannelValue(self):
        return self.interface.aggregateRSSI()

    def _get_speed_by_current_network(self):  # Deleted method.
        raise NotImplementedError(
            f'{repr(self._get_speed_by_current_network.__name__)} '
            f'Deleted method. Because it already not support.')

    def Get_maxSpeed(self):
        return subprocess.getoutput(cmd='airport -I | grep maxRate').strip()

    def get_last_speed_by_current_network(self):
        return self.last_speed.strip().split(':')[-1]

    def IsEnable(self):
        return not subprocess.getoutput(cmd='airport -I | grep SSID').split(':')[-1].strip() == ''

    def isUsedProxy(self):
        """
        :return: [False] if proxy/VPN not used, [True] is Using.
        """
        return self.interface.isProxy()

    def wifiChannel(self):
        """Return Wi-fi channel """
        return self.interface.channel()

    def UnplugWifi(self):
        """Unplug wi-fi"""
        self.interface.setPower_error_(None, None)

    def SecurityType(self):
        """Return security type of current wi-fi network"""
        return self.secT.split(':')[-1]

    def get_info(self, ssid):
        return \
        str(CoreWLAN.CWInterface.interfaceWithName_("en0").scanForNetworksWithName_error_(ssid, None)).split('[')[
            1].split(', ')[:4]

    def GetCounrtyCodeByCurrentWifi(self):
        return self.interface.countryCodeInternal()

   
