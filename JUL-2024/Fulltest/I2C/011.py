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

device_add1='007c'
device_add2='007f'

expected='max9611'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (config.SOC == 'E3'):
        CH = 0
    else:
        CH = 4
          
    a.send('cat /sys/bus/i2c/devices/{}-{}/name'.format(CH,device_add1)) 
    if (a.buff.find(expected)!=-1):
        a.buff=""
        a.send('cat /sys/bus/i2c/devices/{}-{}/name'.format(CH,device_add2))
        if (a.buff.find(expected)!=-1):
            print_result.func_pass(a)
        else:
            print_result.func_fail(a)
    else:
        print_result.func_fail(a)

