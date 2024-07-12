#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'DU-Normal 2.1.1-CHECK_DMESG', \
            2:'DU-Normal 2.1.2-CHECK_INTERRUPT', \
            3:'DU-Normal 2.1.3-RAM_DISPLAY_IMAGE_ON_HDMI0', \
            4:'DU-Normal 2.1.4-RAM_DISPLAY_IMAGE_ON_HDMI1', \
            5:'DU-Normal 2.1.5-RAM_DISPLAY_IMAGE_ON_VGA', \
            6:'DU-Normal 2.1.6-SD1_DISPLAY_IMAGE_ON_HDMI0', \
            7:'DU-Normal 2.1.7-SD1_DISPLAY_IMAGE_ON_HDMI1',\
            8:'DU-Normal 2.1.8-SD1_DISPLAY_IMAGE_ON_VGA',\
            9:'DU-Normal 2.1.9-SD2_DISPLAY_IMAGE_ON_HDMI0',\
            10:'DU-Normal 2.1.10-SD2_DISPLAY_IMAGE_ON_HDMI1',\
            11:'DU-Normal 2.1.11-SD2_DISPLAY_IMAGE_ON_VGA',\
            12:'DU-Normal 2.1.12-COUNT_INTERRUPT_ON_HDMI0',\
            13:'DU-Normal 2.1.13-COUNT_INTERRUPT_ON_HDMI1',\
            14:'DU-Normal 1.1.14-COUNT_INTERRUPT_ON_VGA',\
            15:'DU-Normal 2.1.15-S2RAM_ON_HDMI0',\
            16:'DU-Normal 2.1.16-S2RAM_ON_HDMI1',\
            17:'DU-Normal 2.1.17-S2RAM_ON_VGA',\
            18:'DU-Normal 2.1.18-CHANGE_RESOLUTION_ON_HDMI0',\
            19:'DU-Normal 2.1.19-CHANGE_RESOLUTION_ON_HDMI1',\
            20:'DU-Normal 2.1.20-CHANGE_RESOLUTION_ON_VGA',\
            21:'DU-Normal 2.1.21-CHANGE_COLOR_ON_HDMI0',\
            22:'DU-Normal 2.1.22-CHANGE_COLOR_ON_HDMI1',\
            23:'DU-Normal 2.1.23-CHANGE_COLOR_ON_VGA',\
            24:'DU-Normal 2.1.24-CHECK_DRM',\
            25:'DU-Normal 2.1.25-SWITCH_HDMI0_TO_DU1',\
            26:'DU-Normal 2.1.26-SWITCH_HDMI1_TO_DU2',\
            27:'DU-Normal 2.1.27-SWITCH_VGA_TO_DU3',\
            28:'DU-Normal 2.1.28-CHANGE_FORMAT_SCREEN_ON_HDMI0',\
            29:'DU-Normal 2.1.29-CHANGE_FORMAT_SCREEN_ON_HDMI1',\
            30:'DU-Normal 2.1.30-CHANGE_FORMAT_SCREEN_ON_VGA',\
            31:'DU-Normal 2.1.31-CHANGE_RESOLUTION_FROM_HDMI0_TO_DU1',\
            32:'DU-Normal 2.1.32-CHANGE_RESOLUTION_FROM_HDMI1_TO_DU2',\
            33:'DU-Normal 2.1.33-CHANGE_RESOLUTION_FROM_VGA_TO_DU3',\
            34:'DU-Normal 2.1.34-MULTILAYER_HDMI0',\
            35:'DU-Normal 2.1.35-MULTILAYER_HDMI1',\
            36:'DU-Normal 2.1.36-MULTILAYER_VGA',\
            37:'DU-Normal 2.1.37-CHANGE_LAYER_POSITION_FROM_HDMI0_TO_DU1',\
            38:'DU-Normal 2.1.38-CHANGE_LAYER_POSITION_FROM_HDMI1_TO_DU2',\
            39:'DU-Abnormal 2.1.39-CHANGE_LAYER_POSITION_FROM_VGA_TO_DU3',\
            40:'DU-Abnormal 2.1.40-PULL_OUT_CALBLE_HDMI0',\
            41:'DU-Abnormal 2.1.41-CTRL+C_HDMI0',\
            42:'DU-Abnormal 2.1.42-CTRL+Z_HDMI0',\
            43:'DU-Boundary 2.1.43-CONFIRM_HDMI0_RESOLUTION',\
            44:'DU-Boundary 2.1.44-CONFIRM_HDMI1_RESOLUTION',\
            45:'DU-Boundary 2.1.45-CONFIRM_VGA_RESOLUTION',\
            46:'DU-SMP 2.1.46-SMP_CONCURRENT_ACCESS',\
            47:'DU-SMP 2.1.47-SMP_MULTI_PORT_ACCESS',\
            48:'DU-SMP 2.1.48-SMP_MULTI_INSTANCE_TEST',\
            49:'DU-Durability 2.1.49-ENDURANCE_TEST',\
            50:'DU-Normal 2.1.50-VERIFY_DRM-KMS_DRIVER_FUNCTIONALILY',\
            51:'DU-Normal 2.1.51-KMSXX_AUTOTEST',\
            52:'DU-Normal 2.1.52-WRITE_BACK_V4L2'
} 
