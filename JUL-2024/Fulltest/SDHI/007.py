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


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    MOUNT_POINT=sdhi.mountpoint(a,'sd1')
     
    if (MOUNT_POINT == None): 
       print_result.func_fail(a)

    a.send('yes | mkfs.ext3 /dev/{}'.format(MOUNT_POINT))
    
    if (a.buff.find('does not exist and no size was specified')!=-1):
        print_result.func_fail(a)

    #a.wait('Proceed anyway? (y,N)','y',3)

    #a.buff=""
    #a.send('umount /mnt/')

    #if (a.buff.find('umount:')!=-1):
    #    print_result.func_fail(a)

    print_result.func_pass(a)
                  
   
