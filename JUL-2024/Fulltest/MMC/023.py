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
import subprocess


STRESS_TIME=3600

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    MOUNT_POINT=mmc.mountpoint(a)

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file bs=1M count=128')   

    a.buff=""
    a.send('mount /dev/{} /mnt'.format(MOUNT_POINT))
 
    if (a.buff.find('already mounted')!=-1):
        a.buff=""
        a.send('umount /dev/{}'.format(MOUNT_POINT))
        if (a.buff.find('umount: /mnt')!=-1):
            print_result.func_fail(a)

        a.buff=""
        a.send('mount /dev/{} /mnt'.format(MOUNT_POINT))

    if (a.buff.find('mounted filesystem')==-1):
        print_result.func_fail(a)
     
    a.send('stress --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(config.NUM_CPU,config.NUM_CPU*2,config.NUM_CPU,STRESS_TIME),0,False)
    
    TIME_OUT = 0 
    while (a.buff.find('successful run completed in')==-1):
        a.send('dd if=/tmp/file of=/mnt/128m.txt bs=4096 count=32768',0.02)
        sleep(10)
        if (a.buff.find('PANIC')!=-1) or (a.buff.find('WARNING')!=-1) \
	   or (a.buff.find('dd:')!=-1):
            print_result.func_fail(a)

        TIME_OUT = TIME_OUT + 10
        if (TIME_OUT > STRESS_TIME + 20): break
      

    a.buff=""
    a.send('umount /mnt')

    if (a.buff.find('umount: /mnt')!=-1):
       print_result.func_fail(a)
 
    print_result.func_pass(a) 
