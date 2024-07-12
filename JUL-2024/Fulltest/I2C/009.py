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
        CH = 0
    else:
        CH = 4
          
    a.send('cat /sys/bus/i2c/devices/{}-0020/name'.format(CH)) 
   
    if (a.buff.find('pca9654')!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
