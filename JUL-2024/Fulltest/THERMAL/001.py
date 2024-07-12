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
import re


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
    
    a.buff=""          
    a.send('dmesg | grep thermal')
    
    if (re.search('rcar_gen3_thermal e6198000.thermal: Sensor 0: Loaded [1-9] trip points',a.buff)!=None) \
      and (re.search('rcar_gen3_thermal e6198000.thermal: Sensor 1: Loaded [1-9] trip points',a.buff)!=None) \
      and (re.search('rcar_gen3_thermal e6198000.thermal: Sensor 2: Loaded [1-9] trip points',a.buff)!=None):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)

