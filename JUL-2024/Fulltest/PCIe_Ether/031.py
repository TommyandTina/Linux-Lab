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
import pcie

INTR_BEFORE=['hp','0','0']
INTR_AFTER=['hp','0','0']

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    #pcie.check_pcie(a)
    a.buff=""
    a.send('ifconfig enp1s0 up')
    a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))
    a.send('\n')    
    a.buff=""
    a.send('ping -c 20 {}'.format(config.SERVER_ADDR),0,False) 
    
    print ('\n Pull out and pull in Ethernet cable:\n')
    sys.stdout.flush()

    #a.wait('round-trip min/avg/max')
    #sleep(0.5)
  
   # if (a.buff.find('e1000e 0000:01:00.0 enp1s0: NIC Link is Down')!=-1) \
    #  or (a.buff.find('e1000e 0000:01:00.0 enp1s0: NIC Link is Up')!=-1):
     #   print_result.func_fail(a)
    if (a.buff.find('0% packet loss')!=-1):
        print_result.func_fail(a)
    a.wait('round-trip min/avg/max')
    sleep(0.5)

    a.buff=""
    a.send('ping -c 20 {}'.format(config.SERVER_ADDR))

    if (a.buff.find('100% packet loss')!=-1):
        print_result.func_fail(a)

    print_result.func_pass(a)         
