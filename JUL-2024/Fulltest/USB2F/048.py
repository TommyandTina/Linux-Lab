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

STRESS_TIME = 3600

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,usb2f.MODULE_TEST)
    a.start()
    a.buff=""
         
    if ( usb2f.g_mass_storage_stress_test(a,STRESS_TIME) == False):
        print_result.func_fail(a)
    
    print_result.func_pass(a) 
 
