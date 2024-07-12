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

SIZE='1MB'
SETTING='speed 115200 cs8 cstopb'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    restart_board.main(a)

    print('\n\n---------- BOARD -----------')
    sys.stdout.flush()

    a.send('stty -F /dev/ttySC1 {}'.format(SETTING))

#    a.send('cat /dev/ttySC1',0,False)

    if (SIZE == '1MB'):
        START_STR=scif.START_STR_FILE_1MB
        END_STR=scif.END_STR_FILE_1MB
        FILE_ON_BOARD=scif.FILE_1MB_ON_BOARD
    elif (SIZE == '100KB'):
        START_STR=scif.START_STR_FILE_100KB
        END_STR=scif.END_STR_FILE_100KB
    elif(SIZE == '4MB'):
        START_STR=scif.START_STR_FILE_4MB
        END_STR=scif.END_STR_FILE_4MB

    a.send('taskset -c 0 cat /dev/ttySC1 > data_out1.txt & taskset -c 1 cat {} > /dev/ttySC1 &'.format(FILE_ON_BOARD),0,False)
    
    print('\n\n---------- HOST-PC -----------')

    print('\nstty -F {} {}'.format(config.SERIAL_PORT_SC1,SETTING))
    sys.stdout.flush()

    print('\ncat {} > data_out2.txt & cat file_{}.dat > {}'.format(config.SERIAL_PORT_SC1,SIZE,config.SERIAL_PORT_SC1))
    sys.stdout.flush()
   
    os.system('cat {} > data_out2.txt & cat file_{}.dat > {}'.format(config.SERIAL_PORT_SC1,SIZE,config.SERIAL_PORT_SC1)) 

    print('\n\n----------- BOARD ------------')
    sys.stdout.flush()

    while (True):
        a.buff = ""
        a.send('',0,False)
        finish = a.find_str("Done                    taskset -c 1")
        if (finish != None):
            break
        sleep(30)

    os.system('echo {} | sudo -S killall cat'.format(config.SER_PASS))
    
    if (a.send('echo Success') == False):
        print_result.func_fail(a)

    print_result.func_pass(a)
