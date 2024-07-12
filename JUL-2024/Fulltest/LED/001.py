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
          
    for led in [6,5,4]:
        a.buff=""
        a.send('echo 1 > /sys/class/leds/led{}/brightness'.format(led))

        if (a.buff.find('No such file or directory')!=-1):
            print_result.func_fail(a)
     
        sleep(1)

        a.buff=""
        a.send('echo 0 > /sys/class/leds/led{}/brightness'.format(led))

        if (a.buff.find('No such file or directory')!=-1):
            print_result.func_fail(a)
       
        sleep(1)
    
    print_result.func_pass(a)
	 
  

    
                  
   
