# -*- coding: utf-8 -*-
"""
Created on Thu May 16 22:19:07 2019

@author: MarcFish
"""

import sys

from agent.agent_blhx import agent_blhx
from agent.agent_yys import agent_yys

sys.path.append('.')
sys.path.append('.')


if __name__=='__main__':
    blhx = agent_blhx('machine')
    #yys = agent_yys('machine')
    #yys.soul_eleven()
    blhx.attack_7_2()
    