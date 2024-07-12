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
import gpio

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
    count = 0

    a.send('find /sys/class/gpio/gpiochip*')
    for i in a.buff.splitlines():
        if (('/sys/class/gpio/gpiochip' in i) and ('/sys/class/gpio/gpiochip*' not in i)):
            count += 1

    if (count < gpio.MAX_BANK + 1):
            print_result.func_fail(a)

    print_result.func_pass(a)
