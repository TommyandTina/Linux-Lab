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


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (config.SOC == 'E3'):
        ND = ['e60b0000.i2c', 'e6500000.i2c', 'e66d0000.i2c']
    else:
        ND = ['e60b0000.i2c', 'e6510000.i2c', 'e66d8000.i2c']
   
    a.send('cat /proc/interrupts | grep i2c', 0.05)
    
    for i in ND:
        if (a.buff.find(i) == -1):
            print_result.func_fail(a)

    print_result.func_pass(a)
                  
   
