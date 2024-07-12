#!/usr/bin/python
import serial
import threading
from time import time
from time import sleep
import sys
import re
import os
sys.path.append(os.path.relpath('..'))
import config
import cp_device

IMAGE_FILE = '~/image.bmp'
AUTOTEST_FOLDER = '~/kmsxx_autotest'

if (config.SOC == 'E3'):
    HDMI0_INTR = 'feb00000.display'
else:
    HDMI0_INTR = 'fead0000.hdmi'
    HDMI1_INTR = 'feae0000.hdmi'
    VGA_INTR = 'feb00000.display'

if (config.PLATFORM.find('ulcb')!=-1):
    PORT = {'HDMI0':'HDMI-A-2'}
elif (config.PLATFORM.find('salvator-x')!=-1):
    if (config.SOC == 'H3'):
        PORT = {'VGA':'VGA-1','HDMI0':'HDMI-A-1', 'HDMI1':'HDMI-A-2'}
    elif (config.SOC == 'M3N') or (config.SOC == 'M3'):
        PORT = {('VGA'):'VGA-1',('HDMI0'):'HDMI-A-1'}
elif (config.PLATFORM.find('ebisu')!=-1):
    PORT = {('VGA'):'VGA-1',('HDMI0'):'HDMI-A-1'}

def manual_judgement():

    print('\n\nIs the result OK? [yes/no]:')
    sys.stdout.flush()

    result = raw_input().lower()

    while ((result != 'yes') and (result != 'no')):
        print('\nPlease input correctly yes or no:')
        sys.stdout.flush()

        result = raw_input().lower()

    if (result == 'yes'):
        return True
    else:
        return False

def mountpoint(a,slot):
    a.buff=""
    tmp = slot.lower()

    if (tmp == 'sd1'):
        a.send('find /sys/devices/platform/soc/ee100000.mmc/ -name mmcbl*p*')
        sleep(0.5)
    elif (tmp == 'sd2'):
        if (config.SOC == "E3"):
            a.send('find /sys/devices/platform/soc/ee120000.mmc/ -name mmcbl*p*')
        else:
            a.send('find /sys/devices/platform/soc/ee160000.mmc/ -name mmcbl*p*')
        sleep(0.5)
    else:
        return(None)

    for line in a.buff.splitlines():
       if (re.search('mmcblk[0-9]p[0-9]',line)):
           return(line.split('/')[11])

def bmap_test(a,picture_on,image):

    a.send('fbset -xres 800 -yres 600 -laced 0;fbset -xres 640 -yres 480 -laced 0')

    if (picture_on == 'RAM'):
        a.send('mount -t tmpfs -o size=20m tmpfs /tmp')

        a.buff=""
        a.send('cp {} /tmp/Image.bmp'.format(image))
        if (a.buff.find('cp:')!=-1):
            return False

        a.send('bmap /dev/fb0 /tmp/Image.bmp')

    elif (picture_on == 'SD1') or (picture_on == 'SD2'):
       MP = mountpoint(a,picture_on)

       if (MP == None):
           return False
       
       if (cp_device.mount_device(a,MP,'/mnt') == False):
           return False

       a.buff="" 
       a.send('cp {} /mnt/Image.bmp'.format(image))
       if (a.buff.find('cp:')!=-1):
            return False

       a.send('bmap /dev/fb0 /mnt/Image.bmp')

       if (cp_device.umount_device(a,'/mnt') == False):
           return False
       
    if (manual_judgement() == False):
        return False
       
 
    return True
        
def count_interrupt(a,port):
    
    if (port == 'HDMI0'):
        interrupt = HDMI0_INTR
    elif (port == 'HDMI1'):
        interrupt = HDMI1_INTR
    elif (port == 'VGA'):
        interrupt = VGA_INTR

    a.buff=""
    a.send('cat /proc/interrupts | grep {}'.format(interrupt))
     
    intr_before = int(a.find_str(interrupt,'grep {}'.format(interrupt)).split()[1])

    print ('\n\nPlease plug in and plug out {} cable and press any key to continue:\n'.format(port))
    sys.stdout.flush()

    raw_input()

    a.buff=""
    a.send('cat /proc/interrupts | grep {}'.format(interrupt))

    intr_after = int(a.find_str(interrupt,'grep {}'.format(interrupt)).split()[1])

    if (intr_after <= intr_before):
        return False


    return True

