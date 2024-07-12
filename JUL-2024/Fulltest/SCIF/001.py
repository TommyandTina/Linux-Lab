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

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    a.send('dmesg | grep SCI')

    if (a.buff.find('SuperH (H)SCI(F) driver initialized')==-1):
        print_result.func_fail(a)
    
    a.buff=""
    a.send('dmesg | grep serial')

    if (a.buff.find('ttySC1')==-1) or (a.buff.find('ttySC0')==-1):
        print_result.func_fail(a)

    print_result.func_pass(a)
 
