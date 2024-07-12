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

TOTAL_ERR = 0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    a.send('dmesg | grep rcar-du')
    if (a.buff.find('rcar-du feb00000.display: [drm] fb0:')==-1) \
      or (a.buff.find('Initialized rcar-du')==-1):
          TOTAL_ERR += 1    
    
    a.buff=""
    a.send('dmesg | grep display')
    if (a.buff.find('Device feb00000.display probed')==-1):
        TOTAL_ERR += 1
    
    a.buff=""
    a.send('dmesg | grep hdmi')
    if (a.buff.find('Detected HDMI TX controller')==-1)\
      or (a.buff.find('registered DesignWare HDMI I2C bus driver')==-1):
        TOTAL_ERR += 1

    a.buff=""
    if (TOTAL_ERR > 0):
        print_result.func_fail(a)
    
    print_result.func_pass(a) 
