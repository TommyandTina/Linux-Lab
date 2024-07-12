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

PLAYBACK_OPTION = "-D plughw:0,0 -t wav -d 60 -c 2 -r 44100 -f S24_LE"

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if(sound.sound_setting(a)==False):
        print_result.func_fail(a)

    a.buff=""

    if (sound.playback(a,PLAYBACK_OPTION,sound.AUDIO_FILE_44100,'Ctrl+Z',20) == False):
        print_result.func_fail(a)

    if (sound.manual_judgement() == False):
        print_result.func_fail(a)

    print_result.func_pass(a) 
