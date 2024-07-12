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
          
    a.send('amixer sset "DVC Out" 50%')

    a.send('amixer sset "Digital Playback Volume1" 50%')

    a.send('amixer sset "DVC In" 20%')

    if (a.buff.find('amixer:')!=-1):
        print_result.func_fail(a)

    a.send('atest')
   
    if (a.buff.find('Channel 0: OK')==-1) or (a.buff.find('Channel 1: OK')==-1):
        a.send('echo "Try again"')

        a.send('amixer sset "DVC Out" 50%')
    
        a.send('amixer sset "Digital Playback Volume1" 50%')
    
        a.send('amixer sset "DVC In" 20%')
    
        if (a.buff.find('amixer:')!=-1):
            print_result.func_fail(a)
    
        a.send('atest')
       
        if (a.buff.find('Channel 0: OK')==-1) or (a.buff.find('Channel 1: OK')==-1):
            print_result.func_fail(a)

    a.send('atest -vvvv -s 44100')
  
    print_result.func_pass(a) 
