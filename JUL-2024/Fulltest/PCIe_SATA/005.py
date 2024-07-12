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
import sata

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
    a.send('hdparm -I /dev/sda | grep -i speed')
    if (a.buff.find('Gen3 signaling speed (6.0Gb/s)')!=-1):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)
    
 

       
