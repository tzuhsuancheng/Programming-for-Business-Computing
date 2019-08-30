#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:19:22 2019

@author: Howard-001
"""
import pygame as py
from pygame import *
import random

class Player(py.sprite.Sprite):
    x = 100
    y = 460
    
    road = 3
    
    road_height = 57
    
    boost = False
    
    
   
    def __init__(self, scale, imageChangeSpeed, terminalVelocity):
        self.run=[]
        
       
        self.u_run = []
        
       
        
        self.jump=[]
        
       
        self.u_jump = []
        
        
        
        self.fire=[]
        
#        for i in range(20):
#            self.run.append(py.image.load('src/image/Rosa_2/Normal_sprint/N_sprint_'+str(i)+'.png').convert_alpha())
#        
#        for i in range(20):
#            self.t_run.append(py.image.load('src/image/Rosa_2/Transform_sprint/T_sprint_'+str(i)+'.png').convert_alpha())
#        
#        for i in range(20):
#            self.u_run.append(py.image.load('src/image/Rosa_2/Ultimate_sprint/U_sprint_'+str(i)+'.png').convert_alpha())
#        
#        
#        
#        
#        #2,4,5
#        for i in range(20):
#            self.jump.append(py.image.load('src/image/Rosa_2/Normal_jump/N_jump_'+str(i)+'.png').convert_alpha())
#        
#        for i in range(20):
#            self.t_jump.append(py.image.load('src/image/Rosa_2/Transform_jump/T_jump_'+str(i)+'.png').convert_alpha())
#        
#        for i in range(20):
#            self.u_jump.append(py.image.load('src/image/Rosa_2/Ultimate_jump/U_jump_'+str(i)+'.png').convert_alpha())
#           
           
        
#        
        for i in range(20):
            if i<10:
                temp=py.image.load('src/image/Rosa/Normal_sprint/tenor-000'+str(i)+'.png').convert_alpha()
            else:
                temp=py.image.load('src/image/Rosa/Normal_sprint/tenor-00'+str(i)+'.png').convert_alpha()
             
            self.run.append(temp)
            print(temp.get_rect().size)
#            
         
            
        for i in range(8):
            self.u_run.append(py.image.load('src/image/Rosa/Ultimate_sprint/U_sprint'+str(i+1)+'.png').convert_alpha())
        
        
#        
        for i in range(3):
            self.jump.append(py.image.load('src/image/Rosa/Normal_jump/jump'+str(i+1)+'.png').convert_alpha())
        
        
        for i in range(3):
            self.u_jump.append(py.image.load('src/image/Rosa/Ultimate_jump/U_Jump'+str(i+1)+'.png').convert_alpha())
#        
        
        for i in range(9):
            self.fire.append(py.image.load('src/image/Bomb_Explode/Explode'+str(i+1)+'.png').convert_alpha())
           
        

        self.scale = scale
        self.imageChangeSpeed = imageChangeSpeed
        self.terminalVelocity = terminalVelocity

        self.height = 80
        self.width = 90
        
       
        self.isJump = False
        self.jumpTime = 14
        
      

    dead = False

    def update(self,hurdleManager):
       
        print('road:', self.road)
        
#        if not self.boost:
        
            
            
        if not self.dead: 
            self.touchingHurdle(hurdleManager)
            self.jumping()
        


    def touchingHurdle(self,hurdleManager):
        for hurdle in hurdleManager.hurdleList:
            
            #print('hurdle:',hurdle.x,hurdle.y,'rosa:',self.x+self.width ,self.y)
            
            if self.x + self.width - 10 > hurdle.x + 5 :
                if self.x + 10 < hurdle.x + hurdle.width:
                    if self.y + self.height > hurdle.y:
                        hurdle.touch = True
                        
                        if not hurdle.boost and not self.boost:
                            print('dead')
                
                            self.dead = True
                        else:
                            
                            self.boost = True
                            




   

    
    def jumping(self):
        print('jumping22')
        
        
        if  self.isJump:
            print('jumping')
            if self.jumpTime >= -14:
                self.y -= (self.jumpTime * abs(self.jumpTime)) * 0.2
                
                self.jumpTime -= 1
                #print('jumping')
            else:  
               
                self.jumpTime = 14
                self.isJump = False
                
   
    runTick = 0
    
    u_runTick = 0
    
    transform = 0
    
    def show(self,window):
      
        if self.isJump:
            if not self.boost:
                print('time:',self.jumpTime)
                
                img=0
                
                if(self.jumpTime > 1):
                        
                    img=self.jump[0]
                        
                elif(1 >= self.jumpTime >= -1):
                        
                    img=self.jump[1]
                        
                elif(self.jumpTime < -1):
                        
                    img=self.jump[2]
            else:
                if(self.jumpTime > 1):
                        
                    img=self.u_jump[0]
                        
                elif(1 >= self.jumpTime >= -1):
                        
                    img=self.u_jump[1]
                        
                elif(self.jumpTime < -1):
                        
                    img=self.u_jump[2]
                
            
            window.blit(img, (self.x, self.y))
            
        else:
            
            if not self.boost:
                
                temp=self.run[self.runTick].get_width()
                  
                window.blit(self.run[self.runTick], (self.x, self.y))
        
                self.runTick += 1
        
                if self.runTick >=  6:
                    self.runTick = 0
                    
               
                    
                    
                
            else:
                window.blit(self.u_run[self.u_runTick], (self.x-30, self.y))
        
                self.u_runTick += 1
        
                if self.u_runTick >=  8:
                    self.u_runTick = 0
                    
#                if self.transform < 12:
#                    window.blit(img, (self.x, self.y))
                
                
                    
        
    explode_c = 0
        
    def explode(self,window):
        if self.explode_c < 18:
            img=self.fire[int(self.explode_c/2)]
            
            
            window.blit(img, (self.x-30, self.y-300))
            self.explode_c+=1
            


