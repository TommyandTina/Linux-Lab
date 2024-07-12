#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import conserial
import print_result
import subprocess


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    for i in range(0,3):
        a.buff=""
        a.send('cat /sys/class/thermal/thermal_zone{}/trip_point_0_temp'.format(i))

        try:
            int (a.buff.splitlines()[len(a.buff.splitlines())-2].split()[0])
        except ValueError:
            print_result.func_fail(a)

        a.buff=""
        a.send('cat /sys/class/thermal/thermal_zone{}/trip_point_0_type'.format(i))

        if (a.buff.find('passive')==-1) and (a.buff.find('critical')==-1):
            print_result.func_fail(a)

	if (a.buff.find('passive')!=-1):
	    a.buff=""
            a.send('cat /sys/class/thermal/thermal_zone{}/trip_point_1_temp'.format(i))

            try:
                int (a.buff.splitlines()[len(a.buff.splitlines())-2].split()[0])
            except ValueError:
                print_result.func_fail(a)

            a.buff=""
            a.send('cat /sys/class/thermal/thermal_zone{}/trip_point_1_type'.format(i))

            if (a.buff.find('passive')==-1) and (a.buff.find('critical')==-1):
                print_result.func_fail(a)

    
    print_result.func_pass(a)
