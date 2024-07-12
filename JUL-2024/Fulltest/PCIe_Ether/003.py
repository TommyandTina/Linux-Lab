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
    a.buff=""

    a.send('dmesg | grep e1000e')

    if (a.buff.find('e1000e: Intel(R) PRO/1000 Network Driver')!=-1) \
      and (a.buff.find('e1000e 0000:01:00.0 eth0: (PCI Express:2.5GT/s:Width x1)')!=-1) \
	and (a.buff.find('e1000e 0000:01:00.0 eth0: Intel(R) PRO/1000 Network Connection')!=-1) \
	    and (a.buff.find('e1000e 0000:01:00.0 eth0: MAC: 3, PHY: 8, PBA No:')!=-1):
	print_result.func_pass(a)
    else:
        print_result.func_fail(a)
    

