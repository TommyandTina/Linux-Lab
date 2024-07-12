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


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
  
    eth.check_eth(a)

    a.send('cat /proc/interrupts | grep eth0')

    if (a.buff.find(':rx_nc')!=-1) and (a.buff.find(':tx_be')!=-1) \
      and (a.buff.find('tx_nc')!=-1) and (a.buff.find('multi')!=-1) and (a.buff.find('emac')!=-1):
        print_result.func_pass(a)   
    else:
        print_result.func_fail(a)



