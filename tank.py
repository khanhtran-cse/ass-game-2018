import pygame
import config
import math

# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Tank
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard
class Tank(pygame.sprite.Sprite):
    speed = 7
    rotate_speed = 10
    bounce = 24
    gun_offset = -11
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.width = self.image.get_width()
        self.rect = self.image.get_rect(midbottom=config.SCREENRECT.midbottom)
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
            x,y = self.calculateHeadDelta(Tank.speed)
            self.rect.move_ip(x,y)
        elif(direction == 'back'):
            x,y = self.calculateHeadDelta(Tank.speed)
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
        self.rect = self.rect.clamp(config.SCREENRECT)  

    #Get the initialize position of the shot
    def gunpos(self):
        pos = self.rect.center
        x,y = self.calculateHeadDelta(self.width/2)
        return (pos[0] + x, pos[1] + y, self.angle)

    def destroy(self):
        self.isDestroy = True
        self.rect.move_ip(-1000,-1000)