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
import usb2f

STORAGE='RAM'
CP_TO='WRITE_SPEED'
SIZE=300
SPEED=10

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,usb2f.MODULE_TEST)
    a.start()
    a.buff=""
         
    if ( usb2f.g_mass_storage(a,STORAGE,CP_TO,SIZE,False,False,SPEED) == False):
        print_result.func_fail(a)
    
    print_result.func_pass(a) 
 
