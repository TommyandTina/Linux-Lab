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
import s2ram
import wait_process
import sound


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    if (sound.sound_setting(a) == False):
        print_result.func_fail(a)

    if (s2ram.pm_suspend_while_doing_st(a,'aplay {} &'.format(sound.AUDIO_FILE)) == False):
        print_result.func_fail(a)

    if (s2ram.pm_wakeup(a) == False):
        print_result.func_fail(a) 

    wait_process.wait(a,'aplay',30)
        
    if (sound.manual_judgement() == False):
        print_result.func_fail(a)

    print_result.func_pass(a)

