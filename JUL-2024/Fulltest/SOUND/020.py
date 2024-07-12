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

WHILE_RECORDING=True

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if(sound.sound_setting(a)==False):
        print_result.func_fail(a)

    if (sound.unbind(a,WHILE_RECORDING)==False):
        print_result.func_fail(a)
 
    print_result.func_pass(a) 
