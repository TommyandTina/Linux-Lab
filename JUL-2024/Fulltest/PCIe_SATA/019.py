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
import s2ram
import print_result
import subprocess


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    if (s2ram.pm_suspend(a)==False):
       print_result.func_fail(a)


    if (s2ram.pm_wakeup(a)==False):
       print_result.func_fail(a)
    a.send('find /sys/devices/platform/soc/fe000000.pcie/ -name sd*')
    a.send('time dd if=/dev/zero  of=/dev/sda bs=64M count=10 skip=8 oflag=direct  > write_dd.tx')

    SPEED=a.find_str('MB/s').split(", ")[3].split()[0]

    print ("\n \n SPEED = {} MB/s".format(SPEED))

    if (int(SPEED) < 300):
        print_result.func_fail(a)

    print_result.func_pass(a)

  

    
                  
   
