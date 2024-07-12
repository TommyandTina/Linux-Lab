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

                 
def mountpoint(a,slot):
    a.buff=""
    tmp = slot.lower()    
    
    if (tmp == 'sd1'): 
        a.send('find /sys/devices/platform/soc/ee100000.mmc/ -name mmcbl*p*')
        sleep(0.5)
    elif (tmp == 'sd2'):
        a.send('find /sys/devices/platform/soc/ee160000.mmc/ -name mmcbl*p*')
        sleep(0.5)  
    else:
        return(None)
 
    for line in a.buff.splitlines():
       if (re.search('mmcblk[0-9]p[0-9]',line)):
           return(line.split('/')[11]) 

def cp_ram_to_sd(a,slot,size,data="no_data"):
    
    return cp_device.cp_ram_to_device(a,mountpoint(a,slot),size,data)

def cp_ram_to_sd_umount_after_bind(a,slot,size,data="no_data"):

    return cp_device.cp_ram_to_device_umount_after_bind(a,mountpoint(a,slot),size,data)

def cp_folder_to_sd(a,slot,stage,size,data="no_data"):

    return cp_device.cp_folder_to_device(a,mountpoint(a,slot),stage,size,data)

def cp_sd_to_ram(a,slot,size):
 
    return cp_device.cp_device_to_ram(a,mountpoint(a,slot),size)

def cp_folder_to_ram(a,slot,stage,size):

    return cp_device.cp_folder_to_ram(a,mountpoint(a,slot),stage,size)

def cp_no_space_left(a,slot):
    return cp_device.cp_no_space_left(a,mountpoint(a,slot))

def write_speed(a,slot,expectation):

    return cp_device.write_speed(a,mountpoint(a,slot),expectation)
      
def read_speed(a,slot,expectation):

    return cp_device.read_speed(a,mountpoint(a,slot),expectation) 

def cp_between_two_sd(a,slot1,slot2,size):
    
    return cp_device.cp_between_two_device(a,mountpoint(a,slot1),mountpoint(a,slot2),size)   

def cp_folder_between_two_sd(a,slot1,slot2,stage,size):
   
    return cp_device.cp_folder_between_two_device(a,mountpoint(a,slot1),mountpoint(a,slot2),stage,size)

def cp_RAM_to_two_sd_simultaneously(a,slot1,slot2,size):
     
    return cp_device.cp_RAM_to_two_device_simultaneously(a,mountpoint(a,slot1),mountpoint(a,slot2),size)

def cp_two_sd_to_RAM_simultaneously(a,slot1,slot2,size):
   
    return cp_device.cp_two_device_to_RAM_simultaneously(a,mountpoint(a,slot1),mountpoint(a,slot2),size)

def cp_between_two_simultaneously(a,slot1,slot2,size,time=1):
    if (slot1 != "RAM") and (slot2 != "RAM"):
        return cp_device.cp_between_two_simultanesouly(a,mountpoint(a,slot1),mountpoint(a,slot2),size,time)
    elif (slot1 == "RAM"):
        return cp_device.cp_between_two_simultanesouly(a,"RAM",mountpoint(a,slot2),size,time)
    else:
        return cp_device.cp_between_two_simultanesouly(a,mountpoint(a,slot1),"RAM",size,time)

def write_speed(a,slot,expectation): 
     
    return cp_device.write_speed(a,mountpoint(a,slot),expectation)

def read_speed(a,slot,expectation):
  
    return cp_device.read_speed(a,mountpoint(a,slot),expectation)       

def cp_s2ram(a,slot1,slot2,size,while_cp=False):
    if (slot1 != "RAM") and (slot2 != "RAM"):
        return cp_device.cp_s2ram(a,mountpoint(a,slot1),mountpoint(a,slot2),size,while_cp)
    elif (slot1 == "RAM"):
        return cp_device.cp_s2ram(a,"RAM",mountpoint(a,slot2),size,while_cp)
    else:
        return cp_device.cp_s2ram(a,mountpoint(a,slot1),"RAM",size,while_cp)

def cp_ram_to_device_interrupt(a,slot,size,command):

    return cp_device.cp_ram_to_device_interrupt(a,mountpoint(a,slot),size,command)

