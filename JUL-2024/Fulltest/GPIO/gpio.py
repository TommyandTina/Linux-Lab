#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config

 
if (config.SOC == 'E3'):
    MAX_BANK = 6             
    GPIO_CHIP = ['494', '471', '445', '429', '418', '398', '380']         
    NUM_GPIO = ['18', '23', '26', '16', '11', '20', '18']
    GPIO_NODE = ['e6050000.gpio', 'e6051000.gpio','e6052000.gpio', 'e6053000.gpio', 'e6054000.gpio', 'e6055000.gpio', 'e6055400.gpio']
else:
    MAX_BANK = 7
    GPIO_CHIP = ['496', '467', '452', '436', '418', '392', '360', '356']
    NUM_GPIO = ['16', '29', '15', '16', '18', '26', '32', '4']
    GPIO_NODE = ['e6050000.gpio', 'e6051000.gpio','e6052000.gpio', 'e6053000.gpio', 'e6054000.gpio', 'e6055000.gpio', 'e6055400.gpio', 'e6055800.gpio']

if (config.SOC == 'E3'):
    GPIO_PORT1 = '479'
    GPIO_PORT2 = '482'
else:
    GPIO_PORT1 = '364'
    GPIO_PORT2 = '381'

if (config.SOC == 'H3') or (config.SOC == 'M3N'):
    LEFT_BOUNDARY = 346
    RIGHT_BOUNDARY = 511
elif (config.SOC == 'M3'):
    if (config.PLATFORM == 'm3ulcb'):
        LEFT_BOUNDARY = 290
        RIGHT_BOUNDARY = 511
    else:
        LEFT_BOUNDARY = 346
        RIGHT_BOUNDARY = 511
elif (config.SOC == 'E3'):
    LEFT_BOUNDARY = 370
    RIGHT_BOUNDARY = 511

