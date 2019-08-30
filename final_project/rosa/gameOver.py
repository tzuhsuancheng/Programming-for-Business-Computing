#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 15:26:07 2019

@author: Howard-001
"""

import pygame as py

class GameOver:
    windowX = 1200
    
    def __init__(self,font1,font2):
        
        self.gameover = py.image.load('src/image/Ingame_page/gameover.png').convert_alpha()
        self.restart = py.image.load('src/image/Ingame_page/restart.png').convert_alpha()
        self.back = py.image.load('src/image/Ingame_page/exit.png').convert_alpha()
        
        
      
        self.on_restart = True
        self.on_back = False
        
        
        
    
    def update(self):
#        x,y=py.mouse.get_pos()
#        press=py.mouse.get_pressed()[0]
#        
#        
#        if 370 + self.back_home.get_width() >= x >= 370 and 400 + self.back_home.get_width() >= y >= 400: #press back home
#            
#            self.on_back_home = True
#            if press:
#                return 1
#            else:
#                return 2
#            
#        elif 700 + self.restart.get_width() >= x >= 700 and 400 + self.restart.get_width() >= y >= 400: #press restart
#            self.on_restart = True
#            if press:
#                print('restart')
#                return 3
#            else:
#                return 2
#        else:
#            self.on_back_home = False
#            self.on_restart = False
#             
#            return 2
        press = py.key.get_pressed()
        
        if self.on_restart and not self.on_back :
            if press[py.K_DOWN]:
                self.on_restart = False
                self.on_back = True
                return 2
            elif press[py.K_RETURN]:
                return 3
            else:
                return 2
            
        elif not self.on_restart and self.on_back:
            if press[py.K_UP]:
                self.on_restart = True
                self.on_back = False
                return 2
            elif press[py.K_RETURN]:
                return 1
            else:
                return 2
                
        
            
                
      
        

    def show(self,y,score,window,font):
        
        self.points = font.render('points:'+str(score),True, (255, 255, 255))
        window.blit(self.points,(600 - self.points.get_width()/2 , y + 250))
        
        
#        self.pointsShadow = self.font2.render('points : '+str(score),True, (0, 0, 0))

#    
#        window.blit(self.deathMessage1, (self.windowX / 2 - self.deathMessage1.get_width() / 2, y))
#        window.blit(self.deathMessage1Shadow, (self.windowX / 2 - self.deathMessage1.get_width()/2 + 5, y + 5))
#        
#        
#        
#       
#        window.blit(self.pointsShadow,(self.windowX/2 - self.points.get_width()/2 , y + 205))
#        
#        if self.on_back_home:
#            window.blit(self.back_home_max,(370-10,450-10))
#        else:
#            window.blit(self.back_home,(370,450))
#        
#        if self.on_restart:
#            window.blit(self.restart_max,(700-10,450-10))
#        else:
#            window.blit(self.restart,(700,450))
        window.blit(self.gameover,(0,0))
        
        if self.on_restart:
            window.blit(self.restart,(0,0))   
        elif self.on_back:
            window.blit(self.back,(0,0))
            
            
            
       