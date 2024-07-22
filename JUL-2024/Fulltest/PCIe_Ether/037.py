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
        sys.stdout.flush()
        print_result.wrong_env(a)    
    pcie.check_pcie(a)
    a.send('ifconfig enp1s0 up')
    a.buff=""
    a.send('ifconfig enp1s0 1.0.0.1')

    if (a.buff.find('enp1s0: link is not ready')!=-1):
        a.wait('enp1s0: link becomes ready')

    a.buff=""
    a.send('ifconfig enp1s0')

    if (a.buff.find('inet addr:1.0.0.1')==-1):
        print_result.func_fail(a)

    a.send('ifconfig enp1s0 127.255.255.255')
   
    a.buff=""
    a.send('ifconfig enp1s0')

    if (a.buff.find('inet addr:127.255.255.255')==-1):
        print_result.func_fail(a)

    print_result.func_pass(a)

       
     
