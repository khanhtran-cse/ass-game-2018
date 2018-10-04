#!/usr/bin/env python

import random, os.path
import math

#import basic pygame modules
import pygame
from pygame.locals import *

from Tank import Tank
from Shot import Shot
from Score import Score
from Explosion import Explosion

import Util
import config

import time

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#game constants
MAX_SHOTS      = 4     #most player bullets onscreen
ALIEN_ODDS     = 22     #chances a new alien appears
ALIEN_RELOAD   = 12     #frames between new aliens
SCREENRECT     = config.SCREENRECT
SCORE          = 0
FPS = config.FPS
LOCK_TIME = 0.5

def getSpriteByPosition(position,group):
    for index,spr in enumerate(group):
        if (index == position):
            return spr
    return False

def deactiveGroup(group):
    for index,spr in enumerate(group):
        spr.setActive(False)

def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    #Load images, assign to sprite classes
    #(do this before the classes are used, after screen setup)
    Tank.imagesA = Util.getTankImages('tank-A.png')
    Tank.imagesB = Util.getTankImages('tank-B.png')
    Tank.imagesAActive = Util.getTankImages('tank-A-active.png')
    Tank.imagesBActive = Util.getTankImages('tank-B-active.png')
    img = Util.load_image('explosion1.gif')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Shot.images = Util.getShotImages()

    #decorate the game window
    # icon = pygame.transform.scale(Alien.images[0], (32, 32))
    # pygame.display.set_icon(icon)
    pygame.display.set_caption('Tank Battle')
    pygame.mouse.set_visible(0)

    #create the background, tile the bgd image
    bgdtile = Util.load_image('background.png')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0,0))
    pygame.display.flip()

    #load the sound effects
    boom_sound = Util.load_sound('boom.wav')
    shoot_sound = Util.load_sound('car_door.wav')
    if pygame.mixer:
        music = os.path.join(Util.main_dir, 'data', 'house_lo.wav')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    # Initialize Game Groups
    shotsA = pygame.sprite.Group()
    shotsB = pygame.sprite.Group()

    tanksA = pygame.sprite.Group()
    tanksB = pygame.sprite.Group()

    all = pygame.sprite.RenderUpdates()
    # lastalien = pygame.sprite.GroupSingle()

    #assign default groups to each sprite class
    Tank.containersA = tanksA, all
    Tank.containersB = tanksB, all
    Shot.containersA = shotsA, all
    Shot.containersB = shotsB, all
    Explosion.containers = all
    Score.containers = all

    #Create Some Starting Values
    global score
    kills = 0
    clock = pygame.time.Clock()

    #initialize our starting sprites
    global SCORE
    player = Tank('A')
    # player.setActive(True)
    activeAIndex = 0

    Tank('A')
    Tank('A')
    Tank('A')
    
    player2 = Tank('B')
    player2.setActive(True)
    activeBIndex = 0

    Tank('B')
    Tank('B')
    Tank('B')
    # Alien() #note, this 'lives' because it goes into a sprite group
    if pygame.font:
        all.add(Score())


    activeALock = 0
    activeBLock = 0
    overgameTime = 1000/FPS
    while len(tanksA) > 0 and len(tanksB) > 0:

        #get input
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
        keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        #update all the sprites
        all.update()

        currentTime = time.time()
        if(keystate[K_PERIOD] and currentTime > activeALock):
            #change active of A
            activeALock = currentTime + LOCK_TIME

            activeAIndex += 1
            deactiveGroup(tanksA)
            if(activeAIndex >= len(tanksA)):
                activeAIndex = 0

            if(len(tanksA) > 0):
                player = getSpriteByPosition(activeAIndex,tanksA)
                player.setActive(True)
        
        if(keystate[K_b] and currentTime > activeBLock):
            activeBLock = currentTime + LOCK_TIME
            #change active of B
            activeBIndex += 1
            deactiveGroup(tanksB)
            if(activeBIndex >= len(tanksB)):
                activeBIndex = 0

            if(len(tanksB) > 0):
                player2 = getSpriteByPosition(activeBIndex,tanksB)
                player2.setActive(True)

        #handle player 1 input
        if(keystate[K_UP]):
            player.move('head')
        elif(keystate[K_DOWN]):
            player.move('back')
        elif(keystate[K_LEFT]):
            player.move('left')
        elif(keystate[K_RIGHT]):
            player.move('right')

        #handle player 2 input
        if(keystate[K_w]):
            player2.move('head')
        elif(keystate[K_s]):
            player2.move('back')
        elif(keystate[K_a]):
            player2.move('left')
        elif(keystate[K_d]):
            player2.move('right')
        # direction = keystate[K_RIGHT] - keystate[K_LEFT]
        # player.move(direction)
        firing = keystate[K_COMMA] and not player.isDestroy
        if(len(shotsA) < MAX_SHOTS):
            if(player.isAllowedGun()):
                Shot(player.gunpos(),'A')
                shoot_sound.play()

        #Player 2 shot
        firing = keystate[K_SPACE] and not player2.isDestroy
        if(len(shotsB) < MAX_SHOTS):
            if(player2.isAllowedGun()):
                Shot(player2.gunpos(),'B')
                shoot_sound.play()

        # # # Create new alien
        # if alienreload:
        #     alienreload = alienreload - 1
        # elif not int(random.random() * ALIEN_ODDS):
        #     Alien()
        #     alienreload = ALIEN_RELOAD

        # Drop bombs
        # if lastalien and not int(random.random() * BOMB_ODDS):
        #     Bomb(lastalien.sprite)

        for index,spr in enumerate(tanksA):
            spr.autoMove(tanksB)
            if(not spr.isActive() and len(shotsA) < MAX_SHOTS -1):
                if(spr.isAllowedGun()):
                    Shot(spr.gunpos(),'A')
                    shoot_sound.play()
                
        for index,spr in enumerate(tanksB):
            spr.autoMove(tanksA)
            if(not spr.isActive() and len(shotsB) < MAX_SHOTS -1):
                if(spr.isAllowedGun()):
                    Shot(spr.gunpos(),'B')
                    shoot_sound.play()

        # Detect collisions
        colA = pygame.sprite.groupcollide(tanksA, shotsB, True,True)
        for shot in colA:
            boom_sound.play()
            Explosion(shot)
            Explosion(colA[shot][0])
            SCORE = SCORE + 1
            shot.destroy()

        colB = pygame.sprite.groupcollide(tanksB, shotsA, True, True)
        for shot in colB:
            boom_sound.play()
            Explosion(shot)
            Explosion(colB[shot][0])
            SCORE = SCORE + 1
            shot.destroy()

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        if(player.isDestroy or player2.isDestroy):
            overgameTime-=1

        if(overgameTime < 0):
            if(player.isDestroy):
                player.kill()
            if(player2.isDestroy):
                player2.kill()
        #cap the framerate
        clock.tick(FPS)

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()



#call the "main" function if running this script
if __name__ == '__main__': main()

