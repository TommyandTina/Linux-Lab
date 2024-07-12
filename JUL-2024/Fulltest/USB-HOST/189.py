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
import time

CHANNEL='usb3'
SIZE='10'
DATA='no_data'

STRESS_TIME=3600

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
   
    DEVICE = usb.mountpoint(a,CHANNEL)
    if (DEVICE == None):
        print_result.func_fail(a)
        sys.exit()

    a.buff=""
    a.send('stress --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(config.NUM_CPU,config.NUM_CPU*2,config.NUM_CPU,STRESS_TIME),0,False)
        
    START_TIME = time.time()
    i = 1
    FAIL_CNT = 0
    while (a.buff.find('successful run completed in')==-1):
        print ('\n\n----------- TEST_TIME {} -----------'.format(i))
        i += 1
        if (usb.cp_ram_to_usb(a,CHANNEL,SIZE,DATA)==False):
            print_result.func_fail(a)
            FAIL_CNT += 1
        sleep(1)
        if (a.buff.find('PANIC')!=-1) or (a.buff.find('WARNING')!=-1):
            print_result.func_fail(a)
            sys.exit(1)
        
        if ((time.time() - START_TIME) > (STRESS_TIME+20)): break
        
    if (FAIL_CNT>0):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)    
