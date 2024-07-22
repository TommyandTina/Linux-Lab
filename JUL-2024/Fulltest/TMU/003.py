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
import tmu

TMU = tmu.tmu0

INTR_BEFORE=0
INTR_AFTER=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    if (tmu.check_cs(a,TMU) == False):
        print_result.func_fail(a)

    a.buff=""          
    a.send('grep {} /proc/interrupts'.format(TMU))
    
    INTR_BEFORE=a.find_str('{}'.format(TMU),'grep {}'.format(TMU)).split()[1]
   
    a.buff=""
    a.send('date; sleep 5; date')
    
    a.buff=""
    a.send('grep {} /proc/interrupts'.format(TMU))
    
    INTR_AFTER=a.find_str('{}'.format(TMU),'grep {}'.format(TMU)).split()[1]

    if (int(INTR_BEFORE) < int(INTR_AFTER)):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)

