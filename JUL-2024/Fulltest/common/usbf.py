#!/usr/bin/python
import serial
import threading
from time import sleep
from time import time
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import control_board
import s2ram

usb2f_node = "e6590000.usb"
usb3f_node = "ee020000.usb"

def check_log(f,s):

    FILE = open('{}'.format(f),'r')

    FILE.seek(0,0)

    while (FILE.tell() != os.fstat(FILE.fileno()).st_size):

        TMP = FILE.readline()
        if (TMP.find(s) != -1):
            FILE.close()
            return (TMP)

    FILE.close()
    return None
    
def usb3f_switch_peri(a):
 
    a.send('mount -t debugfs none /sys/kernel/debug/')

    a.send('echo 1 > /sys/kernel/debug/usb/ee020000.usb/b_device')

    if (config.SOC == 'E3'):
        sleep(4)

def check_attached(a,module):
    
    if (module == 'USB2F'):
        device_node = usb2f_node
    elif (module == 'USB3F'):
        device_node = usb3f_node

    a.buff=""
    a.send("cat /sys/devices/platform/soc/{}/udc/{}/state".format(device_node,device_node))
    if (a.buff.find('configured') == -1):
        if (module == 'USB2F'):
            return False
        elif (module == 'USB3F'):
            a.buff=""
            usb3f_switch_peri(a)
            sleep(1)
            a.buff=""
            a.send("cat /sys/devices/platform/soc/{}/udc/{}/state".format(device_node,device_node))
            if (a.buff.find('configured') == -1):
                return False
             
    return True

def e3_plug_out_workarround(a):
    
    a.send('echo 2 > /sys/kernel/debug/usb/ee020000.usb/b_device')
    print('\nPlease plug out cable:')
    sys.stdout.flush()
    sleep(5)
    a.send('echo 1 > /sys/kernel/debug/usb/ee020000.usb/b_device')
    print('\nPlease plug in cable:')
    sys.stdout.flush()
    sleep(5)
    a.send('echo 2 > /sys/kernel/debug/usb/ee020000.usb/b_device')
    sleep(2)

