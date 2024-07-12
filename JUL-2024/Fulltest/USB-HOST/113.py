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
import control_board
import usb

CHANNEL='usb2'
TYPE='memory'

if __name__ == '__main__' :
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    a.send(' ',0,False)

    print('\nPlease press 1 button on the keyboard when you see log as <Testing ... (interrupt to exit)>')
    print('\nPress any key to continue...')
    sys.stdout.flush()
    raw_input()    

    a.send('test_keyboard=/dev/input/by-id/`ls /dev/input/by-id | grep kbd`')
    a.send('evtest $test_keyboard',0,False)
    if(a.buff.find('evtest:')!=-1):
        print_result.func_fail(a)

    if(a.wait('SYN_REPORT',10) == False):
        print_result.func_fail(a)
    sleep(5)
    
    a.send('\x03')
    sleep(1)

    print_result.func_pass(a)
