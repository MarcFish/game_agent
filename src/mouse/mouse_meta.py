# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:01:25 2019

@author: MarcFish
"""

import random
import time


# 元类
class mouse_meta:
    def __init__(self,param={}):
        self._param=param
        return
    
    def click(self,x=None,y=None,Button=None):
        return
    
    def move_to(self,x=None,y=None):
        return
    
    def drag(self,x1=None,y1=None,x2=None,y2=None):
        return
    
    @staticmethod 
    def sleep(t=0.1):
        time.sleep(random.uniform(t,t+t*2))
        return
