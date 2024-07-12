#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config
import subprocess
import random
import s2ram

#######################################################
def mount_device(a,mountpoint1,mountpoint2='/mnt/'):

    a.buff=""
    a.send('mount /dev/{} {}'.format(mountpoint1,mountpoint2))
    #config.wait(a,'root@{}'.format(config.PLATFORM))

    if (a.buff.find('already mounted')!=-1):
        a.send('umount /dev/{}'.format(mountpoint1))
        #a.buff=""
        #config.wait(a,'root@{}'.format(config.PLATFORM))
        
        a.buff=""
        a.send('mount /dev/{} {}'.format(mountpoint1,mountpoint2))
        #a.buff=""
        #config.wait(a,'root@{}'.format(config.PLATFORM))
   
    if (a.buff.find('warning: mounting fs with errors, running e2fsck is recommended')!=-1) \
      or (a.buff.find('wrong fs type, bad option, bad superblock')!=-1):
        a.send('umount /dev/{}'.format(mountpoint1))
 
        a.send('echo y | mkfs.ext4 /dev/{}'.format(mountpoint1))

        a.send('mount /dev/{} {}'.format(mountpoint1,mountpoint2)) 

    if (a.buff.find('mounted filesystem')==-1):
        return(False)
    
    return(True)
                 
#######################################################
def umount_device(a,mountpoint='/mnt'):

    a.buff=""
    a.send('umount {}'.format(mountpoint))
    #a.buff=""
    #config.wait(a,'root@{}'.format(config.PLATFORM))

    if (a.buff.find('umount: {}'.format(mountpoint))!=-1):
       return(False)

    return(True)
    
#######################################################
def equal_megabyte(size):

    if (size[len(size)-1]=='G'):
        size = size.replace(size[len(size)-1],'',1)
        size = int(float(size)*1024)

    elif (size[len(size)-1]=='M'):
        size = size.replace(size[len(size)-1],'',1)
        size = int(float(size))

    elif (size[len(size)-1]=='K'):
        size = size.replace(size[len(size)-1],'',1)
        size = int(float(size)/1024)
    else:
        size = int(float(size))
  
    return(size)
    

#########################################################
def cp_ram_to_device(a,mountpoint,size,data="no_data",time=1):
   
    if (mountpoint == None): return False 

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file-{}M bs=1M count={}'.format(size,size),0.005)

    if (a.buff.find('dd:')!=-1):
        return False
 
    if (mount_device(a,mountpoint) == False):
        return False
   
    if (data == "no_data"): 
        a.send('rm -rf /mnt/*; sync')
    elif (data == "has_data"):
        a.send('dd if=/dev/urandom of=/mnt/file-50m bs=1M count=50; sync')

    ERR_COUNT=0
    for i in range(1,time+1):
        
        if (time > 1):
            print ('\n\n----------- TIME {} -----------'.format(i))
            if (i > 1):
                a.buff=""
                a.send('dd if=/dev/urandom of=/tmp/file-{}M bs=1M count={}'.format(size,size))

        a.send('cp /tmp/file-{}M /mnt/'.format(size))

        a.buff="" 
        a.send('md5sum /tmp/file-{}M /mnt/file-{}M'.format(size,size))

        if (a.buff.find('exception Emask') != -1):
            return False

        MD5SUM_SRC = a.find_str('/tmp/file-{}M'.format(size),'md5sum').split()[0]
        MD5SUM_DST = a.find_str('/mnt/file-{}M'.format(size),'md5sum').split()[0]

        if (MD5SUM_SRC != MD5SUM_DST):
           ERR_COUNT = ERR_COUNT + 1
 
    if (umount_device(a) == False):
        return False   
   
    a.send('rm /tmp/file-{}M'.format(size))

    if (ERR_COUNT != 0):
        return False

    return(True)  
    
#################################################################

