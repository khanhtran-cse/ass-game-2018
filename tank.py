import pygame
import random
import time

from bullet import *
from menu import *
from score import *
from main import *

class MyTank():

    # Image for rendering Jerry
    shape = [
            pygame.image.load('./images/my-tank-left.png'),
            pygame.image.load('./images/my-tank-right.png'),
            pygame.image.load('./images/my-tank-up.png'),
            pygame.image.load('./images/my-tank-down.png')
        ]

    index_myTank = 1

    def __init__(self,gameDisplay,x,y,id_tank,id_group,speed_x,speed_y):
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y
        self.id_tank = id_tank
        self.id_group = id_group
        self.speed_x = speed_x
        self.speed_y = speed_y

    def draw(self,positionImage):
        self.gameDisplay.blit(positionImage,(self.x,self.y))

    def shoot(self):
        print("Shoot")

    def move(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("UP")
                self.index_myTank = 2
                self.speed_x = 0
                self.speed_y = -5

            elif event.key == pygame.K_DOWN:
                print("DOWN")
                self.index_myTank = 3
                self.speed_x = 0
                self.speed_y = 5

            elif event.key == pygame.K_LEFT:
                print("LEFT")
                self.index_myTank = 0
                self.speed_x = -5
                self.speed_y = 0

            elif event.key == pygame.K_RIGHT:
                print("RIGHT")
                self.index_myTank = 1
                self.speed_x = 5
                self.speed_y = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.speed_y = 0
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.speed_x = 0

        return [self.speed_x,self.speed_y]

    #Colision for tank
    def colision_Tank(self):
        pass

    #Cho nay cho con AI quyet dinh
    def Automove(self):
        pass




