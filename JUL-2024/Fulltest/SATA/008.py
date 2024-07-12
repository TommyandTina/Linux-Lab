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
import sata
import re

CHANNEL='usb2ch1'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,sata.MODULE_TEST)
    a.start()
    a.buff=""

    MOUNT_POINT = sata.mountpoint(a)

    if (MOUNT_POINT == None):
        print_result.func_fail(a)

    DEVICE = re.findall(r'[A-Za-z]+|\d+', MOUNT_POINT)[0]
    
    a.send('(echo d; echo 1; echo d; echo 2; echo d; echo 3; echo d; echo n; echo p; echo 1; echo 2048; echo "+5G"; echo t; echo 83; echo w) | fdisk /dev/{}'.format(DEVICE))
    
    a.buff=""
    a.send('echo y | mkfs.ext3 -L "HD" /dev/{}1'.format(DEVICE))

    if (re.search('Writing superblocks and filesystem accounting information:+\s+\S+\S+\s+\S+\S+done',a.buff)==None):
        print_result.func_fail(a)     

    a.buff=""
    a.send('(echo n; echo p; echo 2; echo 10487808; echo "+5G"; echo t; echo 2; echo 83; echo w) | fdisk /dev/{}'.format(DEVICE))

    a.buff=""
    a.send('echo y | mkfs.ext3 -L "HD" /dev/{}2'.format(DEVICE))
    if (a.buff.find('exception Emask') != -1):
        print_result.func_fail(a)

    if (re.search('Writing superblocks and filesystem accounting information:+\s+\S+\S+\s+\S+\S+done',a.buff)==None):
        print_result.func_fail(a)

    a.send('fdisk -l /dev/{}'.format(DEVICE))

    print_result.func_pass(a)

 

       
