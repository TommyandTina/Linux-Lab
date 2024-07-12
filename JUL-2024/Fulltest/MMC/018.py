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
import mmc
import re



if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
          
    MOUNT_POINT=mmc.mountpoint(a)
    
    if (MOUNT_POINT == None): 
        print_result.func_fail(a)

    a.buff=""
    a.send('fdisk -l /dev/{}'.format(MOUNT_POINT))

    for line in a.buff.splitlines():
        if (re.search('Disk',line)):
           sectors = int(line.split()[6])
           break
    
    a.buff=""
    a.send('dd if=/dev/zero of=/dev/{} bs=1024 count=1 seek={}'.format(MOUNT_POINT,sectors+1))

    if (a.buff.find('cannot seek: Invalid argument')==-1):
        print_result.func_fail(a)

    print_result.func_pass(a)
     
   
