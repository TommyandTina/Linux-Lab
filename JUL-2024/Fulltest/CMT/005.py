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
import subprocess
import cmt

CMT = cmt.cmt0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    if (cmt.check_cs(a,CMT) == False):
        print_result.func_fail(a)

    #a.buff=""          
    #a.send('grep {} /proc/interrupts'.format(CMT),0.05)
    
    #if (a.buff.find('GICv2')==-1):
    #    print_result.func_fail(a)

    a.buff=""
    a.send('date -s 2018/11/19',0.05)
   
    a.send('date -s 17:30',0.05)
    
    a.buff=""
    a.send('date',0.05)
           
    if (a.buff.find('Mon Nov 19')!=-1) and (a.buff.find('17:30')!=-1) and (a.buff.find('UTC 2018')):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)