def cp_ram_to_device_umount_after_bind(a,mountpoint,size,data="no_data",time=1):

    if (mountpoint == None): return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file-{}M bs=1M count={}'.format(size,size))

    if (a.buff.find('dd:')!=-1):
        return False

    if (umount_device(a) == False):
        return False

    if (mount_device(a,mountpoint) == False):
        return False

    if (data == "no_data"):
        a.send('rm -rf /mnt/*; sync')
    elif (data == "has_data"):
        a.send('dd if=/dev/urandom of=/mnt/file-50m bs=1M count=50; sync')

    ERR_COUNT=0
    for i in range(1,time+1):

        if (time > 1):
            print ('\n\n----------- TIME {} -----------'.format(i))
            if (i > 1):
                a.buff=""
                a.send('dd if=/dev/urandom of=/tmp/file-{}M bs=1M count={}'.format(size,size))

        a.send('cp /tmp/file-{}M /mnt/'.format(size))

        a.buff=""
        a.send('md5sum /tmp/file-{}M /mnt/file-{}M'.format(size,size))

        MD5SUM_SRC = a.find_str('/tmp/file-{}M'.format(size),'md5sum').split()[0]
        MD5SUM_DST = a.find_str('/mnt/file-{}M'.format(size),'md5sum').split()[0]

        if (MD5SUM_SRC != MD5SUM_DST):
           ERR_COUNT = ERR_COUNT + 1

    if (umount_device(a) == False):
        return False

    a.send('rm /tmp/file-{}M'.format(size))

    if (ERR_COUNT != 0):
        return False

    return(True)

#################################################################

