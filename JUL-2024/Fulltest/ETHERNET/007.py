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
import eth


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()
  
    eth.check_eth(a)

    a.send('ethtool -i eth0')

    if (a.buff.find('driver: ravb')!=-1) and (a.buff.find('version')!=-1) and (a.buff.find('firmware-version:')!=-1) \
      and (a.buff.find('expansion-rom-version:')!=-1) and (a.buff.find('bus-info:')!=-1) and (a.buff.find('supports-statistics: yes')!=-1) \
      and (a.buff.find('supports-test:')!=-1) and (a.buff.find('supports-eeprom-access:')!=-1) \
      and (a.buff.find('supports-register-dump:')!=-1) and (a.buff.find('supports-priv-flags:')!=-1):
        print_result.func_pass(a)   
    else:
        print_result.func_fail(a)

