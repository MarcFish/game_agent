# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:17:41 2019

@author: MarcFish
"""
import subprocess

from mouse.mouse_meta import mouse_meta


class mouse_simulator(mouse_meta):
    def click(self,x=None,y=None,Button=None):
        ADB_PATH = self._param.get('ADB_PATH')
        EMULATOR = self._param.get('EMULATOR')
        subprocess.run('%s -s %s %s' % (ADB_PATH, EMULATOR, 'shell input tap {} {}'.format(x,y)))
        self.sleep()
        return
    def move_to(self,x=None,y=None):
        return
    def drag(self,x1=None,y1=None,x2=None,y2=None):
        return