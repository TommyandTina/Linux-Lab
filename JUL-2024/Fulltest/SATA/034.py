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
import sata


SIZE = 350
COMMAND = "cd /sys/bus/platform/drivers/{}; echo {} > unbind".format(sata.DRIVER_PATH,sata.SATA_INTERRUPT)

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,sata.MODULE_TEST)
    a.start()
    a.buff=""
                 
    if (cp_device.cp_ram_to_device_while_doing_st(a,sata.mountpoint(a),SIZE,COMMAND) == False):
        print_result.func_fail(a)
    
    a.buff=""
    a.send('pwd')
    a.wait('[1]+  Done ',60)
    
    if (unbind_bind.bind(a,sata.DRIVER_PATH,sata.SATA_INTERRUPT) == False):
        print_result.func_fail(a)

    if (sata.cp_ram_to_hd(a,SIZE)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a) 
