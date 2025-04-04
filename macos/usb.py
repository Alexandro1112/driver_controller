import objc
from Foundation import NSBundle
import CoreFoundation


class USB:
    def __init__(self):
        iokit = NSBundle.bundleWithIdentifier_('com.apple.framework.IOKit')
        functions = [
            ("IOServiceGetMatchingService", b'II@'),
            ("IOServiceMatching", b'@*'),
            ('IORegistryEntryCreateCFProperties', b'IIo^@@I'),
            ]

        variables = [
            ('kIOMasterPortDefault', b'I')
        ]

        objc.loadBundleFunctions(iokit, globals(), functions)
        objc.loadBundleVariables(iokit, globals(), variables)

        usb_devs = globals()['IOServiceGetMatchingService'](
            globals()['kIOMasterPortDefault'],
            globals()['IOServiceMatching'](b'IOUSBHostDevice')
        )
        
        if usb_devs is None:
            self.props = []

        err, self.props = globals()['IORegistryEntryCreateCFProperties'](
            usb_devs,
            None,
            CoreFoundation.kCFAllocatorDefault,
            0
        )

    def query_devices(self):
        return self.props or []

    def nameOrAddr(self):
        if self.props:
            return self.props['USB Product Name']

    def identifier(self):
        if self.props:
            return self.props['IOServiceDEXTEntitlements']

    def vendorTitle(self):
        if self.props:
            return self.props['kUSBVendorString']

    def powerData(self):
        if self.props:
            return self.props['IOPowerManagement']
