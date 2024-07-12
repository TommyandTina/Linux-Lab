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
    a.send('ifconfig enp1s0 224.0.0.0')
    sleep(0.5)

    if (a.buff.find('enp1s0: link is not ready')!=-1):
        a.wait('enp1s0: link becomes ready')

    if (a.buff.find('SIOCSIFADDR: Invalid argument')==-1):
        print_result_func.fail(a)

    a.buff=""
    a.send('ifconfig enp1s0 239.255.255.255')
    sleep(0.5)

    #if (a.buff.find('SIOCSIFADDR: Invalid argument')==-1):
     #   print_result.func_fail(a)
    #a.buff=""
    #a.send('ifconfig')
    #sleep(0.5)

    if (a.buff.find('SIOCSIFADDR: Invalid argument')==-1):
        print_result.func_fail(a)

    print_result.func_pass(a)

       
     

