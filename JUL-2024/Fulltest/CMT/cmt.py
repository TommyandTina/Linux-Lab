import serial
import threading
from time import sleep
import sys
import os

cmt0 = "e60f0000.timer"

def change_cs(a,cmt):
    a.buff=""
    a.send('echo {} > /sys/devices/system/clocksource/clocksource0/current_clocksource'.format(cmt))

    if (a.buff.find('Switched to clocksource {}'.format(cmt)) == -1):
        return False

    a.buff=""
    a.send('cat /sys/devices/system/clocksource/clocksource0/current_clocksource')

    if (a.buff.find('{}'.format(cmt)) == -1):
        return False

    return True

def check_cs(a,cmt):
    a.buff=""
    a.send('cat /sys/devices/system/clocksource/clocksource0/current_clocksource')

    if (a.buff.find('{}'.format(cmt)) == -1):
        if (change_cs(a,cmt) == False):
            return False

    return True
