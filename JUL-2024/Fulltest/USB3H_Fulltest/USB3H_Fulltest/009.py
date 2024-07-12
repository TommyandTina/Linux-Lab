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
import time

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()

    restart_board.main(a)
    
    mountpoint = (usb.mountpoint_usb3(a, channel = "usb3"))
    if mountpoint == None:
        print_result.func_fail(a)
    a.buff=""
    a.send("dd if=/dev/{} of=/dev/null bs=512 count=1 skip=8".format(mountpoint))
    a.send("dd if=/dev/zero of=/dev/{} bs=512 count=1 seek=8".format(mountpoint))

    print_result.func_pass(a)
