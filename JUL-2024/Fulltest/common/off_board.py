#!/usr/bin/python
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import control_board

def main():

    if (config.FEATBOX == True):
        control_board.off_board()
    else:
        print('\nPlease press switch and plug out cable to turn off board \n')
        sys.stdout.flush()    
        
if __name__ == '__main__':
    
    main()


