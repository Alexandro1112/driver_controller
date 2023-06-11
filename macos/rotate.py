import objc
import Quartz


def load():
    """Load MonitorPanel framework API."""
    objc.loadBundle('MonitorPanel', bundle_path='/System/Library/PrivateFrameworks/MonitorPanel.framework.framework',
                    module_globals=globals())


class Rotation:
    def setRotate(self, angle):
        load()

        rotate_object = globals()['MPDisplay'].alloc().init()
        if angle % 90 != 0:
            raise ValueError('The angle must be 90, 180, 270, or 0 degrees, not {}.'.format(angle))
        if not rotate_object.canChangeOrientation():
            raise PermissionError(f'Can not manage main display, including {self.setRotate.__name__} possibility.')
        else:
            rotate_object.setOrientation_(angle)

    def get_rotate(self):
        load()
        return Quartz.CGDisplayRotation(Quartz.CGMainDisplayID())
