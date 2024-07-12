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
import s2ram
import print_result
import pcie


INTR_BEFORE=0
INTR_AFTER=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    pcie.check_pcie(a)
    a.send('ifconfig enp1s0 up 192.168.10.125')
    a.buff=""
    if (s2ram.pm_suspend_while_doing_st(a,'ping -c 30 {} & sleep 5;'.format(config.SERVER_ADDR))==False):
        print_result.func_fail(a)

    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
    
    if (pcie.ping_server_ip(a,config.SERVER_ADDR,20) == False):
        print_result.func_fail(a)
    
    print_result.func_pass(a)
 

