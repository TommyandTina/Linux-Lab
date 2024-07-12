#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import re
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import conserial
import print_result
import sata


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1,sata.MODULE_TEST)
    a.start()
    a.buff=""

    DEVICE = sata.mountpoint(a)

    if (DEVICE == None):
        print_result.func_fail(a)

    DEVICE = re.findall(r'[A-Za-z]+|\d+', DEVICE)[0]
          
    a.send('smartctl -d ata -a /dev/{}'.format(DEVICE))
  
    if (a.buff.find('No Errors Logged')==-1):
        print_result.func_fail(a)
 
    print_result.func_pass(a)
                 
