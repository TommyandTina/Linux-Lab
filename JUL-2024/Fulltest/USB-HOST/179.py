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
import cp_device
import usb

CHANNEL = 'usb2ch1'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
          
    MP = usb.mountpoint(a,CHANNEL)
  
    if (MP == None):
        print_result.func_fail(a)

    if (cp_device.mount_device(a,MP) == False):
        print_result.func_fail(a)

    print('\nPlease plug out USB:')
    sys.stdout.flush()

    if (a.wait('USB disconnect',30) == False):
        print_result.func_fail(a)

    print('\nPlease plug in USB:')
    sys.stdout.flush()

    if (a.wait('Attached SCSI removable disk',30) == False):
        print_result.func_fail(a)

    MP = usb.mountpoint(a,CHANNEL)

    if (MP == None):
        print_result.func_fail(a)

    if (cp_device.mount_device(a,MP) == False):
        print_result.func_fail(a)

    for i in range(0,2):
        if (cp_device.umount_device(a) == False):
            print_result.func_fail(a) 
     
    print_result.func_pass(a)

    

