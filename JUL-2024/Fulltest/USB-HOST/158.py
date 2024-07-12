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

CHANNEL2 = 'usb3'
SIZE = '1024'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
          
    if (usb.cp_between_usb_hdd_usb3(a,'usb2ch1',CHANNEL2,SIZE)==False):
        if (usb.cp_between_usb_hdd_usb3(a,'usb2ch2',CHANNEL2,SIZE)==False):
            print('No USB HDD or USB3 found!')
            print_result.func_fail(a)
    print_result.func_pass(a)

    

