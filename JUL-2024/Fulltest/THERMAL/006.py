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


temp_before=[0,0,0]
temp_after=[0,0,0]

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
   

    a.buff=""
    a.send('killall -9 yes')
    sleep(2)
    print ('\n\nPlease wait 2 minutes \n')
    sys.stdout.flush()
    sleep(120)

    for i in range(0,3):
        a.buff=""    
        a.send('cat /sys/class/thermal/thermal_zone{}/temp'.format(i))
        
        try:
            temp_before[i] = int(a.buff.splitlines()[len(a.buff.splitlines())-2].split()[0])
        except ValueError:
            print_result.func_fail(a)

    
    for i in range(0,10):
        a.send('yes > /dev/null &')

    sleep(5)

    for i in range(0,3):
        a.buff=""
        a.send('cat /sys/class/thermal/thermal_zone{}/temp'.format(i))
 
        try:
            temp_after[i] = int(a.buff.splitlines()[len(a.buff.splitlines())-2].split()[0])
        except ValueError:
            print_result.func_fail(a)

    for i in range(0,3):
        if (temp_after[i]<temp_before[i]):
            print_result.func_fail(a)

    a.send('killall -9 yes')
    sleep(2)

    print_result.func_pass(a)
