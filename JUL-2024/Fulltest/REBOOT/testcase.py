#!/usr/bin/python

import sys
import os
sys.path.append(os.path.relpath('..'))
sys.path.append(os.path.relpath('../common/'))
import config
import time
import re
import datetime
import threading
import serial
import usb2h_fulltest

MODULE_TEST = usb2h_fulltest.MODULE_TEST
SOC = config.SOC

list_TC = {\
    1:'{}_{}_reboot'.format(MODULE_TEST,SOC), \
}
