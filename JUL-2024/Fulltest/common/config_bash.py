#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
import os
import testcase
import subprocess
sys.path.append(os.path.relpath('..'))
import config


def bash_change_soc(a):
    a.buff=""
    a.send('cd {}'.format(config.BASH_TESTDIR_PATH))
    a.send('sed -i \'s/SOC="\(.*\)"/SOC="{}"/\' config.sh'.format(config.SOC))
     
    a.send('cd ~')
    
def bash_change_cpu_number(a):
    a.buff=""
    a.send('cd {}'.format(config.BASH_TESTDIR_PATH))
    a.send('sed -i \'s/CPU_NUMBER=[0-9]/CPU_NUMBER={}/\' config.sh'.format(config.NUM_CPU))
     
    a.send('cd ~')





          
	
