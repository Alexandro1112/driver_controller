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

    def __init__(self):
        self.sound1 = '/System/Library/Sounds/Pop.aiff',
        self.sound2 = '/System/Library/Sounds/Blow.aiff',
        self.sound3 = '/System/Library/Sounds/Glass.aiff',
        self.sound4 = '/System/Library/Sounds/Funk.aiff',
        self.sound5 = '/System/Library/Sounds/Submarine.aiff',
        self.sound6 = '/System/Library/Sounds/Sosumi.aiff'

    @staticmethod
    def pop_sound(iters: int):
        """
     Pop voice-notify.
     :param iters How mane
     iterations(repeats) of sound.
     (Available only on Mac-os)
     """

        subprocess.getoutput(
            cmd='for i in {1..%s}; do afplay /System/Library/Sounds/Pop.aiff -v 10; done' % iters)

    @staticmethod
    def blow_sound(iters: int):
        """Blow voice-notify.
     :param iters How mane
     iterations(repeats) of sound.
     (Available only on Mac-os)
     """
        subprocess.getoutput(
            cmd='for i in {1..%s}; do afplay /System/Library/Sounds/Blow.aiff -v 10; done' % iters)

    @staticmethod
    def glass_sound(iters: int):
        """
     Glass voice-notify.
     :param iters How mane
     iterations(repeats) of sound.
     (Available only on Mac-os)
     """
        subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                 '/System/Library/Sounds/Glass.aiff -v 10; done' % iters)

    @staticmethod
    def funk_sound(iters: int):
        """
     Funk voice-notify.
     :param iters How many
     iters(repeats) of sound.
     (Available only on Mac-os)
     """
        subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                 '/System/Library/Sounds/Funk.aiff -v 10; done' % iters)

    @staticmethod
    def submarine_sound(iters: int):
        """
     Submarine voice-notify.
     :param iters How many
     iterations(repeats) of sound.
     (Available only on Mac-os)
     """
        subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                 '/System/Library/Sounds/Submarine.aiff -v 10; done' % iters)

    @staticmethod
    def morse_sound(iters: int):
        """
     Submarine voice-notify.
     :param iters How many
     iterations(repeats) of sound.
     (Available only on Mac-os)
     """
        subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                 '/System/Library/Sounds/Morse.aiff -v 10; done' % iters)

    @staticmethod
    def ping_sound(iters: int):
        """
     Ping voice-notify.
     :param iters How mane
     iterations(repeats) of sound.
     (Available only on Mac-os)
     """
        subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                 '/System/Library/Sounds/Ping.aiff -v 10; done' % iters)

    @staticmethod
    def sosumi_sound(iters: int):
        """
     Sosumi voice-notify.
     :param iters How mane
     iterations(repeats) of sound.
     (Available only on Mac-os)
     """
        subprocess.getoutput(cmd='for i in {1..%s}; do afplay '
                                 '/System/Library/Sounds/Sosumi.aiff -v 10; done' % iters)

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