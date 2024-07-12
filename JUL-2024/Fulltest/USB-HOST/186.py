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
import cp_device
import print_result
import cp_text
import wait_process
import usb

SCRIPT = 'usb_smp_read_write_copy_one.sh'
CHANNEL = 'usb2ch1'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()
    a.buff=""

    MP = usb.mountpoint(a,CHANNEL)

    if (MP == None):
        print_result.func_fail(a)

    if (cp_device.mount_device(a,MP,'/mnt') == False):
        print_result.func_fail(a)
    
    a.buff=""

    if (cp_text.copy(a,os.path.abspath('./'),SCRIPT) == False):
        print_result.func_fail(a)

    a.send('chmod +x {}'.format(SCRIPT))

    
    FILE_SIZE = 0
    for i in range(0,config.NUM_CPU):
        FILE_SIZE = FILE_SIZE + 10
        a.buff=""
        a.send('taskset -c {} ./{} /tmp /mnt {} &> /dev/null &'.format(i,SCRIPT,FILE_SIZE),0,False)
        if (a.buff.find('taskset:') != -1):
            print_result.func_fail(a)

    if (wait_process.wait(a,'usb_smp',30) == False):
        print_result.func_fail(a)
   
    TOTAL_ERR = 0
    FILE_SIZE = 0
    for i in range(0,config.NUM_CPU):
        FILE_SIZE = FILE_SIZE + 10
        a.buff=""
        a.send('md5sum /tmp/file_{}mb /mnt/file_{}mb'.format(FILE_SIZE,FILE_SIZE))

        try:
            MD5_SRC = a.find_str('/tmp/file_{}mb'.format(FILE_SIZE),'md5sum').split()[0]
            MD5_DST = a.find_str('/mnt/file_{}mb'.format(FILE_SIZE),'md5sum').split()[0]

            if (MD5_SRC != MD5_DST):
                TOTAL_ERR = TOTAL_ERR + 1
        except:
            TOTAL_ERR = TOTAL_ERR + 1

        a.send('rm /tmp/file_{}mb; rm /mnt/file_{}mb'.format(FILE_SIZE,FILE_SIZE))
 
    if (cp_device.umount_device(a,'/mnt') == False):
        print_result.func_fail(a)  

    if (TOTAL_ERR > 0):
        print_result.func_fail(a)        
 
    print_result.func_pass(a)
