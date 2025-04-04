import time
import AVFoundation


class AudioRecorder:
    def record(self, url, duration):
        url = AVFoundation.NSURL.fileURLWithPath_(url)
        query = {
            AVFoundation.AVSampleRateKey: 44100.0,
            AVFoundation.AVNumberOfChannelsKey: 2,
            AVFoundation.AVEncoderBitRateKey: 12800,
            AVFoundation.AVLinearPCMBitDepthKey: 16,
            AVFoundation.AVEncoderAudioQualityKey: AVFoundation.AVAudioQualityHigh,
        }
        audio, err = AVFoundation.AVAudioRecorder.alloc().initWithURL_settings_error_(url, query, None)
        if audio is None:
            raise FileNotFoundError
        audio.record()
        time.sleep(duration)
        audio.stop()
        audio.release()
  