def g_serial(a,module='USB2F',transfer_to='None',s2r=False,pull_out=False):

    LOG_FILE='/tmp/tmp_g_serial.txt'

    os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS))

    print('----------- BOARD ------------')
    sys.stdout.flush()
  
    a.buff=""
    a.send('modprobe g_serial')
   
    if (a.buff.find('g_serial ready')==-1):
        a.send('rmmod g_serial')
        a.send('modprobe g_serial')
        if (a.buff.find('g_serial ready')==-1):
            return False
  
    if (check_attached(a,module) == False):
        return False

    a.buff=""
    a.send('ls /dev/ttyGS0')
    
    if (a.buff.splitlines()[len(a.buff.splitlines())-2].find('/dev/ttyGS0')==-1):
        return False     

    if (s2r == True):
        if (s2ram.pm_suspend(a) == False):
            return False
        if (s2ram.pm_wakeup(a) == False):
            return False

    print('\n\n---------- HOST-PC -----------')
    sys.stdout.flush()

    print('\ndmesg')
    sys.stdout.flush()
    os.system('dmesg 2>&1 | tee {}'.format(LOG_FILE))

    TMP = check_log(LOG_FILE,'USB ACM device')

    if (TMP == None): 
        return False
    else:
        SERIAL_PORT = TMP.split()[len(TMP.split())-4].split(':')[0]

    print('\nls /dev/{}'.format(SERIAL_PORT))
    sys.stdout.flush()
    os.system('ls /dev/{} 2>&1 | tee {}'.format(SERIAL_PORT,LOG_FILE))
    
    if (check_log(LOG_FILE,'/dev/{}'.format(SERIAL_PORT)) == None):
        return False
   
     
    os.system('echo {} | sudo -S stty -F /dev/{} raw -echo -echoe -echok -echoctl -echoke'.format(config.SER_PASS,SERIAL_PORT))
        
    if (transfer_to == 'HOST'):
       
        print('\n----------- BOARD ------------') 
       
        os.system('cat /dev/{} > {} &'.format(SERIAL_PORT,LOG_FILE))
        
        a.send('cat > /dev/ttyGS0',0,False)
        a.serial.write('abcd...\n')
        a.serial.write('123456\n')
      
        a.send('\x03')
     
        os.system('pkill -f \'cat /dev/{}\''.format(SERIAL_PORT))
        
        if (check_log(LOG_FILE,'abcd...') == None) or (check_log(LOG_FILE,'123456') == None):
            return False

        print('\n\n---------- HOST-PC -----------')
        sys.stdout.flush()
  
        print('\ncat /dev/{}'.format(SERIAL_PORT))
        sys.stdout.flush()
        os.system('cat {} '.format(LOG_FILE))
    
    elif (transfer_to == 'BOARD'):
        
        print('\n\n---------- HOST-PC -----------\n')
        print('echo \'Test transferring data from HOST to BOARD via usb serial\' > /dev/{}'.format(SERIAL_PORT))
        sys.stdout.flush()
        
        print('\n----------- BOARD ------------')
        a.buff=""
        a.send('cat /dev/ttyGS0',0,False)
        os.system('echo \'Test transferring data from HOST to BOARD via usb serial\' > /dev/{}'.format(SERIAL_PORT))

        sleep(0.5)
          
        if (a.buff.find('Test transferring data from HOST to BOARD via usb serial')==-1):
            return False

        os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS))

        if (pull_out != True):   
            a.serial.write('\x03')  
        else:
            a.buff=""
            if (config.FEATBOX_USB_MODULE == True):
                if (module == 'USB3F'):
                    control_board.usb_out('usb3','function')
                    sleep(0.5)
                    control_board.usb_in('usb3','function')
                else:
                    control_board.usb_out('usb2ch1','function')
                    sleep(0.5)
                    control_board.usb_in('usb2ch1','function')
            else:
                if (config.SOC == 'E3') and (module == 'USB3F'):
                    a.serial.write('\x03')
                    e3_plug_out_workarround(a)
                else:
		    print('\nPlease plug out and plug in cable:\n')
                    sys.stdout.flush()
                    sleep(10)
 
            print('\n\n---------- HOST-PC -----------\n')
            print('\ndmesg')
            sys.stdout.flush()
            os.system('dmesg 2>&1 | tee {}'.format(LOG_FILE))

            TMP = check_log(LOG_FILE,'USB ACM device')

            if (TMP == None):
                return False
            else:
                SERIAL_PORT = TMP.split()[len(TMP.split())-4].split(':')[0]

            print('\nls /dev/{}'.format(SERIAL_PORT))
            sys.stdout.flush()
            os.system('ls /dev/{} 2>&1 | tee {}'.format(SERIAL_PORT,LOG_FILE))

            if (check_log(LOG_FILE,'/dev/{}'.format(SERIAL_PORT)) == None):
                return False
 
            print('\n\n---------- HOST-PC -----------\n')
            print('echo \'Test again =]]\' > /dev/{}'.format(SERIAL_PORT))
            sys.stdout.flush()

            print('\n----------- BOARD ------------')
            a.buff=""
            a.send('cat /dev/ttyGS0',0,False)
            os.system('echo \'Test again =]]\' > /dev/{}'.format(SERIAL_PORT))

            sleep(0.5)
            a.serial.write('\x03')

            if (a.buff.find('Test again =]]')==-1):
                return False

    a.send('rmmod g_serial')     

