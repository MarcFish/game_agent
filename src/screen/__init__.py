# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:04:53 2019

@author: MarcFish
"""

from screen.screen_simulator import screen_simulator
from screen.screen_machine import screen_machine

def screen(mode,param={}):
    if mode == 'simulator':
        return screen_simulator(param)
    elif mode == 'machine':
        return screen_machine(param)
    else:
        print('Wrong')
    