#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:18:51 2019

@author: Howard-001
"""

import pygame as py

class Ground:
    
    #forest's x
    x = 0
    
   
    
    def __init__(self):
       
        
        
        self.forest = py.image.load('src/image/Ingame_page/forest.png').convert_alpha()
        
        self.sky = py.image.load('src/image/Ingame_page/sky.png').convert_alpha()
        self.start = py.image.load('src/image/Ingame_page/start.png').convert_alpha()
        
        
        
        
#        for i in range (1,6):
#            self.img.append(py.image.load('src/image/Ingame_page/BG'+str(i+1)+'.png'))
#        
#        self.sun=[]
#        
#        for i in range(12):
#            self.sun.append( py.image.load('image/sun/sun'+str(i)+'.png'))
#            
#        
#        
    def update (self,movespeed):
        if self.x >= -1200:
            self.x -= movespeed
        else:
            self.x = 1200
        
       
            
   
   
    start_c = 0
    
    
    def show(self,window):
       
        window.blit(self.sky,(0,0))
        
        window.blit(self.forest,(0,0))
        
        window.blit(self.forest,(self.x,0))
        window.blit(self.forest,(self.x+1200,0))
        window.blit(self.forest,(self.x-1200,0))
        
        
        if self.start_c <= 40:
            
            if 8 >= self.start_c >= 0 or 24 >= self.start_c >= 16 or 40 >= self.start_c >= 32:
                window.blit(self.start,(0,0))
            self.start_c += 1
            
            
            
        
       
        
            
            
                
            
