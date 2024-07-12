#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import conserial
import print_result
import sound

RECORD_FILE = '/tmp/audio.wav'

RECORD_OPTION = '-D plughw:0,0 -f s16_le -t wav -c 2 -r 44100 -d 360'
PLAYBACK_OPTION = '-D plughw:0,0 -f s16_le -t wav -c 2 -r 44100'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (sound.sound_setting(a) == False):
        print_result.func_fail(a)

    if (sound.record(a,RECORD_OPTION,RECORD_FILE) == False):
        print_result.func_fail(a)

    if (sound.playback(a,PLAYBACK_OPTION,RECORD_FILE)==False):
        print_result.func_fail(a)

    if (sound.manual_judgement() == False):
        print_result.func_fail(a)

    print_result.func_pass(a)

