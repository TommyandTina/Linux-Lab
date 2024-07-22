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
import sdhi


CARD_SLOT = 'sd1'
SIZE = 350

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
   
    DEVICE = sdhi.mountpoint(a,CARD_SLOT)

    a.buff=""
    a.send('fdisk -l /dev/{}'.format(DEVICE))

    SECTORS = int(a.buff.splitlines()[2].split()[6])

    a.buff=""
    a.send('dd if=/dev/zero of=/dev/{} bs=512 count=1 seek={}'.format(DEVICE,SECTORS-1))

    if (a.buff.find('dd:') != -1):
        print_result.func_fail(a)

    print_result.func_pass(a)            
     