
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
sys.path.append(os.path.relpath('../common/'))
import conserial
import print_result

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""
          
    a.send('dmesg | grep spi')

    if (a.buff.find('DMA available') == -1):
        print_result.func_fail(a)       
    
    a.buff=""
    a.send('./22_test_msiof_abnormal_word_size.sh m')

    if (a.buff.find('MSIOF Loopback Test End.') == -1):
        print_result.func_fail(a)

    print_result.func_pass(a)
