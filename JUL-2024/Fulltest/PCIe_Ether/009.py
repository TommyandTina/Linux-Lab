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
   # a.buff=""
    #a.send('ifconfig enp1s0 up {}'.format(config.SERVER_ADDR))
    #a.send('ping -I enp1s0 -c 10 -s 100 {}'.format(config.IP_ADDR))
    #a.send('ping -I enp1s0 -c 10 -s 127 {}'.format(config.IP_ADDR))
    #a.send('ping -I enp1s0 -c 10 -s 1000 {}'.format(config.IP_ADDR))
    #a.send('ping -I enp1s0 -c 10 -s 15000 {}'.format(config.IP_ADDR))
    
 #  if (a.buff.find('ping: sendto: Network is unreachable')!=-1):
  #      return True
#
 #   if (a.buff.find('{} packets received, 0% packet loss'.format(time))!=-1):
  #      return False
    a.buff=""
   # a.send=('ifconfig enp1s0 up 192.168.10.14')
    #a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))
    pcie.ping_server_ip(a,config.SERVER_ADDR,1)
    pcie.ping_server_ip(a,config.SERVER_ADDR,100)
    pcie.ping_server_ip(a,config.SERVER_ADDR,127)
    pcie.ping_server_ip(a,config.SERVER_ADDR,1000)
    pcie.ping_server_ip(a,config.SERVER_ADDR,15000)
    
    #a.buff=""
   # if (a.buff.find('ping: sendto: Network is unreachable')!=-1):
    #    print_result.func_fail(a)

    if (a.buff.find('10 packets received, 0% packet loss')!=-1):
      #and (a.buff.find('127 packets received, 0% packet loss')!=-1) \
       # and (a.buff.find('1000 packets received, 0% packet loss')!=-1) \
        #  and (a.buff.find('15000 packets received, 0% packet loss')!=-1):

        print_result.func_pass(a)
    else:
        print_result.func_fail(a)   
    
