# -*- coding: utf-8 -*-
"""
Created on Sat May 18 00:03:41 2019

@author: MarcFish
"""

import cv2
import numpy as np


class screen_meta:
    
    def __init__(self,param={}):
        self._param = param
        self.match_dict = {}
        for name,img in self._param.get('match_dict').items():
            self.match_dict[name] = img
        return
    
    def _get_current_screen(self):
        return
    
    def _get_match_img(self,target):
        return self.match_dict.get(target)
    
    current_screen = property(fget=_get_current_screen)
    
    def find_location(self,target):
        match_img = self._get_match_img(target)
        sift = cv2.xfeatures2d.SIFT_create()
        kp1, des1 = sift.detectAndCompute(match_img, None)
        kp2, des2 = sift.detectAndCompute(self.current_screen, None)
        FLANN_INDEX_KDTREE = 1
        index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
        search_params = dict(checks = 50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)
        matches = flann.knnMatch(des1,des2,k=2)
        good = []
        for m,n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)
        # 当有足够的健壮匹配点对（至少4个）时
        MIN_MATCH_COUNT = 15
        if len(good) >= MIN_MATCH_COUNT:
            # 从匹配中提取出对应点对
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,2)
    
            (x, y) = np.mean(dst_pts, axis=0)
            print(x, y)
            return (x,y)
        else:
            print( "Not enough matches are found - {}/{}".format(len(good), MIN_MATCH_COUNT))
            return None, None