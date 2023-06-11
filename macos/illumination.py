import objc


def load():
    objc.loadBundle('CoreBrightness', bundle_path='/System/Library/PrivateFrameworks/CoreBrightness.framework',
                    module_globals=globals())


class Illumination:
    """Illumination object.
    Connect keyboard and CoreBrightness API.
    """
    def setBrightness(self, level: float):
        """set brightness on keyboard."""
        load()
        brightness = globals()['KeyboardBrightnessClient'].alloc().init().setBrightness_forKeyboard_(level, True)
        if not bool(brightness):
            raise ValueError('Can not set level of illumination with value equal {}'.format(level))
        else:
            return 0

    def getBrightness(self):
        load()
        return round(globals()['KeyboardBrightnessClient'].alloc().init().brightnessForKeyboard_(True))
