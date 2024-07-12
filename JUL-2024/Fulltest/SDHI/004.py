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

SD_CHANNEL='sd1'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()

    for i in range(0,5):    
        a.buff="" 
        a.send(' ',0,False)

        print('\nPlease plug in SD0:')
        sys.stdout.flush()
    
        if (a.wait('mmcblk',30) == False): 
            print_result.func_fail(a)

        sleep(0.5)
        if (sdhi.mountpoint(a,SD_CHANNEL) == None):
            print_result.func_fail(a)

        print('\nPlease plug out SD0:')
        sys.stdout.flush()

        if (a.wait('card aaaa removed',10) == False):
            print_result.func_fail()

        if (sdhi.mountpoint(a,SD_CHANNEL) != None):
            print_result.func_fail(a)

    print_result.func_pass(a) 
