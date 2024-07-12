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
          
    a.send('insmod memd.ko')

    if (a.buff.find('memd driver loaded')==-1):
        print_result.func_fail(a)       

    a.buff=""    
    a.send('echo rd 0xe6150040 > /proc/reg')

    if (a.buff.find('FDC') == -1):
        print_result.func_fail(a)

    print_result.func_pass(a)
