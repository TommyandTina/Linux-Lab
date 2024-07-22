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

CHANNEL='usb3'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
   
    DEVICE = usb.mountpoint(a,CHANNEL)
    if (DEVICE == None):
        print_result.func_fail(a)
        sys.exit()

    a.buff=""
    a.send('fdisk -l /dev/{}'.format(DEVICE))

    SECTORS = int(a.find_str('Disk /dev/').split()[6])
 
    a.buff=""
    a.send("dd if=/dev/zero of=/dev/{} bs=512 count=1 seek={}".format(DEVICE, SECTORS-1))

    if (a.buff.find('copied') == -1):
        print_result.func_fail(a)

    print_result.func_pass(a)    