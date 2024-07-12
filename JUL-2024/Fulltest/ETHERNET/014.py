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
import subprocess
import eth


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    os.system('mkdir -p /home/{}/test_ether'.format(config.SER_USRNAME))

     
    eth.check_eth(a)
    
    for SIZE in (1,50,350):
        a.buff=""
        a.send('dd if=/dev/urandom of=file-{}m bs=1M count={}'.format(SIZE,SIZE))
 
    a.buff=""
    a.send('ftp -n {}'.format(config.SERVER_ADDR),0,False)
    sleep(0.2)
    a.wait('Connected')

    a.buff=""
    a.send('user {} {}'.format(config.SER_USRNAME,config.SER_PASS),0,True,120,'ftp')
  
    if (a.buff.find('successful') == -1):
        a.send('quit',0,False,120,'ftp')
        print_result.func_fail(a)
    
    for SIZE in (1,50,350):
        a.buff="" 
        a.send('put file-{}m /home/{}/test_ether/file-{}m'.format(SIZE,config.SER_USRNAME,SIZE),0,True,1200,'ftp')
  
        if (a.buff.find('Transfer complete')==-1):
            print_result.func_fail(a)    

    sleep(1)
    a.send('quit',0,False,1200,'ftp')    
    sleep(0.5)

    print_result.func_pass(a) 
   
