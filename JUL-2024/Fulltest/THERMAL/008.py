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
import s2ram


temp_before=[0,0,0]
temp_after=[0,0,0]

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
   
    if (s2ram.pm_suspend(a)==False):
        print_result.func_fail(a)

    if (s2ram.pm_wakeup(a)==False):
        print_result.func_pass(a)
  
    for i in range(0,3):
        a.buff=""
        a.send('cat /sys/class/thermal/thermal_zone{}/temp'.format(i))

        try:
            temp_before[i] = int(a.buff.splitlines()[len(a.buff.splitlines())-2].split()[0])
        except ValueError:
            print_result.func_fail(a)

    print_result.func_pass(a)