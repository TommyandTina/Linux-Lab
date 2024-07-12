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
import re

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    MOUNT_POINT=usb.mountpoint_usb_hdd(a,'usb2ch1')
    if (MOUNT_POINT == None):
        MOUNT_POINT=usb.mountpoint_usb_hdd(a,'usb2ch2')
    if (MOUNT_POINT == None):
        print_result.func_fail(a)

    a.buff=""
    a.send('echo y | mkfs.ext3 -L "USBHDD" /dev/{}'.format(MOUNT_POINT))

    if (re.search('Writing superblocks and filesystem accounting information:+\s+\S+\S+\s+\S+\S+done',a.buff)==None):
        print_result.func_fail(a)     

    print_result.func_pass(a)

    

