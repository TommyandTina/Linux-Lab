#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import s2ram
import subprocess
import signal

START_STR_FILE_1MB='10000110110101101010111111111111101101010101001101010101011010101010000000000101'
END_STR_FILE_1MB='10000110110101101010111111111111101101010101001101010101011010101010000000000101'
FILE_1MB_ON_BOARD='~/file_1MB.dat'

START_STR_FILE_4MB='10000110110101101010111111111111101101010101001101010101011010101010000000000101'
END_STR_FILE_4MB='1000011011010110101011111111111110110101010100'


def check_SH_SCI_DMA(a,value="=n"):

    a.buff=""
    a.send('zcat /proc/config.gz | grep SERIAL_SH_SCI_DMA')

    if (a.buff.find('CONFIG_SERIAL_SH_SCI_DMA=y')!=-1):
        if (value == "=n"):
            print('\nWrong environment\n')
            sys.stdout.flush()
            return False
    else:
        if (value == "=y"):
            print('\nWrong environment\n')
            sys.stdout.flush()
            return False

    return True

def check_SCIF1(a,value='scif'):

    a.buff=""
    a.send('dmesg | grep scif')

    if (a.buff.find('ttySC1') == -1):
        return False

    TMP = a.find_str('ttySC1')


    if (TMP.find(' {}'.format(value)) == -1):
        return False

#    if (value == 'scif'):
#        if (TMP.find('hscif') != -1):
#            return False
#
#    elif (value == 'hscif'):
#        if (TMP.find(value) == -1):
#            return False

    return True
        


def confirm_change_config_SC0(a,config_value):

    print('\n\n----------- BOARD ------------')
    sys.stdout.flush()

    a.send('stty -F /dev/ttySC0 {}'.format(config_value),0,False)
    sleep(1)
    a.serial.write('hp')

    print('\n\n---------- HOST-PC -----------')
    print('stty -F {} {}'.format(config.SERIAL_PORT,config_value))
    sys.stdout.flush()

    os.system('stty -F {} {}'.format(config.SERIAL_PORT,config_value))

    a.buff=""

    if (a.send('cat /proc/interrupts | grep serial') == False):
        return False

    return True

def send_data_host_to_board(a,size='1MB',setting=None,s2r=False,stress=False):

    if (setting == None):
        print('\nPlease input setting\n')
        return False
        
    if (stress == True):
        TIME_OUT=3700
    elif '9600' in setting:
        TIME_OUT=100*12
    elif '38400' in setting:
        TIME_OUT=100*3
    elif '57600' in setting:
        TIME_OUT=100*2
    else:
        TIME_OUT=100

    if (s2r == True):
        if (s2ram.pm_suspend(a) == False):
            return False

        if (s2ram.pm_wakeup(a,ignore_error=False) == False):
            return False

    print('\n\n---------- BOARD -----------')
    sys.stdout.flush()

    a.buff=""
    
    a.send('stty -F /dev/ttySC1 {}'.format(setting))

    a.send('cat /dev/ttySC1',0,False)

    os.system('stty -F {} {} > /tmp/scif.log'.format(config.SERIAL_PORT_SC1,setting))

    send_process=subprocess.Popen('cat file_{}.dat - > {}'.format(size,config.SERIAL_PORT_SC1), shell=True,preexec_fn=os.setsid)

    while(TIME_OUT > 0):
        if ("DONE" in a.buff) or ("successful run completed" in a.buff): 
            break
        else:
            TIME_OUT -= 1
            sleep(1)

    a.send('\x03')
    os.killpg(os.getpgid(send_process.pid), signal.SIGTERM)

    sleep(2)
    
    print('\n\n---------- HOST-PC -----------')
    print('\nstty -F {} {}'.format(config.SERIAL_PORT_SC1,setting))
    sys.stdout.flush()
    os.system('cat /tmp/scif.log')

    print('\ncat -A file_{}.dat > {}'.format(size,config.SERIAL_PORT_SC1))
    sys.stdout.flush()

    print('\n\n----------- BOARD ------------')
    sys.stdout.flush()

    if (a.send('echo Success') == False):
        return False
    
    return True

