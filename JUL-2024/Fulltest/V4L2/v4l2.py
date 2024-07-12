#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config

if (config.SOC == 'H3'):
    VSP_INTR = ['fea30000.vsp','fe920000.vsp','fea20000.vsp','fea28000.vsp','fea30000.vsp','fe9a0000.vsp','fe9b0000.vsp']
    MAX_VIDEO=20
    MAX_SUBDEV=40  

elif (config.SOC == 'M3'):
    VSP_INTR = ['fe960000.vsp','fea20000.vsp','fea28000.vsp','fea30000.vsp','fe9a0000.vsp']
    MAX_VIDEO=9
    MAX_SUBDEV=18

elif (config.SOC == 'M3N'):
    VSP_INTR = ['fe960000.vsp','fe9a0000.vsp','fea20000.vsp','fea28000.vsp']
    MAX_VIDEO=9
    MAX_SUBDEV=18
	
VSP_FOLDER_TEST='/home/root/v4l2_test'
