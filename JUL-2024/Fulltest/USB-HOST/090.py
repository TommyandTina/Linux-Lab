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

CHANNEL1 = 'RAM'
CHANNEL2 = 'usb2ch1'
CHANNEL3 = 'usb2ch2'
SIZE = 200

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    if (usb.cp_between_three_simultaneously(a,CHANNEL1,CHANNEL2,CHANNEL3,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)
    