def fbdev_test(a,port,option,image):

    a.send('fbset -xres 800 -yres 600 -laced 0;fbset -xres 640 -yres 480 -laced 0')
    
    a.send('mount -t tmpfs -o size=20m tmpfs /tmp')

    a.send('cp {} /tmp/Image.bmp'.format(image))

    for i in option:
        a.buff=""
        a.send('fbset {}'.format(i))
        if (a.buff.find('fbset:')!=-1):
            return False
        a.send('bmap /dev/fb0 /tmp/Image.bmp')

    if (manual_judgement() == False):
        return False

    return True

def check_drm(a,no_option=False):

    total_err = 0
    encoder_id = {}
    possible_crtc = {}

    a.buff=""

    if (no_option == True):
        a.send('modetest -M rcar-du')
    else:
        a.send('modetest -M rcar-du -c')
    
    for i in PORT:
        if (a.buff.find(PORT[i])==-1):
            total_err += 1
        else:
            tmp = a.find_str(PORT[i]).split()[6]
            encoder_id.update({i:tmp})
    if (no_option == False):
        a.buff=""
        a.send('modetest -M rcar-du -e')
    
    for i in PORT:
        if (a.buff.find(encoder_id[i])==-1):
            total_err += 1
        else:
            tmp = a.find_str(encoder_id[i]).split()[3]

            if (i == 'VGA'):
                if (config.SOC == 'E3'):
                    tmp = int(tmp,16) - 1
                else:
                    tmp = int(tmp,16) + 1
                tmp = '0x{0:08X}'.format(tmp)

            possible_crtc.update({i:tmp})
      
    if (no_option == False):
        a.buff=""
        a.send('modetest -M rcar-du -p')

    for i in PORT:
        if (a.buff.find(possible_crtc[i])==-1):
            total_err += 1
    
    if (total_err > 0):
        return False

    return True
        
### Return (connector_ID,crtc_ID,plane_ID) #########
def check_properties(a,du_port,check_crtc=False,check_plane=False):
 
    crtc_ID = None
    possible_crtc = None
    plane_ID = []

    a.buff=""
  
    a.send('modetest -M rcar-du -c | grep {}'.format(PORT[du_port]))

    tmp = a.find_str(PORT[du_port],'grep')
    
    connector_ID = tmp.split()[0]

    encoder_ID = tmp.split()[6]

    if (check_crtc != False) or (check_plane != False):
        a.buff=""
        a.send('modetest -M rcar-du -e | grep {}'.format(encoder_ID))

        tmp = a.find_str(encoder_ID,'grep')

        crtc_ID = tmp.split()[1]
        possible_crtc = tmp.split()[3]

        if (du_port == 'VGA'):
            possible_crtc = int(possible_crtc,16) + 1
            possible_crtc = '0x{0:08X}'.format(possible_crtc)
         
        if (check_plane != False):
            a.buff=""
            a.send('modetest -M rcar-du -p | grep {}'.format(possible_crtc))

            for line in a.buff.splitlines():
                if (line.find(possible_crtc)!=-1) and (line.find('grep')==-1):
                    plane_ID.append(line.split()[0]) 
    
    # I do not know why crtc ID of VGA will be equal zero when executing 'modetest -M rcar-du -e' if HDMI(s) is/are plugged in
    # Maybe this cmd is just used to list encoders
    if (du_port == 'VGA'):
        if (config.SOC == 'H3'):
            num_lines = 50
        elif (config.SOC == 'M3N'):
            num_lines = 8
        elif (config.SOC == 'E3'):
            num_lines = 2

        a.buff=""
        a.send('modetest -M rcar-du | grep CRTCs: -A {} | tail -n 1'.format(num_lines))

        crtc_ID = a.find_str('(0,0)').split()[0]                 
   
    return (connector_ID,crtc_ID,plane_ID)

