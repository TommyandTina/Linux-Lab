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


CARD_SLOT = 'sd2'
FOLDER_STAGE = 5
SIZE = 50

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
                  
    if (sdhi.cp_folder_to_sd(a,CARD_SLOT,FOLDER_STAGE,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a) 
