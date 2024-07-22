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
import wait_process
import sound


if __name__ == '__main__':
    a=conserial.serial_thread(config.SERIAL_PORT,1)
    a.start()
    a.buff=""

    #if (sound.sound_setting(a) == False):
    #    print_result.func_fail(a)

    VOLUME = [200,100,50,10,0]
    VALUE = {200:8388607, 100:8388607, 50:4194304, 10:838861, 0:0}

    a.buff=""
    a.send('aplay -d 120 -D plughw:0,0 -t wav -c 2 -r 44100 {} &'.format(sound.AUDIO_FILE_44100),0,False)
  
    if (a.buff.find('aplay:')!=-1):
        print_result.func_fail(a)


    for i in VOLUME:
        a.buff=""
        a.send("amixer cset name='DVC Out Playback Volume' {}%".format(i))

        if (a.buff.find('values={},{}'.format(VALUE[i],VALUE[i]))==-1):
            print_result.func_fail(a)

        a.send('sleep 5')

    for i in reversed(VOLUME):
        if (i != 0):
            a.buff=""
            a.send("amixer cset name='DVC Out Playback Volume' {}%".format(i))

            if (a.buff.find('values={},{}'.format(VALUE[i],VALUE[i]))==-1):
                print_result.func_fail(a)

            a.send('sleep 5')
  
    wait_process.wait(a,'aplay',20)
      
    if (sound.manual_judgement() == False):
        print_result.func_fail(a)

    print_result.func_pass(a)