#---------------------------------------------------------------------------
def g_ether(a,module='USB2F',ping_to='None',s2r=False,pull_out=False,smp=False):
    
    LOG_FILE='/tmp/tmp_g_ether.txt'

    os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS))

    print('----------- BOARD ------------')
    sys.stdout.flush()

    a.buff=""

    a.send('dmesg -C')

    a.send('modprobe g_ether')

    if (a.buff.find('g_ether ready')==-1):
        a.send('rmmod g_ether')
        a.send('modprobe g_ether')
        if (a.buff.find('g_ether ready')==-1):
            return False

    if (check_attached(a,module) == False):
        return False

    print('\n\n---------- HOST-PC -----------\n')
    print('dmesg')
    sys.stdout.flush()
    os.system('dmesg 2>&1 | tee {}'.format(LOG_FILE))

    TMP = check_log(LOG_FILE,' renamed from ')
    if (TMP != None):
        USB_PORT_HOST = TMP.split(']')[1].split(' ')[3].split(':')[0]
    else:
        TMP = check_log(LOG_FILE,' register \'cdc_ether\'')
        if (TMP == None):
            return False
        else:
            USB_PORT_HOST = TMP.split(']')[1].split(' ')[3].split(':')[0]

    if (ping_to != 'None'):
        print('\nsudo ifconfig {} 192.168.11.2 up'.format(USB_PORT_HOST))
        sys.stdout.flush()
        os.system('echo {} | sudo -S ifconfig {} 192.168.11.2 up 2>&1 | tee -a {}'.format(config.SER_PASS,USB_PORT_HOST,LOG_FILE))
 
    print('ifconfig -a')
    sys.stdout.flush()
    os.system('ifconfig -a')
     
    print('----------- BOARD ------------')
    sys.stdout.flush()
   
    a.send('dmesg')  

    if (ping_to != 'None'):
        a.send('ifconfig usb0 192.168.11.1 up')
 
    a.send('ifconfig -a')

    if (s2r == True):
        if (ping_to == 'HOST'):
            a.buff=""
            a.send('ping -c 20 192.168.11.2 &')

            if (s2ram.pm_suspend(a)==False):
                return False
            if (s2ram.pm_wakeup(a)==False):
                return False

            a.buff=""
            a.send('ping -c 10 192.168.11.2')

            if (a.buff.find(' 0% packet loss') == -1):
                return False

        elif (ping_to == 'BOARD'):
            print('\n\n---------- HOST-PC -----------')
            print('\nping -c 20 192.168.11.1 &')
            sys.stdout.flush()
            os.system('ping -c 20 192.168.11.1 2>&1 | tee {} &'.format(LOG_FILE))
            sleep(1.5)
         
            print('\n----------- BOARD ------------')
            if (s2ram.pm_suspend(a)==False):
                return False
            if (s2ram.pm_wakeup(a)==False):
                return False

            while (check_log(LOG_FILE,'packets transmitted') == None):
                sleep(1)
            
            TMP =  check_log(LOG_FILE,'packet loss')
 
            if (TMP == None) or (TMP.split()[len(TMP.split())-5].split('%')=='0'):    
                return False
 
            print('\n----------- BOARD ------------')
            a.send('ifconfig usb0 192.168.11.1 up')
     
            print('\n\n---------- HOST-PC -----------')
            print('\nsudo ifconfig {} 192.168.11.2 up'.format(USB_PORT_HOST))
            sys.stdout.flush()
            os.system('echo {} | sudo -S ifconfig {} 192.168.11.2 up 2>&1 | tee -a {}'.format(config.SER_PASS,USB_PORT_HOST,LOG_FILE))

    if (ping_to == 'HOST'):
        a.buff=""
         
        if (smp == False):
            a.send('ping -c 10 192.168.11.2')
   
            if (a.buff.find(' 0% packet loss') == -1):
                    return False

        else:
            for i in range (0,config.NUM_CPU):
                if (i < config.NUM_CPU-1):
                    a.send('taskset -c {} ping -c 10 192.168.11.2 &'.format(i),0,False)
                else:
                    a.send('taskset -c {} ping -c 10 192.168.11.2'.format(i))

            sleep(30)

          
    elif (ping_to == 'BOARD'):
        print('\n\n---------- HOST-PC -----------')
        print('\nping -c 10 192.168.11.1')
        sys.stdout.flush()
      
        if (pull_out != True):
            os.system('ping -c 10 192.168.11.1 2>&1 | tee {}'.format(LOG_FILE))
            if (check_log(LOG_FILE,' 0% packet loss') == None):
                return False
        else:
            os.system('ping -c 10 192.168.11.1 2>&1 | tee {}&'.format(LOG_FILE))
            sleep(1.5)
           
            a.buff=""
 
            if (config.FEATBOX_USB_MODULE == True):
                if (module == 'USB3F'):
                    control_board.usb_out('usb3','function')
                    sleep(0.5)
                    control_board.usb_in('usb3','function')
                else:
                    control_board.usb_out('usb2ch1','function')
                    sleep(0.5)
                    control_board.usb_in('usb2ch1','function')            
            
            else:
                if (config.SOC == 'E3') and (module == 'USB3F'):
                    a.serial.write('\x03')
                    e3_plug_out_workarround(a)
                else:
		    print('\nPlease plug out and plug in cable:\n')
                    sys.stdout.flush()
                    sleep(10)

            if (check_log(LOG_FILE,'connect: Network is unreachable')==None):
                while(check_log(LOG_FILE,'packets transmitted')==None):
                    sleep(1)
                TMP = check_log(LOG_FILE,'packet loss')
                if (TMP == None) or (TMP.split()[len(TMP.split())-5].split('%')[0]=='0'):
                    return False

            print('\n----------- BOARD ------------')
            a.send('ifconfig usb0 192.168.11.1 up')

            print('\n\n---------- HOST-PC -----------')
            print('\nsudo ifconfig {} 192.168.11.2 up'.format(USB_PORT_HOST))
            sys.stdout.flush()
            os.system('echo {} | sudo -S ifconfig {} 192.168.11.2 up 2>&1 | tee -a {}'.format(config.SER_PASS,USB_PORT_HOST,LOG_FILE))
            
            print('\nping -c 10 192.168.11.1')
            sys.stdout.flush()
            os.system('ping -c 10 192.168.11.1 2>&1 | tee {}'.format(LOG_FILE))

            if (check_log(LOG_FILE,' 0% packet loss') == None):
                print('\n\n----------- HOST-PC ------------')
                print('\ndmesg')
                sys.stdout.flush()
                os.system('dmesg')
                print('\n----------- BOARD ------------')
                sys.stdout.flush()
                a.send('rmmod g_ether')
                return False

        print('\n----------- BOARD ------------')       

    a.send('rmmod g_ether')
   


