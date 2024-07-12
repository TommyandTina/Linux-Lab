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

    a.buff=""
    a.send('echo "Linux version `uname -r`"')
    print('')
    sys.stdout.flush()
    
if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    main(a)

    a.serial.close()