def cp_folder_to_device(a,mountpoint,stage,size,data="no_data"):

    if (mountpoint == None): return False

    a.buff=""

    tmp_dir=""

    for i in range (1,stage+1):
        tmp_dir="{}/stage{}".format(tmp_dir,i)
   
    a.send('mkdir -p /tmp{}'.format(tmp_dir))
    sleep(0.5)        

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp{}/file-{}M bs=1M count={}'.format(tmp_dir,size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    if (mount_device(a,mountpoint) == False):
        return False

    if (data == "no_data"):
        a.send('rm -rf /mnt/*; sync')
        #a.buff=""
        #config.wait(a,'root@{}'.format(config.PLATFORM))
    elif (data == "has_data"):
        a.send('dd if=/dev/urandom of=/mnt/file-50m bs=1M count=50; sync')
        #a.buff=""
        #config.wait(a,'root@{}'.format(config.PLATFORM))

    a.send('cp -r /tmp/stage1 /mnt/'.format(size))
    #a.buff=""
    #sleep(0.5)

    #config.wait(a,'root@{}'.format(config.PLATFORM))

    a.buff=""
    a.send('md5sum /tmp{}/file-{}M /mnt{}/file-{}M'.format(tmp_dir,size,tmp_dir,size))
    #sleep(0.5)

    #config.wait(a,'root@{}'.format(config.PLATFORM))

    MD5SUM_SRC = a.find_str('/tmp{}/file-{}M'.format(tmp_dir,size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt{}/file-{}M'.format(tmp_dir,size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    if (umount_device(a) == False):
        return False
 
    a.send('rm -rf /tmp/stage1')
 
    return(True)




##################################################################
def cp_device_to_ram(a,mountpoint,size,time=1):

    if (mountpoint == None): return False
    
    if (mount_device(a,mountpoint) == False):
        return(False)
     
    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/file-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False
   
    ERR_COUNT=0
    for i in range(1,time+1):

        if (time > 1):
            print ('\n\n----------- TIME {} -----------'.format(i))
            if (i > 1):
                a.buff=""
                a.send('dd if=/dev/urandom of=/mnt/file-{}M bs=1M count={}'.format(size,size))
                if (a.buff.find('dd:')!=-1):
                    return False

        a.send('cp /mnt/file-{}M /tmp/'.format(size))
    
        a.buff=""
        a.send('md5sum /tmp/file-{}M /mnt/file-{}M'.format(size,size))

        MD5SUM_SRC = a.find_str('/tmp/file-{}M'.format(size),'md5sum').split()[0]
        MD5SUM_DST = a.find_str('/mnt/file-{}M'.format(size),'md5sum').split()[0]

        if (MD5SUM_SRC != MD5SUM_DST):
           ERR_COUNT = ERR_COUNT + 1

    if (umount_device(a)==False):
        return(False)

    a.send('rm /tmp/file-{}M'.format(size))

    if (ERR_COUNT != 0):
        return False

    return(True)

##############################################################################
def cp_folder_to_ram(a,mountpoint,stage,size):

    if (mountpoint == None): return False

    if (mount_device(a,mountpoint) == False):
        return False
    
    a.buff=""
    
    tmp_dir=""

    for i in range (1,stage+1):
        tmp_dir="{}/stage{}".format(tmp_dir,i)

    a.send('mkdir -p /mnt{}'.format(tmp_dir))
    #sleep(0.5)

    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt{}/file-{}M bs=1M count={}'.format(tmp_dir,size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    a.send('cp -r /mnt/stage1 /tmp/'.format(size))
    #a.buff=""
    #sleep(0.5)

    #config.wait(a,'root@{}'.format(config.PLATFORM))

    a.buff=""
    a.send('md5sum /mnt{}/file-{}M /tmp{}/file-{}M'.format(tmp_dir,size,tmp_dir,size))
    #a.buff=""
    #sleep(0.5)

    #config.wait(a,'root@{}'.format(config.PLATFORM))

    MD5SUM_SRC = a.find_str('/tmp{}/file-{}M'.format(tmp_dir,size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt{}/file-{}M'.format(tmp_dir,size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    if (umount_device(a) == False):
        return False

    a.send('rm /tmp{}/file-{}M'.format(tmp_dir,size))

    return(True)



###############################################################################
def cp_no_space_left(a,mountpoint):

    if (mountpoint == None): return False

    if (mount_device(a,mountpoint) == False):
        return False

    a.buff=""
    a.send('df -h /mnt')
    #sleep(0.5)
   
    SIZE_CAP = equal_megabyte(a.buff.splitlines()[3].split()[1])
    USED_CAP = equal_megabyte(a.buff.splitlines()[3].split()[2])
   
    AVAIL_CAP = SIZE_CAP - USED_CAP  
    #AVAIL_CAP = equal_megabyte(a.buff.splitlines()[3].split()[3])
        
    if (AVAIL_CAP >= 200):
        a.buff=""
        a.send('dd if=/dev/urandom of=/mnt/file-{}M bs=1M count={}'.format(AVAIL_CAP-200,AVAIL_CAP-200))
        
        TIME_OUT = int(AVAIL_CAP/0.5)
        #config.wait(a,'MB/s',TIME_OUT)
 
        a.send('df -h /mnt')
        #sleep(0.5)

 
    RANDOM = random.random()

    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/file-{} bs=1M count=300'.format(RANDOM))

    if (a.buff.find('No space left on device')!=-1):
        a.buff=""
        a.send('mount tmpfs /tmp -t tmpfs -o size=400m')
        a.send('dd if=/dev/urandom of=/tmp/file-100m bs=1M count=100')
        a.send('cp /tmp/file-100m /mnt')

    #a.buff=""
    #config.wait(a,'root@{}'.format(config.PLATFORM))

    if (a.buff.find('No space left on device')==-1):
        if (AVAIL_CAP >=200):
            a.send('rm /mnt/file-{}M; rm /mnt/file-{}; rm /tmp/file-100m'.format(AVAIL_CAP-200, RANDOM))
        else:
            a.send('rm /mnt/file-{}; rm /tmp/file-100m'.format(RANDOM))
        #a.buff=""
        #config.wait(a,'root@{}'.format(config.PLATFORM))

        umount_device(a)
        return False
   
    if (AVAIL_CAP >=200): 
        a.send('rm /mnt/file-{}M; rm /mnt/file-{}; rm /tmp/file-100m'.format(AVAIL_CAP-200, RANDOM))
    else:
        a.send('rm /mnt/file-{}; rm /tmp/file-100m'.format(RANDOM))
    
    #a.buff=""
    #config.wait(a,'root@{}'.format(config.PLATFORM))
    
    if (umount_device(a)==False):
       return(False)
        
    return True



################################################################################
def write_speed(a,mountpoint,expectation):

    if (mountpoint == None): return False

    size=350

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    a.send('sync')
    #a.buff=""
    #config.wait(a,'root@{}'.format(config.PLATFORM))
    
    if (mount_device(a,mountpoint)==False):
        return False   
 
    a.buff=""
    a.send('time cp /tmp/file-{}M /mnt/; time umount /mnt'.format(size))

    #config.wait(a,'root@{}'.format(config.PLATFORM))
    
    speed_buff=a.buff  
   
    if (a.buff.find('umount: /mnt')!=-1):
       return(False)

    a.buff=""
    a.send('mount /dev/{} /mnt'.format(mountpoint))
    #sleep(0.5)

    if (a.buff.find('mounted filesystem')==-1):
        return(False)


    a.buff=""    
    a.send('md5sum /tmp/file-{}M /mnt/file-{}M'.format(size,size))

    #config.wait(a,'root@{}'.format(config.PLATFORM))
    
    MD5SUM_SRC = a.find_str('/tmp/file-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/file-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)
    
    TIME_TOTAL=0

    for i in [3,4,5,8,9,10]:
        TIME_TOTAL = TIME_TOTAL + float(speed_buff.splitlines()[i].split()[1].split("m")[0])
        TIME_TOTAL = TIME_TOTAL + float (speed_buff.splitlines()[i].split()[1].split("m")[1].split("s")[0])
    
    SPEED = round(float(size)/TIME_TOTAL, 2)

    print ("\n \n SPEED = {} MB/s".format(SPEED))

    if (umount_device(a)==False):
        return False

    if (SPEED < expectation):
        return(False)

    a.send('rm /tmp/file-{}M'.format(size))
    
    return(True)


################################################################################

def read_speed(a,mountpoint,expectation):

    if (mountpoint == None): return False

    size=350

    a.buff=""
    a.send('rm -rf /tmp/file-{}M'.format(size))
    
    a.send('sync')
    #config.wait(a,'root@{}'.format(config.PLATFORM))
   
    if (mount_device(a,mountpoint)==False):
        return(False)
   
    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/file-{}M bs=1M count={}; sync'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False
   
    a.send('echo 3 > /proc/sys/vm/drop_caches')

    #config.wait(a,'MB/s')

    #a.buff=""
    #config.wait(a,'root@{}'.format(config.PLATFORM))
 
    a.buff=""
    a.send('time cp /mnt/file-{}M /tmp/; time umount /mnt'.format(size))

    #config.wait(a,'root@{}'.format(config.PLATFORM))

    speed_buff=a.buff

    if (a.buff.find('umount: /mnt')!=-1):
       return(False)

    a.buff=""
    a.send('mount /dev/{} /mnt'.format(mountpoint))
    #sleep(0.5)

    if (a.buff.find('mounted filesystem')==-1):
        return(False)


    a.buff=""
    a.send('md5sum /tmp/file-{}M /mnt/file-{}M'.format(size,size))

    #config.wait(a,'root@{}'.format(config.PLATFORM))

    MD5SUM_SRC = a.find_str('/tmp/file-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/file-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    TIME_TOTAL=0

    for i in [3,4,5,8,9,10]:
        #print(speed_buff.splitlines()[i])
        if (speed_buff.splitlines()[i].split()[0]=="real" or speed_buff.splitlines()[i].split()[0]=="user" or speed_buff.splitlines()[i].split()[0]=="sys"):
            TIME_TOTAL = float(TIME_TOTAL) + float(speed_buff.splitlines()[i].split()[1].split("m")[0])
            TIME_TOTAL = float(TIME_TOTAL) + float(speed_buff.splitlines()[i].split()[1].split("m")[1].split("s")[0])

    SPEED = round(float(size)/TIME_TOTAL, 2)

    print ("\n \n SPEED = {} MB/s".format(SPEED))

    if (umount_device(a)==False):
        return False

    if (SPEED < expectation):
        return(False)
   
    a.send('rm /tmp/file-{}M'.format(size))

    return(True)

############################################################################
def cp_between_two_device(a,mountpoint1,mountpoint2,size):

    if (mountpoint1 == None): return False
    if (mountpoint2 == None): return False

    a.send('mkdir -p /mnt/de1')
    a.send('mkdir -p /mnt/de2')

    if (mount_device(a,mountpoint1,'/mnt/de1') == False):
        return False
    
    if (mount_device(a,mountpoint2,'/mnt/de2') == False):
        return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/de1/file-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False
 
    a.send('sync') 
    
    a.send('cp /mnt/de1/file-{}M /mnt/de2/'.format(size))

    a.buff=""
    a.send('md5sum /mnt/de1/file-{}M /mnt/de2/file-{}M'.format(size,size))

    MD5SUM_SRC = a.find_str('/mnt/de1/file-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/de2/file-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    if (umount_device(a,'/mnt/de1/')==False) or (umount_device(a,'/mnt/de2/')==False):
        return(False)

    a.send('rm -rf /mnt/de1; rm -rf /mnt/de2')

    return(True)

############################################################################
def cp_between_two_device_both_two_direct(a,mountpoint1,mountpoint2,size):

    if (mountpoint1 == None): return False
    if (mountpoint2 == None): return False

    a.send('mkdir -p /mnt/de1')
    a.send('mkdir -p /mnt/de2')

    if (mount_device(a,mountpoint1,'/mnt/de1') == False):
        return False

    if (mount_device(a,mountpoint2,'/mnt/de2') == False):
        return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/de1/file1-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/de2/file2-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    a.send('sync')

    
    a.send('cp /mnt/de1/file1-{}M /mnt/de2/'.format(size))

    a.send('cp /mnt/de2/file2-{}M /mnt/de1/'.format(size))

    a.buff=""
    a.send('md5sum /mnt/de1/file1-{}M /mnt/de2/file1-{}M'.format(size,size))

    MD5SUM_SRC = a.find_str('/mnt/de1/file1-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/de2/file1-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    a.buff=""
    a.send('md5sum /mnt/de1/file2-{}M /mnt/de2/file2-{}M'.format(size,size))

    MD5SUM_SRC = a.find_str('/mnt/de1/file2-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/de2/file2-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    if (umount_device(a,'/mnt/de1/')==False) or (umount_device(a,'/mnt/de2/')==False):
        return(False)

    a.send('rm -rf /mnt/de1; rm -rf /mnt/de2')

    return(True)


################################################################################
def cp_folder_between_two_device(a,mountpoint1,mountpoint2,stage,size):

    if (mountpoint1 == None): return False
    if (mountpoint2 == None): return False

    a.send('mkdir -p /mnt/de1')
    a.send('mkdir -p /mnt/de2')

    if (mount_device(a,mountpoint1,'/mnt/de1') == False) or (mount_device(a,mountpoint2,'/mnt/de2')==False):
        return False

    a.buff=""

    tmp_dir=""

    for i in range (1,stage+1):
        tmp_dir="{}/stage{}".format(tmp_dir,i)

    a.send('mkdir -p /mnt/de1{}'.format(tmp_dir))

    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/de1{}/file-{}M bs=1M count={}'.format(tmp_dir,size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    a.send('cp -r /mnt/de1/stage1 /mnt/de2/'.format(size))

    a.buff=""
    a.send('md5sum /mnt/de1{}/file-{}M /mnt/de2{}/file-{}M'.format(tmp_dir,size,tmp_dir,size))
    #a.buff=""
    #sleep(0.5)

    #config.wait(a,'root@{}'.format(config.PLATFORM))

    MD5SUM_SRC = a.find_str('/mnt/de1{}/file-{}M'.format(tmp_dir,size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/de2{}/file-{}M'.format(tmp_dir,size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    if (umount_device(a,'/mnt/de1') == False) or (umount_device(a,'/mnt/de2')==False):
        return False

    a.send('rm -rf /mnt/de1/; rm -rf /mnt/de2/')

    return(True)


##################################################################################################
def cp_RAM_to_two_device_simultaneously(a,mountpoint1,mountpoint2,size):

    if (mountpoint1 == None): return False
    if (mountpoint2 == None): return False

    a.send('mkdir -p /mnt/de1')
    a.send('mkdir -p /mnt/de2')

    if (mount_device(a,mountpoint1,'/mnt/de1') == False):
        return False

    if (mount_device(a,mountpoint2,'/mnt/de2') == False):
        return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file1-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False
   
    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file2-{}M bs=1M count={}'.format(size,size)) 
    if (a.buff.find('dd:')!=-1):
        return False

    a.send('sync')

    a.send('cp /tmp/file1-{}M /mnt/de1/ & cp /tmp/file2-{}M /mnt/de2/'.format(size,size))

    TIME_OUT=0

    while (TIME_OUT < 40):
        a.buff=""
        a.send('ps -a')

        if (a.buff.find('cp')!=-1):
            TIME_OUT = TIME_OUT + 1
            sleep(5)
        else:
            break
	
    a.send('sync')
	
    a.buff=""
    a.send('md5sum /tmp/file1-{}M /mnt/de1/file1-{}M'.format(size,size))

    MD5SUM_SRC = a.find_str('/tmp/file1-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/de1/file1-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    a.buff=""
    a.send('md5sum /tmp/file2-{}M /mnt/de2/file2-{}M'.format(size,size))

    MD5SUM_SRC = a.find_str('/tmp/file2-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/de2/file2-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)


    if (umount_device(a,'/mnt/de1/')==False) or (umount_device(a,'/mnt/de2/')==False):
        return(False)

    a.send('rm -rf /mnt/de1; rm -rf /mnt/de2')

    a.send('rm /tmp/file1-{}M; rm /tmp/file2-{}M'.format(size,size))

    return(True)

#########################################################################################
def cp_two_device_to_RAM_simultaneously(a,mountpoint1,mountpoint2,size):

    if (mountpoint1 == None): return False
    if (mountpoint2 == None): return False

    a.send('mkdir -p /mnt/de1')
    a.send('mkdir -p /mnt/de2')

    if (mount_device(a,mountpoint1,'/mnt/de1') == False):
        return False

    if (mount_device(a,mountpoint2,'/mnt/de2') == False):
        return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/de1/file1-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/mnt/de2/file2-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    a.send('sync')

    a.send('cp /mnt/de1/file1-{}M /tmp/ & cp /mnt/de2/file2-{}M /tmp/'.format(size,size))

    TIME_OUT=0

    while (TIME_OUT < 40):
        a.buff=""
        a.send('ps -a')

        if (a.buff.find('cp')!=-1):
            TIME_OUT = TIME_OUT + 1
            sleep(5)
        else:
            break

    a.buff=""
    a.send('md5sum /mnt/de1/file1-{}M /tmp/file1-{}M'.format(size,size))

    MD5SUM_SRC = a.find_str('/tmp/file1-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/de1/file1-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    a.buff=""
    a.send('md5sum /mnt/de2/file2-{}M /tmp/file2-{}M'.format(size,size))

    MD5SUM_SRC = a.find_str('/tmp/file2-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/de2/file2-{}M'.format(size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)


    if (umount_device(a,'/mnt/de1/')==False) or (umount_device(a,'/mnt/de2/')==False):
        return(False)


################################################################################################
def cp_between_two_simultanesouly(a,mountpoint1,mountpoint2,size,time=1):

    if (mountpoint1 == None) and (mountpoint1 != "RAM"): return False
    if (mountpoint2 == None) and (mountpoint2 != "RAM"): return False

    if (mountpoint1 != "RAM") and (mountpoint2!="RAM"):
        a.send('mkdir -p /mnt/de1')
        a.send('mkdir -p /mnt/de2')
        DIR_1 = "/mnt/de1"
        DIR_2 = "/mnt/de2"
    
        if (mount_device(a,mountpoint1,'/mnt/de1') == False):
            return False

        if (mount_device(a,mountpoint2,'/mnt/de2') == False):
            return False

    else:
        if(mountpoint1 == "RAM"):
            DIR_1 = "/tmp"
            DIR_2 = "/mnt"
            if (mount_device(a,mountpoint2) == False):
                return False
        else:
            DIR_1="/mnt"
            DIR_2="/tmp"
            if (mount_device(a,mountpoint1) == False):
                return False

    for i in range(0,time):
    
        a.buff=""
        a.send('dd if=/dev/urandom of={}/file1-{}M bs=1M count={}'.format(DIR_1,size,size))
        if (a.buff.find('dd:')!=-1):
            return False
 
        a.buff=""
        a.send('dd if=/dev/urandom of={}/file2-{}M bs=1M count={}'.format(DIR_2,size,size))
        if (a.buff.find('dd:')!=-1):
            return False

        a.send('sync')

        a.send('cp {}/file1-{}M {}/ & cp {}/file2-{}M {}/'.format(DIR_1,size,DIR_2,DIR_2,size,DIR_1))

        TIME_OUT=0

        while (TIME_OUT < 40):
            a.buff=""
            a.send('ps -a')

            if (a.buff.find('cp')!=-1):
                TIME_OUT = TIME_OUT + 1
                sleep(5)
            else:
                break

        a.buff=""
        a.send('md5sum {}/file1-{}M {}/file1-{}M'.format(DIR_1,size,DIR_2,size))

        MD5SUM_SRC = a.find_str('{}/file1-{}M'.format(DIR_1,size),'md5sum').split()[0]
        MD5SUM_DST = a.find_str('{}/file1-{}M'.format(DIR_2,size),'md5sum').split()[0]

        if (MD5SUM_SRC != MD5SUM_DST):
           return False

        a.buff=""
        a.send('md5sum {}/file2-{}M {}/file2-{}M'.format(DIR_1,size,DIR_2,size))

        MD5SUM_SRC = a.find_str('{}/file2-{}M'.format(DIR_1,size),'md5sum').split()[0]
        MD5SUM_DST = a.find_str('{}/file2-{}M'.format(DIR_2,size),'md5sum').split()[0]

        if (MD5SUM_SRC != MD5SUM_DST):
           return False

    if (mountpoint1!="RAM") and (mountpoint2!="RAM"):
        if (umount_device(a,'/mnt/de1/')==False) or (umount_device(a,'/mnt/de2/')==False):
           return False
        a.send('rm -rf /mnt/de1; rm -rf /mnt/de2')
    else:
        if (umount_device(a) == False):
           return False

    if (mountpoint1 == 'RAM') or (mountpoint2 == 'RAM'):
        a.send('rm /tmp/file1-{}M ; rm /tmp/file2-{}M'.format(size,size))

    return(True)

def cp_ram_to_device_while_doing_st(a,mountpoint,size,command):
 
    if (mountpoint == None): return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    if (mount_device(a,mountpoint) == False):
        return False

    a.send('cp /tmp/file-{}M /mnt/ & '.format(size))
   
    a.send('{}'.format(command),0,False)
 
    sleep(2)

    return(True)

def cp_ram_to_device_interrupt (a,mountpoint,size,command):

    if (mountpoint == None): return False

    a.buff=""
    a.send('dd if=/dev/urandom of=/tmp/file-{}M bs=1M count={}'.format(size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    if (mount_device(a,mountpoint) == False):
        return False

    sleep(0.25)

    a.send('cp /tmp/file-{}M /mnt/'.format(size),0,False)

    if (command == 'ctrl+C'):
        a.send('\x03')
        sleep(1)
        if (umount_device(a) == False): 
            return False
         
        if (mount_device(a,mountpoint) == False): 
            return False

        a.send('cp /mnt/file-{}M /tmp/'.format(size))

    elif (command == 'ctrl+Z'):
        a.send('\x1A')
        sleep(1)
        
        if (a.buff.find('Stopped(SIGTSTP)') == -1):
            return False

        a.send('fg')
    
    a.buff=""
    a.send('md5sum /tmp/file-{}M /mnt/file-{}M'.format(size,size))

    MD5SUM_SRC = a.find_str('/tmp/file-{}M'.format(size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('/mnt/file-{}M'.format(size),'md5sum').split()[0]


    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)
     
    if (umount_device(a)==False):
       return(False)

    a.send('rm /tmp/file-{}M'.format(size))

    return True   

def cp_s2ram(a,source,dest,size,while_cp=False,umount_aft_s2ram=True,two_direction=False):

    if (source == None): return False
    if (dest == None): return False
   
    if (source != 'RAM') and (dest != 'RAM') :
        SRC_DIR='/mnt/de1'
        DST_DIR='/mnt/de2'

        a.send('mkdir -p {}'.format(SRC_DIR))
        a.send('mkdir -p {}'.format(DST_DIR))

        if (mount_device(a,source,SRC_DIR)==False):
            return False
    
        if (mount_device(a,dest,DST_DIR)==False):
            return False
    elif (source == 'RAM'):
        SRC_DIR='/tmp'
        DST_DIR='/mnt'

        if (mount_device(a,dest,DST_DIR)==False):
            return False
    else:
        SRC_DIR='/mnt'
        DST_DIR='/tmp'
 
        if (mount_device(a,source,SRC_DIR)==False):
            return False

    a.buff=""
    a.send('dd if=/dev/urandom of={}/file-{}M bs=1M count={}'.format(SRC_DIR,size,size))
    if (a.buff.find('dd:')!=-1):
        return False

    if (two_direction == True):
        a.buff=""
        a.send('dd if=/dev/urandom of={}/file-{}M_2 bs=1M count={}'.format(DST_DIR,size,size))
        if (a.buff.find('dd:')!=-1):
            return False

    a.send('sync')
    
    if (while_cp == False):    
        a.send('cp {}/file-{}M {}/'.format(SRC_DIR,size,DST_DIR))
        if (s2ram.pm_suspend(a)==False):
            return False
    else:
        if (s2ram.pm_suspend_while_doing_st(a,'cp {}/file-{}M {}/ &'.format(SRC_DIR,size,DST_DIR))==False):
            return False
    
    if (s2ram.pm_wakeup(a)==False):
        return False
        
    if (while_cp == False):
        if (umount_aft_s2ram == True):                
            if (source == 'RAM'):
                if (umount_device(a,DST_DIR)==False):
                    return False
                if (mount_device(a,dest,DST_DIR)==False):
                    return False
            elif (dest == 'RAM'):
                if (umount_device(a,SRC_DIR)==False):
                    return False
                if (mount_device(a,source,SRC_DIR)==False):
                    return False

        a.send('cp {}/file-{}M {}/'.format(SRC_DIR,size,DST_DIR))     
        
        if (two_direction == True):
            a.send('cp {}/file-{}M_2 {}/'.format(DST_DIR,size,SRC_DIR))
        

    else:
        a.buff=""
        a.send('ps -a') 

        TIME_OUT = 0
        
        while (a.buff.find('cp')!=-1):
            sleep(5)
            TIME_OUT = TIME_OUT + 5
            if (TIME_OUT > 3600):
                return False
            a.buff=""
            a.send('ps -a')
         
    a.buff=""
    a.send('md5sum {}/file-{}M {}/file-{}M'.format(SRC_DIR,size,DST_DIR,size))

    MD5SUM_SRC = a.find_str('{}/file-{}M'.format(SRC_DIR,size),'md5sum').split()[0]
    MD5SUM_DST = a.find_str('{}/file-{}M'.format(DST_DIR,size),'md5sum').split()[0]

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)
   
    if (two_direction == True):
        a.buff=""
        a.send('md5sum {}/file-{}M_2 {}/file-{}M_2'.format(SRC_DIR,size,DST_DIR,size))

        MD5SUM_SRC = a.find_str('{}/file-{}M_2'.format(SRC_DIR,size),'md5sum').split()[0]
        MD5SUM_DST = a.find_str('{}/file-{}M_2'.format(SRC_DIR,size),'md5sum').split()[0]
         
        if (MD5SUM_SRC != MD5SUM_DST):
            return(False)

    if (MD5SUM_SRC != MD5SUM_DST):
       return(False)

    if (source != 'RAM') and (dest != 'RAM') :
        if (umount_device(a,SRC_DIR)==False):
            return False
        if (umount_device(a,DST_DIR)==False):
            return False
    else:
        if (umount_device(a)==False):
            return False

        a.send('rm /tmp/file-{}M'.format(size))
        if (two_direction == True):
            a.send('rm /tmp/file-{}M_2'.format(size))

    return(True)
        
 

