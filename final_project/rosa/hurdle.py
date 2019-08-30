#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:20:53 2019

@author: Howard-001
"""
import pygame as py
from pygame import *
import random

py.mixer.init()
explodefx = py.mixer.Sound("src/music/explode.wav")
explodefx.set_volume(1.0)


class HurdleManager(py.sprite.Sprite):
    
    def __init__(self,y, spawnRange):
        
        self.y = y
        
        self.bomb = []
        
        for i in range(15):
            self.bomb.append(py.image.load('src/image/Bomb_waiting/bomb'+str(i+1)+'.png').convert_alpha())
            
        self.boost = []
        
        for i in range(13):
            self.boost.append(py.image.load('src/image/Boost/Heart'+str(i+1)+'.png').convert_alpha())
            
        self.fire=[]
        
       
        for i in range(9):
            self.fire.append(py.image.load('src/image/Bomb_Explode/Explode'+str(i+1)+'.png').convert_alpha())
           
            
        self.spawnRange = spawnRange
        self.hurdleList = []
       
    def update(self, doSpawn, moveSpeed,window):
        if doSpawn:
            self.spawn()
        self.manage(moveSpeed,window)
    

    def manage(self, moveSpeed,window):
        
        hurdles2 = []
        
        for hurdle in self.hurdleList:
            hurdle.update(moveSpeed)
            hurdle.show(window)
            
            if hurdle.onScreen():
                hurdles2.append(hurdle)

    
        self.hurdleList = hurdles2

    spawnTick = 0

    def spawn(self):
        
        if self.spawnTick >= self.spawnRange[1]:
            
            newHurdle = Hurdle(self.y,self.bomb,False,self.fire)
            self.hurdleList.append(newHurdle)
            self.spawnTick = 0

        elif self.spawnTick > self.spawnRange[0]:
            
            if random.randint(0, self.spawnRange[1] - self.spawnRange[0]) == 0:
                
                if random.randint(0, 10) == 0:
                    
                    newHurdle = Hurdle(self.y,self.boost,True,self.fire)
                else:
                    newHurdle = Hurdle(self.y,self.bomb,False,self.fire)
                    
                 
                self.hurdleList.append(newHurdle)
                
                self.spawnTick = 0


        self.spawnTick += 1


#         if random.randint(0, 10) == 0:
##                
#                if random.randint(0, 10) == 0:
#                    
#                    newHurdle = Hurdle(self.y,self.boost,True)
#                else:
#                    newHurdle = Hurdle(self.y,self.bomb,False)
#                    
#                 
#                self.hurdleList.append(newHurdle)



class Hurdle:
    def __init__(self,y,img,boost,fire):
        self.x = 1200
        self.y = y
        self.img = img
        self.width = 40
        self.height = 40
        
        self.boost = boost
        self.touch = False
        
        if not self.boost:
            self.fire = fire
        
        
        
       

    def update(self, moveSpeed):
        self.move(moveSpeed)
        
    def move(self, moveSpeed):
        self.x -= moveSpeed

    tick = 0
    
   
    
    def show(self,window):
        
        if not self.boost:
            self.tick = 0
        else:
            if self.tick >=  39: 
                self.tick = 0
            
        if not self.touch:    
            window.blit(self.img[int(self.tick/3)],(self.x,self.y))
        elif not self.boost:
            self.explode(window)
            
        
        
        
        self.tick += 1
            
    def onScreen(self):
        if self.x + self.width > 0:
            return True
        else:
            return False
    
    
    explode_c = 0
    
    def explode(self,window):
        if self.explode_c < 18:
            if self.explode_c == 0:
                explodefx.play()
                
            img=self.fire[int(self.explode_c/2)]
            
#            
            window.blit(img, (self.x-80, self.y-340))
            self.explode_c+=1