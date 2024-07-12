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

SIZE='100'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    if (usb.cp_usb_hdd_to_ram(a,'usb2ch1',SIZE)==False):
        if (usb.cp_usb_hdd_to_ram(a,'usb2ch2',SIZE)==False):
            print('No USB HDD found on both USB channels')
            print_result.func_fail(a)
    print_result.func_pass(a)
