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
STRESS_TIME = 3600

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (sound.sound_setting(a) == False):
        print_result.func_fail(a)

    a.send('stress --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(config.NUM_CPU,config.NUM_CPU*2,config.NUM_CPU,STRESS_TIME),0,False)
    
    a.buff=""
    a.send('arecord -t wav -d 1800 -c 2 -r 44100 -f S24_LE {}'.format(RECORD_FILE),0,True,2000)

    if (a.buff.find('arecord:')!=-1):
        print_result.func_fail(a)

    a.send('aplay {}'.format(RECORD_FILE),0,True,2000)
   
    if (a.buff.find('aplay:')!=-1):
        print_result.func_fail(a) 
   
    a.wait('successful run completed',300)

    if (sound.manual_judgement() == False):
        print_result.func_fail(a)

    print_result.func_pass(a)

