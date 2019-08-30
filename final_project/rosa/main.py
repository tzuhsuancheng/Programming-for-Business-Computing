import pygame as py
from pygame import *
import random

import player
import hurdle
import menu
import gameOver
import ground

#遊戲狀態
INIT = 0
MENU = 1
GAME = 2
RESTART = 3


windowX = 1200
windowY = 600

py.init()
clock = time.Clock()
window = display.set_mode((windowX, windowY))

display.set_caption('Rosa Jump!')


font1 = font.Font('src/Font/kongtext.ttf', 100)
font2 = font.Font('src/Font/kongtext.ttf', 40)
font3 = font.Font('src/Font/kongtext.ttf', 30)


# Music # Tzu
py.mixer.init()

bouncefx = py.mixer.Sound("src/music/jump.wav")
bouncefx.set_volume(0.2)

selectfx = py.mixer.Sound("src/music/select.wav")
selectfx.set_volume(0.2)

stampfx = py.mixer.Sound("src/music/stamp/stamp3.wav")
stampfx.set_volume(0.1)

explodefx = py.mixer.Sound("src/music/explode.wav")
explodefx.set_volume(1.0)

powerupfx = py.mixer.Sound("src/music/powerup/powerup2.wav")
powerupfx.set_volume(0.2)

deadfx = py.mixer.Sound("src/music/dead.wav")
deadfx.set_volume(0.5)



score = {'gameScore': 0}
hurdleManager = None
rosa = None
begin = None
game_over = None
Ground = None

boost_time = 0

f = open('highest.txt','r')
highest = f.readline()
highest = int(highest.strip())

f.close()

print(highest)


STATE = INIT

playdead = False

while True:
    
    for event in py.event.get():
        if event.type == QUIT:
            py.quit()
            exit()
            
        elif event.type == KEYDOWN: 
            
            if STATE == GAME:
                if not rosa.dead:
                    
                    if event.key == K_SPACE and not rosa.isJump:
                        
                        rosa.isJump =True
                        bouncefx.play()
                        
                        
                    elif event.key == K_UP and rosa.road != 1 and not rosa.isJump:
                         
                        rosa.y -= rosa.road_height
                        
                        if rosa.road == 3:
                            rosa.road = 2
                        elif rosa.road == 2:
                            rosa.road =1
                        
                        stampfx.play() 
                        
                    elif event.key == K_DOWN and rosa.road != 3 and not rosa.isJump:
                        
                        rosa.y += rosa.road_height
                        
                        if rosa.road == 1:
                            rosa.road = 2
                        elif rosa.road == 2:
                            rosa.road = 3
                        
                        stampfx.play() 
                else:
                    if game_over.on_restart and not game_over.on_back :
                        if event.key == K_DOWN:
                            game_over.on_restart = False
                            game_over.on_back = True
                            
                            selectfx.play()
                             
                        elif event.key == K_RETURN:
                            STATE = RESTART
                        
                        
                    elif not game_over.on_restart and game_over.on_back:
                        if event.key == K_UP:
                            
                            game_over.on_restart = True
                            game_over.on_back = False
                            
                            selectfx.play()
                            
                        elif event.key == K_RETURN:
                            
                            STATE = INIT
                            
                                    
            elif STATE == MENU:
                if event.key == K_RETURN:
                    begin.change_to_game = True
#                    
#    
    
     
    if STATE == INIT:
        
        playdead = False
        
       
        py.mixer.music.stop()
        openfx = py.mixer.music.load("src/music/bgm_open/bgm_open2.wav")
        py.mixer.music.set_volume(0.3)
        py.mixer.music.play(-1)
        
        
        begin = menu.Menu()
        game_over = gameOver.GameOver(font1,font2)
       
        STATE = MENU
        
        
        
    elif STATE == MENU:
        
        
        
        begin.show(window)
        
        if begin.EXPLODE and begin.bomb_explode_c == 0:
              explodefx.play()
        
        if begin.change_to_game:
            
            
            py.mixer.stop()
            gamefx = py.mixer.music.load("src/music/bgm_game/bgm_game.wav")
            py.mixer.music.set_volume(0.2)
            py.mixer.music.play(-1)
