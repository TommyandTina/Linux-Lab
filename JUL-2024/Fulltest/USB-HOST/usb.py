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
import re

MODULE_TEST="USB_HOST"

if (config.SOC.find('E3')!=-1):
    USB2_CH1_INTERRUPT='ee080100.usb'
else:
    USB2_CH1_INTERRUPT='ee0a0100.usb'

if (config.SOC.find('H3')!=-1):
    USB2_CH2_INTERRUPT='ee0c0100.usb'
elif (config.SOC.find('M3N')!=-1):
    USB2_CH2_INTERRUPT='ee080100.usb'
elif (config.SOC.find('M3')!=-1):
    USB2_CH2_INTERRUPT='ee080100.usb'
elif (config.SOC.find('E3')!=-1):
    USB2_CH2_INTERRUPT='None'

USB3_INTERRUPT='ee000000.usb'
                 
def list_usb_partition(a,channel):
    if (channel == 'usb2ch1'): 
        a.send('find /sys/devices/platform/soc/{}/ -name sd*'.format(USB2_CH1_INTERRUPT),0.005)
        return True
    elif (channel == 'usb2ch2'):
        a.send('find /sys/devices/platform/soc/{}/ -name sd*'.format(USB2_CH2_INTERRUPT),0.005)
        return True
    elif (channel == 'usb3'):
        a.send('find /sys/devices/platform/soc/{}/ -name sd*'.format(USB3_INTERRUPT),0.005)
        return True
    else:
        return False

def mountpoint(a,channel):
    a.buff=""
    channel = channel.lower()    
    
    if not list_usb_partition(a, channel):
        return None 
    for line in a.buff.splitlines():
        if (re.search('sd[a-z][0-9]',line)):
            return(line.split('/')[len(line.split('/'))-1])
    device = None
    for line in a.buff.splitlines():
        if (re.search('sd[a-z]',line)):
            device = line.split('/')[len(line.split('/'))-1]
    
    if (device != None):
        a.send('(echo n; echo p; echo 1; echo 2048; echo "+5G"; echo t; echo 83; echo w) | fdisk /dev/{}'.format(device))
        a.send('echo y | mkfs.ext3 /dev/{}1'.format(device))
        print ("\n \n Device is formatted")
        
        a.buff=""
        if not list_usb_partition(a, channel):
            return None 
        for line in a.buff.splitlines():
            if (re.search('sd[a-z][0-9]',line)):
                return(line.split('/')[len(line.split('/'))-1])
    else:
    #   print ("\n \n Device not found")
        return None 
        
    a.buff=""
    a.send(' ',0,False)
    sleep(1)

    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in(channel,'memory')
    else:
        return None

    if (a.wait('Attached SCSI removable disk',30) == False):
        return None

    a.buff=""
    if not list_usb_partition(a, channel):
        return None 
    for line in a.buff.splitlines():
        if (re.search('sd[a-z][0-9]',line)):
            return(line.split('/')[len(line.split('/'))-1])

    return None
     
def mountpoint_usb_hub(a,channel):
    a.buff=""
    if (channel == 'usb2ch1'): 
        a.send('find /sys/devices/platform/soc/{}/ -name product -print0 | xargs -0 grep "2.0 [Hh][uU][bB]"'.format(USB2_CH1_INTERRUPT))
    elif (channel == 'usb2ch2'):
        a.send('find /sys/devices/platform/soc/{}/ -name product -print0 | xargs -0 grep "2.0 [Hh][uU][bB]"'.format(USB2_CH2_INTERRUPT))    
    elif (channel == 'usb3'):
        a.send('find /sys/devices/platform/soc/{}/ -name product -print0 | xargs -0 grep "[Hh][uU][bB]"'.format(USB3_INTERRUPT))
    else:
        return None

    for line in a.buff.splitlines():
        if (re.search('/product',line) and re.search("[Hh][uU][bB]",line)):
            return mountpoint(a,channel)
    
    sys.stdout.flush()
    return None

def mountpoint_usb_hdd(a,channel):
    a.buff=""
    if (channel == 'usb2ch1'): 
        a.send('find /sys/devices/platform/soc/{}/ -name product -print0 | xargs -0 grep "Portable"'.format(USB2_CH1_INTERRUPT))
    elif (channel == 'usb2ch2'):
        a.send('find /sys/devices/platform/soc/{}/ -name product -print0 | xargs -0 grep "Portable"'.format(USB2_CH2_INTERRUPT))    
    elif (channel == 'usb3'):
        a.send('find /sys/devices/platform/soc/{}/ -name product -print0 | xargs -0 grep "Portable"'.format(USB3_INTERRUPT))
    else:
        return None

    for line in a.buff.splitlines():
        if (re.search('/product',line) and re.search('Portable SSD',line)):
            return mountpoint(a,channel)

    sys.stdout.flush()
    return None
    
def cp_ram_to_usb(a,channel,size,data="no_data"):
    return cp_device.cp_ram_to_device(a,mountpoint(a,channel),size,data)

def cp_folder_to_usb(a,channel,stage,size,data="no_data"):
    return cp_device.cp_folder_to_device(a,mountpoint(a,channel),stage,size,data)

def cp_usb_to_ram(a,channel,size):
    return cp_device.cp_device_to_ram(a,mountpoint(a,channel),size)

def cp_folder_to_ram(a,channel,stage,size):
    return cp_device.cp_folder_to_ram(a,mountpoint(a,channel),stage,size)

