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
import restart_board
import scif


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    restart_board.main(a)

    print('\n----------- BOARD ------------')
    sys.stdout.flush()

    if (scif.check_SH_SCI_DMA(a,'=n') == False):
        print_result.wrong_env(a)
        
    a.send('cat /proc/tty/driver/sci')
    
    if (a.buff.find('fe:') != -1):
        print_result.func_fail(a)    

    a.send('stty -F /dev/ttySC0 speed 115200 evenp cs8 cstopb',0,False)

    #print('\n\n---------- HOST-PC -----------')
    #print('\nstty -F {} speed 115200 evenp cs8 cstopb'.format(config.SERIAL_PORT))
    #sys.stdout.flush()
    #os.system('stty -F {} speed 115200 evenp cs8 cstopb'.format(config.SERIAL_PORT))
   
    #print('\n----------- BOARD -----------')
    #sys.stdout.flush()
    #a.send('cat /dev/ttySC0',0,False)
    
    print('\n\n---------- HOST-PC -----------')
    print('echo "abcd" > {}'.format(config.SERIAL_PORT))
    sys.stdout.flush()

    print('\n----------- BOARD -----------')
    sys.stdout.flush()
     
    os.system('echo "abcd" > {}'.format(config.SERIAL_PORT))
    sleep(1)

    a.buff=""
    a.send('cat /proc/tty/driver/sci')
    if (a.buff.find('fe:') == -1):
        print_result.func_fail(a)

    print_result.func_pass(a)
