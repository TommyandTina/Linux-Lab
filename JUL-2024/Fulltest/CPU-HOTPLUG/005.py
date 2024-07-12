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
import control_board
import print_result
import subprocess


FAILED=1
PASSED=0

RESULT=0


def pm_suspend(a):
    
    a.buff=""
          
    a.send('i2cset -f -y 7 0x30 0x20 0x0f')

    if (config.FEATBOX == True):
        print('\n')
        sys.stdout.flush()
        control_board.sw23_off()
    else:
        if (config.PLATFORM.find('salvator-x')!=-1):
            print ('\n\nSwitch SW23 off and input \'yes\' to continue:')
            sys.stdout.flush()
            sw23 = raw_input()
            while (sw23 != "yes"):
                print('Input \'yes\' to continue: ')
                sys.stdout.flush()
                sw23 = raw_input ()
 
    a.send('echo N > /sys/module/printk/parameters/console_suspend')

    a.buff="" 
    a.send('echo mem > /sys/power/state',0,False)
    
    TIMEOUT=0

    if (config.SOC != 'M3N'):
        while (a.buff.find('CPU{} killed'.format(config.NUM_CPU-1))==-1):
            sleep(0.5)
            TIMEOUT = TIMEOUT + 1
            if (TIMEOUT > 60):
                return(False)
        i=2
        while (i < config.NUM_CPU):
            if (a.buff.find('CPU{} killed'.format(i))==-1):
                return(False)
            i=i+1                               
    else:
         while (a.buff.find('Disabling non-boot CPUs')==-1):
            sleep(0.5)
            TIMEOUT = TIMEOUT + 1
            if (TIMEOUT > 60):
                return(False)


    sleep(2)
    
    return(True)
   

def pm_wakeup(a):
    
    a.buff=""
    if (config.FEATBOX == True):
        control_board.sw23_on()
    else:
        print ('\n Switch power switch: \n')
        sys.stdout.flush()
 
    TIMEOUT=0
    while (a.buff.find('PM: suspend exit'.format(config.NUM_CPU))==-1):
        sleep(0.5)
        TIMEOUT = TIMEOUT + 1
        if (TIMEOUT > 60):
            return(False)
  
    if (a.buff.find('failed to resume')!=-1):
        return(False)

    i=2

    if (config.SOC != 'M3N'):
        while (i < config.NUM_CPU):
           if (a.buff.find('CPU{} is up'.format(i))==-1):
                return(False)
           i=i+1  

    if (config.BOOT_NFS==True):
       while (a.buff.find('Link is Up')==-1):
           sleep(0.5)
           TIMEOUT = TIMEOUT + 1
           if (TIMEOUT > 60):
              return(False)
   
    sleep(0.5)  
    a.buff=""
    a.send("echo \"Wake up sucessfully\"")
    sleep(1)
    
    if (a.buff.find('Wake up sucessfully')==-1):
        return(False)
      
    return(True)   

  

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()

    a.buff=""
    a.send('echo 0 > /sys/devices/system/cpu/cpu1/online')
    sleep(0.5)
    if (a.buff.find('psci: CPU1 killed')==-1):
        print_result.func_fail(a)

    a.buff=""
    a.send('cat /proc/cpuinfo | grep processor')
    sleep(0.5)
    if (a.buff.find('processor       : 1')!=-1):
        print_result.func_fail(a)

    if (pm_suspend(a)==False):
        print_result.func_fail(a)

    if (pm_wakeup(a)==False):
        print_result.func_fail(a)

    a.buff=""
    a.send('cat /proc/cpuinfo | grep processor')
    sleep(0.5)
    if (a.buff.find('processor       : 1')!=-1):
        print_result.func_fail(a)

    a.send('echo 1 > /sys/devices/system/cpu/cpu1/online')
    sleep(0.5)

    a.buff=""
    a.send('cat /proc/cpuinfo | grep processor')
    sleep(0.5)

    if (a.buff.find('1')==-1):
        print_result.func_fail(a)

    print_result.func_pass(a)
    
                  
   

