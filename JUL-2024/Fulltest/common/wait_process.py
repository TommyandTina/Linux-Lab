#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import control_board
import subprocess


def wait(a,pattern,check_period=5,time_out=1200):

    a.buff=""

    a.send('ps -a')

    total_time = 0

    while (a.buff.find(pattern) != -1):
        sleep(check_period)
        total_time = total_time + check_period
        if (total_time > time_out):
            return False
        a.send(' ',0,False)
        a.buff=""
        a.send('ps -a')
          
    return True        
       
                        
   
