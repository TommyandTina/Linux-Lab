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

    print 'Make sure you connected a hard disk with USB-SCSI cable'
    sys.stdout.flush()
    sleep(1)
    a.buff=""
    a.send('dmesg | grep scsi')  
    if (a.buff.find('usb-storage')==-1):
        print_result.func_fail(a)
    
    a.buff=""    
    a.send('dmesg | grep SCSI') 
    if (a.buff.find('Attached SCSI')==-1 and a.buff.find('disk')==-1):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)

