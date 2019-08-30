#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 21:24:17 2019

@author: Howard-001
"""
import pygame as py

class Menu(py.sprite.Sprite):
    
    change_to_game = False
    
    def __init__(self):
        
        self.background = []
        for i in range(6):
            self.background.append(py.image.load('src/image/Title_page/TL'+str(i+1)+'.png').convert_alpha())
       
        self.rosa_jump = []
        self.jumpTime = 10 
        self.jump_y = 360
        
        for i in range(3):
            #self.rosa_jump.append(py.image.load('src/image/Rosa/Normal_jump/N_jump'+str(i+1)+'.png').convert_alpha())
            self.rosa_jump.append(py.image.load('src/image/Rosa/Normal_jump/jump'+str(i+1)+'.png').convert_alpha())
        
        self.bomb = []
        
        for i in range(15):
            self.bomb.append(py.image.load('src/image/Bomb_waiting/bomb'+str(i+1)+'.png').convert_alpha())
            
        self.explode = []
        
        for i in range(9):
            self.explode.append(py.image.load('src/image/Bomb_Explode/Explode'+str(i+1)+'.png').convert_alpha())
            
        
        self.boost = []
        
        for i in range(13):
            self.boost.append(py.image.load('src/image/Boost/Heart'+str(i+1)+'.png').convert_alpha())
            
        
     
      
    jump_c = 0
    bomb_wait_c = 0
    bomb_explode_c = 0
    
    boost_c = 0
    
    EXPLODE = False
    
    press_enter = 0       
            
    def show(self,window):
        window.blit(self.background[4],(0,0))
        window.blit(self.background[5],(0,0))
        window.blit(self.background[1],(0,0))
        
        if self.press_enter == 16: self.press_enter = 0
        if 8>= self.press_enter >= 0: window.blit(self.background[2],(0,0))
        self.press_enter += 1
        
        
        
        window.blit(self.background[3],(0,0))
        
        
#        window.blit(self.background,(0,0))
#        
#        window.blit(self.head,(window.get_width()/2 - self.head.get_width()/2,50))
#        
#        window.blit(self.introduction,(window.get_width()/2 - self.introduction.get_width()/2,350))
#        
        self.jumping()
        
        img=0
                
        if(self.jumpTime > 1):
                        
            img=self.rosa_jump[0]
                        
        elif(1 >= self.jumpTime >= -1):
                        
            img=self.rosa_jump[1]
                        
        elif(self.jumpTime < -1):
                        
            img=self.rosa_jump[2]
            
        window.blit(img,(600-self.rosa_jump[int(self.jump_c/3)].get_width()/2,self.jump_y))
        
        
        
        if not self.EXPLODE:
            if self.bomb_wait_c >=  45: 
                self.bomb_wait_c = 0
                self.EXPLODE = True
                
            window.blit(self.bomb[int(self.bomb_wait_c/3)],(190,380))
            self.bomb_wait_c += 1
        else:
            window.blit(self.explode[int(self.bomb_explode_c/2)],(93,37))
            
            self.bomb_explode_c += 1
            
            if self.bomb_explode_c >=  18: 
                self.bomb_explode_c = 0
                self.EXPLODE = False
                
            
            
            
        
        if self.boost_c >= 39: self.boost_c = 0
        window.blit(self.boost[int(self.boost_c/3)],(358,380))
        self.boost_c += 1
            
        
     
        
    def jumping(self):
        print('jumping22')
        
        
        
        print('jumping')
        if self.jumpTime >= -10:
            self.jump_y -= (self.jumpTime * abs(self.jumpTime)) * 0.3
                
            self.jumpTime -= 1
                #print('jumping')
        else:  
               
            self.jumpTime = 10
            
        
        
       
    