#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import subprocess


def sw23_on():
    subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                    \"python3 ~/01_featbox_software/auto_ctrl.py {} boot > /dev/null\" 2>&1 > /dev/null".format(config.PI_IPADDR,config.PI_NUM),shell=True)
    sleep(0.5)
 
def sw23_off():
    subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                    \"python3 ~/01_featbox_software/auto_ctrl.py {} unboot > /dev/null\"  2>&1 > /dev/null".format(config.PI_IPADDR,config.PI_NUM),shell=True)
    sleep(0.5)     

def restart():
    subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                     \"python3 ~/01_featbox_software/auto_ctrl.py {} off; \
                       python3 ~/01_featbox_software/auto_ctrl.py {} on;  \
                       python3 ~/01_featbox_software/auto_ctrl.py {} boot\"  2>&1 > /dev/null".format(config.PI_IPADDR,config.PI_NUM,config.PI_NUM,config.PI_NUM))
    sleep(0.5)

def restart_2():
    subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                      \"python3 ~/01_featbox_software/auto_ctrl.py {} reset;  \
		        python3 ~/01_featbox_software/auto_ctrl.py {} boot > /dev/null\" 2>&1 > /dev/null".format(config.PI_IPADDR,config.PI_NUM,config.PI_NUM),shell=True)
    sleep(0.5)

def sw12_pin7_sata():
    subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                    \"python3 ~/01_featbox_software/auto_ctrl.py {} sata > /dev/null\"".format(config.PI_IPADDR,config.PI_NUM),shell=True)
    sleep(0.5)

def sw12_pin7_pcie():
    subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                    \"python3 ~/01_featbox_software/auto_ctrl.py {} pcie > /dev/null\"".format(config.PI_IPADDR,config.PI_NUM),shell=True)
    sleep(0.5)
  
def off_board():
    subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                    \"python3 ~/01_featbox_software/auto_ctrl.py {} unboot > /dev/null\"  2>&1 > /dev/null".format(config.PI_IPADDR,config.PI_NUM),shell=True)
    sleep(0.5)
    
def on_board():
    subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                    \"python3 ~/01_featbox_software/auto_ctrl.py {} boot > /dev/null\"  2>&1 > /dev/null".format(config.PI_IPADDR,config.PI_NUM),shell=True)
    sleep(0.5)

def usb_in(Channel,Type):
     
    if (Channel=='usb2ch1'):
        subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                       \"python3 ~/01_featbox_software/auto_ctrl.py {} usb {} out {}; sleep 0.5; \
                         python3 ~/01_featbox_software/auto_ctrl.py {} usb {} in {}\"".format(config.PI_IPADDR,config.PI_NUM,config.FEATBOX_USB2_CH1[Type],config.FEATBOX_USB2_CH1['device']\
                                                                                      ,config.PI_NUM,config.FEATBOX_USB2_CH1[Type],config.FEATBOX_USB2_CH1['device']),shell=True)          
    if (Channel=='usb2ch2'):
        subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                       \"python3 ~/01_featbox_software/auto_ctrl.py {} usb {} out {}; sleep 0.5; \
                         python3 ~/01_featbox_software/auto_ctrl.py {} usb {} in {}\"".format(config.PI_IPADDR,config.PI_NUM,config.FEATBOX_USB2_CH2[Type],config.FEATBOX_USB2_CH2['device']\
                                                                                      ,config.PI_NUM,config.FEATBOX_USB2_CH2[Type],config.FEATBOX_USB2_CH2['device']),shell=True)

    if (Channel=='usb3'):
        subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                       \"python3 ~/01_featbox_software/auto_ctrl.py {} usb {} out {}; sleep 0.5; \
                         python3 ~/01_featbox_software/auto_ctrl.py {} usb {} in {}\"".format(config.PI_IPADDR,config.PI_NUM,config.FEATBOX_USB3[Type],config.FEATBOX_USB3['device']\
                                                                                      ,config.PI_NUM,config.FEATBOX_USB3[Type],config.FEATBOX_USB3['device']),shell=True)
    sleep(0.5)   

def usb_out(Channel,Type): 

    if (Channel=='usb2ch1'):
        subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                       \"python3 ~/01_featbox_software/auto_ctrl.py {} usb {} out {}\"".format(config.PI_IPADDR,config.PI_NUM,config.FEATBOX_USB2_CH1[Type],config.FEATBOX_USB2_CH1['device']),shell=True)

    if (Channel=='usb2ch2'):
        subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                       \"python3 ~/01_featbox_software/auto_ctrl.py {} usb {} out {}\"".format(config.PI_IPADDR,config.PI_NUM,config.FEATBOX_USB2_CH2[Type],config.FEATBOX_USB2_CH2['device']),shell=True)

    if (Channel=='usb3'):
        subprocess.call("sshpass -p \"raspberry\" ssh -o StrictHostKeyChecking=no pi@{} \
                       \"python3 ~/01_featbox_software/auto_ctrl.py {} usb {} out {}\"".format(config.PI_IPADDR,config.PI_NUM,config.FEATBOX_USB3[Type],config.FEATBOX_USB3['device']),shell=True)
    sleep(0.5)
                               
