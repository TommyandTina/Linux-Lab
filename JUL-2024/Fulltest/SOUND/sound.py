#!/usr/bin/python
import serial
import threading
from time import sleep
import sys
import os
sys.path.append(os.path.relpath('..'))
import config

if (config.SOC.find('E3') != -1):
    SOUND_CARD = 'asoc-simple-card'
else:
    if (config.SOC.find('M3') != -1):
        SOUND_CARD = 'asoc-audio-graph-card2'
    else:
        SOUND_CARD = 'asoc-audio-graph-card'

SOUND_INTR = 'ec500000.sound'
AUDIO_FILE = '~/audio.wav'
AUDIO_FILE_44100 = '~/audio_44100.wav'

def sound_setting(a):

    CMD = ['amixer set \'DVC Out Mute\' off','amixer set \'DVC In Mute\' off','amixer set "DVC Out" 20%','amixer set "DVC In" 50%','amixer set "Digital Playback Volume1" 85%']

    for i in CMD:
        a.buff=""
        a.send(i)
        if (a.buff.find('amixer:')!=-1):
            return False
    
    return True

def playback(a,option,audio_file,interrupt=None,time_interrupt=1):
    
    a.buff=""

    if (interrupt == None):
        a.send('aplay {} {}'.format(option,audio_file),0.001)
     
        if (a.buff.find('aplay:')!=-1):
            return False
    else:
        a.send('aplay {} {}'.format(option,audio_file),0.001,False)

        if (a.buff.find('aplay:')!=-1):
            return False

        sleep(time_interrupt)

        if (interrupt == 'Ctrl+C'):
            a.buff=""
            a.send('\x03')
            if (a.buff.find('Aborted by signal Interrupt...')==-1):
                return False
        elif (interrupt == 'Ctrl+Z'):
            a.buff=""
            a.send('\x1A')
            if (a.buff.find('Stopped(SIGTSTP)')==-1):
                return False
            
            sleep(time_interrupt/2)
            
            a.buff=""
            a.send('fg')
            if (a.buff.find('aplay {} {}'.format(option,audio_file))==-1):
                return False
            
    return True
     
def record(a,option,record_file='/tmp/record.wav',interrupt=None,time_interrupt=1):

    a.buff=""

    if (interrupt == None):   
        a.send('arecord {} {}'.format(option,record_file),0.001)
        if (a.buff.find('arecord:')!=-1):
            return False

    else:
        a.send('arecord {} {}'.format(option,record_file),0.001,False)
        if (a.buff.find('arecord:')!=-1):
            return False

        sleep(time_interrupt)

        if (interrupt == 'Ctrl+C'):
            a.buff=""
            a.send('\x03')
            if (a.buff.find('Aborted by signal Interrupt...')==-1):
                return False
        elif (interrupt == 'Ctrl+Z'):
            a.buff=""
            a.send('\x1A')
            if (a.buff.find('Stopped(SIGTSTP)')==-1):
                return False
            
            sleep(time_interrupt/2)
            
            a.buff=""
            a.send('fg')
            if (a.buff.find('arecord {} {}'.format(option,record_file))==-1):
                return False
  
    return True                

def unbind(a,while_recording=False):

    a.buff=""

    a.send('cd /sys/bus/platform/drivers/rcar_sound; find -type l')

    if (a.buff.find('./ec500000.sound')==-1):
        return False

    a.buff=""
    a.send('cd /sys/bus/platform/drivers/{}/; find -type l'.format(SOUND_CARD))

    if (a.buff.find('./sound')==-1):
        return False
   
    if (while_recording == True):
        a.buff=""
        a.send('arecord /home/audio.wav&')
        if (a.buff.find('arecord:')!=-1):
            return False 

    a.send('cd /sys/bus/platform/drivers/{}/'.format(SOUND_CARD))

    a.send('echo ec500000.sound > /sys/bus/platform/drivers/rcar_sound/unbind')

    a.send('echo sound > /sys/bus/platform/drivers/{}/unbind'.format(SOUND_CARD))

    a.buff=""
    a.send('cd /sys/bus/platform/drivers/rcar_sound; ls -d  ec500000.sound')

    if (a.buff.find('ls: cannot access \'ec500000.sound\': No such file or directory')==-1):
        return False

    a.buff=""
    a.send('cd /sys/bus/platform/drivers/{}/; ls -d ./sound'.format(SOUND_CARD))

    if (a.buff.find('ls: cannot access \'./sound\': No such file or directory')==-1):
        return False

    a.buff=""
    a.send('echo ec500000.sound > /sys/bus/platform/drivers/rcar_sound/bind',0,False)

    sleep(1.5)

    if (a.buff.find('rcar_sound ec500000.sound: probed')==-1):
        return False

    a.buff=""
    a.send('echo sound > /sys/bus/platform/drivers/{}/bind'.format(SOUND_CARD),0,False)

    sleep(1.5)

    if (sound_setting(a)==False):
        return False

    a.send('cd ~')

    a.buff=""
    a.send('amixer')

    a.buff=""
    a.send('arecord /home/audio.wav -d 30')

    if (a.buff.find('arecord:')!=-1):
        return False

    a.buff=""
    a.send('aplay /home/audio.wav')

    if (a.buff.find('aplay:')!=-1):
        return False

    return True

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
        

   
