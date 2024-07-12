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


PORT = gpio.LEFT_BOUNDARY - 1


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('cd /sys/class/gpio')
   
    a.buff="" 
    a.send('echo {} > export'.format(PORT))

    if (a.buff.find('write error: Invalid argument')==-1):
        a.send('cd ~')
        print_result.func_fail(a)
   
    a.send('cd ~')
    print_result.func_pass(a)
