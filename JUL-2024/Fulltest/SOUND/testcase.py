#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os

list_TC = { 1:'SOUND-Normal 2.1.1-CHECK_DMESG_AFTER_START_THE_BOARD', \
            2:'SOUND-Normal 2.1.2-CHECK_INTERRUPT', \
            3:'SOUND-Normal 2.1.3-CHECK_INTERFACE_DEVICE', \
            4:'SOUND-Normal 2.1.4-APLAY_FILE', \
            5:'SOUND-Normal 2.1.5-RECORD_FILE_S24_LE_STEREO', \
            6:'SOUND-Normal 2.1.6-RECORD_APLAY_FILE_S24_LE_BIT_RATE_44100_STEREO', \
            7:'SOUND-Normal 2.1.7-RECORD_APLAY_FILE_S24_LE_BIT_RATE_48000_STEREO',\
            11:'SOUND-Normal 2.1.11-RECORD_APLAY_FILE_S24_LE_BIT_RATE_96000_STEREO',\
            12:'SOUND-Normal 2.1.12-RECORD_APLAY_FILE_S24_LE_BIT_RATE_192000_STEREO',\
            13:'SOUND-Normal 2.1.13-RECORD_APLAY_FILE_S16_LE_BIT_RATE_44100_STEREO',\
            14:'SOUND-Normal 2.1.14-RECORD_APLAY_FILE_S24_LE_BIT_RATE_44100_MONO',\
            15:'SOUND-Normal 2.1.15-VOLUME_UP_VOLUME_DOWN_OUTPUT',\
            16:'SOUND-Normal 2.1.16-RECORD_REPEATEDLY',\
            17:'SOUND-Normal 2.1.17-APLAY_REPEATEDLY',\
            18:'SOUND-Normal 2.1.18-S2RAM_WHILE_PLAYING_AUDIO',\
            19:'SOUND-Normal 2.1.19-UNBIND_BIND_DEVICE',\
            20:'SOUND-Normal 2.1.20-UNBIND_BIND_DEVICE_WHILE_RECORDING',\
            21:'SOUND-Normal 2.1.21-RECORD_WHILE_PLAYING',\
            22:'SOUND-Normal 2.1.22-APLAY_WHILE_RECORDING',\
            23:'SOUND-Normal 2.1.23-CTRL+C_APLAY',\
            24:'SOUND-Normal 2.1.24-CTRL+C_RECORD',\
            25:'SOUND-Normal 2.1.25-CTRL+Z_APLAY',\
            26:'SOUND-Normal 2.1.26-CTRL+Z_RECORD',\
            27:'SOUND-Normal 2.1.27-VOLUME_UP_VOLUME_DOWN_APLAY',\
            28:'SOUND-Normal 2.1.28-VOLUME_UP_VOLUME_DOWN_RECORD',\
            29:'SOUND-Normal 2.1.29-SMP_MULTIPLE_CPU',\
            30:'SOUND-Normal 2.1.30-STRESS_CPU',\
            31:'SOUND-Normal 2.1.31-LOOKBACK_TEST_WITHOUT_HUMAN_EARS_48000',\
            32:'SOUND-Normal 2.1.32-LOOKBACK_TEST_WITHOUT_HUMAN_EARS_44100'\
} 

