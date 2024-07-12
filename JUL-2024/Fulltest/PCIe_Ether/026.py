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

    print ('\n------- BOARD -------\n')


    pcie.check_pcie(a)
    a.send('ethtool -s enp1s0 autoneg off speed 100 duplex full')
    a.wait('Link is Up',30)
    a.send('ethtool enp1s0')
    a.buff=""
    a.send('iperf -s -u',0,False)
   

    print ('\n\n------- HOST-PC --------') 
    for i in (10,20,30,100,1000,2000):
        if (i==10): 
            os.system('echo \" \" > log.txt; echo \"iperf -c {} -u -b {}M\" >> log.txt; '.format(config.IP_ADDR,i))
        else:       
            os.system('echo \" \" >> log.txt; echo \"iperf -c {} -u -b {}M\" >> log.txt;'.format(config.IP_ADDR,i)) 

        os.system('iperf -c {} -u -b {}M >> log.txt 2>&1'.format(config.IP_ADDR,i))

        if (a.buff.find('100 %') != -1):
            a.send('\x03')
            print_result.func_fail(a)

    sleep(2) 
    a.send('\x03')
    sleep(0.5)
  
    print ('\n------- BOARD -------\n')
    a.buff=""; 
    a.send('iperf -s',0,False)
  
    print ('\n\n------- HOST-PC --------')
    os.system('echo \" \" >> log.txt; echo \"iperf c {}\" >> log.txt ;iperf -c {} >> log.txt'.format(config.IP_ADDR,config.IP_ADDR))
    sleep(0.25)
   
    a.send('\x03');   

    os.system('cat log.txt; rm log.txt')

    if (a.buff.find('connected with') == -1):
        print_result.func_fail(a)

    print_result.func_pass(a)
   
