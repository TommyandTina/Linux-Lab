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

    a.buff=""
    a.send('dd if=/dev/urandom of=./file-{}m bs=1M count={}'.format(SIZE,SIZE))

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
    a.send('put file-{}m /home/{}/test_ether/file-{}m'.format(SIZE,config.SER_USRNAME,SIZE),0,False,1200,'ftp')
    
    if (a.buff.find('PORT command successful')==-1):
       a.send('quit',0,False,60,'ftp')
       print_result.func_fail(a)
         
    sleep(1)
    a.send('\x1A')
    sleep(2)

    if (a.buff.find('Stopped(SIGTSTP)        ftp -n')==-1):
       print_result.func_fail(a)
    
    a.send('fg',0,False)
    sleep(0.5)
    
    TIME_OUT=0
    while (a.buff.find('Transfer complete')==-1):
        sleep(1)
        TIME_OUT = TIME_OUT + 1
        if (TIME_OUT > 120):
            a.send('quit',0,False,60,'ftp')
            print_result.func_fail(a)    

    sleep(1)
    a.send('quit',0,False,1200,'ftp')    
    sleep(0.5)

    print_result.func_pass(a) 
   
