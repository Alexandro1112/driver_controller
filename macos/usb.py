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
            globals()['IOServiceMatching'](b'IOUSBDevice')
        )

        err, self.props = globals()['IORegistryEntryCreateCFProperties'](
            usb_devs,
            None,
            CoreFoundation.kCFAllocatorDefault,
            0
        )
        if self.props:
            for keys, values in self.props.items():
                setattr(self, keys, values)  # add attributes

    def query(self):
        return self.props

    def __getattr__(self, item):
        if self.props:
            pass
        raise NotImplementedError

    def get(self, name):
        if len(name.split()) >= 2:
            return getattr(self, name).strip()
