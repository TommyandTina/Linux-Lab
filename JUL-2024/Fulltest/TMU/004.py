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

TIME_AFTER=1
TIME_BEFORE=0

INTR_BEFORE=0
INTR_AFTER=0

DELAY=300

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    if (tmu.check_cs(a,TMU) == False):
        print_result.func_fail(a)

    a.buff=""          
    a.send('grep {} /proc/interrupts'.format(TMU))
    
    INTR_BEFORE=(a.buff.splitlines()[2]).split()[1]
  
    a.send('date -s 11:11') 
    a.buff=""
    a.send('date; sleep {}; date'.format(DELAY))
   
    TIME_BEFORE=a.buff.splitlines()[2].split()[3].split(':')
    TIME_BEFORE = int(TIME_BEFORE[0])*3600 + int(TIME_BEFORE[1])*60 + int(TIME_BEFORE[2])
   
    TIME_AFTER=a.buff.splitlines()[3].split()[3].split(':')
    TIME_AFTER = int(TIME_AFTER[0])*3600 + int(TIME_AFTER[1])*60 + int(TIME_AFTER[2])

    #if (TIME_AFTER == TIME_BEFORE + DELAY):
    #    print_result.func_pass(a)
    #else:
    #    print_result.func_fail(a) 

    a.buff=""
    a.send('grep {} /proc/interrupts'.format(TMU))
    
    INTR_AFTER=(a.buff.splitlines()[2]).split()[1]
    
    if (int(INTR_BEFORE) < int(INTR_AFTER)):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)


