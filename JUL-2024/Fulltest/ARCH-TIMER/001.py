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


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep timer')

    if (a.buff.find('arch_timer:')!=-1) and (a.buff.find('cp15 timer(s) running at')!=-1) \
      and (a.buff.find('Calibrating delay loop (skipped), value calculated using timer frequency')!=-1):
        print_result.func_pass(a)       
    else:
        print_result.func_fail(a)
                  
   
