import pygame
import math
import config

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
        if self.rect.top <= 0 or self.rect.left <= 0 or \
         self.rect.right >= config.SCREENRECT.right or \
         self.rect.bottom >= config.SCREENRECT.bottom:
            self.kill()
