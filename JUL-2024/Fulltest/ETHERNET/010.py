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
    a.send('ethtool -s eth0 msglvl 0xffffffff')

    if (a.buff.find('not setting')!=-1):
        print_result.func_fail(a)

    if (a.buff.find('Link is Down')!=-1):
        a.wait('Link is Up')

    a.buff=""
    a.send('ethtool eth0')

    if (a.buff.find('Current message level: 0xffffffff')==-1):
        print_result.func_fail(a)

    a.buff=""
    a.send('ethtool -s eth0 msglvl 0x000000cc')

    if (a.buff.find('not setting')!=-1):
        print_result.func_fail(a)

    if (a.buff.find('Link is Down')!=-1):
        a.wait('Link is Up')

    a.buff=""
    a.send('ethtool eth0')

    if (a.buff.find('Current message level: 0x000000cc')==-1): 
        print_result.func_fail(a)   

    print_result.func_pass(a)
