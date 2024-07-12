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
SETTING='speed 38400 cs8 -cstopb'
S2RAM=True

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    restart_board.main(a)

    if (scif.check_SH_SCI_DMA(a,'=y') == False):
        print_result.wrong_env(a)

    if (scif.check_SCIF1(a,'hscif') == False):
        print_result.wrong_env(a)

    if (scif.send_data_host_to_board(a,SIZE,SETTING,S2RAM)==False):
        print_result.func_fail(a)

    print_result.func_pass(a) 
