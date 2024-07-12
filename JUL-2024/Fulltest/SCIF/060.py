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

SIZE='4MB'
SETTING='speed 9600 cs8 -cstopb'
STRESS_TIME=3600

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    restart_board.main(a)

    if (scif.check_SH_SCI_DMA(a,'=y') == False):
        print_result.wrong_env(a)

    if (scif.check_SCIF1(a,'scif') == False):
        print_result.func_fail(a)

    a.send('stress --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(config.NUM_CPU,config.NUM_CPU*2,config.NUM_CPU,STRESS_TIME),0,False)

    if (scif.send_data_host_to_board(a,SIZE,SETTING,False,True)==False):
        print_result.func_fail(a)

    if (a.wait('successful run completed',7500) == False):
        print_result.func_fail(a)

    print_result.func_pass(a) 
