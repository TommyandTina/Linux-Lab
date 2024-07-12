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
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    pcie.check_pcie(a)

    #a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))
    #sleep(0.5)

    a.buff=""

    a.send('ethtool -s enp1s0 autoneg on')
    a.send('ethtool -s enp1s0 autoneg on speed 10 duplex half')
    a.wait('e1000e 0000:01:00.0 enp1s0: NIC Link is Up 10 Mbps Half Duplex, Flow Control: None',10)

    a.buff=""
    a.send('ethtool enp1s0')

    if (a.buff.find('Speed: 10Mb/s')==-1) \
        or (a.buff.find('Duplex: Half')==-1) \
        or (a.buff.find('Auto-negotiation: on')==-1):
        print_result.func_fail(a)
    
    pcie.ping_addr(a)
        #print_result.func_fail(a) 

    print_result.func_pass(a)

 
    #if (pcie.ping_addr(a) == False):
    #    print_result.func_fail(a)
    #else:
    #    print_result.func_pass(a)


