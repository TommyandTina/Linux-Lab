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

INTR1_UDP=0
INTR2_TCP=0
A=9

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
  
    pcie.check_pcie(a)
    #a.send('ifconfig enp1s0 up 192.168.10.14')
    a.send('ifconfig enp1s0 up 192.168.10.125')
    a.buff=""
    a.send('ethtool -s enp1s0 autoneg off')
    a.buff=""
    a.send('ethtool -s enp1s0 autoneg off speed 100 duplex half')

    #for i in (0,1,2,3,4,5,6,7,8,9):
    a.buff=""
    a.send('netperf -t UDP_STREAM -H 192.168.10.14')
    
    if (a.buff.find('establish_control could not establish the control connection')!=-1):
        print_result.func_fail(a)
    #INTR_UDP = int(a.find_str('Throughput').split()[4])
    #if (INTR_UDP < A):
    #    print_result.func_fail(a)
    #for i in (0,1,2,3,4,5,6,7,8,9):
        #if (a.buff.find('9{}'.format(i))==-1):
         #   print_result.func_fail(a) 
    a.buff=""
    a.send('netperf -t TCP_STREAM -H 192.168.10.14')
    #INTR1_TCP = int(a.find_str('').split()[4])
    #if (INTR1_TCP != A):
    #   print_result.func_fail(a)

    if (a.buff.find('establish_control could not establish the control connection')!=-1):
        print_result.func_fail(a)
    
   # if (a.buff.find < 90):
     #    print_result.func_fail(a)
    for i in (0,1,2,3,4,5,6,7,8,9):
        if (a.buff.find('9{}'.format(i))!=-1):
            print_result.func_fail(a)


    print_result.func_pass(a)
   
  
