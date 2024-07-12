#!/usr/bin/python
import serial
import threading
from time import sleep
from time import time
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import print_result
import usb3f

STORAGE='RAM'
CP_TO='STORAGE'
SIZE=300

if __name__ == '__main__':
    a=config.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
        
    os.system('/bin/bash ls')
