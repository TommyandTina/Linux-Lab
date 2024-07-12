#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'RCARTHERMAL-Normal 2.1.1-CHECK_DMESG_AFTER_START_THE_BOARD', \
            2:'RCARTHERMAL-Normal 2.1.2-CHECK_INTERRUPT_AFTER_START_THE_BOARD', \
            3:'RCARTHERMAL-Normal 2.1.3-THERMAL_CHECK_ALL_DEVICE', \
            4:'RCARTHERMAL-Normal 2.1.4-THERMAL_CHECK_TEMP_AND_POINT_DEVICE', \
            5:'RCARTHERMAL-Normal 2.1.5-THERMAL_TEMPERATURE_OF_EACH_SENSORS', \
            6:'RCARTHERMAL-Normal 2.1.6-THERMAL_TEMPERATURE_INCREASE_TEST', \
            8:'RCARTHERMAL-Normal 2.1.8-THERMAL_S2RAM', \
            9:'RCARTHERMAL-Normal 2.1.8-THERMAL_UNBIND_BIND' \
} 
