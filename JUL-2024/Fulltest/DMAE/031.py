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
import s2ram


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    a.send('amixer set \'DVC Out Mute\' off')
    a.send('amixer set \'DVC In Mute\' off')
    a.send('amixer set \"DVC Out\" 20%')
    a.send('amixer set \"DVC In\" 20%')

    #a.send('amixer cset numid=1 200')
    #a.send('amixer cset numid=2 1')
    #a.send('amixer cset numid=4 1')
    #a.send('amixer cset numid=5 1')
    #a.send('amixer cset numid=7 1')
    #a.send('amixer cset numid=8 1')

    a.send('aplay audio.wav &')

    if (s2ram.pm_suspend(a)==False):
        print_result.func_fail(a)

    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
  
    a.buff=""
    a.send('ps -a')
    
    if (a.buff.find('aplay')==-1):
        print_result.func_fail(a)
 
    TIMEOUT=0
    while (a.buff.find('aplay')!=-1):
        TIMEOUT = TIMEOUT + 20
        sleep(20)
        a.buff=""
        a.send('ps -a')
        if (TIMEOUT > 150):
            print_result.func_fail(a)
  
    print_result.func_pass(a)

