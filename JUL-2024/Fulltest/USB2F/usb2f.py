#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import usbf
import control_board
import re

MODULE_TEST="USB2F"

def g_mass_storage(a,storage,cp_to,size,s2r=False,pull_out=False,speed_expectation=10):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb2ch1','function')
    return usbf.g_mass_storage(a,'USB2F',storage,cp_to,size,s2r,pull_out,speed_expectation)

def g_mass_storage_stress_test(a,stress_time):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb2ch1','function')
    return usbf.g_mass_storage_stress_test(a,'USB2F',stress_time)

def g_serial(a,tranfer_to,s2r=False,pull_out=False):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb2ch1','function')
    return usbf.g_serial(a,'USB2F',tranfer_to,s2r,pull_out)

def g_ether(a,ping_to,s2r=False,pull_out=False,smp=False):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb2ch1','function')
    return usbf.g_ether(a,'USB2F',ping_to,s2r,pull_out,smp)

def g_zero(a,modprobe_cmd,testusb_option):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb2ch1','function')
    return usbf.g_zero(a,'USB2F',modprobe_cmd,testusb_option)    

def g_audio(a,send_to):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb2ch1','function')
    return usbf.g_audio(a,'USB2F',send_to)



