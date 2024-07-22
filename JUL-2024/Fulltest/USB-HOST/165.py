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


CHANNEL='usb2ch2'
TYPE='memory'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
   
    a.send(' ',0,False)
  
    for i in range(1,6):
        print ("\n------{}------".format(i))     
        a.buff=""
        if (config.FEATBOX_USB_MODULE == True):
            control_board.usb_in(CHANNEL,TYPE)
        else:
            print('\nPlease plug in USB:')
            sys.stdout.flush()
       
        if (a.wait('Attached SCSI removable disk',30) == False): 
            print_result.func_fail(a)
    
        sleep(1)
        a.send(' ',0,False)
    
        if (config.FEATBOX_USB_MODULE == True):
            control_board.usb_out(CHANNEL,TYPE)
        else:
            print('\nPlease plug out USB:')
            sys.stdout.flush()
    
        if (a.wait('USB disconnect',20) == False):
            print_result.func_fail()
        
        sleep(1)
        a.send(' ',0,False)

    print_result.func_pass(a) 