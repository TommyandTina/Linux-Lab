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

INTR=dmae.SYS_DMAC1_INTR
CHANNEL=0
START=2
MAX=dmae.SYS_DMAC_CHANNEL_MAX

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('modprobe dmatest'.format(INTR))
 
    if (a.buff.find('modprobe: FATAL:')!=-1):
        print_result.func_fail(a)

    a.send('echo 32 > /sys/module/dmatest/parameters/iterations')
    a.send('echo 100000 > /sys/module/dmatest/parameters/timeout')
    a.send('echo {}.dma-controller > /sys/module/dmatest/parameters/device'.format(INTR))
    
    a.buff=""
    a.send('echo 1 > /sys/module/dmatest/parameters/run',0,False)
    sleep(1) 
    for i in range(START,MAX+1):
        if (a.buff.find('chan{}-copy0: summary 32 tests, 0 failures'.format(i))==-1) \
            and (a.buff.find('chan{}-copy: summary 32 tests, 0 failures'.format(i))==-1):
                a.send('rmmod dmatest',0,False)
                sleep(0.5)
                print_result.func_fail(a)

    a.send('rmmod dmatest')

    print_result.func_pass(a)
   
