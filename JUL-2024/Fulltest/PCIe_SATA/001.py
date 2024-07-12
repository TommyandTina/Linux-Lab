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
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep "PCI.*link"')

    if (a.buff.find('rcar-pcie ee800000.pcie: PCIe link down')==-1):
      #or (a.buff.find('rcar-pcie fe000000.pcie: PCI host bridge to bus 0000:00')==-1) \
      #or (a.buff.find('rcar-pcie ee800000.pcie: PCIe link down')==-1):
        print_result.func_fail(a)       
    else:
        print_result.func_pass(a)
                  
