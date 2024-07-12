#!/usr/bin/python

import sys
import os
sys.path.append(os.path.relpath('..'))
sys.path.append(os.path.relpath('../common/'))
import config
import conserial
import print_result
import restart_board
import serial
import threading
from time import sleep
import usb2h_fulltest

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb2h_fulltest.MODULE_TEST)
    a.start()
    a.buff=""
    
    restart_board.main(a)

    #####################################################################################################
    print("\n\n----------Item 1----------\n")

    if (s2ram.pm_suspend(a)==False):
        print_result.func_fail(a)
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
    
    print_result.func_pass(a)
