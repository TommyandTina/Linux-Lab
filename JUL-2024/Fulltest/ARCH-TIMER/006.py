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
import s2ram
import print_result
import subprocess


INTR_BEFORE=0
INTR_AFTER=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    if (s2ram.pm_suspend(a)==False):
        print_result.func_fail(a)

    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
    
    a.buff=""          
    a.send('grep arch_timer /proc/interrupts')
 
    INTR_BEFORE=a.find_str('arch_timer','grep arch_timer').split()[1]
    
    a.buff=""
    a.send('date; sleep 5; date',0.05)
 
 
    a.buff=""
    a.send('grep arch_timer /proc/interrupts')
 
    INTR_AFTER=a.find_str('arch_timer','grep arch_timer').split()[1]
    
    if (int(INTR_BEFORE) < int(INTR_AFTER)):
        print_result.func_pass(a)
    else:
        print_result.func_fail(a)
    print_result.func_pass(a)
 