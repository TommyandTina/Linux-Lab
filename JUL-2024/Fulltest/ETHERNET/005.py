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
import eth

INTR1_BEFORE=0
INTR2_BEFORE=0

INTR1_BEFORE=0
INTR2_BEFORE=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
  
    eth.check_eth(a)

    a.buff=""
    a.send('cat /proc/interrupts | grep eth0')

    INTR1_BEFORE = int(a.find_str('eth0:ch0:rx_be').split()[1])
    INTR2_BEFORE = int(a.find_str('eth0:ch18:tx_be').split()[1])
   
    eth.ping(a,config.SERVER_ADDR,20)    

    a.buff=""
    a.send('cat /proc/interrupts | grep eth0')

    INTR1_AFTER = int(a.find_str('eth0:ch0:rx_be').split()[1])
    INTR2_AFTER = int(a.find_str('eth0:ch18:tx_be').split()[1])

    if (INTR1_AFTER > INTR1_BEFORE) and (INTR2_AFTER > INTR2_BEFORE):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)
