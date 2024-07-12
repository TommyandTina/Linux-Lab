import serial
import threading
from time import sleep
import sys
import os

tmu0 = "e61e0000.timer"

def change_cs(a,tmu):
    a.buff=""
    a.send('echo {} > /sys/devices/system/clocksource/clocksource0/current_clocksource'.format(tmu))

    if (a.buff.find('Switched to clocksource {}'.format(tmu)) == -1):
        return False

    a.buff=""
    a.send('cat /sys/devices/system/clocksource/clocksource0/current_clocksource')

    if (a.buff.find('{}'.format(tmu)) == -1):
        return False

    return True

def check_cs(a,tmu):
    a.buff=""
    a.send('cat /sys/devices/system/clocksource/clocksource0/current_clocksource')

    if (a.buff.find('{}'.format(tmu)) == -1):
        if (change_cs(a,tmu) == False):
            return False

    return True
