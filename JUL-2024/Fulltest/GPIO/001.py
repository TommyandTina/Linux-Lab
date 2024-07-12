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
          
    a.send('dmesg | grep gpio_rcar ')
     
    for i in range(gpio.MAX_BANK + 1):
        if (a.buff.find('gpio_rcar {}: driving {} GPIOs'.format(gpio.GPIO_NODE[i],gpio.NUM_GPIO[i]))==-1):
            print_result.func_fail(a)

    print_result.func_pass(a)
