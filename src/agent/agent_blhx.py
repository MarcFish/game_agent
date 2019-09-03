# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:56:10 2019

@author: MarcFish
"""

import os
import cv2

from agent.agent_meta import agent_meta


class agent_blhx(agent_meta):
    def __init__(self,mode):
        super(agent_blhx,self).__init__(mode,self._param)
        return
    
    def _get_param(self):
        blhx_path = './res/blhx/'
        blhx_fs = os.listdir(blhx_path)
        blhx_dict = {}
        for file in blhx_fs:
            blhx_dict.update({os.path.splitext(file)[0]:cv2.imread(blhx_path+file)})
        param = {}
        param.update({'match_dict':blhx_dict})
        param.update({'ADB_PATH':'F:/program/project/agent/others/adb/adb.exe'})
        '''param.update({'ADB_PATH': 'E:/mumu/emulator/nemu/vmonitor/bin/adb.exe',
            'MUMU_SHARED':'E:/mumu/emulator/nemu/EmulatorShell/products/blhx/',
            'EMULATOR':"127.0.0.1:7555",
            'ADB_HOST':'127.0.0.1:7555'
            })'''
        param.update({'window_class':'Qt5QWindowIcon',
            'window_name':'碧蓝航线 - MuMu模拟器'
            })
        return param
    
    _param = property(fget=_get_param)
    
    def attack_7_2(self):
        while(1):
            self.click_target_area_once('7-2')
            self.click_target_area_once('go1')
            self.click_target_area_once('go2')
            self.click_target_area_once('avoid')
            if not self.is_target_appear('boss'):
                self.click_target_area_once('ship2')
                self.click_target_area_once('ship2_2')
                self.click_target_area_once('ship3')
            self.click_target_area_once('attack')
            self.click_target_area_once('continue1')
            self.click_target_area_once('continue2')
            self.click_target_area_once('s')
            self.click_target_area_once('s2')
            self.click_target_area_once('confirm')