#---------------------------------------------------------------------------
def g_mass_storage(a,module='USB2F',storage='RAM',cp_to='BOARD',size=100,s2r=False,pull_out=False,speed_expectation=10):

    LOG_FILE='/tmp/tmp_mass_storage.txt'

    os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS))

    print('----------- BOARD ------------')
    sys.stdout.flush()

    if (storage == 'RAM'):
        a.send('mount -t tmpfs -o size=400M tmpfs /tmp')

        a.send('dd if=/dev/zero of=/tmp/tmp.img bs=1M count=350')

        a.send('mkfs.ext3 -L storage /tmp/tmp.img')

        a.buff=""   
        a.send('modprobe g_mass_storage file=/tmp/tmp.img')
            
    elif (storage == 'SD'):
        #a.send('modprobe usb-dmac')
        #a.send('lsmod')

        a.send('dmesg | grep mmc1')
        a.buff="" 
        a.send('modprobe g_mass_storage file=/dev/mmcblk1p1 removable=1')
     
    sleep(2)
 
    if (a.buff.find('g_mass_storage ready')==-1):
        a.send('rmmod g_mass_storage')
        if (storage == 'RAM'):
            a.send('modprobe g_mass_storage file=/tmp/tmp.img')
        elif (storage == 'SD'):
            a.send('modprobe g_mass_storage file=/dev/mmcblk1p1 removable=1')        
       
        sleep(2)
 
        if (a.buff.find('g_mass_storage ready')==-1):
            return False
    
    if (check_attached(a,module) == False):
        return False
  
    sleep(2)
 
    print('\n---------- HOST-PC -----------')
    sys.stdout.flush()

    print('\ndmesg')
    sys.stdout.flush() 
    os.system('dmesg 2>&1 | tee {}'.format(LOG_FILE))

    print('\ndf -h')
    sys.stdout.flush()
    os.system('df -h 2>&1 | tee -a {}'.format(LOG_FILE))
      
 
    MOUNT_POINT = check_log(LOG_FILE,'Attached SCSI')

    if (MOUNT_POINT == None):
        return False
    else:
        if (MOUNT_POINT.find('Attached SCSI removable disk') != -1):
            MOUNT_POINT = MOUNT_POINT.split()[len(MOUNT_POINT.split())-5].split('[')[1].split(']')[0]        
        else:
            MOUNT_POINT = MOUNT_POINT.split()[len(MOUNT_POINT.split())-4].split('[')[1].split(']')[0]      
 
    TEST_DIR = check_log(LOG_FILE,'/dev/{}'.format(MOUNT_POINT))
        
    if (TEST_DIR == None):
        TEST_DIR = '/media/test_{}'.format(module)
        os.system('echo {} | sudo -S mkdir -p {}'.format(config.SER_PASS,TEST_DIR))
        print('\nsudo mount /dev/{} {}'.format(MOUNT_POINT,TEST_DIR))
        sys.stdout.flush() 
        os.system('echo {} | sudo -S mount /dev/{} {}'.format(config.SER_PASS,MOUNT_POINT,TEST_DIR))
        print('\ndf -h')
        sys.stdout.flush()
        os.system('df -h 2>&1 | tee -a {}'.format(LOG_FILE))
    else:
        TEST_DIR = TEST_DIR.split()[5]


    if (cp_to == 'BOARD'):
        print('\ndd if=/dev/urandom of=./file-{}M bs=1M count={}'.format(size,size))
        sys.stdout.flush()
        os.system('dd if=/dev/urandom of=./file-{}M bs=1M count={} 2>&1 | tee {}'.format(size,size,LOG_FILE))

        if (check_log(LOG_FILE,'dd:') != None):
            os.system('echo {} | sudo -S umount {}'.format(config.SER_PASS,TEST_DIR))
            return False
         
        if (s2r == True):
            os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS,TEST_DIR))
            print('\n---------- HOST-PC -----------')
            sys.stdout.flush()
            if (s2ram.pm_suspend(a)==False):
                return False
            if (s2ram.pm_wakeup(a)==False):
                return False
            print('\n---------- HOST-PC -----------')
            sys.stdout.flush() 

            print('\ndmesg')
            sys.stdout.flush()
            os.system('dmesg 2>&1 | tee {}'.format(LOG_FILE))

            print('\ndf -h')
            sys.stdout.flush()
            os.system('df -h 2>&1 | tee -a {}'.format(LOG_FILE))

            MOUNT_POINT_2 = check_log(LOG_FILE,'Attached SCSI disk')

            if (MOUNT_POINT_2 == None):
                return False
            else:
                MOUNT_POINT_2 = MOUNT_POINT_2.split()[len(MOUNT_POINT_2.split())-4].split('[')[1].split(']')[0]
            
            if (MOUNT_POINT != MOUNT_POINT_2):
                print('\nsudo umount {}'.format(TEST_DIR))
                sys.stdout.flush()
                os.system('echo {} | sudo -S umount {}'.format(config.SER_PASS,TEST_DIR))
                print('\nsudo mount /dev/{} {}'.format(MOUNT_POINT_2,TEST_DIR))
                sys.stdout.flush()
                os.system('echo {} | sudo -S mount /dev/{} {}'.format(config.SER_PASS,MOUNT_POINT_2,TEST_DIR))

        print('\nsudo cp ./file-{}M {}'.format(size,TEST_DIR))
        sys.stdout.flush()
   
        if (pull_out != True):
            os.system('echo {} | sudo -S cp ./file-{}M {} 2>&1 | tee {}'.format(config.SER_PASS,size,TEST_DIR,LOG_FILE))
        else:
            os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS))
              
            os.system('echo {} | sudo -S cp ./file-{}M {} 2>&1 | tee {} &'.format(config.SER_PASS,size,TEST_DIR,LOG_FILE))   
            sleep(1)
             
            os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS))
            a.buff=""

            if (config.FEATBOX_USB_MODULE == True):
                if (module == 'USB3F'):
                    control_board.usb_out('usb3','function')
                    sleep(0.5)
                    control_board.usb_in('usb3','function')
                else:
                    control_board.usb_out('usb2ch1','function')
                    sleep(0.5)
                    control_board.usb_in('usb2ch1','function')
            else:
                if (config.SOC == 'E3') and (module == 'USB3F'):
                    a.serial.write('\x03')
                    e3_plug_out_workarround(a)
                else:
		    print('\nPlease plug out and plug in cable:\n')
                    sys.stdout.flush()
                    sleep(10)
  
            sleep(2)

            print('\ndmesg')
            sys.stdout.flush()
            os.system('dmesg 2>&1 | tee {}'.format(LOG_FILE))
 
            print ('\ndf -h')
            sys.stdout.flush()
            os.system('df -h 2>&1 | tee -a {}'.format(LOG_FILE))
            
            MOUNT_POINT_2 = check_log(LOG_FILE,'Attached SCSI disk')

            if (MOUNT_POINT_2 == None):
                return False
            else:
                MOUNT_POINT_2 = MOUNT_POINT_2.split()[len(MOUNT_POINT_2.split())-4].split('[')[1].split(']')[0]

            if (MOUNT_POINT != MOUNT_POINT_2):
                print('\nsudo umount {}'.format(TEST_DIR))
                sys.stdout.flush()
                os.system('echo {} | sudo -S umount {}'.format(config.SER_PASS,TEST_DIR))
                print('\nsudo mount /dev/{} {}'.format(MOUNT_POINT_2,TEST_DIR))
                sys.stdout.flush()
                os.system('echo {} | sudo -S mount /dev/{} {}'.format(config.SER_PASS,MOUNT_POINT_2,TEST_DIR))

            print('\nsudo cp ./file-{}M {}'.format(size,TEST_DIR))
            sys.stdout.flush()
            os.system('echo {} | sudo -S cp ./file-{}M {} 2>&1 | tee {}'.format(config.SER_PASS,size,TEST_DIR,LOG_FILE))

    elif (cp_to == 'HOST'):
        print('\nsudo dd if=/dev/urandom of={}/file-{}M bs=1M count={}'.format(TEST_DIR,size,size))
        sys.stdout.flush()
        os.system('echo {} | sudo -S dd if=/dev/urandom of={}/file-{}M bs=1M count={} 2>&1 | tee {}'.format(config.SER_PASS,TEST_DIR,size,size,LOG_FILE))

        if (check_log(LOG_FILE,'dd:') != None):
            os.system('echo {} | sudo -S umount {}'.format(config.SER_PASS,TEST_DIR))
            return False

        print('\nsudo cp {}/file-{}M ./'.format(TEST_DIR,size))
        sys.stdout.flush()
        os.system('echo {} | sudo -S cp {}/file-{}M ./ 2>&1 | tee {}'.format(config.SER_PASS,TEST_DIR,size,LOG_FILE))

    elif (cp_to == "WRITE_SPEED"):
        print('\nsudo dd if=/dev/zero of=/dev/{} bs=300M count=1 oflag=direct'.format(MOUNT_POINT))
        sys.stdout.flush()
	os.system('echo {} | sudo -S dd if=/dev/zero of=/dev/{} bs=5M count=60 oflag=direct 2>&1 | tee {}'.format(config.SER_PASS,MOUNT_POINT,LOG_FILE))

    elif (cp_to == 'READ_SPEED'):
        print('\nsudo dd if=/dev/{} of=/dev/null bs=300M count=1 iflag=direct'.format(MOUNT_POINT))
        sys.stdout.flush()
        os.system('echo {} | sudo -S dd if=/dev/{} of=/dev/null bs=300M count=1 iflag=direct 2>&1 | tee {}'.format(config.SER_PASS,MOUNT_POINT,LOG_FILE))        
    
    if (cp_to=='WRITE_SPEED') or (cp_to=='READ_SPEED'):
        TMP = check_log(LOG_FILE,'copied')
        SPEED = float(TMP.split()[len(TMP.split())-2].replace(",", "."))
        TYPE_SPEED = TMP.split()[len(TMP.split())-1]
        
        if (TYPE_SPEED == 'KB/s'):
            SPEED = SPEED * 1024
        elif (TYPE_SPEED == 'GB/s'):
            SPEED = SPEED/1024        
         
        print('\nSPEED = {} MB/s'.format(SPEED))       
        sys.stdout.flush()

    if (cp_to == 'HOST') or (cp_to == 'BOARD'):
        
        #Check no_space_left test case (size < 400):

        if (storage == 'RAM') and (size < 400) and (check_log(LOG_FILE,'cp:') != None):
            print('\ndmesg')
            sys.stdout.flush()
            os.system('dmesg')
            os.system('echo {} | sudo -S umount {}'.format(config.SER_PASS,TEST_DIR))
            return False        

        print('\nmd5sum ./file-{}M {}/file-{}M'.format(size,TEST_DIR,size))
        sys.stdout.flush()
        os.system('md5sum ./file-{}M {}/file-{}M  2>&1 | tee {}'.format(size,TEST_DIR,size,LOG_FILE))

        MD5SUM_HOST='hp'
        MD5SUM_STORAGE='h2p'

        MD5_TMP = check_log(LOG_FILE,'./file-{}'.format(size))
   
        if (MD5_TMP != None):
            MD5SUM_HOST = MD5_TMP.split()[0]

        MD5_TMP = check_log(LOG_FILE,'{}/file-{}'.format(TEST_DIR,size))    
         
        if (MD5_TMP != None):
            MD5SUM_STORAGE = MD5_TMP.split()[0]    


    os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS))
    
    print('\nsudo umount {}'.format(TEST_DIR)) 
    sys.stdout.flush()
    os.system('echo {} | sudo -S umount {} 2>&1 | tee {}'.format(config.SER_PASS,TEST_DIR,LOG_FILE))

    if (check_log(LOG_FILE,'umount:') != None):
        return False
  
    print('\n----------- BOARD ------------')
    sys.stdout.flush()
    a.send('rmmod g_mass_storage')   
   
    if (storage == 'RAM'): 
        a.send('rm -rf /tmp/tmp.img')

    print('\n\n---------- HOST-PC -----------')
    print('\ndmesg')
    sys.stdout.flush()
    os.system('dmesg 2>&1 | tee {}'.format(LOG_FILE))   

    if (check_log(LOG_FILE,'can\'t set config #1, error') != None):
        return False     
    
    if (cp_to == 'BOARD') or (cp_to == 'HOST'):
        #check no space left
        if (storage == 'RAM') and (size >= 400): 
            if (MD5SUM_HOST == MD5SUM_STORAGE):
	        return False
        else:
            if (MD5SUM_HOST != MD5SUM_STORAGE):
                return False

    elif (cp_to == 'READ_SPEED') or (cp_to == 'WRITE_SPEED'):
        if (SPEED < speed_expectation):
            return False

    return True

