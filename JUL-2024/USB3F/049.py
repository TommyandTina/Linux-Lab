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
import usb3f

STORAGE='RAM' #RAM, SD
CP_TO='BOARD' #BOARD (from host), HOST (from board), WRITE_SPEED, READ_SPEED, NONE, READ_AND_WRITE_SPEED
SIZE=100 #MB
S2R=True #True, False

if __name__ == '__main__':
    serial_thread_id=conserial.serial_thread(config.SERIAL_PORT,1)
    serial_thread_id.start()
    serial_thread_id.buff=""
         
    if ( usb3f.g_mass_storage(serial_thread_id,STORAGE,CP_TO,SIZE,S2R) == False):
        print_result.func_fail(serial_thread_id)
    
    print_result.func_pass(serial_thread_id) 
 
