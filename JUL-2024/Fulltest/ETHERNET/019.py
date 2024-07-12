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
import eth


SIZE=350

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    print ('\n------- Prepare data on HOST-PC ------\n')
    
    print ('mkdir -p /home/{}/test_ether'.format(config.SER_USRNAME))
    sys.stdout.flush()

    os.system('mkdir -p /home/{}/test_ether'.format(config.SER_USRNAME))

    print ('\ndd if=/dev/urandom of=/home/{}/test_ether/file-{}m bs=1M count={}'.format(config.SER_USRNAME,SIZE,SIZE))
    sys.stdout.flush()

    os.system('dd if=/dev/urandom of=/home/{}/test_ether/file-{}m bs=1M count={}'.format(config.SER_USRNAME,SIZE,SIZE))
    
    print ('\n--------- BOARD --------\n')
    sys.stdout.flush()

    eth.check_eth(a)
    
    a.buff=""
    a.send('ftp -n {}'.format(config.SERVER_ADDR),0,False);
    a.wait('Connected')

    a.buff=""
    a.send('user {} {}'.format(config.SER_USRNAME,config.SER_PASS),0,True,1200,'ftp')
  
    if (a.buff.find('successful') == -1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)
    
    a.buff="" 
    a.send('get /home/{}/test_ether/file-{}m file-{}m'.format(config.SER_USRNAME,SIZE,SIZE),0,False,1200,'ftp')
    sleep(0.5)
    if (a.buff.find('PORT command successful')==-1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)
         
    sleep(1)
    a.send('\x03')
    sleep(2)
    if (a.buff.find('receive aborted')==-1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)

    if (a.buff.find('Transfer complete')==-1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)
    
    a.buff=""  
    a.send('get /home/{}/test_ether/file-{}m file-{}m'.format(config.SER_USRNAME,SIZE,SIZE),0,True,1200,'ftp')
    
    if (a.buff.find('PORT command successful')==-1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)

    if (a.buff.find('Transfer complete')==-1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)

    a.send('quit',0,False,1200,'ftp')    
    sleep(0.5)

    print_result.func_pass(a) 
   
