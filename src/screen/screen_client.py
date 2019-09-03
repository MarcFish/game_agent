# -*- coding: utf-8 -*-
"""
Created on Wen May 22 13:11:32 2019

@author: MarcFish
"""
import win32gui
from PIL import ImageGrab
import numpy as np

from screen.screen_meta import screen_meta

class screen_simulator(screen_meta):
    def _get_current_screen(self):
        rect = win32gui.GetWindowRect(self._param.get('hwnds'))
        return np.array(ImageGrab.grab().crop(rect),'uint8')
    
    current_screen = property(fget=_get_current_screen)