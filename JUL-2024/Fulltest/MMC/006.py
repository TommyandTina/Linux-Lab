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
import mmc
import subprocess


FAILED=1
PASSED=0

RESULT=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
                  
    if (mmc.cp_ram_to_mmc(a,350)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a) 
