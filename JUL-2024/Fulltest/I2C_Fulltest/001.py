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
import s2ram
import print_result
import subprocess
import restart_board
import time

STRESS_TIME = 1800

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()

    restart_board.main(a)

    a.buff=""
    
    if config.PLATFORM == "salvator-x":
        a.send('stress-ng --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(4,4,2,STRESS_TIME),0,False)
    else:   
        a.send('stress-ng --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(2,4,2,STRESS_TIME),0,False)

    START_TIME = time.time()
    a.send("~/i2c_endurance 2",0.001,False)
    a.buff = ""
    while (a.buff.find('stress-ng')==-1):
        
        if ((time.time() - START_TIME) > (STRESS_TIME+20)):
            break
    a.send('\x03')
    a.send("./i2c_syscall 2 0x4f 0x12")

    if config.PLATFORM == "salvator-x":
        a.send('stress-ng --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(4,4,2,STRESS_TIME),0,False)
    else:   
        a.send('stress-ng --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(2,4,2,STRESS_TIME),0,False)

    START_TIME = time.time()
    a.send("~/i2c_endurance 4",0.001,False)
    a.buff = ""
    while (a.buff.find('stress-ng')==-1):
        
        if ((time.time() - START_TIME) > (STRESS_TIME+20)):
            break
    a.send('\x03')
    a.send("./i2c_syscall 4 0x7f 0x0a")

    print_result.func_pass(a)