#this function support to get supported plane
def check_properties_plane(a,du_port,check_crtc=False,check_plane=False):

    crtc_ID = None
    possible_crtc = None
    plane_ID = []

    a.buff=""

    a.send('modetest -M rcar-du -c | grep {}'.format(PORT[du_port]))

    tmp = a.find_str(PORT[du_port],'grep')

    connector_ID = tmp.split()[0]

    encoder_ID = tmp.split()[6]

    if (check_crtc != False) or (check_plane != False):
        a.buff=""
        a.send('modetest -M rcar-du -e | grep {}'.format(encoder_ID))

        tmp = a.find_str(encoder_ID,'grep')

        crtc_ID = tmp.split()[1]

        if (int(crtc_ID) != 0):
            if(check_plane != False):
                a.buff=""
                a.send('modetest -M rcar-du -p | grep -w {}'.format(crtc_ID))

                for line in a.buff.splitlines():
                    if (line.find(crtc_ID)!=-1) and (line.find('grep')==-1) and (line.find('type')==-1) and (line.find('(')==-1):

                        if (line.split()[1] == crtc_ID):
                            plane_ID.append(line.split()[0])
        elif (int(crtc_ID) == 0):
            plane_ID.append(0)

    return (connector_ID,crtc_ID,plane_ID)    

def switch_screen(a,du_port):

    check_crtc = True
    check_plane = False
    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    a.buff=""
    a.send('modetest -M rcar-du -s {}@{}:1024x768@AR24'.format(connector_ID,crtc_ID),0,False)
    sleep(0.5)
    if (a.buff.find('failed')!=-1):
        return False
    sleep(4.5)
    
    if (manual_judgement() == False):
        a.send('\n')  
        return False
    else:
        a.send('\n')
        return True

def change_format_screen(a,du_port):
    
    check_crtc = True
    check_plane = True

    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    for plane in plane_ID:
        print('\n\n------PLANE {}-------'.format(plane))
        sys.stdout.flush()

        for i in ["RG16","AR15","XR24","AR24","UYVY","YUYV","NV12","NV21","NV16","NV61"]:
            a.buff=""
            a.send('modetest -M rcar-du -P {}@{}:800x600+20+20@{}'.format(plane,crtc_ID,i),0,False)
            sleep(0.5)
            if (a.buff.find('failed')!=-1):
                return False
            sleep(1.5)
    
    a.send('',0,False)
 
    if (manual_judgement() == False):
        return False
    
    return True

#this function will run for the supported plane on connection
def change_format_screen_plane(a,du_port):

    check_crtc = True
    check_plane = True

    connector_ID,crtc_ID,plane_ID = check_properties_plane(a,du_port,check_crtc,check_plane)

    print('\n\nPlease just plug in {} only, plug out all others and press any key to continue:'.format(du_port))
    sys.stdout.flush()

    raw_input()

    if (int(crtc_ID) != 0):
        for plane in plane_ID:
            print('\n\n------PLANE {}-------'.format(plane))
            sys.stdout.flush()

            for i in ["RG16","AR15","XR15","XR24","AR24","UYVY","YUYV","NV12","NV21","NV16","NV61"]:
                a.buff=""
                a.send('modetest -M rcar-du -P {}@{}:800x600+20+20@{}'.format(plane,crtc_ID,i),0,False)
                sleep(0.5)
                if (a.buff.find('failed')!=-1):
                    return False
                sleep(1.5)

        a.send('',0,False)

        if (manual_judgement() == False):
            return False
    elif (int(crtc_ID) == 0):
        return False

    return True

def change_resolution_screen(a,du_port):

    check_crtc = True
    check_plane = False

    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    if (du_port == 'VGA'):
        resolution = ["640x480","800x600","1024x768"]
    elif (du_port.find('HDMI')!=-1):
        if (config.SOC == 'E3'):
            resolution = ["640x480","800x600","1024x768","1280x720"]
        else:
            resolution = ["640x480","800x600","1024x768","1280x720","1920x1080i","1920x1080"]

    for i in resolution:
        a.buff=""
        a.send('modetest -M rcar-du -s {}@{}:{}@XR24'.format(connector_ID,crtc_ID,i),0,False)
        sleep(0.5)
        if (a.buff.find('failed')!=-1):
            return False

        sleep(4.5)

    a.send('',0,False)

    if (manual_judgement() == False):
        return False

    return True

