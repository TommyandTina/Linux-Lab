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
          
    a.send('ls /sys/bus/platform/drivers | grep dma')

    if (a.buff.find('omap-dma-engine')!=-1) and (a.buff.find('rcar-dmac')!=-1) \
      and (a.buff.find('renesas_sdhi_internal_dmac')!=-1) and (a.buff.find('usb-dmac')!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
