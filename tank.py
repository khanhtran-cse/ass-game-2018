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
    index_myTank = 0
    def __init__(self,gameDisplay,x,y,id_tank,id_group):
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y
        self.id_tank = id_tank
        self.id_group = id_group

    def draw(self,positionImage):
        self.gameDisplay.blit(positionImage,(self.x,self.y))

    def shoot(self):
        print("Shoot")

    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                self.index_myTank = 2
                self.y += -10
            elif event.key == pygame.K_DOWN:
                print("DOWN")
                self.index_myTank = 3
                self.y += 10
            elif event.key == pygame.K_LEFT:
                print("LEFT")
                self.index_myTank = 0
                self.x += -10
            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                self.index_myTank = 1
                self.x += 10
            elif event.key == pygame.K_SPACE:
                self.shoot()
                bullet = Bullet(gameDisplay=self.gameDisplay,id_tank=self.id_tank,id_group=self.id_group,speed=10,x_start=self.x,y_start=self.y,x_end=0,y_end=0)
                # chua bat duoc su kien ve hinh
                bullet.motion(bullet.bullet[0])
                bullet.draw(bullet.bullet[0])



    #Cho nay cho con AI quyet dinh
    def Automove(self):
        pass




