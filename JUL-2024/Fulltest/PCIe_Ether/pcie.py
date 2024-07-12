#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config


PC_FOLDER="/home/{}/test_pcie".format(config.SER_USRNAME)
	                 
def check_pcie(a):
    a.buff=""  
    a.send('ifconfig | grep enp1s0')

    if (a.buff.find('Link encap:Ethernet')==-1):
        a.buff = ""
        a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR)) 
        a.buff=""
        a.send('ifconfig enp1s0 up')
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

def ping_server_ip(a,IP,time):

    a.buff=""
    #a.send('ifconfig enp1s0 up {}'.format(config.SERVER_ADDR))
    a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))

    a.send('ping -I enp1s0 -c 10 -s {} {}'.format(time,IP))
    
    if (a.buff.find('ping: sendto: Network is unreachable')!=-1):
        return False
  
    if (a.buff.find('{} packets received, 0% packet loss'.format(time))!=-1):
        return True
    else:
        return False

def ping_ip(a,IP,time):

    a.buff=""
    #a.send('ifconfig enp1s0 up {}'.format(config.SERVER_ADDR))
   # a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))

    a.send('ping -c 10 -s {} {}'.format(time,IP))

    if (a.buff.find('ping: sendto: Network is unreachable')!=-1):
        return False

    if (a.buff.find('{} packets received, 0% packet loss'.format(time))!=-1):
        return True
    else:
        return False

    
def ping_ip_addr(a,IP,time):

    a.buff=""
    #a.send('ifconfig enp1s0 up {}'.format(SERVER_IP))
   # a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))

    a.send('ping -I enp1s0 -c 10 {}'.format(IP))

    if (a.buff.find('ping: sendto: Network is unreachable')!=-1):
        return False

    if (a.buff.find('{} packets received, 0% packet loss'.format(time))!=-1):
        return True
    else:
        return False


def check_mask(a):
    a.buff=""
    a.send('ifconfig enp1s0 up {}'.format(config.NET_MASK))
    if (a.buff.find('SIOCSIFADDR: No such device')!=-1):
       return False
    else:
       return True
   
def ping_addr(a):
    a.buff=""
   # a.send('ifconfig enp1s0 up {}'.format(config.SERVER_ADDR))
    a.send('ping -I enp1s0 -c 10 {}'.format(config.SERVER_ADDR))
    if (a.buff.find('ping: sendto: Network is unreachable')!=-1):
        return False

    if (a.buff.find('10 packets transmitted, 10 packets received, 0% packet loss')!=-1):
        return True
    else:
        return False




