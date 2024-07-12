#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import cp_device
import re

                 
def mountpoint(a):
    a.buff=""
    a.send('find /sys/devices/platform/soc/ee140000.mmc/ -name mmcbl*p*')
    sleep(0.5)
  
    for line in a.buff.splitlines():
       if (re.search('mmcblk[0-9]p[0-9]',line)):
           return(line.split('/')[11]) 

def cp_ram_to_mmc(a,size,data="no_data"):
    
    return cp_device.cp_ram_to_device(a,mountpoint(a),size,data)

def cp_ram_to_mmc_umount_after_bind(a,size,data="no_data"):

    return cp_device.cp_ram_to_device_umount_after_bind(a,mountpoint(a),size,data)

def cp_mmc_to_ram(a,size):
 
    return cp_device.cp_device_to_ram(a,mountpoint(a),size)


def write_speed(a,expectation):

    return cp_device.write_speed(a,mountpoint(a),expectation)
      

def read_speed(a,expectation):

    return cp_device.read_speed(a,mountpoint(a),expectation)

def cp_s2ram(a,source,dest,size,while_cp=False):
    
    if (source == 'RAM'):
        return cp_device.cp_s2ram(a,'RAM',mountpoint(a),size,while_cp)
    else:
        return cp_device.cp_s2ram(a,mountpoint(a),'RAM',size,while_cp)

