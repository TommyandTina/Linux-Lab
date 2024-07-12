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


FAILED=1
PASSED=0

RESULT=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
  
    a.buff=""        
    a.send('echo 0 > /sys/devices/system/cpu/cpu1/online')
    sleep(0.5)
    if (a.buff.find('psci: CPU1 killed')==-1):
        print_result.func_fail(a)
  
    a.buff=""
    a.send('cat /proc/interrupts')
    sleep(2)
    if (a.buff.find('CPU1')!=-1):
        print_result.func_fail(a)
   
    a.buff=""
    a.send('cat /proc/cpuinfo | grep processor')
    sleep(0.5)
    if (a.buff.find('processor       : 1')!=-1):
        print_result.func_fail(a)

    a.send('echo 1 > /sys/devices/system/cpu/cpu1/online')
    sleep(0.5)

    print_result.func_pass(a)
