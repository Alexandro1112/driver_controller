import AppKit
import pyperclip

class Buffer:
    def copyText(self, text):
        init = AppKit.NSStringPboardType

        pb = AppKit.NSPasteboard.generalPasteboard()
        pb.declareTypes_owner_([init], None)

        newStrIng = AppKit.NSString.stringthString_(text)
        newData = newStrIng.nsstring().dataUsingEncoding_(AppKit.NSUTF8StringEncoding)
        pb.setData_forType_(newData, init)

    def paste(self):
        return pyperclip.paste()