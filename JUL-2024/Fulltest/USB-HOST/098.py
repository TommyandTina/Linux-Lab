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

CHANNEL1 = 'usb2ch1'
CHANNEL2 = 'usb3'
STAGE = 1
SIZE = 50

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    if (usb.cp_folder_between_two_usb(a,CHANNEL1,CHANNEL2,STAGE,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)
    