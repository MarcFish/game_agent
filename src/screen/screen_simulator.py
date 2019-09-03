# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:03:32 2019

@author: MarcFish
"""
import subprocess
import cv2

from screen.screen_meta import screen_meta

class screen_simulator(screen_meta):
    def _get_current_screen(self):
        MUMU_SHARED = self._param.get('MUMU_SHARED')
        ADB_PATH = self._param.get('ADB_PATH')
        EMULATOR = self._param.get('EMULATOR')
        subprocess.run('%s -s %s %s /mnt/shared/products/yys/%s.png' % (ADB_PATH, EMULATOR, 'shell screencap -p', 'screen'))
        return cv2.imread(MUMU_SHARED+'screen.png')
    
    current_screen = property(fget=_get_current_screen)