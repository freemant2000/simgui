import imp
from simpleaudio import WaveObject
from time import sleep

wo=WaveObject.from_wave_file("/home/kent/test.wav")
wo.play()
sleep(4)