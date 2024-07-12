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
import vin

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('cd {}'.format(vin.VIDEO_TESTS_FOLDER))

    a.buff=""
    a.send('./set-edid')
    if (a.buff.find('EDID set successfully') == -1):
        print_result.func_fail(a)

    a.buff=""
    a.send('./yavta-hdmi 0',0,True,120)

    a.buff=""
    a.send('ls /tmp/vin-tests')

    for i in range(0,10):
        for f in ['bin', 'png', 'pnm']:
            if (a.buff.find('frame-00000{}.{}'.format(i,f)) == -1):
                print_result.func_fail(a)

    a.send('cd ~')

    print_result.func_pass(a)
