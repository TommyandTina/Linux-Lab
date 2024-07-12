#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config


PC_FOLDER="/home/{}/test_ether".format(config.SER_USRNAME)
                 
def check_eth(a):
    a.buff=""  
    a.send('ifconfig | grep eth')

    if (a.buff.find('Link encap:Ethernet')==-1):
        a.buff=""
        a.send('ifconfig eth0 {}'.format(config.IP_ADDR))
        if (a.buff.find('SIOCSIFADDR: No such device')!=-1):
            return False
        else:
            a.wait("Link is Up")
    return True

def check_boot_from_nfs(a):
    a.buff=""
    a.send('cat /proc/cmdline')

    if (a.buff.find('root=/dev/nfs')!=-1):
        return True
    else:
        return False

def ping(a,IP,time):

    a.buff=""
    a.send('ping -c {} {}'.format(time,IP))
    
    if (a.buff.find('ping: sendto: Network is unreachable')!=-1):
        return False
  
    if (a.buff.find('{} packets received, 0% packet loss'.format(time))!=-1):
        return True
    else:
        return False    


