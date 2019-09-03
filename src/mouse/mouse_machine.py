# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:58:07 2019

@author: MarcFish
"""
import subprocess

from mouse.mouse_meta import mouse_meta


class mouse_machine(mouse_meta):
    def __init__(self,param):
        super(mouse_machine,self).__init__(param)
        self.ADB_PATH = self._param.get('ADB_PATH')  # 若没有则输出错误
        return
    def click(self,x=None,y=None,Button=None):
        if x is None or y is None:
            pass
        else:
            subprocess.run('%s %s'%(self.ADB_PATH,'shell input tap {} {}'.format(x,y)))
            self.sleep()
        return
    
    def move_to(self,x=None,y=None):
        return
    
    def drag(self,x1=None,y1=None,x2=None,y2=None):
        if x1 is None or y1 is None or x2 is None or y2 is None:
            pass
        else:
            subprocess.run('%s %s'%(self.ADB_PATH,'shell input swipe {} {} {} {}'.format(x1,y1,x2,y2)))
            self.sleep()
        return
    