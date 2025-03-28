import AppKit
import Quartz
import Foundation
from .exceptions import *

class BackGroundScreen:

    def current_background_image(self):
        import AppKit

        Id = Quartz.NSScreen.mainScreen()
        boolean = AppKit.NSWorkspace.sharedWorkspace().desktopImageURLForScreen_(Id)
        return boolean

    def set_backgroud(self, filename: str, stretch_img_by_screen_size: bool, image_bg_color='white'):
        try:
            file_url = Foundation.NSURL.fileURLthPath_(filename)
                config = {
                    AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                    AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                 not True else AppKit.YES,
                    AppKit.NSWorkspaceDesktopImageFillColorKey: eval(f"AppKit.NSColor.{image_bg_color}Color()")
                }

            ws = AppKit.NSWorkspace.sharedWorkspace()
            for screens in AppKit.NSScreen.screens():
                ws.setDesktopImageURL_forScreen_options_error_(
                    file_url, screens, config, None)
        except Exception:
            raise UnsupportedFormat(f'Image not support format {repr(str(filename).split(".")[-1])}.')
