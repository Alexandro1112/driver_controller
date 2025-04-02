
from AVFoundation import *
from Cocoa import NSURL
from time import sleep
import time

__all__ = ('WebCameraCapture', )

class WebCameraCapture(object):
    """Collect data in camera"""
    def webcam_capture(self,  filename, camera_index):
        """
        Record video in webcam
        :param record_time: Recording time(seconds)
        :param filename: Name of created file

        :return: [None]
        """

        

        session = AVCaptureSession.alloc().init()

        device = AVCaptureDevice.devicesWithMediaType_(AVMediaTypeVideo)[camera_index]

        input, err = AVCaptureDeviceInput.deviceInputWithDevice_error_(device, None)
        session.addInput_(input)
        output_url = NSURL.fileURLWithPath_(filename)

        video_settings = {
            AVVideoWidthKey: 640,
            AVVideoHeightKey: 180,
            AVVideoCompressionPropertiesKey: {
                AVVideoAverageBitRateKey: 10 ** 10,
                AVVideoProfileLevelKey: AVVideoProfileLevelH264HighAutoLevel,
                AVVideoAllowFrameReorderingKey: kCFBooleanFalse
            },
            AVVideoColorPropertiesKey: {
                AVVideoColorPrimariesKey: AVVideoColorPrimaries_ITU_R_709_2,
                AVVideoTransferFunctionKey: AVVideoTransferFunction_ITU_R_709_2,
                AVVideoFieldMode: kCFBooleanTrue

            }
        }

        output = AVCaptureMovieFileOutput.alloc().init()
        session.addOutput_(output)
        session.startRunning()

        output.startRecordingToOutputFileURL_recordingDelegate_(output_url, CFDictionaryRef(video_settings))


        output.stopRecording()
        session.stopRunning()
        return session

    def webcamera_video_capture(self, filename, record_time, camera_index):
        session = AVCaptureSession.alloc().init()
        session.setSessionPreset_(AVCaptureSessionPresetHigh)

        devices = AVCaptureDevice.devicesWithMediaType_(AVMediaTypeVideo)
        device = devices[camera_index] if devices else None

        input = AVCaptureDeviceInput.deviceInputWithDevice_error_(device, None)[0]
        output = AVCaptureMovieFileOutput.alloc().init()

        if session.canAddInput_(input):
            session.addInput_(input)
        if session.canAddOutput_(output):
            session.addOutput_(output)

        session.startRunning()

        file_url = NSURL.fileURLWithPath_(NSString.stringWithString_(filename))
        output.startRecordingToOutputFileURL_recordingDelegate_(file_url, True)

        sleep(record_time)

        output.stopRecording()
        session.stopRunning()

    @property
    def list_devises(self):
        """
        Return all available devises for recording audio/video.
        :return: Devises
        """

        params = [AVCaptureDeviceTypeBuiltInWideAngleCamera,
                  AVCaptureDeviceTypeExternalUnknown]
        dtype = (
            AVFoundation.AVCaptureDevicePositionFront & AVFoundation.AVCaptureDevicePositionBack
        )

        camerasData = AVFoundation.AVCaptureDeviceDiscoverySession.discoverySessionWithDeviceTypes_mediaType_position_(
            params,
            AVFoundation.AVMediaTypeVideo,
            dtype
        )
        return camerasData.devices()
    
