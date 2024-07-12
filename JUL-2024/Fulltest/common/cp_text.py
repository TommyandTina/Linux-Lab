#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config

def copy(self,folder,file_name):

    FILE = "{}/{}".format(folder,file_name)
    try:
        with open(FILE,'r') as f:
            lines = f.readlines()
    except:
        print('Cannot open file {}'.format(FILE))
        sys.stdout.flush()
        return False

    content = ""
  
    for line in lines:
        content = content + line 
    
    self.send('echo \'{}\' > {}'.format(content,file_name))
    
    return True
