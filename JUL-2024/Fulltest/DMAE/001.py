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
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep DMA')

    if (a.buff.find('DMA: preallocated 1024 KiB GFP_KERNEL pool for atomic allocations')!=-1 or a.buff.find('DMA: preallocated 512 KiB GFP_KERNEL pool for atomic allocations')!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
