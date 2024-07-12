#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import conserial
import control_board
import subprocess

def main(a):

    sys.stdout.flush()

    a.send("echo e659c000.usb > /sys/bus/platform/drivers/renesas_usbhs/unbind")


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    main(a)

    a.serial.close()

