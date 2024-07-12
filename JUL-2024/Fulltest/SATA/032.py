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
import sata

size=50

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,sata.MODULE_TEST)
    a.start()

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file-{}M bs=1M count={}'.format(size,size))

    mountpoint = sata.mountpoint(a)

    if (mountpoint == None):
        print_result.func_fail(a)

    a.buff=""
    a.send('cat /proc/interrupts | grep sata')
    
    INTR_BEFORE = int(a.find_str('sata_rcar').split()[1])

    if (cp_device.mount_device(a,mountpoint) == False):
        print_result.func_fail(a)
    
    a.send('cp /tmp/file-{}M /mnt/'.format(size))

    a.buff=""
    a.send('cat /proc/interrupts | grep sata')

    INTR_AFTER = int(a.find_str('sata_rcar').split()[1])
   
    if (cp_device.umount_device(a) == False):
        print_result.func_fail(a)
   
    a.send('rm /tmp/file-{}M'.format(size))

    if (INTR_AFTER <= INTR_BEFORE):
        print_result.func_fail(a)

    print_result.func_pass(a)
  
 

       
