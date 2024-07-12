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



if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
    a.buff=""
    
    a.send('dmesg | grep "PCIe.*link"') 
    a.buff=""
    a.send(' dmesg  | egrep "pci 0000|rcar-pci" | egrep "8086|reg"')
    
    if (a.buff.find('pci 0000:01:00.0: reg 0x10:')!=-1):
        print_result.func_pass(a)        
    else:
        print_result.func_fail(a)
                  
