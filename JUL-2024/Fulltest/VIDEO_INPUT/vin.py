#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config

	
VIDEO_TESTS_FOLDER='/home/root/vin-tests'
