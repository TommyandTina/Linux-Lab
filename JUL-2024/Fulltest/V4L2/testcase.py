#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'V4L2-Normal 2.1.1-INTERRUPTS_CONFIRMATION', \
            2:'V4L2-Normal 2.1.2-CONFIRMATION_OF_DEVICE_NODE',\
            3:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0001',\
            4:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0002',\
            5:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0003',\
            6:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0004',\
            7:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0005',\
            8:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0006',\
            9:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0007',\
            12:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0010',\
            13:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0011',\
            14:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0012',\
            15:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0013',\
            16:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0014',\
            17:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0015',\
            18:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0016',\
            20:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0018',\
            23:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0021',\
            24:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0022',\
            25:'V4L2-Normal 2.1.3-VSP-UNIT-TEST-0023'\
} 
