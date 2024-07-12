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


FAILED=1
PASSED=0

RESULT=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep sdhi')
    
    if (a.buff.find('ee100000.mmc: mmc1 base at 0x00000000ee100000, max clock rate')!=-1) \
      and (a.buff.find('ee140000.mmc: mmc0 base at 0x00000000ee140000, max clock rate')!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
