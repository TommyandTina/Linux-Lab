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

TYPE_USB2H = "USB1.1"
SIZE_FILE = 1 if TYPE_USB2H == "USB1.1" else 5
CN = 3
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
    a.buff = ""
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    if a.buff.find("wrong fs type, bad option, bad superblock on") != -1:  
        a.send('echo y | mkfs.ext4 /dev/{}'.format(mountpoint))
        a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("cp testdata /mnt/usb/")
    a.send("umount /mnt/usb")
    
if __name__ == '__main__':
    a = conserial.serial_thread(config.SERIAL_PORT,1, usb2h_fulltest.MODULE_TEST)
    a.start()
    a.buff = ""
    
    #####################################################################################################
    print_item(a, 22)
    restart_board.main(a)
    prepare_testdata(a)
    
    mountpoint = usb2h_fulltest.mountpoint_usb2h(a, USB2H_LIST[CN])
    command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp /mnt/usb/testdata testdata_from_usb &"]
    if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
        print_result.func_fail(a)
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
        
    a.send("wait")
    a.send("sync")
    a.send("cmp testdata testdata_from_usb")
    a.send("umount /mnt/usb")

    bs = 1
    count = 1
    mountpoint = usb2h_fulltest.wait_usb2h(a, USB2H_LIST[CN], False)
    a.send("dd if=/dev/{} of=/dev/null bs={}M count={} iflag=direct".format(mountpoint, bs, count))
    a.send("dd if=/dev/zero of=/dev/{} bs={}M count={} oflag=direct".format(mountpoint, bs, count))
    
    print_result.func_pass(a)
