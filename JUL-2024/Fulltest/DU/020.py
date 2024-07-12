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

PORT = 'VGA'
OPTION = ['-xres 640 -yres 480 -laced 0','-xres 1024 -yres 768 -laced 1']

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (du.fbdev_test(a,PORT,OPTION,du.IMAGE_FILE) == False):
        print_result.func_fail(a)
    
    print_result.func_pass(a) 
