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


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,sata.MODULE_TEST)
    a.start()
    a.buff=""
   
    DEVICE = sata.mountpoint(a)
    if (DEVICE == None):
        print_result.func_fail(a)

    a.buff=""
    a.send('fdisk -l /dev/{}'.format(DEVICE))

    SECTORS = int(a.find_str('Disk').split()[6])

    a.buff=""
    a.send('dd if=/dev/zero of=/dev/{} bs=512 count=1 seek={}'.format(DEVICE,SECTORS-1))

    if (a.buff.find('cannot seek: Invalid argument') != -1) \
      or (a.buff.find('No space left on device') != -1):
        print_result.func_fail(a)

    print_result.func_pass(a)            
     
