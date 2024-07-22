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
import sdhi


CARD_SLOT1 = 'sd1'
CARD_SLOT2 = 'sd2'
SIZE = 10

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
                  
    if (sdhi.cp_between_two_sd(a,CARD_SLOT1,CARD_SLOT2,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a) 