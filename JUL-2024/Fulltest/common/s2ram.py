#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import control_board
import subprocess


def pm_suspend(a):
   
    a.buff=""
    if (config.SOC == 'E3'):
        a.send('i2cset -f -y 8 0x30 0x20 0x0f', 0.01)
    else:
        a.send('i2cset -f -y 7 0x30 0x20 0x0f', 0.01)

    if (a.buff.find('Error:')!=-1) or (a.buff.find('i2cset:')!=-1):
        return False         
 
    TIMEOUT=0
    while (a.buff.find('root@{}'.format(config.PLATFORM))==-1):
        sleep(0.5)
        TIMEOUT = TIMEOUT + 1
        if (TIMEOUT > 60):
            return(False)

    if (config.FEATBOX == True):
	sleep(0.5)
        print('\n')
        sys.stdout.flush()
        control_board.sw23_off()
    else:
        print ('\n\nSwitch SW23 off and input \'yes\' to continue:')
        sys.stdout.flush()
        sw23 = raw_input()
        while (sw23 != "yes"):
            print('Input \'yes\' to continue: ')
            sys.stdout.flush()            
            sw23 = raw_input ()

    a.send('echo N > /sys/module/printk/parameters/console_suspend', 0.01)

    a.buff="" 
    a.send('echo mem > /sys/power/state', 0.01,False)
    
    TIMEOUT=0
    while (a.buff.find('CPU{} killed'.format(config.NUM_CPU-1))==-1):
        sleep(0.5)
        TIMEOUT = TIMEOUT + 1
        if (TIMEOUT > 360):
            return(False)
	if (a.buff.find('failed to suspend')!=-1):
            return False

    i=1
    while (i < config.NUM_CPU):
        if (a.buff.find('CPU{} killed'.format(i))==-1):
            return(False)
        i=i+1                               
    
    sleep(2)
    
    return(True)
 
def pm_suspend_while_doing_st(a,command):

    if (config.SOC == 'E3'):
        a.send('i2cset -f -y 8 0x30 0x20 0x0f', 0.01)
    else:
        a.send('i2cset -f -y 7 0x30 0x20 0x0f', 0.01)
    if (a.buff.find('Error:')!=-1) or (a.buff.find('i2cset:')!=-1):
        return False

    TIMEOUT=0
    while (a.buff.find('root@{}'.format(config.PLATFORM))==-1):
        sleep(0.5)
        TIMEOUT = TIMEOUT + 1
        if (TIMEOUT > 60):
            return(False)

    if (config.FEATBOX == True):
        control_board.sw23_off()
    else:
        print ('\n\nSwitch SW23 off and input \'yes\' to continue:')
        sys.stdout.flush()
        sw23 = raw_input()
        while (sw23 != "yes"):
            print('Input \'yes\' to continue: ')
            sys.stdout.flush()
            sw23 = raw_input ()

    a.send('echo N > /sys/module/printk/parameters/console_suspend', 0.01)

    a.buff=""
    a.send('{} echo mem > /sys/power/state'.format(command,sleep),0.01,False)

    TIMEOUT=0
    while (a.buff.find('CPU{} killed'.format(config.NUM_CPU-1))==-1):
        sleep(0.5)
        TIMEOUT = TIMEOUT + 1
        if (TIMEOUT > 360):
            return(False)
        if (a.buff.find('failed to suspend')!=-1):
            return False

    i=1
    while (i < config.NUM_CPU):
        if (a.buff.find('CPU{} killed'.format(i))==-1):
            return(False)
        i=i+1

    sleep(2)

    return(True)

def pm_suspend_while_doing_st_multi(a,command_list):

    if (config.SOC == 'E3'):
        a.send('i2cset -f -y 8 0x30 0x20 0x0f', 0.01)
    else:
        a.send('i2cset -f -y 7 0x30 0x20 0x0f', 0.01)
    if (a.buff.find('Error:')!=-1) or (a.buff.find('i2cset:')!=-1):
        return False

    TIMEOUT=0
    while (a.buff.find('root@{}'.format(config.PLATFORM))==-1):
        sleep(0.5)
        TIMEOUT = TIMEOUT + 1
        if (TIMEOUT > 60):
            return(False)

    if (config.FEATBOX == True):
        control_board.sw23_off()
    else:
        print ('\n\nSwitch SW23 off and input \'yes\' to continue:')
        sys.stdout.flush()
        sw23 = raw_input()
        while (sw23 != "yes"):
            print('Input \'yes\' to continue: ')
            sys.stdout.flush()
            sw23 = raw_input ()

    a.send('echo N > /sys/module/printk/parameters/console_suspend', 0.01)

    a.buff=""
    for command in command_list:
        a.send(command)
        
    a.send('echo mem > /sys/power/state',0.01,False)

    TIMEOUT=0
    while (a.buff.find('CPU{} killed'.format(config.NUM_CPU-1))==-1):
        sleep(0.5)
        TIMEOUT = TIMEOUT + 1
        if (TIMEOUT > 360):
            return(False)
        if (a.buff.find('failed to suspend')!=-1):
            return False

    i=1
    while (i < config.NUM_CPU):
        if (a.buff.find('CPU{} killed'.format(i))==-1):
            return(False)
        i=i+1

    sleep(2)

    return(True)



def pm_wakeup(a,ignore_error=True):
   
    a.buff=""
 
    if (config.FEATBOX == True):
        control_board.sw23_on()
    else:
        print ('\n Switch power switch: \n')
        sys.stdout.flush()

    TIMEOUT=0
    while (a.buff.find('PM: suspend exit'.format(config.NUM_CPU-1))==-1):
        sleep(0.5)
        TIMEOUT = TIMEOUT + 1
        if (TIMEOUT > 60):
            return(False)
  
    if (a.buff.find('failed to resume')!=-1):
        return(False)

    i=1
    while (i < config.NUM_CPU):
       if (a.buff.find('CPU{} is up'.format(i))==-1):
            return(False)
       i=i+1 

    if (ignore_error == False):
        if (a.buff.find('error')!=-1):
            return(False) 

    if (config.BOOT_NFS==True):
       while (a.buff.find('Link is Up')==-1):
           sleep(0.5)
           TIMEOUT = TIMEOUT + 1
           if (TIMEOUT > 60):
              return(False)
       sleep(2)
   
    sleep(2)  
    a.buff=""
    a.send("echo \"Wake up sucessfully\"", 0.01)
    sleep(1)
    
    if (a.buff.find('Wake up sucessfully')==-1):
        return(False)
      
    return(True)   

  

    
                  
   
