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

CHANNEL1 = 'RAM'
CHANNEL2 = 'usb3'
SIZE = 200

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    
    restart_board.main(a)

    csv_file= "h3_Ver30_infotainment_v02_195.csv"
    
    mountpoint = (usb.mountpoint_usb_hdd(a, channel = "usb3"))

    if mountpoint == None:
        print_result.func_fail(a)
    
    a.buff=""
    a.send("insmod qos.ko")
    a.send("qos_tp setall {}".format(csv_file))
    a.send("qos_tp switch")
    
    a.send("dd if=/dev/{}  of=/dev/null bs=64M count=50 iflag=direct & top -b -d 1 -n 10 > aaa.txt".format(mountpoint))
    a.send("grep process_name aaa.txt")
    a.send("export pid=$!")
    a.send("echo $pid")
    a.send("wait $pid")
    a.send("grep $pid aaa.txt")
    
    a.send("dd if=/dev/zero of=/dev/{} bs=64M count=50 oflag=direct & top -b -d 1 -n 10 > aaa.txt".format(mountpoint))
    a.send("grep process_name aaa.txt")
    a.send("export pid=$!")
    a.send("echo $pid")
    a.send("wait $pid")
    a.send("grep $pid aaa.txt")
    
    print_result.func_pass(a)
