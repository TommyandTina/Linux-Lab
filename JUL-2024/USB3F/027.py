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
import usb3f

STORAGE='SD'
CP_TO='HOST'
SIZE=1024

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
         
    if ( usb3f.g_mass_storage(a,STORAGE,CP_TO,SIZE) == False):
        print_result.func_fail(a)
    
    print_result.func_pass(a) 
 
