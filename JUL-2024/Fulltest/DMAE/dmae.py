#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config

                
AUDIO_DMAC0_INTR = "ec700000"
AUDIO_DMAC1_INTR = "ec720000"
AUDIO_DMAC_CHANNEL_MAX = 15

SYS_DMAC0_INTR = "e6700000"
SYS_DMAC1_INTR = "e7300000"
SYS_DMAC2_INTR = "e7310000"
SYS_DMAC_CHANNEL_MAX = 15

USB_DMAC0_INTR = "e65a0000"
USB_DMAC1_INTR = "e65b0000"
USB_DMAC_CHANNEL_MAX = 1

DMA_DRIVER_PATH='rcar-dmac'
USB_DMAC_DRIVER_PATH='usb-dmac'

def check_channel(a,intr,channel_max):

    a.buff=""
    
    a.send('ls -la /sys/class/dma/ | grep {}'.format(intr))

    ALL_CHAN = a.buff.splitlines()

    for i in ALL_CHAN:
        if (i.find('chan') != -1):
                CHAN = i.split()[8].split('chan')[0]

                for j in range(0,channel_max+1):    
                    if (a.buff.find('{}chan{}'.format(CHAN,j)) == -1):
                        return False
                
                return True

    return False 