#---------------------------------------------------------------------------
def g_mass_storage_stress_test(a,module='USB2F',stress_time=3600):

    LOG_FILE='/tmp/tmp_mass_storage.txt'

    os.system('echo {} | sudo -S dmesg -C'.format(config.SER_PASS))

    print('----------- BOARD ------------')
    sys.stdout.flush()

    a.send('mount -t tmpfs -o size=400M tmpfs /tmp')

    a.send('dd if=/dev/zero of=/tmp/tmp.img bs=1M count=350')

    a.send('mkfs.ext3 -L storage /tmp/tmp.img')

    a.buff=""
    a.send('modprobe g_mass_storage file=/tmp/tmp.img')

    sleep(2)

    if (a.buff.find('g_mass_storage ready')==-1):
        a.send('rmmod g_mass_storage')
        
        a.send('modprobe g_mass_storage file=/tmp/tmp.img')
        sleep(2)

    if (a.buff.find('g_mass_storage ready')==-1):
        return False

    if (check_attached(a,module) == False):
        return False
 
    print('\n---------- HOST-PC -----------')
    sys.stdout.flush()

    print('\ndmesg')
    sys.stdout.flush() 
    os.system('dmesg 2>&1 | tee {}'.format(LOG_FILE))

    print('\ndf -h')
    sys.stdout.flush()
    os.system('df -h 2>&1 | tee -a {}'.format(LOG_FILE))
      
 
    MOUNT_POINT = check_log(LOG_FILE,'Attached SCSI disk')

    if (MOUNT_POINT == None):
        return False
    else:
        MOUNT_POINT = MOUNT_POINT.split()[len(MOUNT_POINT.split())-4].split('[')[1].split(']')[0]        
              
 
    TEST_DIR = check_log(LOG_FILE,'/dev/{}'.format(MOUNT_POINT))
        
    if (TEST_DIR == None):
        TEST_DIR = '/media/test_{}'.format(module)
        os.system('echo {} | sudo -S mkdir -p {}'.format(config.SER_PASS,TEST_DIR))
        print('\nsudo mount /dev/{} {}'.format(MOUNT_POINT,TEST_DIR))
        sys.stdout.flush() 
        os.system('echo {} | sudo -S mount /dev/{} {}'.format(config.SER_PASS,MOUNT_POINT,TEST_DIR))
    else:
        TEST_DIR = TEST_DIR.split()[5]

    print('\n----------- BOARD ------------')
    sys.stdout.flush()

    a.buff=""
    a.send('stress --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s'.format(config.NUM_CPU,config.NUM_CPU*2,config.NUM_CPU,stress_time),0,False)

    print('\n----------- HOST-PC ------------')
    sys.stdout.flush()
    
    START = time()

    while (time() - START < stress_time):
        print('\nsudo time dd if=/dev/{} of=/dev/zero bs=300M iflag=direct'.format(MOUNT_POINT))
        sys.stdout.flush()
        os.system('echo {} | sudo -S time dd if=/dev/{} of=/dev/zero bs=300M iflag=direct 2>&1 | tee {}'.format(config.SER_PASS,MOUNT_POINT,LOG_FILE))
         
        print('\nsudo time dd if=/dev/zero of=/dev/{} bs=300M oflag=direct'.format(MOUNT_POINT))
        sys.stdout.flush()
        os.system('echo {} | sudo -S time dd if=/dev/zero of=/dev/{} bs=300M count=1 2>&1 | tee -a {}'.format(config.SER_PASS,MOUNT_POINT,LOG_FILE))

        if (check_log(LOG_FILE,'dd: failed to open') != None) or (check_log(LOG_FILE,'cannot seek: Invalid argument')):
            return False
   
    a.wait('successful run completed')

    print('\nsudo umount {}'.format(TEST_DIR))
    sys.stdout.flush()
    os.system('echo {} | sudo -S umount {} 2>&1 | tee {}'.format(config.SER_PASS,TEST_DIR,LOG_FILE))

    if (check_log(LOG_FILE,'umount:') != None):
        return False
     
    print('\n----------- BOARD ------------')
    sys.stdout.flush()

    a.send('rmmod g_mass_storage')

    if (a.buff.find('rmmod:')!=-1):
        return False

    a.send('rm -rf /tmp/tmp.img')

    return True

