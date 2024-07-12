#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import conserial
import control_board
import subprocess
import re

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'sata':
    	control_board.sw12_pin7_sata()
    elif mode == 'pcie':
	control_board.sw12_pin7_pcie()
    else:
	print("Invalid mode")
