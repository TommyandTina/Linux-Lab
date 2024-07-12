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
import sdhi


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    MOUNT_POINT=sdhi.mountpoint(a,'sd1')
     
    if (MOUNT_POINT == None):
       print ('\n\nPlease insert SD card into SD0')
       print_result.func_fail(a)

    a.send('yes | mkfs.ext3 /dev/{}'.format(MOUNT_POINT))
    
    if (a.buff.find('does not exist and no size was specified')!=-1):
       print_result.func_fail(a)

    a.send('mount /dev/{} /mnt'.format(MOUNT_POINT))
    sleep(0.5)

    if (a.buff.find('mounted filesystem')==-1):
       print_result.func_fail(a)

    a.buff=""
    a.send('rm -rf /mnt/*')

    a.buff=""
    a.send('cp -r /core-image-weston-salvator-x.tar /mnt')

    a.buff=""
    a.send('ls /mnt')

    a.buff=""
    a.send('tar -xf /mnt/core-image-weston-salvator-x.tar -C /mnt/')

    a.buff=""
    a.send('cp /Image /mnt/boot; cp /r8a77951-salvator-xs.dtb /mnt/boot')

    a.buff=""
    a.send('chmod 755 /mnt; chmod 755 /mnt/boot; chmod 755 /mnt/boot/*')

    a.buff=""
    a.send('ls /mnt/boot/')

    if (a.buff.find('Image')==-1) or (a.buff.find('r8a77951-salvator-xs.dtb')==-1):
       print_result.func_fail(a)

    a.buff=""
    a.send('umount /mnt/')

    if (a.buff.find('umount:')!=-1):
       print_result.func_fail(a)

    print_result.func_pass(a)
