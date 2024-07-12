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
  
    eth.check_eth(a)

    a.buff=""
    a.send('ethtool -s eth0 autoneg on speed 100 duplex full',0,False)

    sleep(2)

    if (a.buff.find('not setting')!=-1):
        print_result.func_fail(a)

    if (a.buff.find('Link is Down')!=-1):
        a.wait('Link is Up')

    a.buff=""
    a.send('ethtool eth0')

    if (a.buff.find('Speed: 100Mb/s')!=-1) and (a.buff.find('Duplex: Full')!=-1) \
      and (a.buff.find('Auto-negotiation: on')!=-1): 
        print_result.func_pass(a)   
    else:
        print_result.func_fail(a)
