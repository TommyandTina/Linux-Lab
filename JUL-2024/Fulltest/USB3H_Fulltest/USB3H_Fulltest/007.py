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

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()

    restart_board.main(a)
    
    mountpoint = (usb.mountpoint_usb3(a, channel = "usb3"))
    if mountpoint == None:
        print_result.func_fail(a)
    a.buff=""
    
    a.send("dd if=/dev/urandom of=150m.dat bs=1M count=150")

    a.send("mkdir -p /mnt/usb")
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    
    a.send("cp ./150m.dat /mnt/usb/",0.001,False)
    time.sleep(0.5)
    
    #Ctrl + C
    a.send('\x03')
    
    a.send("cp ./150m.dat /mnt/usb/")
    a.send("sync")

    a.send("cmp ./150m.dat /mnt/usb/150m.dat")
    a.send("umount /dev/{}".format(mountpoint))

    print_result.func_pass(a)
