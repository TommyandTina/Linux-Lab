#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import conserial
import print_result
import dmae

DMAC = dmae.AUDIO_DMAC1_INTR
CHANNEL_MAX = dmae.AUDIO_DMAC_CHANNEL_MAX

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (dmae.check_channel(a,DMAC,CHANNEL_MAX) == False):
        print_result.func_fail(a)

    print_result.func_pass(a)          
  
