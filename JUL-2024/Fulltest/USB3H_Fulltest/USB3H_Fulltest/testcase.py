#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))

list_TC = { 1:'{}_PFM_TC5_6'.format(config.SOC), \
            2:'{}_PFM_TC11_12'.format(config.SOC), \
            3:'{}_PFM_TC13_14'.format(config.SOC), \
            4:'{}_SMP_TC1'.format(config.SOC), \
            5:'{}_Dura_TC1'.format(config.SOC), \
            6:'{}_Normal_TC55_62'.format(config.SOC), \
            7:'{}_Normal_TC63'.format(config.SOC), \
            8:'{}_Normal_TC64'.format(config.SOC), \
            9:'{}_Normal_TC65_66'.format(config.SOC), \
            10:'{}_Normal_TC47'.format(config.SOC), \
            11:'{}_Normal_TC48'.format(config.SOC), \
            12:'{}_Normal_TC49'.format(config.SOC), \
            13:'{}_Normal_TC50'.format(config.SOC), \
            14:'{}_Normal_TC51'.format(config.SOC), \
            15:'{}_Normal_TC52'.format(config.SOC), \
            16:'{}_Normal_TC53'.format(config.SOC), \
            17:'{}_Normal_TC54'.format(config.SOC), \
            18:'{}_Normal_TC69'.format(config.SOC), \
            19:'{}_Normal_TC74_77'.format(config.SOC), \
            101:'{}_S2R_TC1_9_USB2'.format(config.SOC), \
            102:'{}_S2R_TC1_9_USB3'.format(config.SOC), \
            103:'{}_S2R_TC1_9_HUBUSB2'.format(config.SOC), \
            104:'{}_S2R_TC1_9_HUBUSB3'.format(config.SOC), \
            105:'{}_S2R_TC1_9_HUBUSB2MOUSEKEYBOARD'.format(config.SOC), \
            106:'{}_S2R_TC1_9_HUBUSB3MOUSEKEYBOARD'.format(config.SOC), \
            107:'{}_S2R_TC10-12'.format(config.SOC), \
            108:'{}_S2R_TC13-15'.format(config.SOC), \
} 
