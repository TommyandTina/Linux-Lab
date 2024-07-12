#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath(".."))
import config
sys.path.append(os.path.relpath("../common/"))
import conserial
import print_result
import usb
import restart_board
import time
import s2ram

TEST_USB2_PFM = False
TEST_USB3_PFM = True

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1, usb.MODULE_TEST)
    a.start()

    restart_board.main(a)
    #####################################################################################################
    print("\nPrepare \n")
    print("\nPlug in USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    mountpoint = usb.wait_usb3h(a = a, insert = True)
    a.send("mkdir -p /mnt/usb")
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    if a.buff.find("wrong fs type, bad option, bad superblock on"):
        a.send('echo y | mkfs.ext4 /dev/{}'.format(mountpoint))
        a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("dd if=/dev/urandom of=testdata bs=10M count=50")
    a.send("cp testdata /mnt/usb/")
    a.send("umount /mnt/usb")
    print("\nPull out USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()

    #####################################################################################################

    print("\n\n----------Item 1----------\n")
    sys.stdout.flush()
    a.buff = ""
    if (s2ram.pm_suspend(a)==False):
        print_result.func_fail(a)
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
        
    print("\nPlug in USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    mountpoint = usb.wait_usb3h(a = a, insert = True)
    
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("cp testdata /mnt/usb/testdata_from_nfs")
    a.send("cp /mnt/usb/testdata_from_nfs testdata_from_usb")
    a.send("cmp testdata testdata_from_usb")
    a.send("umount /mnt/usb")
    
    #####################################################################################################

    print("\n\n----------Item 2----------\n")
    sys.stdout.flush()
    a.buff = ""
    mountpoint = usb.wait_usb3h(a = a, insert = False)
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("cp /mnt/usb/testdata testdata_from_usb &")
    
    if (s2ram.pm_suspend(a)==False):
        print_result.func_fail(a)
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
    
    a.send("wait")
    a.send("cmp /mnt/usb/testdata testdata_from_usb")
    a.send("umount /mnt/usb")
    
    #####################################################################################################
    
    print("\n\n----------Item 3----------\n")
    sys.stdout.flush()
    a.buff = ""
    mountpoint = usb.wait_usb3h(a = a, insert = False)
    command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp testdata /mnt/usb/testdata_from_nfs &"]
    if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
        print_result.func_fail(a)
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
    
    a.send("wait")
    a.send("cmp testdata /mnt/usb/testdata_from_nfs")
    a.send("umount /mnt/usb")
    
    #####################################################################################################
    
    print("\n\n----------Item 4----------\n")
    sys.stdout.flush()
    a.buff = ""
    if (s2ram.pm_suspend(a)==False):
        print_result.func_fail(a)
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
        
    mountpoint = usb.wait_usb3h(a = a, insert = False)
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("cp testdata /mnt/usb/testdata_from_nfs")
    a.send("cp /mnt/usb/testdata_from_nfs testdata_from_usb")
    a.send("cmp testdata testdata_from_usb")
    a.send("umount /mnt/usb")
    
    #####################################################################################################
    
    print("\n\n----------Item 5----------\n")
    sys.stdout.flush()
    a.buff = ""
    print("\nPull out USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    
    if (s2ram.pm_suspend(a)==False):
        print_result.func_fail(a) 
    print("\nPlug in USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
    mountpoint = usb.wait_usb3h(a = a, insert = False)
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("cp testdata /mnt/usb/testdata_from_nfs")
    a.send("cp /mnt/usb/testdata_from_nfs testdata_from_usb")
    a.send("cmp testdata testdata_from_usb")
    a.send("umount /mnt/usb")
    
    #####################################################################################################
    
    print("\n\n----------Item 6----------\n")
    sys.stdout.flush()
    a.buff = ""
    mountpoint = usb.wait_usb3h(a = a, insert = False)    
    command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp /mnt/usb/testdata testdata_from_usb &"]
    if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
        print_result.func_fail(a)
    print("\nPull out USB3 device\n")
    print("Press any button to continue")
    sys.stdout.flush()
    temp = raw_input()
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)

    a.send("wait")
    a.send("sync")
    a.send("cmp testdata testdata_from_usb")
    a.send("umount /mnt/usb")
    
    #####################################################################################################
    
    print("\n\n----------Item 7----------\n")
    sys.stdout.flush()
    a.buff = ""    
    print("\nPlug in USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input() 
    mountpoint = usb.wait_usb3h(a = a, insert = True)

    command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp testdata /mnt/usb/testdata_from_nfs &"]
    if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
        print_result.func_fail(a)
    print("\nPull out USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
        
    print("\nPlug in USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    mountpoint = usb.wait_usb3h(a = a, insert = True)
    a.send("mount /dev/{} /mnt/usb".format(mountpoint))
    a.send("cmp testdata /mnt/usb/testdata_from_nfs")
    a.send("umount /mnt/usb")
    
    #####################################################################################################
    
    print("\n\n----------Item 8----------\n")
    sys.stdout.flush()
    a.buff = ""   
    command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp /mnt/usb/testdata testdata_from_usb &"]
    if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
        print_result.func_fail(a)
    print("\nPull out USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    print("\nPlug in USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input() 
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)
    a.send("cmp /mnt/usb/testdata testdata_from_usb")
    a.send("umount /mnt/usb")
    
    #####################################################################################################
    
    print("\n\n----------Item 9----------\n")
    sys.stdout.flush()
    a.buff = ""     
    command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp testdata /mnt/usb/testdata_from_nfs &"]
    if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
        print_result.func_fail(a)
    print("\nPull out USB3 device\n")
    print("\nPress any button to continue\n")
    sys.stdout.flush()
    temp = raw_input()
    print("\nPlug in USB3 device\n")
    print("Press any button to continue")
    sys.stdout.flush()
    temp = raw_input()
    if (s2ram.pm_wakeup(a)==False):
        print_result.func_fail(a)    
    a.send("cmp testdata /mnt/usb/testdata_from_nfs")
    a.send("umount /mnt/usb")
    
    if TEST_USB2_PFM:
        #####################################################################################################
        print("\n\n----------Item 10----------\n")
        sys.stdout.flush()
        a.buff = ""     
        
        if (s2ram.pm_suspend(a)==False):
            print_result.func_fail(a)
        if (s2ram.pm_wakeup(a)==False):
            print_result.func_fail(a)
        
        mountpoint = usb.wait_usb3h(a = a, insert = False)

        a.send("dd if=/dev/{} of=/dev/null bs=64M count=1 iflag=direct".format(mountpoint))
        a.send("dd if=/dev/zero of=/dev/{} bs=64M count=1 oflag=direct".format(mountpoint))

        #####################################################################################################
        print("\n\n----------Item 11----------\n")
        sys.stdout.flush()
        a.buff = ""     
  
        a.send('echo y | mkfs.ext4 /dev/{}'.format(mountpoint))
        mountpoint = usb.wait_usb3h(a = a, insert = False)

        command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp /mnt/usb/testdata test_data_from_usb &"]
        if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
            print_result.func_fail(a)
        if (s2ram.pm_wakeup(a)==False):
            print_result.func_fail(a)
            
        a.send("cmp /mnt/usb/testdata test_data_from_usb")
        a.send("umount /mnt/usb")
        a.send("dd if=/dev/{} of=/dev/null bs=64M count=1 iflag=direct".format(mountpoint))
        a.send("dd if=/dev/zero of=/dev/{} bs=64M count=1 oflag=direct".format(mountpoint))
        
        #####################################################################################################
        print("\n\n----------Item 12----------\n")
        sys.stdout.flush()
        a.buff = ""
         
        a.send('echo y | mkfs.ext4 /dev/{}'.format(mountpoint))
        mountpoint = usb.wait_usb3h(a = a, insert = False)

        command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp testdata /mnt/usb/test_data_from_nfs &"]
        if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
            print_result.func_fail(a)
        if (s2ram.pm_wakeup(a)==False):
            print_result.func_fail(a)
            
        a.send("cmp testdata /mnt/usb/test_data_from_nfs")
        a.send("umount /mnt/usb")
        a.send("dd if=/dev/{} of=/dev/null bs=64M count=1 iflag=direct".format(mountpoint))
        a.send("dd if=/dev/zero of=/dev/{} bs=64M count=1 oflag=direct".format(mountpoint))

    if TEST_USB3_PFM:
        #####################################################################################################
        print("\n\n----------Item 13----------\n")
        sys.stdout.flush()
        a.buff = ""     
        
        if (s2ram.pm_suspend(a)==False):
            print_result.func_fail(a)
        if (s2ram.pm_wakeup(a)==False):
            print_result.func_fail(a)
        
        mountpoint = usb.wait_usb3h(a = a, insert = False)

        a.send("dd if=/dev/{} of=/dev/null bs=64M count=10 iflag=direct".format(mountpoint))
        a.send("dd if=/dev/zero of=/dev/{} bs=64M count=10 oflag=direct".format(mountpoint))

        #####################################################################################################
        print("\n\n----------Item 14----------\n")
        sys.stdout.flush()
        a.buff = ""
           
        print("\nPrepare \n")
        mountpoint = usb.wait_usb3h(a = a, insert = False)
        a.send("mkdir -p /mnt/usb")
        a.send("mount /dev/{} /mnt/usb".format(mountpoint))
        if a.buff.find("wrong fs type, bad option, bad superblock on"):
            a.send('echo y | mkfs.ext4 /dev/{}'.format(mountpoint))
            a.send("mount /dev/{} /mnt/usb".format(mountpoint))
        a.send("dd if=/dev/urandom of=testdata bs=10M count=50")
        a.send("cp testdata /mnt/usb/")
        a.send("umount /mnt/usb")
        
        mountpoint = usb.wait_usb3h(a = a, insert = False)

        command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp /mnt/usb/testdata test_data_from_usb &"]
        if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
            print_result.func_fail(a)
        if (s2ram.pm_wakeup(a)==False):
            print_result.func_fail(a)
            
        a.send("cmp /mnt/usb/testdata test_data_from_usb")
        a.send("umount /mnt/usb")
        a.send("dd if=/dev/{} of=/dev/null bs=64M count=10 iflag=direct".format(mountpoint))
        a.send("dd if=/dev/zero of=/dev/{} bs=64M count=10 oflag=direct".format(mountpoint))
        
        #####################################################################################################
        print("\n\n----------Item 15----------\n")
        sys.stdout.flush()
        a.buff = ""
        
        print("\nPrepare \n")
        mountpoint = usb.wait_usb3h(a = a, insert = False)
        a.send("mkdir -p /mnt/usb")
        a.send("mount /dev/{} /mnt/usb".format(mountpoint))
        if a.buff.find("wrong fs type, bad option, bad superblock on"):
            a.send('echo y | mkfs.ext4 /dev/{}'.format(mountpoint))
            a.send("mount /dev/{} /mnt/usb".format(mountpoint))
        a.send("dd if=/dev/urandom of=testdata bs=10M count=50")
        a.send("cp testdata /mnt/usb/")
        a.send("umount /mnt/usb")

        mountpoint = usb.wait_usb3h(a = a, insert = False)

        command_list = ["mount /dev/{} /mnt/usb".format(mountpoint), "cp testdata /mnt/usb/test_data_from_nfs &"]
        if (s2ram.pm_suspend_while_doing_st_multi(a, command_list)==False):
            print_result.func_fail(a)
        if (s2ram.pm_wakeup(a)==False):
            print_result.func_fail(a)
            
        a.send("cmp testdata /mnt/usb/test_data_from_nfs")
        a.send("umount /mnt/usb")
        a.send("dd if=/dev/{} of=/dev/null bs=64M count=10 iflag=direct".format(mountpoint))
        a.send("dd if=/dev/zero of=/dev/{} bs=64M count=10 oflag=direct".format(mountpoint))

    print_result.func_pass(a)
