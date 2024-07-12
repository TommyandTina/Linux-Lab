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
import unbind_bind
import dmae

DRIVER_PATH = dmae.DMA_DRIVER_PATH 
INTR = "{}.dma-controller".format(dmae.AUDIO_DMAC1_INTR)

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (unbind_bind.unbind(a,DRIVER_PATH,INTR) == False):
        print_result.func_fail(a)

    if (unbind_bind.bind(a,DRIVER_PATH,INTR) == False):
        print_result.func_fail(a)

    print_result.func_pass(a)

