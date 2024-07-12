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
import mmc


SIZE = 350
DRIVER_PATH = "renesas_sdhi_internal_dmac"
INTR = "ee140000.mmc"
COMMAND = "cd /sys/bus/platform/drivers/{}; echo {} > unbind".format(DRIVER_PATH,INTR)

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
                 
    if (cp_device.cp_ram_to_device_while_doing_st(a,mmc.mountpoint(a),SIZE,COMMAND) == False):
        print_result.func_fail(a)

    if (unbind_bind.bind(a,DRIVER_PATH,INTR) == False):
        print_result.func_fail(a)

    if (mmc.cp_ram_to_mmc_umount_after_bind(a,SIZE,'has_data')==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a) 
