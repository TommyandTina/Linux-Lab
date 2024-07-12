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
    a.send('echo 0 > /sys/devices/system/cpu/cpu2/online')
    sleep(0.5)
    if (a.buff.find('psci: CPU2 killed')==-1):
        print_result.func_fail(a)

    a.buff=""
    a.send('cat /sys/devices/system/cpu/offline')
    sleep(0.5)
    if (a.buff.find('2')==-1):
        print_result.func_fail(a)

    a.buff=""
    a.send('echo 1 > /sys/devices/system/cpu/cpu2/online')
    sleep(0.5)
    if (a.buff.find('Detected PIPT I-cache on CPU2')==-1) and (a.buff.find('CPU2: Booted secondary processor')==-1):
        print_result.func_fail(a)

    a.buff=""
    a.send('cat /sys/devices/system/cpu/online')
    sleep(0.5)
    if (a.buff.find('0-{}'.format(config.NUM_CPU-1))==-1):
        print_result.func_fail(a)


    print_result.func_pass(a)    
