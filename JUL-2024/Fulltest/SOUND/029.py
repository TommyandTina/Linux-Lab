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

RECORD_OPTION = "-t wav -d 60 -c 2 -r 44100 -f S24_LE"
RECORD_FILE = "/tmp/record.wav"
PLAYBACK_OPTION = ""

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if(sound.sound_setting(a)==False):
        print_result.func_fail(a)


    for i in range(0,config.NUM_CPU):
        a.buff=""
        a.send('taskset -c {} arecord {} {} &'.format(i,RECORD_OPTION,RECORD_FILE))
        if (a.buff.find('arecord:')!=-1):
            print_result.func.fail(a)
        
        sleep(10)
        
        a.buff=""
        a.send('taskset -c {} aplay {}'.format(i,RECORD_FILE))
        if (a.buff.find('aplay:')!=-1):
            print_result.func_fail(a)
         

    if (sound.manual_judgement() == False):
        print_result.func_fail(a)

    print_result.func_pass(a) 
