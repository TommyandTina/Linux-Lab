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
import subprocess



if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    MOUNT_POINT=mmc.mountpoint(a)

    a.send('mount /dev/{} /mnt'.format(MOUNT_POINT))
    sleep(0.5)
    if (a.buff.find('mounted filesystem')==-1):
        print_result.func_fail(a)

    a.buff=""
    a.send('umount /mnt/')

    if (a.buff.find('umount:')!=-1):
        print_result.func_fail(a)

    print_result.func_pass(a)
                  
   
