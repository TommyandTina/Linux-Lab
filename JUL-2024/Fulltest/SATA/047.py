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
import sata


SIZE = 50

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1,sata.MODULE_TEST)
    a.start()
    a.buff=""
  
    a.send('mount tmpfs /tmp -t tmpfs -o size=1000M')
  
    for i in range (0,config.NUM_CPU):
        a.send('dd if=/dev/urandom of=/tmp/file{} bs=1M count={}'.format(i,SIZE))
    
    if (cp_device.mount_device(a,sata.mountpoint(a)) == False):
        print_result.func_fail(a)
   
    for i in range(0,config.NUM_CPU):
        if (i < config.NUM_CPU-1):
            a.send('taskset -c {} cp /tmp/file{} /mnt/ &'.format(i,i))
        else:
            a.send('taskset -c {} cp /tmp/file{} /mnt/'.format(i,i))

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

    for i in range(0,config.NUM_CPU):
          
        a.buff=""
        a.send('md5sum /tmp/file{} /mnt/file{}'.format(i,i))

        MD5SUM=a.buff.splitlines()
        MD5SUM_SRC = MD5SUM[len(MD5SUM)-2].split()[0]
        MD5SUM_DST = MD5SUM[len(MD5SUM)-3].split()[0]

        if (MD5SUM_SRC != MD5SUM_DST):
            print_result.func_fail(a)


    if (cp_device.umount_device(a) == False):
        print_result.func_fail(a)

    print_result.func_pass(a) 
