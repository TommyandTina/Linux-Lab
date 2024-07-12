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
import du

PICTURE_ON = 'SD2'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (du.bmap_test(a,PICTURE_ON,du.IMAGE_FILE) == False):
        print_result.func_fail(a)
    
    print_result.func_pass(a) 
