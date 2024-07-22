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
import cp_device
import usb

CHANNEL='usb3'
DRIVER="xhci-renesas-hcd"
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

    COMMAND = "cd /sys/bus/platform/drivers/{}; echo {} > unbind".format(DRIVER,INTR)

    if (cp_device.cp_ram_to_device_while_doing_st(a,usb.mountpoint(a,CHANNEL),SIZE,COMMAND) == False):
        print_result.func_fail(a)

    if (unbind_bind.bind(a,DRIVER,INTR) == False):
        print_result.func_fail(a)

    if (usb.cp_ram_to_usb(a,CHANNEL,SIZE)==False):
        print_result.func_fail(a)

    print_result.func_pass(a)