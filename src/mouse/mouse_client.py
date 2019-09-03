# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:17:33 2019

@author: MarcFish
"""
import win32api
import win32gui
import win32con

from mouse.mouse_meta import mouse_meta


class mouse_client(mouse_meta):
    def __init__(self,param):
        super(mouse_client,self).__init__(param)
        self.hwnds = self._param.get('hwnds')
    def click(self,x=None,y=None,Button=None):
        pos = win32api.MAKELOG(x,y)
        win32gui.SendMessage(self.hwnds, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 1)
        self.sleep(0.01)
        win32api.SendMessage(self.hwnds, win32con.WM_LBUTTONDOWN, win32con.VK_LBUTTON, pos)
        self.sleep(0.01)
        win32api.SendMessage(self.hwnds, win32con.WM_LBUTTONUP, None, pos)
        self.sleep(0.01)
        return
    def move_to(self,x=None,y=None):
        return
    def drag(self,x1=None,y1=None,x2=None,y2=None):
        return