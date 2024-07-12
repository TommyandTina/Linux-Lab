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
import pcie_sata

SIZE='50'
DATA='no_data'
STAGE=1

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (pcie_sata.cp_folder_to_hd(a,STAGE,SIZE,DATA)==False):
        print_result.func_fail(a)
    else:
        print_result.func_pass(a)
    
 

       
