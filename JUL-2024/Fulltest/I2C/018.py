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
    
    if (config.SOC == 'E3'):
        CH = 3
    else:
        CH = 2
         
    a.buff=""
    a.send('i2cget -f -y {} 0x10 0x70'.format(CH))
    
    if (a.buff.find('0x00')!=-1):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)
