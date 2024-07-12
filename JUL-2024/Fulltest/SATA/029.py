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

SIZE='1024'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,sata.MODULE_TEST)
    a.start()
    a.buff=""

    a.buff=""

    a.send('find /sys/devices/platform/soc/{}/ -name sd*'.format(sata.SATA_INTERRUPT))

    COUNT=1;

    for line in a.buff.splitlines():
       if (re.search('sd[a-z][0-9]',line)):
           if (COUNT == 1):
               MOUNT_POINT1 = line.split('/')[len(line.split('/'))-1]
           elif (COUNT == 2):
               MOUNT_POINT2 = line.split('/')[len(line.split('/'))-1]
 
           COUNT = COUNT + 1
           if (COUNT > 2):
               break;          
  
    if (COUNT <= 2):
        print_result.func_fail(a)

    if (sata.cp_between_two_partition(a,MOUNT_POINT2,MOUNT_POINT1,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)
    
 

       
