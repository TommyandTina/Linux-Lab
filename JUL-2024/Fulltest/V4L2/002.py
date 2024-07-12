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
import v4l2

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('ls /dev/video*')

    a.send('ls /dev/v4l-subdev*')

    for i in range(0,v4l2.MAX_VIDEO+1):
        if (a.buff.find('/dev/video{}'.format(i))==-1):
            print_result.func_fail(a)

    for i in range(0,v4l2.MAX_SUBDEV+1):
        if (a.buff.find('/dev/v4l-subdev{}'.format(i))==-1):
            print_result.func_fail(a)

    print_result.func_pass(a)
