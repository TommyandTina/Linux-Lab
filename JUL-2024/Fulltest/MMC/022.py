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
import mmc
import re



if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
          
    MOUNT_POINT=mmc.mountpoint(a)

    if (MOUNT_POINT == None):
        print_result.func_fail(a)

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file bs=1M count=128')
    
    a.wait('MB/s')

    a.send('mount /dev/{} /mnt'.format(MOUNT_POINT))
    
    if (a.buff.find('already mounted')!=-1):
        a.buff=""
        a.send('umount /dev/{}'.format(MOUNT_POINT))
        
        if (a.buff.find('umount:')!=-1):
            print_result.func_fail(a)

        a.send('mount /dev/{} /mnt'.format(MOUNT_POINT))
   
    if (a.buff.find('mounted filesystem')==-1):
        print_result.func_fail(a)

    a.buff=""
    
    for i in range(0,config.NUM_CPU):   
        a.send('taskset -c {} dd if=/tmp/file of=/mnt/f128m.cpu{}.txt bs=4096 conv=fdatasync &'.format(i,i))
    
    TIME_OUT=0
 
    while (TIME_OUT < 40):
        a.buff=""
        a.send('ps -a')
 
        if (a.buff.find('dd')!=-1):
            TIME_OUT = TIME_OUT + 1
            sleep(5)
        else:
            break

    a.buff="" 
    a.send('md5sum /tmp/file')
    
    MD5SUM_SRC=a.buff.splitlines()[2].split()[0]
 
    for i in range(0,config.NUM_CPU):
        a.buff=""
        a.send('md5sum /mnt/f128m.cpu{}.txt'.format(i)) 
         
        MD5SUM_DEST=a.buff.splitlines()[2].split()[0]
       
        if (MD5SUM_DEST != MD5SUM_SRC):
            print_result.func_fail(a)
       
    a.buff=""
    a.send('umount /mnt')

    if (a.buff.find('umount: /mnt')!=-1):
       print_result.func_fail(a)

    print_result.func_pass(a) 
     
  
