import pygame
import config
import math
import random

# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Tank
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard
tankAId = 1
tankBId = 1

class Tank(pygame.sprite.Sprite):
    tankAId = 1
    tankBId = 1
    speed = 7
    rotate_speed = 5
    bounce = 24
    gun_offset = -11
    imagesA = []
    imagesB = []
    imagesAActive = []
    imagesBActive = []
    images = []
    def __init__(self, type):
        containers = self.containersA
        self.images = self.imagesA
        self.angle = 0
        if(type == 'B'):
            self.angle = 18
            containers = self.containersB
            self.images = self.imagesB
        pygame.sprite.Sprite.__init__(self, containers)
        self.type = type
        self.rotateCount = 0

        self.image = self.images[self.angle]
        self.width = self.image.get_width()

        centerX = config.SCREENRECT.centerx
        y = random.randint(self.image.get_height(),config.WINDOWS_HEIGHT)
        x = 0
        if(type == 'A'):
            x = random.randint(self.width/2,centerX - self.width/2)
        else:
            x = random.randint(centerX + self.width/2, config.WINDOWS_WIDTH - self.width/2)

        self.rect = self.image.get_rect(midbottom=(x,y))
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1
        self.isDestroy = False
        self.active = False
        if(self.type == 'A'):
            self.id = Tank.tankAId
            Tank.tankAId+=1
        else:
            self.id = Tank.tankBId
            Tank.tankBId +=1

    def setActive(self,enable):
        if(self.active == enable):
            return
            
        self.active = enable
        if(enable):
            if(self.type == 'A'):
                self.images = self.imagesAActive
            else:
                self.images = self.imagesBActive
        else:
            if(self.type == 'A'):
                self.images = self.imagesA
            else:
                self.images = self.imagesB

        self.image = self.images[self.angle]
        newcenter = self.rect.center
        self.rect = self.image.get_rect(center=newcenter)

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
            x,y = self.calculateHeadDelta(Tank.speed)
            self.rotateCount = 0
            self.rect.move_ip(x,y)
        elif(direction == 'back'):
            x,y = self.calculateHeadDelta(Tank.speed)
            self.rect.move_ip(-x,-y)
            self.rotateCount = 0
        elif (direction =='right'):
            self.rotateCount +=1
            if(self.rotateCount > self.rotate_speed):
                self.rotateCount = 0
                self.angle -= 1
                if(self.angle < 0):
                    self.angle += 36
                self.image = self.images[self.angle]
                newcenter = self.rect.center
                self.rect = self.image.get_rect(center=newcenter)
        elif (direction == 'left'):
            self.rotateCount +=1
            if(self.rotateCount > self.rotate_speed):
                self.rotateCount = 0
                self.angle += 1
                if(self.angle >= 36):
                    self.angle -= 36
                self.image = self.images[self.angle]
                newcenter = self.rect.center
                self.rect = self.image.get_rect(center=newcenter)
        self.rect = self.rect.clamp(config.SCREENRECT)  

    #Get the initialize position of the shot
    def gunpos(self):
        pos = self.rect.center
        x,y = self.calculateHeadDelta(self.width/2)
        return (pos[0] + x, pos[1] + y, self.angle)

    def destroy(self):
        self.isDestroy = True
        self.rect.move_ip(-1000,-1000)