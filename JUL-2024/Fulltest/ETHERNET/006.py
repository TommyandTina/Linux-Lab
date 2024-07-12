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
import unbind_bind
import eth

DRIVER_PATH="ravb"
INTR="e6800000.ethernet"

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
 
    
    if (eth.check_boot_from_nfs(a)==True):
        print ('\n\nTo confirm this test case, Rootfs must be booted from SD/USB... instead of NFS')
        print_result.wrong_env(a)
 
    eth.check_eth(a)

    if (unbind_bind.unbind(a,DRIVER_PATH,INTR)==False):
        print_result.func_fail(a)

    if (unbind_bind.bind(a,DRIVER_PATH,INTR)==False):
        print_result.func_fail(a)   
     
    a.send('ifconfig eth0 {} netmask {}'.format(config.IP_ADDR,config.NET_MASK))
   
    a.send('route add default gw {} eth0'.format(config.DEFAULT_GW))
    a.wait('Link is Up')

 
    if (eth.ping(a,config.SERVER_ADDR,10) == False):
        print_result.func_fail(a)

    print_result.func_pass(a)       
  

    
