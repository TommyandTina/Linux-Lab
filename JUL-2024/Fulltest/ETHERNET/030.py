#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import re
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import conserial
import print_result
import eth


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
  
    # Check ethernet device on HOST-PC
    os.system('ifconfig -a > /tmp/check_device.log')
    try:
        with open('/tmp/check_device.log','r') as test_log:
            lines = test_log.readlines()
    except:
        print('Cannot open file to detect ethernet device on Host-PC')
        sys.stdout.flush()
        print_result.wrong_env(a)

    ETH_INTERFACE = None
    for line in lines:
        if (line.find('{}'.format(config.SERVER_ADDR)) != -1):
            ETH_INTERFACE = pre_line.split()[0]
            break
        pre_line = line
    if (ETH_INTERFACE == None):
        print('Cannot detect ethernet interface on Host-PC which is defined IP={} in config.py file'.format(config.SERVER_ADDR))
        sys.stdout.flush()
        print_result.wrong_env(a)                  
           
    print ('\n--------- BOARD ---------- \n')
    eth.check_eth(a)

    a.buff=""
    
    a.send('ip address show eth0')

    for line in a.buff.splitlines():
       if (re.search('link/ether',line)):
           MAC_ADDR = (line.split()[1])
           break

    a.buff=""
    a.send('ethtool -s eth0 wol g')
    if (a.buff.find('ethtool:')!=-1):
        print_result.func_fail(a)    

    a.send('echo s2idle > /sys/power/mem_sleep')

    a.buff=""
    a.send('echo mem > /sys/power/state',0,False)

    TIME_OUT = 0
    while (a.buff.find('Freezing remaining freezable tasks')==-1):
        sleep(1)
        TIME_OUT = TIME_OUT + 1
        if (TIME_OUT > 60):
            print_result.func_fail(a)
  
    sleep(3)

    a.buff=""  
    os.system('echo {} | sudo -S etherwake -i {} {}'.format(config.SER_PASS,ETH_INTERFACE,MAC_ADDR))

    TIME_OUT=0   
    while(a.buff.find('PM: suspend exit')==-1):
        sleep(1)
        TIME_OUT = TIME_OUT + 1
        if (TIME_OUT > 60):
            print ('\n-------------- HOST-PC --------------\n')
            print ('sudo etherwake -i {} {}'.format(ETH_INTERFACE,MAC_ADDR))
            print_result.func_fail(a)
     
    TIME_OUT=0
    while (a.buff.find('Link is Up')==-1):
        sleep(1)
        TIME_OUT = TIME_OUT + 1
        if (TIME_OUT > 60):
            print_result.func_fail(a)
      
    sleep(0.5)
    a.buff=""
    a.send('echo \"Wake up successfully\"')
    sleep(0.5)
    
    if (a.buff.find('Wake up successfully')==-1):
        print_result.func_fail(a)

    print ('\n -------------- HOST-PC --------------\n')
    print ('sudo etherwake -i eth0 {}'.format(MAC_ADDR))

    print_result.func_pass(a)
    
     
