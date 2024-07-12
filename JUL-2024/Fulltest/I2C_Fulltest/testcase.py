#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'I2C-Normal 2.1.1-CHECK_DMESG_AFTER_START_THE_BOARD', \
            2:'I2C-Normal 2.1.2-CHECK_INTERRUPT_AFTER_START_THE_BOARD', \
            3:'I2C-Normal 2.1.3-I2C_CHECK_DEVICE_TEST', \
            4:'I2C-Normal 2.1.4-I2C_CHECK_DEVICE_NODE_TEST', \
            5:'I2C-Normal 2.1.5-I2C_CHECK_DEVICE_CONNECT_TEST', \
            6:'I2C-Normal 2.1.6-I2C_CHECK_DEVICE_CONNECT_TEST', \
            7:'I2C-Normal 2.1.7-I2C_CHECK_DEVICE_CONNECT_TEST', \
            9:'I2C-Normal 2.1.9-I2C_CHECK_DEVICE_CONNECT_TEST', \
            11:'I2C-Normal-2.1.11-I2C_CHECK_DEVICE_CONNECT_TEST', \
            12:'I2C-Normal 2.1.12-CHECK_INTERRUPT_COUTER_I2C_TEST', \
            13:'I2C-Normal 2.1.13-I2C_UNBIND_BIND_DEVICE_TEST', \
            15:'I2C-Normal 2.1.15-I2C_AMIXER', \
            17:'I2C-Normal 2.1.17-I2C_AMIXER', \
            18:'I2C-Normal 2.1.18-I2C_READ', \
            19:'I2C-Normal 2.1.19-I2C_WRITE', \
            20:'I2C-Normal 2.1.20-I2C_S2RAM' \
} 