def multiplane(a,du_port):

    check_crtc = True
    check_plane = True

    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    position = 20

    cmd = 'modetest -M rcar-du'

    for plane in plane_ID:
        cmd += (' -P {}@{}:200x200+{}+{}@AR24'.format(plane,crtc_ID,position,position))
        position += 100    

    a.buff=""
    a.send(cmd,0,False)
    sleep(0.5)
    if (a.buff.find('failed')!=-1):
        return False

    sleep(1)
  
    if (manual_judgement() == False):
        a.send('',0,False)
        return False

    a.send('',0,False)
   
    return True

def change_layer_position(a,du_port):
  
    check_crtc = True
    check_plane = False

    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    for position in ['20+20','150+150','250+250','668+468']:
        a.buff=""
        a.send('modetest -M rcar-du -d -s {}@{}:1024x768@XR24 -P @{}:400x200+{}@XR24'.format(connector_ID,crtc_ID,crtc_ID,position),0,False)
        sleep(0.5)
        if (a.buff.find('failed')!=-1):
            return False

        sleep(3.5)

    a.send('',0,False)

    if (manual_judgement() == False):
        return False

    return True
   

def abnormal_action(a,du_port,action="pullout"):

    check_crtc = True
    check_plane = False

    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    a.buff=""
    if (config.SOC == 'E3'):
        resolution = '1280x720'
    else:
        resolution = '1920x1080'

    a.send('modetest -M rcar-du -s {}@{}:{}@AR24'.format(connector_ID,crtc_ID,resolution),0,False)
    sleep(0.5)
    if (a.buff.find('failed')!=-1):
        return False

    if (action == 'pullout'):
        print('\nPlease plug out and plug in cable and press any key to continue:')
        sys.stdout.flush()

        raw_input()
    elif (action == 'Ctrl+C'):
        a.send('\x03')
        sleep(1)

    elif (action == 'Ctrl+Z'):
        a.send('\x1A')
        sleep(1)
        a.buff=""
        a.send('fg',0,False)
        if (a.buff.find('modetest')==-1):
            return False
 
    a.buff=""
    a.send('modetest -M rcar-du -s {}@{}:{}@AR24'.format(connector_ID,crtc_ID,resolution),0,False)
    sleep(0.5)
    if (a.buff.find('failed')!=-1):
        return False

    if (manual_judgement() == False):
        a.send('\n')
        return False
    else:
        a.send('\n')

def confirm_resolution(a,du_port):
   
    check_crtc = True
    check_plane = False

    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    if (du_port == 'HDMI0'):
        resolution = {'1024x768':True, '1023x767':False, '1024x767':False, '1025x767':False,'1023x768':False,\
                      '1023x769':False, '1024x769':False,'1025x768':False, '1025x769':False }

    elif (du_port == 'HDMI1'):
        resolution = {'1920x1080':True, '1920x1081':False, '1920x1079':False, '1921x1080':False, '1919x1080':False}
    
    elif (du_port == 'VGA'):
        resolution = {'640x480':True, '639x499':False, '640x499':False, '641x499':False, '639x480':False, '639x481':False, '640x481':False, '641x480':False, '641x481':False }

    for i in resolution:
        a.buff=""
        a.send('modetest -M rcar-du -s {}@{}:{}@XR24'.format(connector_ID,crtc_ID,i),0,False)
       
        if (a.buff.find('failed to find mode')!=-1):
            if (resolution[i]==True):
                return False
        else:
            sleep(3)
               
        sleep(2)
 
    a.send('',0,False)

    if (manual_judgement() == False):
        return False

    return True

def smp_concurrent_access(a,du_port):
 
    check_crtc = True
    check_plane = False

    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    size = config.NUM_CPU * 100

    for i in range(0,config.NUM_CPU):
        if (i < config.NUM_CPU-1):
            a.send('taskset -c {} modetest -M rcar-du -d -P @{}:{}x{}@XR24 &'.format(i,crtc_ID,size,size),0,False)
        else:
            a.send('taskset -c {} modetest -M rcar-du -d -P @{}:{}x{}@XR24'.format(i,crtc_ID,size,size),0,False)
        sleep(1)
        size -= 100

    sleep(3)
    a.send('killall -9 modetest')
    a.send('',0,False)

    if (manual_judgement() == False):
        return False

    return True

