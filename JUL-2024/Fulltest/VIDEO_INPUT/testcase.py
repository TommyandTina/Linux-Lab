#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'VIDEO_INPUT-Normal 2.1.1-DMESG_CONFIRMATION', \
            46:'VIDEO_INPUT-Normal 2.1.46-VIN-TESTS-HDMI0'\
} 
