import pathlib
import subprocess
import AppKit
import mutagen.mp3
from time import sleep
import Foundation
from .exceptions import *


class Sound(object):
    """
  class Voice add more available
  voices & effects(which beforehand
  installed in Mac-os by path /System/Library/Sounds/)
  (Available only on Mac-os). And play other sounds.
  """

    

    def playSoundByName(self, soundfile):
        absolute_path = str(pathlib.Path(soundfile).cwd()) + str('/') + soundfile
        url = Foundation.NSURL.URLWithString_(
            absolute_path
        )

        duration_Start = AppKit.NSSound.alloc().initWithContentsOfURL_byReference_(url, True)
        try:
            duration_Start.play()
            sleep(float(duration_Start.duration()))

        except AttributeError:
            raise PathError(f'No sound name {url}, or it not support')

    def sound_length(self, file):
        return mutagen.mp3.MP3(file).info.length