#            
            
            score ['gameScore']= 0
            
            hurdle_1 = hurdle.HurdleManager(390,(40, 80))
            hurdle_2 = hurdle.HurdleManager(445,(40, 80))
            hurdle_3 = hurdle.HurdleManager(500, (40, 80))
            
            rosa = player.Player(20, 1, 10)
            
            Ground = ground.Ground()
            
            
            STATE = GAME
            begin.change_to_game = False
            
           
      
        
    elif STATE == GAME:
        
        
        
        speed = 8
        
        
        if rosa.boost and boost_time < 200:
            
            if boost_time == 0:
                powerupfx.play()
                py.mixer.music.pause()
                superfx = py.mixer.Sound("src/music/super/battle4.wav")
                superfx.set_volume(0.5)
                superfx.play()
               
            boost_time += 1
            speed = 100
            
        elif boost_time == 200:
            
            py.mixer.stop()
            py.mixer.music.unpause()
            
            boost_time += 1
            
            
            
        else:
            
            
            boost_time = 0
            speed = 8
            rosa.boost = False
            
        
        
        if not rosa.dead:
            
            Ground.update(score['gameScore'] / 50 + speed)
            Ground.show(window)
           
            
            
            hurdle_1.update(True, score['gameScore'] / 50 + speed,window)
            hurdle_2.update(True, score['gameScore'] / 50 + speed,window)
            hurdle_3.update(True, score['gameScore'] / 50 + speed,window)
        
            if rosa.road == 1:
                rosa.update(hurdle_1)
            elif rosa.road == 2:
                rosa.update(hurdle_2)
            elif rosa.road == 3:
                rosa.update(hurdle_3)
                
            rosa.show(window)
            
            scoreStr = font2.render(str(round(score['gameScore'])), True, (255, 255, 255))
            window.blit(scoreStr, (50, 50))
            
            if rosa.boost:
                score['gameScore'] += 1
            else:
                score['gameScore'] += 0.1
                
            
        else:
            Ground.update(0)
            Ground.show(window)
            
            hurdle_1.update(False,0,window)
            hurdle_2.update(False,0,window)
            hurdle_3.update(False,0,window)
            
#            if rosa.explode_c == 0:
#                explodefx.play()
#                
#            
#            rosa.explode(window)

            game_over.show(50,round(score['gameScore']),window,font2)
            
            #STATE = game_over.update()
            
            if round(score['gameScore']) > highest:
               highest = round(score['gameScore'])
               f = open('highest.txt','w')
               f.write(str(highest))
               
            
            
            if not playdead:
                py.mixer.music.stop()
                print('=======================\\\\\\\\\\\\\\\\\\\\\\\\\ll')
                deadfx.play()
                playdead = True
                
          
        
        
        highestMessage = font3.render('HI:'+ str(highest), True, (255, 255, 255))
        window.blit(highestMessage,(1000,30))
       
            
    elif STATE == RESTART:
        
         playdead = False
         
         py.mixer.stop()
            
         gamefx = py.mixer.music.load("src/music/bgm_game/bgm_game.wav")
         py.mixer.music.set_volume(0.2)
         py.mixer.music.play(-1)
         
         score ['gameScore'] = 0
         
         hurdle_1 = hurdle.HurdleManager(390,(40, 80))
         hurdle_2 = hurdle.HurdleManager(445,(40, 80))
         hurdle_3 = hurdle.HurdleManager(500, (40, 80))
         
         rosa = player.Player(20, 1, 10)
         
         STATE = GAME
         
            
        
    clock.tick(80)

       
        
    py.display.update()

