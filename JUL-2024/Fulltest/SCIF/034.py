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

STRING="sada"
SETTING='speed 57600 cs8 -cstopb'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    #b=conserial.serial_thread("/dev/ttyUSB1",0)
    b=conserial.serial_thread(config.SERIAL_PORT_SC1,1)
    #b.start()
    a.start()
    a.buff=""

    restart_board.main(a)

    if (scif.check_SH_SCI_DMA(a,'=y') == False):
        print_result.wrong_env(a)

    if (scif.check_SCIF1(a,'hscif') == False):
        print_result.wrong_env(a)

    if (scif.send_string_host_to_board(a,STRING,SETTING)==False):
        print_result.func_fail(a)

    print_result.func_pass(a) 