#--------------------------------------------------------------------------------
def g_zero(a,module='USB2F',modprobe_cmd='modprobe g_zero',testusb_option=''):

    LOG_FILE='/tmp/tmp_g_zero.txt'

    print('----------- BOARD ------------')
    sys.stdout.flush()

    a.buff=""

    a.send('{}'.format(modprobe_cmd))

    if (a.buff.find('zero ready')==-1):
        a.send('rmmod g_zero')
        a.send('{}'.format(modprobe_cmd))
        if (a.buff.find('zero ready')==-1):
            return False
    sleep(0.5)

    if (check_attached(a,module) == False):
        return False

    print('\n\n---------- HOST-PC -----------')
    sys.stdout.flush()
    
    os.system('echo {} | sudo -S mount --bind /dev/bus /proc/bus > /dev/null'.format(config.SER_PASS))
    os.system('echo {} | sudo -S mount --bind /dev/bus/usb /proc/bus/usb > /dev/null'.format(config.SER_PASS))
    os.system('echo {} | sudo -S  ln -s /sys/kernel/debug/usb/devices /proc/bus/usb/devices 2> /dev/null'.format(config.SER_PASS))
    
    print('\nlsusb | grep Gadget')
    sys.stdout.flush()

    os.system('lsusb | grep Gadget 2>&1 | tee {}'.format(LOG_FILE))

    TMP = check_log(LOG_FILE,'Gadget Zero')
    xxx = TMP.split()[1]
    yyy = TMP.split()[3].split(':')[0]

    print('\nsudo testusb -D /proc/bus/usb/{}/{} {}'.format(xxx,yyy,testusb_option))
    sys.stdout.flush()    

    os.system('echo {} | sudo -S testusb -D /proc/bus/usb/{}/{} {} 2>&1 | tee {}'.format(config.SER_PASS,xxx,yyy,testusb_option,LOG_FILE))

    print('----------- BOARD ------------')
    sys.stdout.flush()

    a.send('rmmod g_zero')

    if (check_log(LOG_FILE,'testusb: command')!=None):
        return False

    return True

