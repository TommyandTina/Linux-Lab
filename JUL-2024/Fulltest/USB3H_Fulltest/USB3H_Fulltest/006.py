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
    
    a.send("mkdir -p /mnt/usb")
    a.send("echo test > test.txt")
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("mkdir /mnt/usb/test")
    a.send("cp ./test.txt /mnt/usb/test.txt")
    a.send("cmp ./test.txt /mnt/usb/test.txt")
    a.send("cp /mnt/usb/test.txt ./test.txt")
    a.send("cmp ./test.txt /mnt/usb/test.txt")
    a.send("ls /mnt/usb/test")
    a.send("rm /mnt/usb/test.txt")
    a.send("rmdir /mnt/usb/test")
    a.send("umount /mnt/usb")
    print_result.func_pass(a)
