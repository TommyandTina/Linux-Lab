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
import subprocess


INTR_BEFORE=0
INTR_AFTER=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()

    if (config.SOC == 'E3'):
        ND = 'e66d0000.i2c'    
    else:
        ND = 'e6510000.i2c'

    a.buff=""      
    a.send('arecord -d 10 test.wav')

    if (a.buff.find('arecord:')!=-1):
        print_result.func_fail(a)
        
    a.buff=""
    a.send('cat /proc/interrupts | grep {}'.format(ND))

    INTR_BEFORE=int(a.find_str(ND,'grep {}'.format(ND)).split()[1])

                  
    a.buff=""
    a.send('aplay test.wav')
 
    if (a.buff.find('aplay:')!=-1):
        print_result.func_fail(a)
   
    a.buff=""
    a.send('cat /proc/interrupts | grep {}'.format(ND))

    INTR_AFTER=int(a.find_str(ND,'grep {}'.format(ND)).split()[1])

    if (INTR_AFTER > INTR_BEFORE):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)
