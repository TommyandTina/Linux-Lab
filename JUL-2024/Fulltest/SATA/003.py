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
 
    a.send('hdparm -I /dev/{} | grep -i speed'.format(DEVICE))
    
    CHECK = ['Gen1 signaling speed (1.5Gb/s)','Gen2 signaling speed (3.0Gb/s)','Gen3 signaling speed (6.0Gb/s)']

    for i in CHECK:
        if (a.buff.find(i)==-1):
            print_result.func_fail(a)        
   
    print_result.func_pass(a)
                 
