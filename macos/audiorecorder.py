import time
import AVFoundation
import Foundation


class AudioRecorder(object):
    """Audio recorder"""

    def __init__(self):
        """
     Make variable AVAILABLE_EXTENSIONS is global.
     """
        self.AVAILABLE_EXTENSIONS = (i for i in ('wav', 'mp3'))

    def recorder(self, microphone_index, extension, filename: str, record_time: int):
        """
     :param microphone_index: Microphone index
     :param extension: Extension of creates file
     :param filename: Name
     :param record_time: Record time (format minutes)
     :return:
     """

        length = record_time
        AVFoundation.AVAudioFormat.alloc().initStandardFormatWithSampleRate_channels_(
            44100.0, 1)  # 44100.0 NOT CHANGEABLE!!!!!!!!
        audio_config = {
            AVFoundation.AVEncoderAudioQualityKey: AVFoundation.AVAudioQualityLow,
            AVFoundation.AVEncoderBitRateKey: 320000,  # TODO: add config as arg
            AVFoundation.AVNumberOfChannelsKey: int(microphone_index),
            AVFoundation.AVSampleRateKey: 44100.0
        }

        audio_recorder = AVFoundation.AVAudioRecorder.alloc().initWithURL_settings_error_(
            Foundation.NSURL.fileURLWithPath_(f'{filename}.{extension}'), audio_config, None)
        # Set default argument for none-valid specify.

        audio_recorder[0].record()

        time.sleep(length)
        # Stop recording after pause ``length``
        audio_recorder[0].stop()

        audio_recorder[0].release()