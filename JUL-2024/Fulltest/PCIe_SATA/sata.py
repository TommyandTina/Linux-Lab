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
import control_board
import s2ram
import re


SATA_INTERRUPT='ee300000.sata'
DRIVER_PATH='sata_rcar'

def workaround_SalXS(a):
   
    I2C_SET = ['i2cset -y -f 4 0x20 0x02 0x00','i2cset -y -f 4 0x20 0x03 0x7f','i2cset -y -f 4 0x20 0x01 0x7f']

    for i in I2C_SET:
        a.send(i)
 
    if (a.wait('Attached SCSI disk',20) == False):
        return False
   
    sleep(1.5)
    
    return True

def find_device(a):
    a.buff=""

    a.send('find /sys/devices/platform/soc/{}/ -name sd*'.format(SATA_INTERRUPT))

    for line in a.buff.splitlines():
       if (re.search('sd[a-z]',line)):
           return(line.split('/')[len(line.split('/'))-1])

def mountpoint(a):
    a.buff=""
    
    a.send('find /sys/devices/platform/soc/{}/ -name sd*'.format(SATA_INTERRUPT))
 
    for line in a.buff.splitlines():
       if (re.search('sd[a-z][0-9]',line)):
           return(line.split('/')[len(line.split('/'))-1])

    return None
     
def cp_ram_to_hd(a,size,data="no_data",time=1):
    return cp_device.cp_ram_to_device(a,mountpoint(a),size,data,time)

def cp_folder_to_hd(a,stage,size,data="no_data"):
    return cp_device.cp_folder_to_device(a,mountpoint(a),stage,size,data)

def cp_hd_to_ram(a,size,time=1):
    return cp_device.cp_device_to_ram(a,mountpoint(a),size,time)

def cp_folder_to_ram(a,stage,size):
    return cp_device.cp_folder_to_ram(a,mountpoint(a),stage,size) 

def write_speed(a,expectation):
    return cp_device.write_speed(a,mountpoint(a),expectation)

def read_speed(a,expectation):
    return cp_device.read_speed(a,mountpoint(a),expectation)

def cp_no_space_left(a):
    return cp_device.cp_no_space_left(a,mountpoint(a))

def cp_between_two_simultaneously(a,size,time=1):
    return cp_device.cp_between_two_simultanesouly(a,"RAM",mountpoint(a),size,time)

def cp_between_two_partition(a,mountpoint1,mountpoint2,size):
    return cp_device.cp_between_two_device_both_two_direct(a,mountpoint1,mountpoint2,size)

def cp_ram_to_device_interrupt(a,size,command):
    return cp_device.cp_ram_to_device_interrupt(a,mountpoint(a),size,command)
 
def cp_s2ram(a,source,dest,size,while_cp=False):

    if (source == None): return False
    if (dest == None): return False

    if (source == 'RAM'):
        
        DST_MP=mountpoint(a)
        if (DST_MP == None):
            return False

        SRC_DIR='/tmp'
        DST_DIR='/mnt'
 
        if (cp_device.mount_device(a,DST_MP,DST_DIR)==False):
            return False
    else:
        SRC_MP=mountpoint(a)
        if (SRC_MP == None):
            return False

        SRC_DIR='/mnt'
        DST_DIR='/tmp'

        if (cp_device.mount_device(a,SRC_MP,SRC_DIR)==False):
            return False

    a.buff=""
    a.send('dd if=/dev/urandom of={}/file-{}M bs=1M count={}'.format(SRC_DIR,size,size))

    a.send('sync')

    if (while_cp == False):
        a.send('cp {}/file-{}M {}/'.format(SRC_DIR,size,DST_DIR))
        if (s2ram.pm_suspend(a)==False):
            return False
    else:
        if (s2ram.pm_suspend_while_doing_st(a,'cp {}/file-{}M {}/ & sleep 1;'.format(SRC_DIR,size,DST_DIR))==False):
            return False

    if (s2ram.pm_wakeup(a,True)==False):
        return False

    if (source == 'RAM'):
        if (cp_device.umount_device(a,DST_DIR)==False):
            return False

        #if (workaround_SalXS(a)==False):
        #    return False
  
        DST_MP=mountpoint(a)
     
        if (cp_device.mount_device(a,DST_MP,DST_DIR)==False):
            return False

    elif (dest == 'RAM'):
        if (cp_device.umount_device(a,SRC_DIR)==False):
            return False

        #if (workaround_SalXS(a)==False):
        #    return False

        SRC_MP=mountpoint(a)

        if (cp_device.mount_device(a,SRC_MP,SRC_DIR)==False):
            return False

    a.buff=""
    a.send('md5sum {}/file-{}M {}/file-{}M'.format(SRC_DIR,size,DST_DIR,size))

    MD5SUM_SRC = a.find_str('{}/file-{}M'.format(SRC_DIR,size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('{}/file-{}M'.format(DST_DIR,size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    if (cp_device.umount_device(a)==False):
       return False

    return(True)


def pull_out_while_cp(a,source,dest,size):

    if (source == 'RAM'):

        CHANNEL_PLUG_OUT = dest        

        MPOINT_DST = mountpoint(a)
        if (MPOINT_DST == None):
            return False
 
        SRC_DIR='/tmp'
        DST_DIR='/mnt'

        if (cp_device.mount_device(a,MPOINT_DST,DST_DIR)==False):
            return False
    else:

        CHANNEL_PLUG_OUT = source 

        MPOINT_SRC = mountpoint(a)
        if (MPOINT_SRC == None):
            return False

        SRC_DIR='/mnt'
        DST_DIR='/tmp'

        if (cp_device.mount_device(a,MPOINT_SRC,SRC_DIR)==False):
            return False
 
    a.buff=""
    a.send('dd if=/dev/urandom of={}/file-{}M bs=1M count={}'.format(SRC_DIR,size,size))
          
    a.buff=""
    a.send('cp {}/file-{}M {}'.format(SRC_DIR,size,DST_DIR),0,False)

    print('\nPlug out HD disk immediately:\n')
    sys.stdout.flush()
    sleep(3)

    if (a.buff.find('SATA link down') == -1):
        return False
    
    sleep(2)
    a.send(' ',0,False)
 
    print('\nPlug in HD disk:\n')
    sys.stdout.flush()    

    if (a.wait('SATA link up',20) == False):
        return False

    sleep(1)
    a.send(' ',0,False)
 
    if (source == 'RAM'):
        TMP_MPOINT_DST = MPOINT_DST
        MPOINT_DST = mountpoint(a)
        
        if (MPOINT_DST != TMP_MPOINT_DST):
            cp_device.umount_device(a)
            if (cp_device.mount_device(a,MPOINT_DST,DST_DIR)==False):
                return False

    else:
        TMP_MPOINT_SRC = MPOINT_SRC
        MPOINT_SRC = mountpoint(a)
        
        if (MPOINT_SRC != TMP_MPOINT_SRC):
            cp_device.umount_device(a)
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
   
    if (cp_device.umount_device(a)==False):
       return False
   
    return True 
