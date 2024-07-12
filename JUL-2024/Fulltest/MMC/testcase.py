#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'MMC-Normal 2.1.1-CHECK_DMESG_AFTER_START_THE_BOARD', \
            2:'MMC-Normal 2.1.2-CHECK_INTERRUPT_AFTER_START_THE_BOARD', \
            3:'MMC-Normal 2.1.3-MMC_MOUNT_CONFIRMATION', \
            4:'MMC-Normal 2.1.4-WRITE_DATA_FROM_RAM_TO_MMC_10M', \
            5:'MMC-Normal 2.1.5-WRITE_DATA_FROM_RAM_TO_MMC_100M',\
            6:'MMC-Normal 2.1.10-WRITE_DATA_FROM_RAM_TO_MMC_350', \
            7:'MMC-Normal 2.1.7-READ_DATA_FROM_MMC_TO_RAM_10M',\
            8:'MMC-Normal 2.1.8-READ_DATA_FROM_SDHI_TO_RAM_100M',\
            9:'MMC-Normal 2.1.9-READ_DATA_FROM_MMC_TO_RAM_350M',\
            10:'MMC-Normal 2.1.57-WRITE_SPEED_MMC_TEST',\
            11:'MMC-Normal 2.1.11-READ_SPEED_SDHI_TEST',\
            12:'MMC-Normal 2.1.12-S2RAM_AFTER_WRITING',\
            13:'MMC-Normal 2.1.13-S2RAM_AFTER_READING',\
            14:'MMC-Normal 2.1.14-S2RAM_WHILE_WRITING',\
            15:'MMC-Normal 2.1.15-S2RAM_WHILE_READING',\
            16:'MMC-Normal 2.1.16-UNBIND_BIND_MMC_TEST',\
            17:'MMC-Normal 2.1.17-UNBIND_WHILE_COPY',\
            18:'MMC-Boundary 2.1.18-MMC_TEST_OUTSIDE_BLOCK',\
            19:'MMC-Boundary 2.1.19-MMC_TEST_FINAL_BLOCK',\
            20:'MMC-Boundary 2.1.20-MMC_TEST_INSIDE_BLOCK',\
            21:'MMC-Boundary 2.1.21-MMC_TEST_FINAL_BLOCK',\
            22:'MMC-SMP 2.1.22-SMP_TEST_MULTIPLE_CPU',\
            23:'MMC--Durability 2.1.23-STRESS_CPU_TEST'\
} 
