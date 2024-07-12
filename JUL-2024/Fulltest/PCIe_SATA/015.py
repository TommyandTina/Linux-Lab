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
import s2ram
import print_result
import subprocess

SPEED=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
    time = 20
    #for i in range (1, time +1):
#	if (time > 1):
 #       a.buff = ""
    a.send('time dd if=/dev/sda  of=/dev/zero bs=64M count=10 seek=8 iflag=direct > read_dd.txt')
    sleep(0.5)

    SPEED=a.find_str('MB/s').split(", ")[3].split()[0]

    print ("\n \n SPEED = {} MB/s".format(SPEED))

    if (int(SPEED) < 400):
        print_result.func_fail(a)

    print_result.func_pass(a)
