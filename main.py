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

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#game constants
MAX_SHOTS      = 2     #most player bullets onscreen
ALIEN_ODDS     = 22     #chances a new alien appears
ALIEN_RELOAD   = 12     #frames between new aliens
SCREENRECT     = config.SCREENRECT
SCORE          = 0
FPS = config.FPS

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
    Tank.images = Util.getTankImages()
    img = Util.load_image('explosion1.gif')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Shot.images = Util.getShotImages()

    #decorate the game window
    # icon = pygame.transform.scale(Alien.images[0], (32, 32))
    # pygame.display.set_icon(icon)
    pygame.display.set_caption('Pygame Aliens')
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
    player = Tank('A')
    player = Tank('A')
    player = Tank('A')
    player2 = Tank('B')
    player2 = Tank('B')
    player2 = Tank('B')
    player2 = Tank('B')
    # Alien() #note, this 'lives' because it goes into a sprite group
    if pygame.font:
        all.add(Score())

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
        if not player.reloading and firing and len(shotsA) < MAX_SHOTS:
            Shot(player.gunpos(),'A')
            shoot_sound.play()
        player.reloading = firing

        #Player 2 shot
        firing = keystate[K_SPACE] and not player2.isDestroy
        if not player2.reloading and firing and len(shotsB) < MAX_SHOTS:
            Shot(player2.gunpos(),'B')
            shoot_sound.play()
        player2.reloading = firing

        # # # Create new alien
        # if alienreload:
        #     alienreload = alienreload - 1
        # elif not int(random.random() * ALIEN_ODDS):
        #     Alien()
        #     alienreload = ALIEN_RELOAD

        # Drop bombs
        # if lastalien and not int(random.random() * BOMB_ODDS):
        #     Bomb(lastalien.sprite)

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

