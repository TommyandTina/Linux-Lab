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

CHANNEL = 'usb3'
SIZE = '100'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    if (usb.cp_between_usb_hub2_usb3(a,'usb2ch1',CHANNEL,SIZE)==False):
        print('No USB Hub found on {}'.format('usb2ch1'))
        if (usb.cp_between_usb_hub2_usb3(a,'usb2ch2',CHANNEL,SIZE)==False):
            print('No USB Hub found on {}'.format('usb2ch2'))
            print_result.func_fail(a)
        else:
            print_result.func_pass(a)
    else:
        print_result.func_pass(a)
    