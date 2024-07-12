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
import pcie


SIZE=350

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    os.system('mkdir -p /home/{}/test_pcie'.format(config.SER_USRNAME))

    pcie.check_pcie(a)
    #a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))
    #sleep(0.5)

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file-{}m bs=1M count={}'.format(SIZE,SIZE))
    a.buff="" 
    a.send('ftp -n {}'.format(config.SERVER_ADDR),0,False);
    a.wait('Connected')

    a.buff=""
    a.send('user {} {}'.format(config.SER_USRNAME,config.SER_PASS),0,True,1200,'ftp')
  
    if (a.buff.find('successful') == -1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)
    
    a.buff="" 
    a.send('put /tmp/file-{}m /home/{}/test_pcie/file-{}m'.format(SIZE,config.SER_USRNAME,SIZE),0,False,1200,'ftp')
    sleep(0.5)
    if (a.buff.find('PORT command successful')==-1):
       a.send('quit',0,False,60,'ftp')
       print_result.func_fail(a)
         
    sleep(1)
    a.send('\x03')
    sleep(2)
    if (a.buff.find('send aborted')==-1):
       a.send('quit',0,False,60,'ftp')
       print_result.func_fail(a)

    if (a.buff.find('Transfer complete')==-1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)
    
    a.buff=""  
    a.send('put /tmp/file-{}m /home/{}/test_pcie/file-{}m'.format(SIZE,config.SER_USRNAME,SIZE),0,True,1200,'ftp')
    sleep(0.5)
    if (a.buff.find('PORT command successful')==-1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)
        
    if (a.buff.find('Transfer complete')==-1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)

    a.send('quit',0,False,60,'ftp')
    a.wait('Goodbye')

    print_result.func_pass(a) 
  
