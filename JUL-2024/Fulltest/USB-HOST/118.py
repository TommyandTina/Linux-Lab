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
import s2ram

CHANNEL='usb2'
TYPE='memory'

if __name__ == '__main__' :
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    a.send(' ',0,False)

    if(s2ram.pm_suspend(a)==False):
        print_result.func_fail(a)    

    if(s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)

    print('\nPlease move the mouse when you see log as <Testing ... (interrupt to exit)>')
    print('\nPress any key to continue...')
    sys.stdout.flush()
    raw_input()    

    a.send('test_mouse=/dev/input/by-id/`ls /dev/input/by-id | grep mouse`')
    a.send('evtest $test_mouse',0,False)
    if(a.buff.find('evtest:')!=-1):
        print_result.func_fail(a)

    if(a.wait('SYN_REPORT',20) == False):
        print_result.func_fail(a)
    sleep(5)
    
    a.send('\x03')
    sleep(1)

    print_result.func_pass(a)
