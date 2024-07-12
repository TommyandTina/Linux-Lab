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

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep eth')
    
    if (a.buff.find('psci: probing for conduit method from DT')!=-1) \
      and (a.buff.find('ravb e6800000.ethernet eth0: Base address at 0xe6800000')!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)



   
