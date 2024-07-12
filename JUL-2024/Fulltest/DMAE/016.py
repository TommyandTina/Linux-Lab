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
import dmae

INTR=dmae.USB_DMAC1_INTR
MAX=dmae.USB_DMAC_CHANNEL_MAX

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('cat /proc/interrupts | grep {}'.format(INTR))
    for i in range(0,MAX+1):
        if (a.buff.find('controller:{}'.format(i))==-1):
            print_result.func_fail(a)
    
    print_result.func_pass(a)
   
