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
     
    if (config.SOC == 'E3'):
        ADAPTER = 8
        ND1 = 'e6500000.i2c'
        ND2 = 'e66d0000.i2c'
    else:
        ADAPTER = 7
        ND1 = 'e6510000.i2c'
        ND2 = 'e66d8000.i2c'
      
    a.send('dmesg | grep i2c',0.05)
        
    if (a.buff.find('i2c-sh_mobile e60b0000.i2c: I2C adapter {}, bus speed'.format(ADAPTER))!=-1) \
      and (a.buff.find('i2c-rcar {}: probed'.format(ND1))!=-1) and (a.buff.find('i2c-rcar {}: probed'.format(ND2))!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
