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


INTR_BEFORE=[0,0,0]
INTR_AFTER=[0,0,0]

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
   

    a.buff=""
    a.send('killall -9 yes')
    sleep(2)
    print ('\n Wait 2 minutes \n')
    sleep(120)

   
    a.buff=""    
    a.send('cat /proc/interrupts | grep thermal')
   
    INTR_BEFORE[0]=int(a.find_str('thermal:ch0').split()[1])
    INTR_BEFORE[1]=int(a.find_str('thermal:ch1').split()[1])
    
    for i in range(0,10):
        a.send('yes > /dev/null &')

    sleep(5)

    a.buff=""
    a.send('cat /proc/interrupts | grep thermal')

    INTR_AFTER[0]=int(a.find_str('thermal:ch0').split()[1])
    INTR_AFTER[1]=int(a.find_str('thermal:ch1').split()[1])

    for i in range(0,2):
        if (INTR_AFTER[i] <= INTR_BEFORE[i]):
            a.send('killall -9 yes')
            sleep(2)
            print_result.func_fail(a)


    a.send('killall -9 yes')

    print_result.func_pass(a)
