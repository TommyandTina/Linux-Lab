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


def return_ori():
    a.send('echo {} > unexport'.format(GPIO_PORT1))

    a.send('echo {} > unexport'.format(GPIO_PORT2))

    a.send('cd ~')

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

    if (config.SOC == 'E3'):
        GPIO_PORT1 = int(gpio_chip[1]) + 11
        GPIO_PORT2 = int(gpio_chip[1]) + 8
    else:
        GPIO_PORT1 = int(gpio_chip[6]) + 4
        GPIO_PORT2 = int(gpio_chip[6]) + 21
          
    a.send('cd /sys/class/gpio')
   
    a.send('echo {} > export'.format(GPIO_PORT1))

    a.send('echo {} > export'.format(GPIO_PORT2))

    a.send('echo in > gpio{}/direction'.format(GPIO_PORT1))
 
    a.send('echo low > gpio{}/direction'.format(GPIO_PORT2))

    a.buff=""
    a.send('cat gpio{}/value'.format(GPIO_PORT1))

    if (a.buff.splitlines()[2]!='0'):
        print_result.func_fail(a)

    a.buff=""
    a.send('cat gpio{}/value'.format(GPIO_PORT2))
   
    if (a.buff.splitlines()[2]!='0'):
        return_ori()
        print_result.func_fail(a)

    a.send('echo 1 > gpio{}/value'.format(GPIO_PORT2))

    a.buff=""
    a.send('cat gpio{}/value'.format(GPIO_PORT2))

    if (a.buff.splitlines()[2]!='1'):
        return_ori()
        print_result.func_fail(a)
   
    a.buff="" 
    a.send('cat gpio{}/value'.format(GPIO_PORT1))

    if (a.buff.splitlines()[2]!='1'):
        return_ori()
        print_result.func_fail(a)

    a.send('echo 0 > gpio{}/value'.format(GPIO_PORT2))

    a.buff=""
    a.send('cat gpio{}/value'.format(GPIO_PORT2))

    if (a.buff.splitlines()[2]!='0'):
        return_ori()
        print_result.func_fail(a)

    a.buff=""
    a.send('cat gpio{}/value'.format(GPIO_PORT1))

    if (a.buff.splitlines()[2]!='0'):
        return_ori()
        print_result.func_fail(a)

    a.send('echo {} > unexport'.format(GPIO_PORT1))

    a.send('echo {} > unexport'.format(GPIO_PORT2))

    a.send('cd ~')
   
    print_result.func_pass(a)