def smp_multi_port_access(a):
    
    check_crtc = True
    check_plane = False

    connector_ID_HDMI0,crtc_ID_HDMI0,plane_ID_HDMI0 = check_properties(a,'HDMI0',check_crtc,check_plane)
  
    connector_ID_VGA,crtc_ID_VGA,plane_ID_VGA = check_properties(a,'VGA',check_crtc,check_plane)
  
    for i in range(0,config.NUM_CPU):
        if (i%2==0):
            connector_ID = connector_ID_HDMI0
            crtc_ID = crtc_ID_HDMI0
        else:
            connector_ID = connector_ID_VGA
            crtc_ID = crtc_ID_VGA            

        a.buff=""        
        a.send('taskset -c {} modetest -M rcar-du -d -s {}@{}:1024x768@XR24 -v &'.format(i,connector_ID,crtc_ID),0,False)
        if (a.buff.find('Invalid argument')!=-1):
            a.send('killall -9 modetest')
            a.send('',0,False)

            return False

        sleep(5)
       
    sleep(1)
    a.send('ps -a')

    a.send('killall -9 modetest')
    a.send('',0,False)
    
    if (manual_judgement() == False):
        return False

    return True

   
def smp_multi_instance_test(a):

    check_crtc = True
    check_plane = False

    connector_ID_HDMI0,crtc_ID_HDMI0,plane_ID_HDMI0 = check_properties(a,'HDMI0',check_crtc,check_plane)

    connector_ID_HDMI1,crtc_ID_HDMI1,plane_ID_HDMI1 = check_properties(a,'HDMI1',check_crtc,check_plane)

    connector_ID_VGA,crtc_ID_VGA,plane_ID_VGA = check_properties(a,'VGA',check_crtc,check_plane)
   
    a.send('taskset -c 0 modetest -M rcar-du -d -s {}@{}:1024x768@XR24 -v -s {}@{}:1024x768@XR24 -v -s {}@{}:1024x768@XR24'.format(connector_ID_HDMI0,crtc_ID_HDMI0,connector_ID_HDMI1,crtc_ID_HDMI1,connector_ID_VGA,crtc_ID_VGA),0,False)

    sleep(8)

    a.send('',0,False)
 
    if (manual_judgement() == False):
        return False

    return True
         
def stress_test(a,du_port,stress_time): 

    check_crtc = True
    check_plane = False

    connector_ID,crtc_ID,plane_ID = check_properties(a,du_port,check_crtc,check_plane)

    a.buff=""
    a.send('stress --cpu {} --io {} --vm {} --vm-bytes 20M --timeout {}s &'.format(config.NUM_CPU,config.NUM_CPU*2,config.NUM_CPU,stress_time))

    START = time()

    while (time() - START < stress_time):
         a.buff=""
         a.send('modetest -M rcar-du -d -P @{}:400x400@XR24'.format(crtc_ID),0.001,False)
         sleep(0.5)
         if (a.buff.find('failed')!=-1):
             return False

 
    a.wait('successful run completed')

    a.send('',0,False)

    if (manual_judgement() == False):
        return False


def kmsxx_autotest(a):

    if (config.PLATFORM.find('ulcb')!=-1):
        du_port = {'HDMI0':0}
    elif (config.PLATFORM.find('salvator-x')!=-1):
        if (config.SOC == 'H3'):
            du_port = {'VGA':0,'HDMI0':1, 'HDMI1':2}
        elif (config.SOC == 'M3N') or (config.SOC == 'M3'):
            du_port = {'VGA':0,'HDMI0':1}
    elif (config.PLATFORM.find('ebisu')!=-1):
        du_port = {'VGA':0,'HDMI0':1}
    
    a.send('cd {}'.format(AUTOTEST_FOLDER))

    total_err = 0

    for i in du_port:
        print('\n\nPlease just plug in {} only, plug out all others and press any key to continue:'.format(i))
        sys.stdout.flush()
       
        raw_input()

        a.buff=""
        a.send('bash run_tests.sh {}'.format(du_port[i]))
   
        if(a.buff.find('Kernel panic')!=-1):
            return False
 
        total_err += int(a.find_str('failed').split()[2])

    a.send('cd ~')

    if (total_err > 0):
        return False
    
    return True 

def write_back_V4L2(a):

    a.buff=""
    a.send(' grep -l fea38000 /sys/class/video4linux/video*/name')

    a.buff=""
    a.send('kmstest --flip')

    a.send('kmstest flip')

    if (manual_judgement() == False):
        return False

    return True
    
