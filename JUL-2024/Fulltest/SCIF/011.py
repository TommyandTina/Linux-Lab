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

    if (scif.check_SH_SCI_DMA(a,'=n') == False):
        print_result.wrong_env(a)

    print('\n----------- BOARD ------------')
    sys.stdout.flush()

    a.send('stty -F /dev/ttySC0 115200 cs8 cstopb',0,False)

    if (a.send('ls') == False):
        print_result.func_fail(a)

    print_result.func_pass(a)

