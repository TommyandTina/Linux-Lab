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
          
    a.send('cat /proc/interrupts | grep ee140000.mmc')
    
    if (a.buff.find('GICv2')!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
