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
import subprocess
sys.path.append(os.path.relpath('../SOUND/'))
import sound

if (config.SOC.find('E3') != -1):
    SOUND_CARD = 'asoc-simple-card'
else:
    if (config.SOC.find('M3') != -1):
        SOUND_CARD = 'asoc-audio-graph-card2'
    else:
        SOUND_CARD = 'asoc-audio-graph-card'

if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    
    if (config.SOC == 'E3'):
        ND = 'e66d0000.i2c'
    else:
        ND = 'e6510000.i2c'

    if (sound.sound_setting(a) == False):
        print_result.func_fail(a)

    a.buff=""      
    a.send('arecord -d 10 ~/test.wav')
         
    #Find
    a.buff=""
    a.send('cd /sys/bus/platform/drivers/i2c-rcar; find -type l')
    if (a.buff.find('./{}'.format(ND))==-1):
        config.print_result.func_fail(a)
    a.send('cd /sys/bus/platform/drivers/rcar_sound; find -type l')

    #Unbind SOUND_CARD
    a.buff=""
    a.send('cd /sys/bus/platform/drivers/{}/'.format(SOUND_CARD))
    a.send('echo sound > unbind')
    a.send('ls -d ./sound')
    if (a.buff.find('ls: cannot access \'./sound\': No such file or directory')==-1):
        print_result.func_fail(a)

    #Unbind rcar_sound
    a.buff=""
    a.send('cd /sys/bus/platform/drivers/rcar_sound')
    a.send('echo ec500000.sound > unbind')
    a.send('ls -d ec500000.sound')
    if (a.buff.find('ls: cannot access \'ec500000.sound\': No such file or directory')==-1):
        print_result.func_fail(a)
    
    #Unbind I2C
    a.buff=""
    a.send('cd /sys/bus/platform/drivers/i2c-rcar')
    a.send('echo {} > unbind'.format(ND))
    a.send('ls -d {}'.format(ND))
    if (a.buff.find('ls: cannot access \'{}\': No such file or directory'.format(ND))==-1):
        print_result.func_fail(a)

    sleep(1)

    #Bind I2C
    a.buff=""
    a.send('cd /sys/bus/platform/drivers/i2c-rcar')
    a.send('echo {} > bind'.format(ND),0,False)
    sleep(3)
    a.send('ls -d {}'.format(ND))
    if (a.buff.find('ls: cannot access \'{}\': No such file or directory'.format(ND))!=-1):
        print_result.func_fail(a)

    #Bind rcar_sound
    a.buff=""
    a.send('cd /sys/bus/platform/drivers/rcar_sound')
    a.send('echo ec500000.sound > bind',0,False)
    sleep(3)
    a.send('ls -d ec500000.sound')
    if (a.buff.find('ls: cannot access \'{}\': No such file or directory'.format(ND))!=-1):
        print_result.func_fail(a)

    #Bind SOUND_CARD
    a.buff=""
    a.send('cd /sys/bus/platform/drivers/{}/'.format(SOUND_CARD))
    a.send('echo sound > bind',0,False)
    sleep(3)
    a.send('ls -d ./sound')
    if (a.buff.find('ls: cannot access \'./sound\': No such file or directory')!=-1):
        print_result.func_fail(a)

    a.buff=""
    a.send('aplay ~/test.wav')
 
    if(a.buff.find('Playing WAVE')==-1):
        a.send('cd ~')
        print_result.func_fail(a)
    
    a.send('cd ~')
    
    print_result.func_pass(a)
