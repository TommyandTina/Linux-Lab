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
  
    pcie.check_pcie(a)
    #a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))
    #a.send('ethtool -s enp1s0 autoneg off')
    a.send('ethtool -s enp1s0 autoneg off speed 100 duplex full')
    a.wait('Link is Up',30)
    a.send('ethtool enp1s0')
    a.buff=""
    print ('\n------- HOST-PC -------\n')  
    print ('iperf -s -u')

    os.system('iperf -s -u &')  
    sleep(1)

    print ('\n------- BOARD --------')

    for i in (10,20,30,100,1000,2000):
        a.buff=""
        a.send('iperf -c {} -u -b {}M'.format(config.SERVER_ADDR,i))
        if (a.buff.find('100%')!=-1):
            os.system('killall iperf')
            print_result.func_fail(a)

   
    print ('\n\n------- HOST-PC -------\n')
    print ('iperf -s')
    os.system('iperf -s &')
    sleep(2)
   
    print ('\n------- BOARD --------')
    a.buff=""
    a.send('iperf -c {}'.format(config.SERVER_ADDR))
    
    if (a.buff.find('connected with')==-1):
        print_result.func_fail(a)

    os.system('killall iperf')
 
    print_result.func_pass(a)
   
  