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
    a.send('cat /proc/interrupts | grep e6053000.gpio')
    
    INTR_BEFORE[1] = int(a.find_str('Level').split()[1])
        
    a.buff=""
    a.send('cat /proc/interrupts | grep ee100000.mmc')

#    if (config.SOC != 'E3'):
#        INTR_BEFORE[2] = int(a.find_str('Edge').split()[1])
#    else:
#        INTR_BEFORE[2] = int(a.find_str('ee100000.mmc').split()[1])
    INTR_BEFORE[2] = int(a.find_str('Edge').split()[1])

    print ('\n Insert SD0 card:\n')
 
    for i in range (10,-1,-1):
        if (a.buff.find('card at address aaaa')!=-1):
            sleep(0.2)
            break
        print ('\033[F 00:00:{:02}'.format(i))
        sys.stdout.flush()
        sleep(1)

    a.buff=""
    a.send('cat /proc/interrupts | grep e6053000.gpio')

    INTR_AFTER[1] = int(a.find_str('Level').split()[1])

    a.buff=""
    a.send('cat /proc/interrupts | grep ee100000.mmc')

#    if (config.SOC != 'E3'):
#        INTR_AFTER[2] = int(a.find_str('Edge').split()[1])
#    else:
#        INTR_AFTER[2] = int(a.find_str('ee100000.mmc').split()[1])
    INTR_AFTER[2] = int(a.find_str('Edge').split()[1])

    if (INTR_BEFORE[1] >= INTR_AFTER[1]) or (INTR_BEFORE[2] >= INTR_AFTER[2]):
        print_result.func_fail(a)
 
    INTR_BEFORE[1] = INTR_AFTER[1]
    INTR_BEFORE[2] = INTR_AFTER[2]
   
    print ('\n Pull out SD0 card: \n')

    for i in range (10,-1,-1):
        if (a.buff.find('card aaaa removed')!=-1):
            break
        print ('\033[F 00:00:{:02}'.format(i))
        sys.stdout.flush()
        sleep(1)
   
    a.buff=""
    a.send('cat /proc/interrupts | grep e6053000.gpio')

    INTR_AFTER[1] = int(a.find_str('Level').split()[1])

    a.buff=""
    a.send('cat /proc/interrupts | grep ee100000.mmc')

#    if (config.SOC != 'E3'):
#        INTR_AFTER[2] = int(a.find_str('Edge').split()[1])
#    else:
#        INTR_AFTER[2] = int(a.find_str('ee100000.mmc').split()[1])

    INTR_AFTER[2] = int(a.find_str('Edge').split()[1])

    if (INTR_BEFORE[1] >= INTR_AFTER[1]) or (INTR_BEFORE[2] >= INTR_AFTER[2]):
        print_result.func_fail(a)

    print_result.func_pass(a)         



