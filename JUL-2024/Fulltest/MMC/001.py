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

MMC_No='0'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep mmc{}'.format(MMC_No))
    
    if (a.buff.find('ee140000.mmc: mmc{} base at 0x00000000ee140000, max clock rate 200 MHz'.format(MMC_No))!=-1) \
      and (a.buff.find('new HS400 MMC card at address 0001')!=-1) and (a.buff.find('mmcblk{0}: mmc{0}:0001'.format(MMC_No))!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
