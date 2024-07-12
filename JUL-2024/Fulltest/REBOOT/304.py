#!/usr/bin/python

import sys
import os
sys.path.append(os.path.relpath('..'))
sys.path.append(os.path.relpath('../common/'))
import config
import conserial
import print_result
import restart_board
import serial
import threading
import s2ram
from time import sleep
import usb2h_fulltest

TYPE_USB2H = "USB2.0"
SIZE_FILE = 1 if TYPE_USB2H == "USB1.1" else 5
CN = 0
CN_LIST = usb2h_fulltest.CN_LIST
USB2H_LIST = usb2h_fulltest.USB2H_LIST

def print_item(a, n):
    print("\n\n----------Item {}----------\n".format(n))
    sys.stdout.flush()
    a.buff = ""
    
def plug_in_usb(a):
    print("\nPlug in USB device at {}\n".format(CN_LIST[CN]))
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    
def pull_out_usb(a):
    print("\nPull out USB device at {}\n".format(CN_LIST[CN]))
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()

def prepare_testdata(a):
    print("\n----------Prepare----------\n")
    sys.stdout.flush()
    
    mountpoint = usb2h_fulltest.mountpoint_usb2h(a, USB2H_LIST[CN])
    a.send("dd if=/dev/urandom of=testdata bs=10M count={}".format(SIZE_FILE))
    a.send("mkdir -p /mnt/usb")
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("cp testdata /mnt/usb/")
    a.send("umount /mnt/usb")
    
if __name__ == '__main__':
    a = conserial.serial_thread(config.SERIAL_PORT,1, usb2h_fulltest.MODULE_TEST)
    a.start()
    a.buff = ""
    
    #####################################################################################################
    restart_board.main(a)
    
    usb2h_fulltest.load_qos(a)
    
    for i in range(0, len(usb2h_fulltest.USB2H_LIST)):
        CN = i
        a.send("echo {} > /sys/bus/platform/drivers/ehci-platform/unbind".format(USB2H_LIST[CN]))
        plug_in_usb(a)
        mountpoint = usb2h_fulltest.wait_usb2h_all(a, USB2H_LIST[CN], False)
        a.send("dd if=/dev/{} of=/dev/null bs=1M count=1 iflag=direct".format(mountpoint))
        a.send("dd if=/dev/zero of=/dev/{} bs=1M count=1 oflag=direct".format(mountpoint))  
        pull_out_usb(a)
    
    print_result.func_pass(a)

