#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'TMU-Normal 2.1.1-CHECK_DMESG_AFTER_START_THE_BOARD', \
            2:'TMU-Normal 2.1.2-CHECK_INTERRUPT_AFTER_START_THE_BOARD', \
            3:'TMU-Normal 2.1.3-CHECK_INTERRUPT_COUTER_TIMER_TEST', \
            4:'TMU-Normal 2.1.4-CHECK_INTERRUPT_COUTER_TIMER_TEST', \
            5:'TMU-Normal 2.1.5-SETTING_TIME_FOR_SYSTEM', \
            6:'TMU-Normal 2.1.6-OPERATION_AFTER_S2RAM', \
}

