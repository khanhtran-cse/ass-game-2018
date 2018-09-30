import pygame
import random
import time

from bullet import *
from menu import *
from score import *
from main import *

class MyTank:

    # Image for rendering Jerry
    shape = [
            pygame.image.load('./images/my-tank-left.png'),
            pygame.image.load('./images/my-tank-right.png'),
            pygame.image.load('./images/my-tank-up.png'),
            pygame.image.load('./images/my-tank-down.png')
        ]
    def __init__(self,gamedisplay,x,y,id_tank,id_group):
        self.gamedisplay = gamedisplay
        self.x = x
        self.y = y
        self.id_tank = id_tank
        self.id_group = id_group

    def draw(self,positionImage):
        self.gamedisplay.blit(positionImage,(self.x,self.y))

    def shoot(self):
        print("Shoot")

    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                self.y += -10
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                self.y += 10
            elif event.key == pygame.K_LEFT:
                print("LEFT")
                self.x += -10
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                self.x += 10
            elif event.key == pygame.K_SPACE:
                self.shoot()


    #Cho nay cho con AI quyet dinh
    def Automove(self):
        pass




