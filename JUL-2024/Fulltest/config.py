#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
from time import sleep

#--------- UKV config ------------#
SOC="E3"
SERIAL_PORT="/dev/ttyUSB2"
SERIAL_PORT_SC1="/dev/ttyUSB10"
BOOT_NFS=True

if SOC == "E3":
    NUM_CPU=2
    PLATFORM="ebisu"
elif SOC.find("H3") != -1:
    NUM_CPU=8
    PLATFORM="salvator-x"
elif SOC.find("M3N") != -1:
    NUM_CPU=8
    PLATFORM="salvator-x"    
elif SOC.find("M3") != -1:
    NUM_CPU=6
    PLATFORM="salvator-x"

FEATBOX=True
FEATBOX=False
PI_IPADDR="192.168.10.174"
PI_NUM="0x15"

FEATBOX_USB_MODULE=False
FEATBOX_USB2_CH1={'device':'1', 'memory':'port2', 'keyboard':'port1', 'mouse':'port3', 'function':'port4'}
FEATBOX_USB2_CH2={'device':'1', 'memory':'port2', 'keyboard':'port1', 'mouse':'port3', 'function':'port4'}
FEATBOX_USB3={'device':'1','function':'port4'}


IP_ADDR="192.168.10.55"
NET_MASK="255.255.255.0"
DEFAULT_GW="192.168.10.1"

SERVER_ADDR="192.168.10.98"

SER_USRNAME="bsp"
SER_PASS="Pass1234"


PASS_MEG="#### Result: OK ####"
FAIL_MEG="#### Result: NG ####"
SKIP_MEG="#### Result: SKIP ####"

RESTART_IF_FAILED=False

BASH_TESTDIR_PATH="~/board-salvator/"

