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
import gpio


INTR_BEFORE=['hp','0','0']
INTR_AFTER=['hp','0','0']

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
       
    a.buff=""
    a.send('cat /proc/interrupts | grep e6052000.gpio')
     
    try:
	INTR_BEFORE[1] = a.find_str('GIC-0').split()[1]
    except:
	INTR_BEFORE[1] = a.find_str('GICv2').split()[1]

    a.buff=""
    a.send('cat /proc/interrupts | grep e6800000.ethernet')

    INTR_BEFORE[2] = a.find_str('ethernet','grep').split()[1]
    
    print ('\n Pull out Ethernet cable:\n')
 
    for i in range (10,-1,-1):
        if (a.buff.find('ravb e6800000.ethernet eth0: Link is Down')!=-1):
            break
        print ('\033[F 00:00:{:02}'.format(i))
        sys.stdout.flush()
        sleep(1)
    
    print ('\n Insert Ethernet cable again: \n')

    for i in range (20,-1,-1):
        if (a.buff.find('ravb e6800000.ethernet eth0: Link is Up')!=-1):
            break
        print ('\033[F 00:00:{:02}'.format(i))
        sys.stdout.flush()
        sleep(1)
    
    a.buff=""
    a.send('cat /proc/interrupts | grep e6052000.gpio')

    try:
	INTR_AFTER[1] = a.find_str('GIC-0').split()[1]
    except:
	INTR_AFTER[1] = a.find_str('GICv2').split()[1]

    a.buff=""
    a.send('cat /proc/interrupts | grep e6800000.ethernet')

    INTR_AFTER[2] = a.find_str('ethernet','grep').split()[1]

    if (INTR_BEFORE[1] >= INTR_AFTER[1]) or (INTR_BEFORE[2] >= INTR_AFTER[2]):
        print_result.func_fail(a)

    print_result.func_pass(a)         
