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
import time

MODULE_TEST = "USB2H_FULLTEST"

if (config.SOC.find('H3')!=-1):
    #CN10 LOW
    USB2_CH1_INTERRUPT='ee0a0100.usb'
    #CN10 HIGH
    USB2_CH2_INTERRUPT='ee0c0100.usb'
    #CN37
    USB2_CH3_INTERRUPT='ee0e0100.usb'
    #CN9
    USB2_CH4_INTERRUPT='ee080100.usb'
    CN_LIST = ["CN10L", "CN10H", "CN37", "CN9"]
    USB2H_LIST = [USB2_CH1_INTERRUPT, USB2_CH2_INTERRUPT, USB2_CH3_INTERRUPT, USB2_CH4_INTERRUPT]
    csv_file = "h3_Ver30_infotainment_v02_195.csv"
elif (config.SOC.find('M3N')!=-1):
    #CN10 LOW
    USB2_CH1_INTERRUPT='ee0a0100.usb'
    #CN9
    USB2_CH2_INTERRUPT='ee080100.usb'
    CN_LIST = ["CN10L", "CN10H", "CN37", "CN9"]
    USB2H_LIST = [USB2_CH1_INTERRUPT, None, None, USB2_CH2_INTERRUPT]
    csv_file = "m3n_Ver1x_infotainment_hd_v04_195.csv"

elif (config.SOC.find('M3')!=-1):
    #CN10 LOW
    USB2_CH1_INTERRUPT='ee0a0100.usb'
    #CN9
    USB2_CH2_INTERRUPT='ee080100.usb'
    CN_LIST = ["CN10L", "CN10H", "CN37", "CN9"]
    USB2H_LIST = [USB2_CH1_INTERRUPT, None, None, USB2_CH2_INTERRUPT]
    csv_file = "m3_Ver30_infotainment_v01_195.csv"

elif (config.SOC.find('E3')!=-1):
    USB2_CH1_INTERRUPT='ee080100.usb'
    CN_LIST = ["CN10L", "CN10H", "CN37", "CN9"]
    USB2H_LIST = [None, None, None, USB2_CH1_INTERRUPT]
    csv_file = "e3_Ver1x_meter_video_and_map_v02_390.csv"

    
def list_usb2h_partition(a,channel):
    a.send("find /sys/devices/platform/soc/{}/ -name 'sd*'".format(channel),0.005)
    return True

def mountpoint_usb2h(a,channel):
    a.buff=""
    channel = channel.lower()    
    
    if not list_usb2h_partition(a, channel):
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
        if not list_usb2h_partition(a, channel):
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

def wait_usb2h(a, channel, insert=False):
    if insert:
        while (a.buff.find("Attached SCSI removable disk") == -1):
            sleep(0.1)
        time.sleep(1)
    mountpoint = mountpoint_usb2h(a, channel)
    if mountpoint == None:
        print_result.func_fail(a)
    return mountpoint

def wait_usb2h_hub(a, channel, insert=False):
    if insert:
        while (a.buff.find("Attached SCSI removable disk") == -1):
            sleep(0.1)
        time.sleep(1)
    mountpoint = mountpoint_usb2h(a, channel)
    if mountpoint == None:
        print_result.func_fail(a)
    return mountpoint

def prepare_testdata(a, mountpoint, SIZE_FILE):
    print("\n----------Prepare----------\n")
    sys.stdout.flush()
    
    a.send("dd if=/dev/urandom of=testdata bs=10M count={}".format(SIZE_FILE))
    a.send("mkdir -p /mnt/usb")
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("cp testdata /mnt/usb/")
    a.send("umount /mnt/usb")

def prepare_testdata_multi(a, mountpoint_list, SIZE_FILE):
    print("\n----------Prepare----------\n")
    sys.stdout.flush()
    
    a.send("dd if=/dev/urandom of=testdata bs=10M count={}".format(SIZE_FILE))
    for i in range(0, len(mountpoint_list)):
        mountpoint = mountpoint_list[i]
        a.send("mkdir -p /mnt/usb{}".format(i))
        a.send("mount /dev/{} /mnt/usb{}".format(mountpoint, i))
        a.send("cp testdata /mnt/usb{}/".format(i))
        a.send("umount /mnt/usb{}".format(i))

def wait_usb2h_all(a, channel, insert=False):
    if insert:
        while (a.buff.find("Attached SCSI removable disk") == -1):
            sleep(0.1)
        time.sleep(1)
    mountpoint = mountpoint_usb2h_all(a, channel)
    if mountpoint == None:
        print_result.func_fail(a)
    return mountpoint

def mountpoint_usb2h_all(a,channel):
    a.buff=""
    channel = channel.lower()    
    
    if not list_usb2h_partition_all(a, channel):
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
        if not list_usb2h_partition_all(a, channel):
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

def list_usb2h_partition_all(a,channel):
    a.send("find /sys/devices/platform/soc/ -name 'sd*'",0.005)
    return True

def load_qos(a):
    a.send("insmod qos.ko")
    a.send("qos_tp setall {}".format(csv_file))
    a.send("qos_tp switch")
    
