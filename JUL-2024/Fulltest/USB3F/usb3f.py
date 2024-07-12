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


def g_mass_storage(a,storage,cp_to,size,s2r=False,pull_out=False,speed_expectation=10):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb3','function')
    return usbf.g_mass_storage(a,'USB3F',storage,cp_to,size,s2r,pull_out,speed_expectation)

def g_mass_storage_stress_test(a,stress_time):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb3','function')
    return usbf.g_mass_storage_stress_test(a,'USB3F',stress_time)

def g_serial(a,tranfer_to,s2r=False,pull_out=False):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb3','function')
    return usbf.g_serial(a,'USB3F',tranfer_to,s2r,pull_out)

def g_ether(a,ping_to,s2r=False,pull_out=False,smp=False):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb3','function')
    return usbf.g_ether(a,'USB3F',ping_to,s2r,pull_out,smp)

def g_zero(a,modprobe_cmd,testusb_option):
    if (config.FEATBOX_USB_MODULE == True):
        control_board.usb_in('usb3','function')
    return usbf.g_zero(a,'USB3F',modprobe_cmd,testusb_option)

