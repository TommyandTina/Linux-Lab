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
import sata

SIZE='350'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,sata.MODULE_TEST)
    a.start()
    a.buff=""

    if (sata.cp_hd_to_ram(a,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)
    
 

       
