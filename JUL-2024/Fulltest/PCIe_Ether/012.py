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
import pcie

TAMNGUYEN1=0
TAMNGUYEN2=0

TAMNGUYEN3=0
TAMNGUYEN4=0

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    os.system('mkdir -p /home/{}/test_pcie'.format(config.SER_USRNAME))
   # os.system('dd if=/dev/urandom of=/home/{}/test_pcie/random12.bin bs=1024 count=100K'.format(config.SER_USRNAME))

     
    pcie.check_pcie(a)
    #a.send('ifconfig enp1s0 up {}'.format(config.IP_ADDR))

    a.buff=""
    #a.send('dd if=/dev/urandom of=/tmp/random12.bin bs=1024 count=100K')
    a.send('ftp -n {}'.format(config.SERVER_ADDR),0,False)
    sleep(0.5)
    a.wait('Connected',20)

    a.buff=""
    a.send('user {} {}'.format(config.SER_USRNAME,config.SER_PASS),0,True,120,'ftp')
  
    if (a.buff.find('successful') == -1):
        a.send('quit',0,False,60,'ftp')
        print_result.func_fail(a)
    else:
        a.send('binary',0,True,1200,'ftp')
        a.send('get /home/{}/test_pcie/random12.bin /tmp/random12.bin'.format(config.SER_USRNAME),0,True,1200,'ftp')
        a.send('quit',0,False,60,'ftp')
        sleep(0.5)
        if (a.buff.find('Transfer complete')==-1):
            print_result.func_fail(a)    

       
    sleep(0.5)

    a.buff=""
    sleep(0.5)
    print('\nmd5sum /home/{}/test_pcie/random12.bin'.format(config.SER_USRNAME))
    a.buff=""
    sys.stdout.flush()
    os.system('md5sum /home/{}/test_pcie/random12.bin'.format(config.SER_USRNAME))
    
   # try:
   # TAMNGUYEN1 = int(a.find_str('/home/rvc/test_pcie/random.bin').split('/')[0])
    #except:
     # print_result.func_fail(a)

        #TAMNGUYEN2 = int(a.find_str('/home/rvc/test_pcie/file-1m').split()[9])
    a.buff=""
    a.send('md5sum /tmp/random12.bin')
    #try:
     #   TAMNGUYEN3 = int(a.find_str('/tmp/random.bin').split()[0])
    #except:
     #   print_result.func_fail(a)    
#TAMNGUYEN4 = int(a.find_str('/tmp/file-1m').split()[9])

   # if (TAMNGUYEN1 != TAMNGUYEN3):
    #    print_result.func_fail(a)

 #   if
    print_result.func_pass(a) 
   
