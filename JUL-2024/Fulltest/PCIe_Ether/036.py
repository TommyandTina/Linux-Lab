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

    print ('\n------- Prepare data on HOST-PC ------\n')
       
    print ('mkdir -p /home/{}/test_pcie'.format(config.SER_USRNAME))
    sys.stdout.flush()

    os.system('mkdir -p /home/{}/test_pcie'.format(config.SER_USRNAME))

    print ('\ndd if=/dev/urandom of=/home/{}/test_pcie/file-{}m bs=1M count={}'.format(config.SER_USRNAME,SIZE,SIZE))
    sys.stdout.flush()

    os.system('dd if=/dev/urandom of=/home/{}/test_pcie/file-{}m bs=1M count={}'.format(config.SER_USRNAME,SIZE,SIZE))
    
    print ('\n--------- BOARD --------\n')
    sys.stdout.flush()

    pcie.check_pcie(a)
   
    a.buff="" 
    a.send('ftp -n {}'.format(config.SERVER_ADDR),0,False);
    a.wait('Connected')

    a.buff=""
    a.send('user {} {}'.format(config.SER_USRNAME,config.SER_PASS),0,True,1200,'ftp')
  
    if (a.buff.find('successful') == -1):
        a.send('quit')
        print_result.func_fail(a)
    
    a.buff="" 
    a.send('get /home/{}/test_pcie/file-{}m file-{}m'.format(config.SER_USRNAME,SIZE,SIZE),0,False,1200,'ftp')
    sleep(0.5)
    if (a.buff.find('PORT command successful')==-1):
       a.send('quit',0,False,120,'ftp')
       print_result.func_fail(a)
         
    sleep(1)
    a.send('\x1A')
    sleep(2)

    if (a.buff.find('Stopped(SIGTSTP)        ftp -n')==-1):
       a.send('quit',0,False,120,'ftp')
       print_result.func_fail(a)
    
    a.send('fg')
    sleep(0.5)
    
    TIME_OUT=0
    while (a.buff.find('Transfer complete')==-1):
        sleep(1)
        TIME_OUT = TIME_OUT + 1
        if (TIME_OUT > 120):
            a.send('quit',0,False,120,'ftp')
            print_result.func_fail(a)    

    a.send('quit',0,False,1200,'ftp')    

    print_result.func_pass(a) 
   
