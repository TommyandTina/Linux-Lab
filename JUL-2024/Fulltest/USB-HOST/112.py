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
import usb


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    
    print 'Make sure you connected a keyboard to USB port'
    sys.stdout.flush()
    sleep(1)
    a.buff=""
    a.send('dmesg | grep Keyboard')  
    if (a.buff.find('input: USB HID v1.11 Keyboard')==-1) and (a.buff.find('input: USB HID v1.10 Keyboard')==-1):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)
    

