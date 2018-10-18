import pygame
from util import *

class Health(pygame.sprite.Sprite):
    image =pygame.image.load('./data/health.png')
    width = 50
    def __init__(self, max,type):
        self.max = max
        self.type = type
        if(type == 1):
            self.color = (0,157,30,255)
        else:
            self.color = (243,16,54,255)

    def update(self,actor,current):
        x,y = actor.rect.midtop
        x -= 5
        width = self.width*current/self.max
        if(width<0):
            width = 0
        else:
            width = int(width)
        y = y - width/2
        img = pygame.transform.scale(self.image,(width,5))
        img.fill(self.color)
        self.screen.blit(img,(x,y ))