#-------------------------------------------------------
def g_audio(a,module='USB2F',send_to='BOARD'):

    LOG_FILE='/tmp/tmp_g_audio.txt'

    print('----------- BOARD ------------')
    sys.stdout.flush()

    a.buff=""
    a.send('./configfs-gadget-audio.sh adaptive')

    #a.send('modprobe g_audio p_srate=44100 c_srate=48000')

    #if (a.buff.find('g_audio gadget: g_audio ready')==-1):
    #    a.send('rmmod g_audio')
    #    a.send('modprobe g_audio p_srate=44100 c_srate=48000')
    #    if (a.buff.find('g_audio gadget: g_audio ready')==-1):
    #        return False
   
    if (check_attached(a,module) == False):
        return False
 
    CMD=['amixer cset numid=1 200','amixer cset numid=2 1','amixer cset numid=5 12','amixer cset numid=8 12', \
         'amixer cset numid=6 0','amixer cset numid=9 0','amixer cset numid=4 0','amixer cset numid=7 0']

    for i in CMD:
        a.buff=''
        a.send('{}'.format(i))
        
        #if (a.buff.find('amixer:')):
        #    return False
   
    a.buff=""
    a.send('aplay -l | grep Gadget')

    CARD_BOARD=a.buff.splitlines()[len(a.buff.splitlines())-2].split()[1].split(':')[0]

    print('\n\n---------- HOST-PC -----------')
    print('\naplay -l | grep gadget')
    sys.stdout.flush()
    
    os.system('aplay -l | grep gadget 2>&1 | tee {}'.format(LOG_FILE))
    
    CARD_HOST=check_log(LOG_FILE,'gadget [USB configfs base gadget]').split(':')[0].split()[1]

    if (send_to == 'HOST'):
        print('----------- BOARD ------------')
        sys.stdout.flush()
 
        a.buff=""
        a.send('aplay -D plughw:{} audio_file.wav -d 65'.format(CARD_BOARD),0,False) 
 
        print('\n\n---------- HOST-PC -----------')
        print('\narecord -c 2 -r 44100 -f S16_LE -D hw:{},0 -d 60 /home/rvc/record.wav'.format(CARD_HOST))
        sys.stdout.flush()

        os.system('arecord -c 2 -r 44100 -f S16_LE -D hw:{},0 -d 60 /home/rvc/record.wav'.format(CARD_HOST))

        print('\naplay /home/rvc/record.wav')
        sys.stdout.flush()
       
        os.system('aplay /home/rvc/record.wav')
    else:

        print('\naplay -D plug:hw:{} audio_file.wav -d 65'.format(CARD_HOST))
        sys.stdout.flush()

        os.system('aplay -D plug:hw:{} audio_file.wav -d 65 &'.format(CARD_HOST))
	sleep(1)
        print('\n----------- BOARD ------------')
        sys.stdout.flush()

        a.send('arecord -c 2 -r 48000 -f S16_LE -D hw:{},0 /record.wav -d 60'.format(CARD_BOARD))
       
        CMD=['amixer set \'DVC Out Mute\' off ;','amixer set \'DVC In Mute\' off;','amixer set "DVC Out" 20%;','amixer set "DVC In" 20%;']

        for i in CMD:
            a.buff=''
            a.send('{}'.format(i))

        a.send('aplay /record.wav')

    a.send('\x03')          
    #a.send('rmmod g_audio')

    a.send('./configfs-gadget-audio-clean.sh')
    
    return True 
