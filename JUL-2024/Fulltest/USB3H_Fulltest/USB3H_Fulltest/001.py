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
import restart_board

CHANNEL1 = 'RAM'
CHANNEL2 = 'usb3'
SIZE = 200

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""
    
    restart_board.main(a)

    mountpoint = (usb.mountpoint_usb_hdd(a, channel = "usb3"))
    if mountpoint == None:
        print_result.func_fail(a)
        
    a.send("dd if=/dev/{} of=/dev/null bs=64M count=10 iflag=direct".format(mountpoint))
    a.send("dd if=/dev/zero of=/dev/{} bs=64M count=10 oflag=direct".format(mountpoint))

    print_result.func_pass(a)