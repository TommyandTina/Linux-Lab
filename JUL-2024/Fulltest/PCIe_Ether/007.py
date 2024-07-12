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
  
    pcie.check_pcie(a)

    a.buff=""
    a.send('ethtool enp1s0 | grep Speed -A 2')

    if (a.buff.find('Speed: 1000Mb/s')!=-1) and (a.buff.find('Duplex: Full')!=-1):
        print_result.func_pass(a)   
    else:
        print_result.func_fail(a)

