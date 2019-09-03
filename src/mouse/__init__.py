# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:50:03 2019

@author: MarcFish
"""

from mouse.mouse_client import mouse_client
from mouse.mouse_simulator import mouse_simulator 
from mouse.mouse_machine import mouse_machine


# 工厂
def mouse(mode,param={}):
    if mode == 'client':
        return mouse_client(param)
    elif mode == 'simulator':
        return mouse_simulator(param)
    elif mode == 'machine':
        return mouse_machine(param)
    else :
        print('Wrong')