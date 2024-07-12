#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'PM-Normal 2.1.1-SUSPEND_TO_RAM_1_TIME', \
            2:'PM-Normal 2.1.2-SUSPEND_TO_RAM_10_TIMES', \
} 
