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
import usb



if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep usb') 
    
    if (a.buff.find('{}: new USB bus registered'.format(usb.USB2_CH1_INTERRUPT))==-1) \
      or (a.buff.find('{}: new USB bus registered'.format(usb.USB3_INTERRUPT))==-1):
        print_result.func_fail(a)
    
    if (config.SOC.find('E3') == -1):
        if (a.buff.find('{}: new USB bus registered'.format(usb.USB2_CH2_INTERRUPT))==-1):
            print_result.func_fail(a)

    print_result.func_pass(a)

    