def pull_out_while_cp(a,source,dest,size):


    if (source != 'RAM') and (dest != 'RAM') :

        CHANNEL_PLUG_OUT = source

        MPOINT_SRC = mountpoint(a,source)
        MPOINT_DST = mountpoint(a,dest)
        if (MPOINT_SRC == None) or (MPOINT_DST == None):
            return False

        SRC_DIR='/mnt/de1'
        DST_DIR='/mnt/de2'

        a.send('mkdir -p {}'.format(SRC_DIR))
        a.send('mkdir -p {}'.format(DST_DIR))

        if (cp_device.mount_device(a,MPOINT_SRC,SRC_DIR)==False):
            return False

        if (cp_device.mount_device(a,MPOINT_DST,DST_DIR)==False):
            return False
    elif (source == 'RAM'):

        CHANNEL_PLUG_OUT = dest

        MPOINT_DST = mountpoint(a,dest)
        if (MPOINT_DST == None):
            return False

        SRC_DIR='/tmp'
        DST_DIR='/mnt'

        if (cp_device.mount_device(a,MPOINT_DST,DST_DIR)==False):
            return False
    else:

        CHANNEL_PLUG_OUT = source

        MPOINT_SRC = mountpoint(a,source)
        if (MPOINT_SRC == None):
            return False

        SRC_DIR='/mnt'
        DST_DIR='/tmp'

        if (cp_device.mount_device(a,MPOINT_SRC,SRC_DIR)==False):
            return False

    a.buff=""
    a.send('dd if=/dev/urandom of={}/file-{}M bs=1M count={}; sync'.format(SRC_DIR,size,size))

    a.buff=""
    a.send('cp {}/file-{}M {}'.format(SRC_DIR,size,DST_DIR),0,False)

    if (True != True):
        print('\nCurrently SD hot plug module is not supported')
        sys.stdout.flush()
        
    else:
        print('\nPlug out SD card immediately\n')
        sys.stdout.flush()
        sleep(5)

    if (a.buff.find('print_req_error: I/O error') == -1) and (a.buff.find('Buffer I/O error') == -1)\
       and (a.buff.find('JBD2: Error') == -1):
        return False

    sleep(1)
    a.send(' ',0,False)

    if ( True != True):
        #control_board.usb_in(CHANNEL_PLUG_OUT,'memory')
        print('\nCurrently SD hot plug module is not supported')
        sys.stdout.flush()
    else:
        print('\nPlug in SD card\n')
        sys.stdout.flush()

    if (a.wait('card at address aaaa',30) == False):
        return False

    sleep(2)
    a.send(' ',0,False)

    # Umount device
    if (source != 'RAM') and (dest != 'RAM') :
        if (cp_device.umount_device(a,SRC_DIR)==False):
            return False
        if (cp_device.umount_device(a,DST_DIR)==False):
            return False
    else:
        if (cp_device.umount_device(a)==False):
            return False
    
    # Mount device again
    if (source != 'RAM') and (dest != 'RAM') :
        MPOINT_SRC = mountpoint(a,source)
        if (cp_device.mount_device(a,MPOINT_SRC,SRC_DIR)==False):
            return False

    elif (source == 'RAM'):
        MPOINT_DST = mountpoint(a,dest)
        if (cp_device.mount_device(a,MPOINT_DST,DST_DIR)==False):
            return False

    else:
        MPOINT_SRC = mountpoint(a,source)
        if (cp_device.mount_device(a,MPOINT_SRC,SRC_DIR)==False):
            return False

    a.buff=""
    a.send('cp {}/file-{}M {}'.format(SRC_DIR,size,DST_DIR))

    a.buff=""
    a.send('md5sum {}/file-{}M {}/file-{}M'.format(SRC_DIR,size,DST_DIR,size))

    MD5SUM=a.buff.splitlines()
    MD5SUM_SRC = MD5SUM[len(MD5SUM)-2].split()[0]
    MD5SUM_DST = MD5SUM[len(MD5SUM)-3].split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    if (source != 'RAM') and (dest != 'RAM') :
        if (cp_device.umount_device(a,SRC_DIR)==False):
            return False
        if (cp_device.umount_device(a,DST_DIR)==False):
            return False
    else:
        if (cp_device.umount_device(a)==False):
            return False