def cp_between_two_usb(a,channel1,channel2,size):    
    return cp_device.cp_between_two_device(a,mountpoint(a,channel1),mountpoint(a,channel2),size)

def cp_folder_between_two_usb(a,channel1,channel2,stage,size):   
    return cp_device.cp_folder_between_two_device(a,mountpoint(a,channel1),mountpoint(a,channel2),stage,size)

def cp_between_two_simultaneously(a,channel1,channel2,size,time=1):
    if (channel1 != "RAM") and (channel2 != "RAM"):
        return cp_device.cp_between_two_simultanesouly(a,mountpoint(a,channel1),mountpoint(a,channel2),size,time)
    elif (channel1 == "RAM"):
        return cp_device.cp_between_two_simultanesouly(a,"RAM",mountpoint(a,channel2),size,time)
    else:
        return cp_device.cp_between_two_simultanesouly(a,mountpoint(a,channel1),"RAM",size,time)
    
def cp_between_three_simultaneously(a,channel1,channel2,channel3,size):
    if (channel1 == "RAM"):
        return cp_device.cp_RAM_to_two_device_simultaneously(a,mountpoint(a,channel2),mountpoint(a,channel3),size)
    
    elif (channel3 == "RAM"):
        return cp_device.cp_two_device_to_RAM_simultaneously(a,mountpoint(a,channel1),mountpoint(a,channel2),size)
    
    else:
        print("run simultaneously between three device is not avaiable now")
        return False       
         
def write_speed(a,channel,expectation):
    return cp_device.write_speed(a,mountpoint(a,channel),expectation)

def read_speed(a,channel,expectation):
    return cp_device.read_speed(a,mountpoint(a,channel),expectation)

def cp_no_space_left(a,channel):
    return cp_device.cp_no_space_left(a,mountpoint(a,channel))

def cp_s2ram(a,source,dest,size,while_cp=False,umount_aft_s2ram=False,two_direction=True):
    if (source != "RAM") and (dest != "RAM"):
        return cp_device.cp_s2ram(a,mountpoint(a,source),mountpoint(a,dest),size,while_cp,umount_aft_s2ram,two_direction)
    elif (source == "RAM"):
        return cp_device.cp_s2ram(a,"RAM",mountpoint(a,dest),size,while_cp,umount_aft_s2ram,two_direction)
    else:
        return cp_device.cp_s2ram(a,mountpoint(a,source),"RAM",size,while_cp,umount_aft_s2ram,two_direction)

##USB_hub functions
def cp_ram_to_usb_hub(a,channel,size,data="no_data"):
    return cp_device.cp_ram_to_device(a,mountpoint_usb_hub(a,channel),size,data)

def write_speed_usb_hub(a,channel,expectation):
    return cp_device.write_speed(a,mountpoint_usb_hub(a,channel),expectation)

def read_speed_usb_hub(a,channel,expectation):
    return cp_device.read_speed(a,mountpoint_usb_hub(a,channel),expectation)

def cp_between_usb_hub2_usb3(a,channel1,channel2,size):  
    if (channel1 == "usb2ch1") or (channel1 == "usb2ch2"):
        return cp_device.cp_between_two_device(a,mountpoint_usb_hub(a,channel1),mountpoint(a,channel2),size)
    if (channel2 == "usb2ch1") or (channel2 == "usb2ch2"):
        return cp_device.cp_between_two_device(a,mountpoint(a,channel1),mountpoint_usb_hub(a,channel2),size)
    
##USB_hdd functions
def cp_ram_to_usb_hdd(a,channel,size,data="no_data"):
    return cp_device.cp_ram_to_device(a,mountpoint_usb_hdd(a,channel),size,data)

def cp_ram_folder_to_usb_hdd(a,channel,stage,size,data="no_data"):
    return cp_device.cp_folder_to_device(a,mountpoint_usb_hdd(a,channel),stage,size,data)

def cp_usb_hdd_to_ram(a,channel,size):
    return cp_device.cp_device_to_ram(a,mountpoint_usb_hdd(a,channel),size)

def cp_usb_hdd_folder_to_ram(a,channel,stage,size):
    return cp_device.cp_folder_to_ram(a,mountpoint_usb_hdd(a,channel),stage,size)

def cp_usb_hdd_no_space_left(a,channel):
    return cp_device.cp_no_space_left(a,mountpoint_usb_hdd(a,channel))

def cp_between_usb_hdd_usb3(a,channel1,channel2,size):  
    if (channel1 == "usb2ch1") or (channel1 == "usb2ch2"):
        return cp_device.cp_between_two_device(a,mountpoint_usb_hdd(a,channel1),mountpoint(a,channel2),size)
    if (channel2 == "usb2ch1") or (channel2 == "usb2ch2"):
        return cp_device.cp_between_two_device(a,mountpoint(a,channel1),mountpoint_usb_hdd(a,channel2),size)
    
##pull_out_while_cp
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

    if (config.FEATBOX_USB_MODULE == True):
        sleep(0.5)
        control_board.usb_out(CHANNEL_PLUG_OUT,'memory')
    else:
        print('\nPlug out usb immediately!\n')
        sys.stdout.flush()
        sleep(4)

    if (a.buff.find('error') == -1):
        return False
    
    sleep(2)
    a.send(' ',0,False)
 
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in(CHANNEL_PLUG_OUT,'memory') 
    else:
        print('\nPlug in usb!\n')
        sys.stdout.flush()    

    if (a.wait('Attached SCSI removable disk',30) == False):
        return False

    sleep(1)
    a.send(' ',0,False)
 
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
   
    cp_device.umount_device(a)
      
