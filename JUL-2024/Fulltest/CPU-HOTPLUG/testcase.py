#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'CPUHotplug-Normal 2.1.1-CPU_HOTPLUG_SHUT_DOWN_ENABLE_CPU1', \
            2:'CPUHotplug-Normal 2.1.2-CPU_HOTPLUG_SHUT_DOWN_ENABLE_CPU2', \
            3:'CPUHotplug-Normal 2.1.3-CPU_HOT_PLUG_SHUT_DOWN_ENABLE_CPU3', \
            4:'CPUHotplug-Normal 2.1.4-MAXIMUM PLUG_OUT_CPUS', \
            5:'CPUHotplug-Normal 2.1.5-S2RAM', \
}

