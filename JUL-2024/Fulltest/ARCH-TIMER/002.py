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



if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
    a.buff=""
          
    a.send('cat /proc/interrupts | grep timer',0.05)
    
    if (a.buff.find('GIC-0')!=-1 or a.buff.find('GICv2')!=-1):
        print_result.func_pass(a)        
    else:
        print_result.func_fail(a)
                  
