# -*- coding: utf-8 -*-
"""
Created on Sat May 18 11:50:02 2019

@author: MarcFish
"""
import sys
import win32gui

sys.path.append('../mouse/')
sys.path.append('../screen/')

from mouse import mouse
from screen import screen

class agent_meta:
    
    def __init__(self,mode,param={}):
        param.update({'hwnds':self._get_hwnds(param.get('window_class'),param.get('window_name'))})
        self._m = mouse(mode,param)
        self._s = screen(mode,param)
        return
    
    def click_target_area_once(self,target):
        x,y = self._s.find_location(target)
        self._m.click(x,y)
        return
    
    def is_target_appear(self,target):
        x,y = self._s.find_location(target)
        if x==None or y==None:
            return False
        else :
            self._m.click(x,y)
            return True
        return

    def _get_hwnds(self,window_class,window_name):
        return win32gui.FindWindow(window_class,window_name)
    
    