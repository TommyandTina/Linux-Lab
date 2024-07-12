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


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
  
    if (pcie.check_boot_from_nfs(a)==True):
        print ('\n\nTo confirm this test case, Rootfs must be booted from SD/USB... instead of NFS')
        print_result.wrong_env(a)

    #pcie.check_pcie(a)
    a.buff = ""
    a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))
    a.buff=""
    a.send('ifconfig enp1s0 up')
    a.wait('Link is Up', 10)
    a.buff=""
    a.send('ifconfig enp1s0')
    ##if (a.buff.find('enp1s0    Link encap:Ethernet  HWaddr {}'.format(config.IP_MAC))!=-1)
    a.wait('enp1s0    Link encap:Ethernet  HWaddr', 10)	
    a.buff=""
    a.send('ifconfig enp1s0 down')
    if (a.buff.find('Link is Down')==-1):
        print_result.func_fail(a)
    #a.wait('Link is Down')
    a.buff=""
    a.send('ifconfig')
    if (a.buff.find('enp1s0')!=-1):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)
