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
import unbind_bind
import usb

CHANNEL='usb2ch1'
DRIVER="ehci-platform"
SIZE=300

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
    
    if (CHANNEL == 'usb2ch1'):
        INTR = usb.USB2_CH1_INTERRUPT
    elif (CHANNEL == 'usb2ch2'):
        INTR = usb.USB2_CH2_INTERRUPT
    elif (CHANNEL == 'usb3'):
        INTR = usb.USB3_INTERRUPT 

    if (unbind_bind.unbind(a,DRIVER,INTR)==False):
        print_result.func_fail(a)

    if (unbind_bind.bind(a,DRIVER,INTR)==False):
        print_result.func_fail(a)    
 
    if (usb.cp_ram_to_usb(a,CHANNEL,SIZE,'dont_care')==False):
        print_result.func_fail(a)

    print_result.func_pass(a)
        
       
