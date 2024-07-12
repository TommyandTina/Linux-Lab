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


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('modprobe dmatest')
 
    if (a.buff.find('modprobe: FATAL:')!=-1):
        print_result.func_fail(a)

    a.send('echo 100000 > /sys/module/dmatest/parameters/timeout')
    a.send('echo 32 > /sys/module/dmatest/parameters/iterations')
    a.buff=""
    a.send('echo "" > /sys/module/dmatest/parameters/channel')


    CHANNEL_TEST = []      
    for line in a.buff.splitlines():
        if (line.find('dmatest: Added 1 threads using') != -1):
            TMP = line.split()
            TMP = TMP[len(TMP)-1]
            CHANNEL_TEST.append(TMP)

    a.buff=""
    a.send('echo 1 > /sys/module/dmatest/parameters/run',0,False)
    sleep(1.5) 
    for i in CHANNEL_TEST:
        if (a.buff.find('{}-copy0: summary 32 tests, 0 failures'.format(i))==-1) \
            and (a.buff.find('{}-copy: summary 32 tests, 0 failures'.format(i))==-1):
                a.send('rmmod dmatest',0,False)
                sleep(0.5)
                print_result.func_fail(a)

    a.send('rmmod dmatest')

    print_result.func_pass(a)
   
