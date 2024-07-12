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
import unbind_bind
import sata


SIZE = 350

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,sata.MODULE_TEST)
    a.start()
    a.buff=""
   
    DEVICE = sata.find_device(a)

    if (DEVICE == None):
        print_result.func_fail(a)
     
    if (unbind_bind.unbind(a,sata.DRIVER_PATH,sata.SATA_INTERRUPT) == False):         
        print_result.func_fail(a)
   
    a.buff=""
    a.send('ls /dev/{}'.format(DEVICE))
    
    if (a.buff.find('No such file or directory')==-1):
        print_result.func_fail(a)

    if (unbind_bind.bind(a,sata.DRIVER_PATH,sata.SATA_INTERRUPT) == False):
        print_result.func_fail(a)

    if (sata.cp_ram_to_hd(a,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a) 
