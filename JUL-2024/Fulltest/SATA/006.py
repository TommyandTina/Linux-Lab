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

    a.send('hdparm -tT /dev/{}'.format(DEVICE))
    if (a.buff.find('Timing cached reads')==-1 or a.buff.find('Timing buffered disk reads')==-1):
        print_result.func_fail(a)
          
    a.send('smartctl -d ata -H /dev/{}'.format(DEVICE))
  
    if (a.buff.find('SMART overall-health self-assessment test result: PASSED')==-1):
        print_result.func_fail(a)
 
    print_result.func_pass(a)
                 