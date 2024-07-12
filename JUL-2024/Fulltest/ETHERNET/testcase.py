#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'ETHERNET-Normal 2.1.1-CHECK_DMESG_AFTER_START_THE_BOARD', \
            2:'ETHERNET-Normal 2.1.2-CHECK_INTERRUPT_AFTER_START_THE_BOARD', \
            3:'ETHERNET-Normal 2.1.3-PING_LOCAL_LAN_NETWORK', \
            5:'ETHERNET-Normal 2.1.5-ETHERNET_INTERRUPT_COUNTER_CHECK', \
            6:'ETHERNET-Normal 2.1.6-UNBIND_BIND_ETHERNET_DRIVER_TEST', \
            7:'ETHERNET-Normal 2.1.7-CHECK_DMESG_ETHTOOL',\
#            8:'ETHERNET-Normal 2.1.8-HALF_DUPLEX_ETHERNET_TEST_ETHTOOL',\
            9:'ETHERNET-Normal 2.1.9-FULL_DUPLEX_ETHERNET_TEST_ETHTOOL',\
            10:'ETHERNET-Normal 2.1.10-ETHTOOL_CHECK_MESSAGE_LEVEL',\
            11:'ETHERNET-Normal 2.1.11-IPERF_TRANFERS_RATE_FROM_BOARD_TO_HOST_PC',\
            12:'ETHERNET-Normal 2.1.12-IPERF_TRANFERS_RATE_FROM_HOST_PC_TO_BOARD',\
            13:'ETHERNET-Normal 2.1.13-TRANFERS_DATA_FROM_BOARD_TO_HOST_PC',\
            14:'ETHERNET-Normal 2.1.14-TRANFERS_DATA_FROM_HOST_PC_TO_BOARD',\
            15:'ETHERNET-Normal 2.1.15-UP_DOWN_INTERFACE_NETWORK',\
            16:'ETHERNET-Normal 2.1.16-PING_AFTER_S2RAM',\
            17:'ETHERNET-Normal 2.1.17-PING_DURING_S2RAM',\
            18:'ETHERNET-Abnormal 2.1.18-PULL_OUT_CABLE_WHILE_TRANSMITTING',\
            19:'ETHERNET-Abnormal 2.1.19-Ctr_C_DURING_TRANFER_DATA_FROM_HOST_PC_TO_BOARD',\
            20:'ETHERNET-Abnormal 2.1.20-Ctr_Z_DURING_TRANFER_DATA_FROM_BOARD_TO_HOST_PC',\
            21:'ETHERNET-Abnormal 2.1.21-Ctr_C_DURING_TRANFER_DATA_FROM_BOARD_TO_HOST_PC',\
            22:'ETHERNET-Abnormal 2.1.22-Ctr_Z_DURING_TRANFER_DATA_FROM_BOARD_TO_HOST_PC',\
            23:'ETHERNET-Boundary 2.1.23-Check_class_A_IP_ADDRESS',\
            24:'ETHERNET-Boundary 2.1.24-Check_class_B_IP_ADDRESS',\
            25:'ETHERNET-Boundary 2.1.25-Check_class_C_IP_ADDRESS',\
            26:'ETHERNET-Boundary 2.1.26-Check_class_D_IP_ADDRESS',\
            27:'ETHERNET-Boundary 2.1.27-Check_class_E_IP_ADDRESS',\
            28:'ETHERNET-SMP 2.1.28-SMP_CONCURRENT_ACCESS_TEST',\
            29:'ETHERNET-Durability 2.1.29-STRESS_CPU_TEST',\
            30:'ETHERNET-Normal 2.1.30-WAKE_ON_LAN'\
} 
