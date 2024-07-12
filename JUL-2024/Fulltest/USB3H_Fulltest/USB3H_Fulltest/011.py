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

device = "usb10"

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()

    restart_board.main(a)

    a.buff = ""
    while (a.buff.find("USB device number 2 using xhci-hcd") == -1):
        sleep(0.1)
    time.sleep(1)

    for i in range(0,5):
        a.send("echo {} > /sys/bus/usb/drivers/usb/unbind".format(device))
        time.sleep(1)
        a.send("echo {} > /sys/bus/usb/drivers/usb/bind".format(device))
        time.sleep(1)
        a.send("sleep 4")
    print_result.func_pass(a)
    