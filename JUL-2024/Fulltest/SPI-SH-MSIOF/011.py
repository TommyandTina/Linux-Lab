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

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep spi')

    if (a.buff.find('PIO') == -1):
        print_result.func_fail(a)       
    
    a.buff=""
    a.send('./21_test_msiof_normal_trtx.sh m 2 p')

    if (a.buff.find('MSIOF Loopback Test Passed.') == -1):
        print_result.func_fail(a)

    print_result.func_pass(a)
