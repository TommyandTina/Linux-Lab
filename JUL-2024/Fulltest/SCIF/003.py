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

import scif


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (scif.check_SH_SCI_DMA(a,'=n') == False):
        print_result.wrong_env(a)

    a.buff=""
    a.send('cat /proc/interrupts | grep serial')

    INTR_BEFORE = int(a.find_str('e6e88000.serial:mux').split()[1])

    a.buff=""
    a.send('cat /proc/interrupts | grep serial')

    INTR_AFTER = int(a.find_str('e6e88000.serial:mux').split()[1])
    
    if (INTR_AFTER <= INTR_BEFORE): # "<" :D
        print_result.func_fail(a)

    print_result.func_pass(a)
