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

CONFIG_VALUE = "speed 9600 cs8 -cstopb"

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    restart_board.main(a)   

    if (scif.check_SH_SCI_DMA(a,'=n') == False):
        print_result.wrong_env(a)

    if (scif.confirm_change_config_SC0(a,CONFIG_VALUE) == False):
        print_result.wrong_env(a)

    print_result.func_pass(a)

