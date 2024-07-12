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

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
   
    DEVICE = usb.mountpoint(a,'usb2ch1')
    if (DEVICE == None):
        DEVICE = usb.mountpoint(a,'usb2ch2')
        if (DEVICE == None):
            print ("\n \n Device not found")
            print_result.func_fail(a)
            sys.exit()

    a.buff=""
    a.send('fdisk -l /dev/{}'.format(DEVICE))

    SECTORS = int(a.find_str('Disk /dev/').split()[6])

    a.buff=""
    a.send("dd if=/dev/zero of=/dev/{} bs=1024 count=1".format(DEVICE))

    if (a.buff.find('copied') == -1):
        print_result.func_fail(a)

    print_result.func_pass(a)    
