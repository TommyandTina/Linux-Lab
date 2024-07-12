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

RECORD_OPTION = "-D plughw:0,0 -f s24_le -c 2 -r 44100 -d 20"
RECORD_FILE = "/tmp/record.wav"

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if(sound.sound_setting(a)==False):
        print_result.func_fail(a)

    a.buff=""

    a.send("aplay -D plughw:0,0 -f s24_le -c 2 -r 44100 -t wav {} &".format(sound.AUDIO_FILE_44100),0,False)
 
    for i in range(0,10):
        if (sound.record(a,RECORD_OPTION,RECORD_FILE,'Ctrl+C')==False):
            print_result.func_fail(a)

    a.send('killall aplay')   
    sleep(0.5)
    a.send('',0,False)

    print_result.func_pass(a) 
