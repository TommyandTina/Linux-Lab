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
import cp_device
import unbind_bind
import sdhi


CARD_SLOT = "sd2"
SIZE = 350
DRIVER_PATH = "renesas_sdhi_internal_dmac"
INTR = "ee160000.mmc"
COMMAND = "cd /sys/bus/platform/drivers/{}; echo {} > unbind".format(DRIVER_PATH,INTR)

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
        
    if (unbind_bind.unbind(a,DRIVER_PATH,INTR) == False):         
        print_result.func_fail(a)

    if (unbind_bind.bind(a,DRIVER_PATH,INTR) == False):
        print_result.func_fail(a)

    if (sdhi.cp_ram_to_sd(a,CARD_SLOT,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a) 
