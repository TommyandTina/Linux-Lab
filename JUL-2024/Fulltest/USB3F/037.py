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

MODPROBE_CMD='modprobe usb_f_ss_lb bulk_maxpacket=512; modprobe g_zero'
TESTUSB_OPTION='-t 2'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
         
    if ( usb3f.g_zero(a,MODPROBE_CMD,TESTUSB_OPTION) == False):
        print_result.func_fail(a)
    
    print_result.func_pass(a) 
 
