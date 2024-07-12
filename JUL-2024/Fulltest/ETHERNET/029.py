#!/usr/bin/python
import serial
import threading
from time import sleep
from time import time
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import conserial
import print_result
import cp_text
import eth


SCRIPT = 'ftp_put_board_to_pc_data.sh'
STRESS_TIME = 3600
SIZE = 100

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    a.buff=""

    cp_text.copy(a,os.path.abspath('./'),SCRIPT)
    a.send('chmod +x {}'.format(SCRIPT))

    a.send('sed -i \'s/$IPSERVER/{}/\' {}'.format(config.SERVER_ADDR,SCRIPT))
    a.send('sed -i \'s/PCNAME="rvc"/PCNAME="{}"/\' {}'.format(config.SER_USRNAME,SCRIPT))
    a.send('sed -i \'s/PCPASSWORD="rvc"/PCPASSWORD="{}"/\' {}'.format(config.SER_PASS,SCRIPT))
    a.send('sed -i \'s/PC_FOLDER="\/home\/rvc\/test_ether"/PC_FOLDER="\/home\/{}\/test_ether"/\' {}'.format(config.SER_USRNAME,SCRIPT))
 
    a.buff=""
    a.send('stress --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(config.NUM_CPU,config.NUM_CPU*2,config.NUM_CPU,STRESS_TIME),0,False)   
  
    START = time()

    ERR = False

    while (time() - START < STRESS_TIME):
        a.send('./ftp_put_board_to_pc_data.sh {}'.format(SIZE))
  
    a.wait('successful run completed')

    a.send('rm {}'.format(SCRIPT))
 
    if (a.buff.find('TEST_NG')!=-1):
        print_result.func_fail(a)

    print_result.func_pass(a)
