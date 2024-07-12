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
import cp_device
import sdhi


CARD_SLOT1 = 'sd1'
CARD_SLOT2 = 'sd2'

MP1 = '/mnt/sd1'
MP2 = '/mnt/sd2'

SIZE = 50

NUM_TS = 4

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
 
    a.send('mkdir -p {}; mkdir -p {}'.format(MP1,MP2))
 
    a.send('mount tmpfs /tmp -t tmpfs -o size=1000M')
  
    for i in range (0,NUM_TS):
        a.send('dd if=/dev/urandom of=/tmp/file{} bs=1M count={}'.format(i,SIZE))
    
    if (cp_device.mount_device(a,sdhi.mountpoint(a,CARD_SLOT1),MP1) == False):
        print_result.func_fail(a)
   
    if (cp_device.mount_device(a,sdhi.mountpoint(a,CARD_SLOT2),MP2) == False):
        print_result.func_fail(a)
   
    for i in range(0,NUM_TS):
        if (i % 2 == 0):
            if (i == NUM_TS - 1):
                a.send('taskset -c 0 cp /tmp/file{} {}'.format(i,MP1))
            else:
                a.send('taskset -c 0 cp /tmp/file{} {} &'.format(i,MP1))
        else:
            if (i == NUM_TS - 1):
                a.send('taskset -c 0 cp /tmp/file{} {}'.format(i,MP2))
            else:
                a.send('taskset -c 0 cp /tmp/file{} {} &'.format(i,MP2))


    TIME_OUT=0

    while (TIME_OUT < 40):
        a.buff=""
        a.send('ps -a')

        if (a.buff.find('cp')!=-1):
            TIME_OUT = TIME_OUT + 1
            sleep(5)
        else:
            break

    sleep(1)
       
    for i in range(0,NUM_TS): 
        a.buff=""  
        if (i % 2 == 0): 
             a.send('md5sum /tmp/file{} {}/file{}'.format(i,MP1,i))
        else:
             a.send('md5sum /tmp/file{} {}/file{}'.format(i,MP2,i))

        MD5SUM=a.buff.splitlines()
        MD5SUM_SRC = MD5SUM[len(MD5SUM)-2].split()[0]
        MD5SUM_DST = MD5SUM[len(MD5SUM)-3].split()[0]

        if (MD5SUM_SRC != MD5SUM_DST):
            print_result.func_fail(a)


    if (cp_device.umount_device(a,MP1) == False):
        print_result.func_fail(a)
   
    if (cp_device.umount_device(a,MP2) == False):
        print_result.func_fail(a)

    a.send('rm -rf {}; rm -rf {}'.format(MP1,MP2))

    print_result.func_pass(a) 
