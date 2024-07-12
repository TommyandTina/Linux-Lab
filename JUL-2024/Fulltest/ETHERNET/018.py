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


INTR_BEFORE=['hp','0','0']
INTR_AFTER=['hp','0','0']

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
      
    a.send('\n')    
    a.buff=""
    a.send('ping -c 20 {}'.format(config.SERVER_ADDR),0,False) 
    
    print ('\n Pull out and pull in Ethernet cable:\n')
    sys.stdout.flush()

    a.wait('round-trip min/avg/max')
    sleep(0.5)
  
    if (a.buff.find('ravb e6800000.ethernet eth0: Link is Down')==-1) \
      and (a.buff.find('ravb e6800000.ethernet eth0: Link is Up')==-1):
        print_result.func_fail(a)

    a.buff=""
    a.send('ping -c 20 {}'.format(config.SERVER_ADDR))

    if (a.buff.find('100% packet loss')!=-1):
        print_result.func_fail(a)

    print_result.func_pass(a)         
