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



def unbind(a,driver_path,intr):

    a.send('cd /sys/bus/platform/drivers/{}'.format(driver_path))
   
    a.buff = ""
    a.send('ls -d {}'.format(intr))
  
    if (a.buff.find('ls: cannot access \'{}\': No such file or directory'.format(intr)) != -1):
        return False

    a.buff = ""
    a.send('echo {} > unbind'.format(intr),0,False)
  
    sleep(4)

    a.buff = ""
    a.send('ls -d {}'.format(intr))

    if (a.buff.find('ls: cannot access \'{}\': No such file or directory'.format(intr)) == -1):
        return False

    a.buff = ""
    a.send('cd ~')

    return True


def bind(a,driver_path,intr):

    a.send('cd /sys/bus/platform/drivers/{}'.format(driver_path))

    a.buff = ""
    a.send('echo {} > bind '.format(intr),0,False)
 
    sleep(4)

    a.buff = ""
    a.send('ls -l')

    a.buff = ""
    a.send('cd ~')

    return True

    
                  
   
