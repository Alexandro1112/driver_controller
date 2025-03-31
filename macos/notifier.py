
import AppKit


class Notifier:
    """Send different alerts"""

    def send_text_alert(self, button, message, icon):
        """Method is deprecated.Use other Alert manager PyMasl API."""
        alert = AppKit.NSAlert.alloc().init()
        if isinstance(button, tuple):
            for i in button:
                alert.setMessageText_(i)
                alert.addButtonWithTitle_(i)
        else:
            alert.addButtonWithTitle_(str(button))
        alert.setInformativeText_(message)

        alert.setShowsHelp_(1)
        alert.setAlertStyle_(1)

        alert.startSpeaking_(0)
        alert.showsSuppressionButton()
        img = AppKit.NSImage.alloc().initWithContentsOfFile_(icon)

        alert.setIcon_(img)

        return alert.runModal() - 1000

    def send_notification(self, title, subtitle, informative_text, sound_name, image_path):
        # Create a notification object
        notification = AppKit.NSUserNotification.alloc().init()

        # Set notification properties
        notification.setTitle_(title)
        notification.setSubtitle_(subtitle)
        notification.setInformativeText_(informative_text)
        notification.setSoundName_(sound_name)

        # If you want to set an image, you can use an NSImage
        if image_path:

            image = AppKit.NSImage.alloc().initWithContentsOfFile_(image_path)
            notification.setContentImage_(image)
 
        center = AppKit.NSUserNotificationCenter.defaultUserNotificationCenter()
        center.deliverNotification_(notification)