def send_data_host_to_board_pio(a,size='1MB',setting=None,s2r=False,stress=False):

    if (setting == None):
        print('\nPlease input setting\n')
        return False
        
    if (stress == True):
        TIME_OUT=3800
    elif '9600' in setting:
        TIME_OUT=100*12
    elif '38400' in setting:
        TIME_OUT=100*3
    elif '57600' in setting:
        TIME_OUT=100*2
    else:
        TIME_OUT=100

    if (s2r == True):
        if (s2ram.pm_suspend(a) == False):
            return False

        if (s2ram.pm_wakeup(a,ignore_error=False) == False):
            return False

    print('\n\n---------- BOARD -----------')
    sys.stdout.flush()

    a.buff=""
    
    a.send('stty -F /dev/ttySC1 {}'.format(setting))

    a.send('cat /dev/ttySC1',0,False)
    
    #os.system('echo \"stty -F {} {}\" > /tmp/scif.log'.format(config.SERIAL_PORT_SC1,setting))
    os.system('echo \"9600\" > /tmp/scif.log')

    a.buff=""
    check = False
    for i in range(0,5):
        if not(check):
            print('\n\n---------- {} -----------\n\n'.format(i))
            sys.stdout.flush()
            l = -1
            a.buff=""
            while len(a.buff) == 0:
                sleep(0.1)
            while True:
                if ("DONE" in a.buff):
                    check = True
                    break
                if l == len(a.buff):
                    break
                else:
                    l = len(a.buff)
                    sleep(0.1)                 

    a.send('\x03')
        
    sleep(2)
    
    print('\n\n---------- HOST-PC -----------')
    print('\nstty -F {} {}'.format(config.SERIAL_PORT_SC1,setting))
    sys.stdout.flush()
    os.system('cat /tmp/scif.log')

    print('\ncat -A file_{}.dat > {}'.format(size,config.SERIAL_PORT_SC1))
    sys.stdout.flush()

    print('\n\n----------- BOARD ------------')
    sys.stdout.flush()

    if (a.send('echo Success') == False):
        return False
    
    return True

def send_string_host_to_board(a,string='sada',setting=None):

    if (setting == None):
        print('\nPlease input setting\n')
        return False

    print('\n\n---------- BOARD -----------')
    sys.stdout.flush()

    a.send('stty -F /dev/ttySC1 {}'.format(setting))

    a.send('cat /dev/ttySC1',0,False)

    os.system('stty -F {} {} > /tmp/scif.log'.format(config.SERIAL_PORT_SC1,setting))
   
    a.buff=""

    os.system('echo {} > {}'.format(string,config.SERIAL_PORT_SC1))

    sleep(1)

    a.send('\x03')
  
    print('\n\n---------- HOST-PC -----------')

    print('\nstty -F {} {}'.format(config.SERIAL_PORT_SC1,setting))
    sys.stdout.flush()
    os.system('cat /tmp/scif.log')
    
    print('\necho {} > {}'.format(string,config.SERIAL_PORT_SC1))
    sys.stdout.flush()

    if (a.buff.find(string)==-1):
        return False

    return True

def send_data_board_to_host(a,size='1MB',setting=None,s2r=False):

    if (setting == None):
        print('\nPlease input setting\n')
        return False

    print('\nstty -F {} {}'.format(config.SERIAL_PORT_SC1,setting))
    sys.stdout.flush()
    os.system('stty -F {} {}'.format(config.SERIAL_PORT_SC1,setting))

    print('\ncat {}'.format(config.SERIAL_PORT_SC1))
    sys.stdout.flush()
    os.system('cat {} &'.format(config.SERIAL_PORT_SC1))
 
    print('\n\n---------- BOARD -----------')
    sys.stdout.flush()

    a.send('stty -F /dev/ttySC1 {}'.format(setting))

    if (size == '1MB'):
        START_STR=START_STR_FILE_1MB
        END_STR=END_STR_FILE_1MB
        FILE_ON_BOARD=FILE_1MB_ON_BOARD
    elif (size == '100KB'):
        START_STR=START_STR_FILE_100KB
        END_STR=END_STR_FILE_100KB
        FILE_ON_BOARD=FILE_100KB_ON_BOARD

    if (s2r == False):
        a.send('cat {} > /dev/ttySC1'.format(FILE_ON_BOARD))
    else:

        if (s2ram.pm_suspend_while_doing_st(a,'cat {} > /dev/ttySC1 &'.format(FILE_ON_BOARD))==False):
            return False
        if (s2ram.pm_wakeup(a,ignore_error = False)==False):
            return False
        
        TIME_OUT=0
        
        while(TIME_OUT <= 200):
            a.buff=""
            a.send('ps -a')
            if (a.buff.find('cat')!=-1):
                sleep(30)
                TIME_OUT=TIME_OUT+1
            else:
                break

    #if (a.buff.find(START_STR) == -1) or (a.buff.find(END_STR) == -1):
    #    return False

    os.system('echo {} | sudo -S pkill -f cat'.format(config.SER_PASS,config.SERIAL_PORT_SC1))

    return True

