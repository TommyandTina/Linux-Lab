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
import subprocess
import pcie

INTR1_BEFORE=0

INTR1_AFTER=0


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
  
    pcie.check_pcie(a)
    a.buff = ""
    a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR)) 
    
    a.buff=""
    a.send('cat /proc/interrupts | grep enp1s0')

    #INTR1_BEFORE = int(a.find_str('R-Car PCIe MSI   1').split()[1])
    INTR1_BEFORE = int(a.find_str('PCIe MSI').split()[1])

    pcie.ping_ip_addr(a,config.SERVER_ADDR,10)
    #a.send('ping -I enp1s0 -c 10 {}'.format(config.IP_ADDR))
    a.buff=""
    #a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))
    #a.send('ping -I enp1s0 -c 10 {}'.format(config.IP_ADDR))
    a.send('cat /proc/interrupts | grep enp1s0')

    #INTR1_AFTER = int(a.find_str('R-Car PCIe MSI   1').split()[1])
    INTR1_AFTER = int(a.find_str('PCIe MSI').split()[1])

    if (INTR1_AFTER > INTR1_BEFORE):
         print_result.func_pass(a)   
    else:
        print_result.func_fail(a)
