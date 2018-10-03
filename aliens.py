#!/usr/bin/env python

import random, os.path
import math

#import basic pygame modules
import pygame
from pygame.locals import *

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")


#game constants
MAX_SHOTS      = 2     #most player bullets onscreen
ALIEN_ODDS     = 22     #chances a new alien appears
BOMB_ODDS      = 60    #chances a new bomb will drop
ALIEN_RELOAD   = 12     #frames between new aliens
SCREENRECT     = Rect(0, 0, 1000, 700)
SCORE          = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs


class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()



# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Player
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard


class Player(pygame.sprite.Sprite):
    speed = 7
    rotate_speed = 10
    bounce = 24
    gun_offset = -11
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.width = self.image.get_width()
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1
        self.angle = 0
        self.isDestroy = False

    def calculateHeadDelta(self,distance):
        x = 0
        y = 0
        alpha = self.angle/18*math.pi
        y = -1*distance* math.sin(alpha)
        x = distance*math.cos(alpha)
        return (x,y)        


    def move(self, direction):
        if(self.isDestroy):
            return
        # if direction: self.facing = direction
        if(direction == 'head'):
            # calculate new x, y
            x,y = self.calculateHeadDelta(Player.speed)
            self.rect.move_ip(x,y)
        elif(direction == 'back'):
            x,y = self.calculateHeadDelta(Player.speed)
            self.rect.move_ip(-x,-y)
        elif (direction =='right'):
            self.angle -= 1
            if(self.angle < 0):
                self.angle += 36
            self.image = self.images[self.angle]
            newcenter = self.rect.center
            self.rect = self.image.get_rect(center=newcenter)
        elif (direction == 'left'):
            self.angle += 1
            if(self.angle >= 36):
                self.angle -= 36
            self.image = self.images[self.angle]
            newcenter = self.rect.center
            self.rect = self.image.get_rect(center=newcenter)
        self.rect = self.rect.clamp(SCREENRECT)  

    def gunpos(self):
        pos = self.rect.center
        x,y = self.calculateHeadDelta(self.width/2)
        # if(self.angle >= 9 and self.angle < 27):
        #     pos = self.rect.midleft
        # else:
        #     pos = self.rect.midright
        # print(pos)
        # pos = self.facing*self.gun_offset + self.rect.centerx
        # print(pos,self.rect.top)
        return (pos[0] + x, pos[1] + y, self.angle)

    def destroy(self):
        self.isDestroy = True
        self.rect.move_ip(-1000,-1000)


class Alien(pygame.sprite.Sprite):
    speed = 13
    animcycle = 12
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1,1)) * Alien.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing;
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame//self.animcycle%3]


class Explosion(pygame.sprite.Sprite):
    defaultlife = 12
    animcycle = 3
    images = []
    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life//self.animcycle%2]
        if self.life <= 0: self.kill()


class Shot(pygame.sprite.Sprite):
    speed = 15
    images = []
    def __init__(self, pos, type):
        containers = Shot.containersA
        if(type == 'B'):
            containers = Shot.containersB
        pygame.sprite.Sprite.__init__(self, containers)
        self.image = self.images[pos[2]]
        self.angle = pos[2]
        self.rect = self.image.get_rect(midbottom=(pos[0],pos[1]))

    def calculateHeadDelta(self,distance):
        x = 0
        y = 0
        alpha = self.angle/18*math.pi
        y = -1*distance* math.sin(alpha)
        x = distance*math.cos(alpha)
        return (x,y) 

    def update(self):
        x,y = self.calculateHeadDelta(Shot.speed)
        self.rect.move_ip(x, y)
        if self.rect.top <= 0 or self.rect.left <= 0 or self.rect.right >= SCREENRECT.right or self.rect.bottom >= SCREENRECT.bottom:
            self.kill()


class Bomb(pygame.sprite.Sprite):
    speed = 9
    images = []
    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=
                    alien.rect.move(0,5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= SCREENRECT.bottom:
            Explosion(self)
            self.kill()


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)

def initTankImage():
    img = load_image('tank-0.png')
    i = 0
    imgs = []
    while(i<36):
        imgs.append(pygame.transform.rotate(img,i*10))
        i+=1
    Player.images = imgs

def initShotImage():
    img = load_image('shot.png')
    i = 0
    imgs = []
    while(i<36):
        imgs.append(pygame.transform.rotate(img,i*10))
        i+=1
    Shot.images = imgs

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
    # img = load_image('tank-move-up.png')
    initTankImage()
    img = load_image('explosion1.gif')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Alien.images = load_images('alien1.gif', 'alien2.gif', 'alien3.gif')
    Bomb.images = [load_image('bomb.gif')]
    initShotImage()
    # Shot.images = [load_image('shot.gif')]

    #decorate the game window
    icon = pygame.transform.scale(Alien.images[0], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Pygame Aliens')
    pygame.mouse.set_visible(0)

    #create the background, tile the bgd image
    bgdtile = load_image('background.png')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0,0))
    pygame.display.flip()

    #load the sound effects
    boom_sound = load_sound('boom.wav')
    shoot_sound = load_sound('car_door.wav')
    if pygame.mixer:
        music = os.path.join(main_dir, 'data', 'house_lo.wav')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    # Initialize Game Groups
    aliens = pygame.sprite.Group()
    shotsA = pygame.sprite.Group()
    shotsB = pygame.sprite.Group()

    bombs = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastalien = pygame.sprite.GroupSingle()

    #assign default groups to each sprite class
    Player.containers = all
    Alien.containers = aliens, all, lastalien
    Shot.containersA = shotsA, all
    Shot.containersB = shotsB, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    Score.containers = all

    #Create Some Starting Values
    global score
    alienreload = ALIEN_RELOAD
    kills = 0
    clock = pygame.time.Clock()

    #initialize our starting sprites
    global SCORE
    player = Player()
    player2 = Player()
    # Alien() #note, this 'lives' because it goes into a sprite group
    if pygame.font:
        all.add(Score())

    overgameTime = 2000/40
    while player.alive() and player2.alive():

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
        for shot in pygame.sprite.spritecollide(player, shotsB, 1):
            boom_sound.play()
            Explosion(player)
            Explosion(shot)
            SCORE = SCORE + 1
            player.destroy()

        for shot in pygame.sprite.spritecollide(player2, shotsA, 1):
            boom_sound.play()
            Explosion(player2)
            Explosion(shot)
            SCORE = SCORE + 1
            player2.destroy()

        # for alien in pygame.sprite.groupcollide(shots, aliens, 1, 1).keys():
        #     boom_sound.play()
        #     Explosion(alien)
        #     SCORE = SCORE + 1

        # for bomb in pygame.sprite.spritecollide(player, bombs, 1):
        #     boom_sound.play()
        #     Explosion(player)
        #     Explosion(bomb)
        #     player.destroy()

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
        clock.tick(40)

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()



#call the "main" function if running this script
if __name__ == '__main__': main()

