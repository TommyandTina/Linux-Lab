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
sys.path.append(os.path.relpath('../common/'))
import common_index

if __name__ == '__main__':

    common_index.main()          
	
