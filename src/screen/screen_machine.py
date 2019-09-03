# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:02:41 2019

@author: MarcFish
"""
import subprocess
import cv2
from screen.screen_meta import screen_meta


class screen_machine(screen_meta):
    
    def __init__(self,param):
        super(screen_machine,self).__init__(param)
        self.ADB_PATH = self._param.get('ADB_PATH')
        return
    
    def _get_current_screen(self):
        subprocess.run('%s %s %s'%(self.ADB_PATH,'shell screencap','/sdcard/screen.png'))
        subprocess.run('%s %s %s'%(self.ADB_PATH,'pull','/sdcard/screen.png'))
        return cv2.imread('screen.png')
    
    current_screen = property(fget=_get_current_screen)