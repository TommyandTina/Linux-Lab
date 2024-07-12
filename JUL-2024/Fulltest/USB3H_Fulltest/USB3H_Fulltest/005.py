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

STRESS_TIME=3600

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()

    restart_board.main(a)
    
    mountpoint = (usb.mountpoint_usb3(a, channel = "usb3"))
    if mountpoint == None:
        print_result.func_fail(a)
    a.buff=""
    if (config.SOC == "M3N") or (config.SOC == "E3"):
        a.send("stress-ng --cpu 2 --io 4 --vm 2 --vm-bytes 20M --timeout 3600s &")
    elif (config.SOC.find('H3') !=-1) or (config.SOC.find('M3')!=-1):
        a.send("stress-ng --cpu 4 --io 4 --vm 2 --vm-bytes 20M --timeout 3600s &")
    else:
        print_result.func_fail(a)
    a.send("dd if=/dev/urandom of=testdata bs=1024K count=10")
    a.send("cp testdata testdata_aaa &")

    START_TIME = time.time()
    while (a.buff.find('successful run completed in')==-1):
        a.send("dd if=testdata_aaa of=/dev/sda1 bs=1024K count=10")
        a.send("dd if=/dev/sda1 of=testdata_bbb bs=1024K count=10")
        a.send("mv testdata_bbb testdata_aaa")
        sleep(1)
        if (a.buff.find('PANIC')!=-1) or (a.buff.find('WARNING')!=-1):
            print_result.func_fail(a)
            sys.exit(1)
        
        if ((time.time() - START_TIME) > (STRESS_TIME+20)): break
    a.send("cmp testdata testdata_aaa")
    a.send("md5sum testdata")
    a.send("md5sum testdata_aaa")
    
    print_result.func_pass(a)
