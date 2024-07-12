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
import usb
import restart_board
import time
CHANNEL1 = 'RAM'
CHANNEL2 = 'usb3'
SIZE = 200

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()

    restart_board.main(a)
    
    mountpoint = (usb.mountpoint_usb3(a, channel = "usb3"))
    if mountpoint == None:
        print_result.func_fail(a)
    a.buff=""
    a.send("cd ~/usb3h_test")
    a.send("mkdir -p /mnt/usbfm")
    a.send("mount /dev/{} /mnt/usbfm".format(mountpoint))
    a.send("taskset -c 0 ./fm2.sh &",0,False)
    
    if config.SOC.find("E3") != -1 or config.SOC.find("M3N") != -1:
        a.send("taskset -c 1 ./fm1.sh",0,False)
    elif config.SOC.find("H3") != -1 or config.SOC.find("M3") != -1:
        a.send("taskset -c 1 ./fm2_2.sh & taskset -c 2 ./fm2_3.sh & taskset -c 3 ./fm1.sh",0,False)
    else:
        print_result.func_fail(a)
    time.sleep(1800)
    a.send("wait", TIMEOUT=60)
    a.send("umount /dev/{}".format(mountpoint))

    print_result.func_pass(a)
