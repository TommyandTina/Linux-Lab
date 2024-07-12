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

CHANNEL='usb2ch1'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    MOUNT_POINT=usb.mountpoint(a,CHANNEL)

    if (MOUNT_POINT == None):
        print_result.func_fail(a)

    a.buff=""
    a.send('echo y | mkfs.ext3 -L "USB2-1" /dev/{}'.format(MOUNT_POINT))

    if (re.search('Writing superblocks and filesystem accounting information:+\s+\S+\S+\s+\S+\S+done',a.buff)==None):
        print_result.func_fail(a)     

    print_result.func_pass(a)

 

       
