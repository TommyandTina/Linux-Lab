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
import pcie

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
  
    pcie.check_mask(a)
    a.buff=""
    #a.send('ifconfig enp1s0 up 255.255.255.0')
    a.send('ifconfig enp1s0 netmask {}'.format(config.NET_MASK))
 ##   a.send('ip add {} dev enp1s0'.format(config.IP))
   # a.wait('Link is Up')
    a.buff=""
    a.send('ifconfig enp1s0 | grep inet')
    a.buff=""
    a.send('ifconfig')
    if (a.buff.find('inet addr:{}'.format(config.NET_MASK))!=-1):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)
