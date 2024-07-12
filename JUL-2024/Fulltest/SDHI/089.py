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


CARD_SLOT = 'sd1' 
SIZE = 350
TIME = 100

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
    
    for i in range(1,TIME+1):      
        print ('\n----------- TIME {} -----------'.format(i))         
        if (sdhi.cp_ram_to_sd(a,CARD_SLOT,SIZE)==False):
            print_result.func_fail(a)
        print ('\n \n TIME {}: OK'.format(i))
   
    print_result.func_pass(a) 
