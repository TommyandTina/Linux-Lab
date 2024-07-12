#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import print_result
import scif

if __name__ == '__main__':
    a=config.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (scif.check_SCIF1(a,'scif') == False):
        print('False')
    else:
        print('True')
