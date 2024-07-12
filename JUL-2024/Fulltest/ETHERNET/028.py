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
import cp_text
import eth


SCRIPTS = ['smp_multiple_cpu.sh','task_set_one_cpu_get_data.sh','task_set_one_cpu_put_data.sh',\
           'ftp_put_board_to_pc_data.sh','ftp_get_pc_to_board_data.sh']

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT, 1)
    a.start()

    a.buff=""

    for f in SCRIPTS:
        cp_text.copy(a,os.path.abspath('./'),f)
        a.send('chmod +x {}'.format(f))

    a.send('sed -i \'s/CPU_NUMBER=[0-9]/CPU_NUMBER={}/\' smp_multiple_cpu.sh'.format(config.NUM_CPU))

    for f in ['task_set_one_cpu_get_data.sh','ftp_get_pc_to_board_data.sh','ftp_put_board_to_pc_data.sh']:
        a.send('sed -i \'s/$IPSERVER/{}/\' {}'.format(config.SERVER_ADDR,f))
        a.send('sed -i \'s/PCNAME="rvc"/PCNAME="{}"/\' {}'.format(config.SER_USRNAME,f))
        a.send('sed -i \'s/PCPASSWORD="rvc"/PCPASSWORD="{}"/\' {}'.format(config.SER_PASS,f))
        a.send('sed -i \'s/PC_FOLDER="\/home\/rvc\/test_ether"/PC_FOLDER="\/home\/{}\/test_ether"/\' {}'.format(config.SER_USRNAME,f))
   
    print ('\n\n------- Prepare data on HOST-PC ------\n')
    sys.stdout.flush()

    os.system('mkdir -p /home/{}/test_ether'.format(config.SER_USRNAME))

    FILE_SIZE=30
    for i in range(0,config.NUM_CPU-1):
        FILE_SIZE += 10
        print('\ndd if=/dev/urandom of=/home/{}/test_ether/file-{}mb bs=1M count={}'.format(config.SER_USRNAME,FILE_SIZE,FILE_SIZE))
        sys.stdout.flush()
        os.system('dd if=/dev/urandom of=/home/{}/test_ether/file-{}mb bs=1M count={}'.format(config.SER_USRNAME,FILE_SIZE,FILE_SIZE))
 
    print ('\n--------- BOARD --------\n')
    sys.stdout.flush()

    a.buff="" 
    a.send('./smp_multiple_cpu.sh')

    rm_files=""
    first=False

    for f in SCRIPTS:
        if (first == False):
            rm_files = rm_files + "{}".format(f)
            first=True
        else:
            rm_file = rm_files + ", {}".format(f)

    a.send('rm {}'.format(rm_files))
 
    if (a.buff.find('TEST_NG')!=-1):
        print_result.func_fail(a)

    print_result.func_pass(a)
