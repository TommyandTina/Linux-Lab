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
import usb

CHANNEL='usb3'
SIZE=100
WHILE_CP=False

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    if (usb.cp_s2ram(a,'RAM',CHANNEL,SIZE,WHILE_CP)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)
    
 

       