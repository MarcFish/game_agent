# -*- coding: utf-8 -*-
"""
Created on Sat May 18 15:03:36 2019

@author: MarcFish
"""

import os
import cv2

from agent.agent_meta import agent_meta


class agent_yys(agent_meta):
    def __init__(self,mode):
        super(agent_yys,self).__init__(mode,self._param)
        return
    
    def _get_param(self):
        yys_path = './res/yys/'
        yys_fs = os.listdir(yys_path)
        yys_dict = {}
        for file in yys_fs:
            yys_dict.update({os.path.splitext(file)[0]:cv2.imread(yys_path+file)})
        param = {}
        param.update({'match_dict':yys_dict})
        param.update({'ADB_PATH':'F:/program/project/agent/others/adb/adb.exe'})
        '''param.update({'ADB_PATH': 'E:/mumu/emulator/nemu/vmonitor/bin/adb.exe',
            'MUMU_SHARED':'E:/mumu/emulator/nemu/EmulatorShell/products/yys/',
            'EMULATOR':"127.0.0.1:7555",
            'ADB_HOST':'127.0.0.1:7555'
            })'''
        param.update({'window_class':'Qt5QWindowIcon',
            'window_name':'阴阳师 - MuMu模拟器'
            })
        return param
    
    _param = property(fget=_get_param)
    
    def soul_eleven(self):
        while(1):
            self.click_target_area_once('victory')
            self.click_target_area_once('goon')
            
    def active(self):
        while(1):
            self.click_target_area_once('challenge_b')
            self.click_target_area_once('ready')
            self.click_target_area_once('victory')
            self.click_target_area_once('goon')
            
    def yuling(self):
        while(1):
            self.click_target_area_once('challenge')
            self.click_target_area_once('victory')
            self.click_target_area_once('goon')
            
    def soul_eleven_captian(self):
        while(1):
            self.click_target_area_once('start_battle')
            self.click_target_area_once('victory')
            self.click_target_area_once('goon')
    