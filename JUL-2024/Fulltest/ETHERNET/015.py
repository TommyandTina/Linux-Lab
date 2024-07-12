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
import eth


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
 
    if (eth.check_boot_from_nfs(a)==True):
        print ('\n\nTo confirm this test case, Rootfs must be booted from SD/USB... instead of NFS')
        print_result.wrong_env(a)
 
    eth.check_eth(a)

    if (eth.ping(a,config.SERVER_ADDR,10) == False):
        print_result.func_fail(a)

    a.buff=""
    a.send('ifconfig eth0 down')

    if (eth.ping(a,config.SERVER_ADDR,10) == True):
        print_result.func_fail(a)

    a.buff=""
    a.send('ifconfig eth0 up')
    a.wait('Link is Up')

    a.send('ifconfig eth0 {} netmask {}'.format(config.IP_ADDR,config.NET_MASK))

    a.send('route add default gw {}'.format(config.DEFAULT_GW))

    if (eth.ping(a,config.SERVER_ADDR,10) == False):
        print_result.func_fail(a)

    print_result.func_pass(a)
    
   

    

