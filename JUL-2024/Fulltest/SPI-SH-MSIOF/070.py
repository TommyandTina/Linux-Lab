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

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep spi')

    if (a.buff.find('DMA available') == -1):
        print_result.func_fail(a)       

    for i in range(1,11):
        print ("\n------{}------".format(i))
        a.buff=""
        a.send('./32_SMP_Multi-Instance_3.sh')

        if (a.buff.find('Slave mode Passed.') == -1):
            print_result.func_fail(a)

        if (a.buff.find('Master mode Passed.') == -1):
            print_result.func_fail(a)

	if (a.buff.find('failed') != -1):
            print_result.func_fail(a)

    print_result.func_pass(a)
