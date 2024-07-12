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
    gpio_chip = []

    a.send('ls -l /sys/class/gpio/gpiochip*')
    for i in a.buff.splitlines():
        if (('/sys/class/gpio/gpiochip' in i) and ('/sys/class/gpio/gpiochip*' not in i)):
            if ("i2c" not in i):
                gpio_chip.append(str(i)[62:65])
    
    a.send('cd /sys/class/gpio')

    for i in gpio_chip:
        a.buff=""
        a.send('cat gpiochip{}/base'.format(i))
        
        if (a.buff.splitlines()[2].split()[0] != i):
            print_result.func_fail(a)
            
        a.buff=""
        a.send('cat gpiochip{}/label'.format(i))
        
        if (a.buff.splitlines()[2] not in gpio.GPIO_NODE):
            print_result.func_fail(a)

        a.buff=""
        a.send('cat gpiochip{}/ngpio'.format(i))
        
        if (a.buff.splitlines()[2] not in gpio.NUM_GPIO):
            print_result.func_fail(a)

    a.send('cd ~')
    print_result.func_pass(a)
