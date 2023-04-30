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
            if image_bg_color == 'green':
                file_url = Foundation.NSURL.fileURLthPath_(filename)
                config = {
                    AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                    AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                 not True else AppKit.YES,
                    AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.greenColor()
                }
            elif image_bg_color == 'red':
                file_url = Foundation.NSURL.fileURLthPath_(filename)
                config = {
                    AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                    AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size
                                                                                 is not True else AppKit.YES,
                    AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.redColor()
                }
            elif image_bg_color == 'blue':
                file_url = Foundation.NSURL.fileURLthPath_(filename)
                config = {
                    AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                    AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                 not True else AppKit.YES,
                    AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.blueColor()
                }
            elif image_bg_color == 'yellow':
                file_url = Foundation.NSURL.fileURLWithPath_(filename)
                config = {
                    AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                    AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                 not True else AppKit.YES,
                    AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.yellowColor()
                }
            elif image_bg_color == 'white':
                file_url = Foundation.NSURL.fileURLWithPath_(filename)
                config = {
                    AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                    AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                 not True else AppKit.YES,
                    AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.whiteColor()
                }
            elif image_bg_color == 'black':
                file_url = Foundation.NSURL.fileURLWithPath_(filename)
                config = {
                    AppKit.NSWorkspaceDesktopImageScalingKey: AppKit.NSImageScaleProportionallyUpOrDown,
                    AppKit.NSWorkspaceDesktopImageAllowClippingKey: AppKit.NO if stretch_img_by_screen_size is
                                                                                 True else AppKit.YES,
                    AppKit.NSWorkspaceDesktopImageFillColorKey: AppKit.NSColor.blackColor()
                }
            elif image_bg_color != (i for i in ('black', 'white', 'yellow', 'blue', 'red', 'green')):
                raise RgbValueError(f'No color {image_bg_color} for background.')

            ws__ = AppKit.NSWorkspace.sharedWorkspace()
            for screens in AppKit.NSScreen.screens():
                ws__.setDesktopImageURL_forScreen_options_error_(
                    file_url, screens, config, None)
        except Exception:
            raise UnsupportedFormat(f'Image not support format {repr(str(filename).split(".")[-1])}.')