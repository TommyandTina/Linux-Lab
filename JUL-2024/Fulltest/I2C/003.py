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
          
    a.send('ls /sys/bus/platform/drivers | grep i2c',0.05)
    
    if (a.buff.find('i2c-rcar')!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
