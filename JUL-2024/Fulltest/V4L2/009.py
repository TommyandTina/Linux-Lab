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
          
    a.send('cd {}'.format(v4l2.VSP_FOLDER_TEST))

    a.buff=""

    a.send('./vsp-unit-test-0007.sh')

    if (a.buff.find('No such file or directory')!=-1):
        print_result.func_fail(a)

    if (a.buff.find('fail')!=-1):
        print_result.func_fail(a)

    a.send('cd ~')

    print_result.func_pass(a)
