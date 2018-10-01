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

    bullet = [
        pygame.image.load("./images/bullet-left.png"),
        pygame.image.load("./images/bullet-right.png"),
        pygame.image.load("./images/bullet-up.png"),
        pygame.image.load("./images/bullet-down.png")
    ]

    index_myTank = 1
    index_bullet = 1

    def __init__(self,gameDisplay,x,y,id_tank,id_group,speed_x,speed_y, x_bullet, y_bullet,speed_bullet_x,speed_bullet_y):
        self.gameDisplay = gameDisplay
        self.x = x
        self.y = y
        self.id_tank = id_tank
        self.id_group = id_group
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.x_bullet = x_bullet
        self.y_bullet = y_bullet
        self.speed_bullet_x = speed_bullet_x
        self.speed_bullet_y = speed_bullet_y

    def draw(self,positionImage):
        self.gameDisplay.blit(positionImage,(self.x,self.y))


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


    def shoot(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.index_myTank == 0:
                    self.index_bullet = 0
                    self.x_bullet = self.x
                    self.y_bullet = self.y
                    self.speed_bullet_x = -5
                    self.speed_bullet_y = 0

                elif self.index_myTank == 1:
                    self.index_bullet = 1
                    self.x_bullet = self.x
                    self.y_bullet = self.y
                    self.speed_bullet_x = 5
                    self.speed_bullet_y = 0

                elif self.index_myTank == 2:
                    self.index_bullet = 2
                    self.x_bullet = self.x
                    self.y_bullet = self.y
                    self.speed_bullet_x = 0
                    self.speed_bullet_y = -5

                elif self.index_myTank == 3:
                    self.index_bullet = 3
                    self.x_bullet = self.x
                    self.y_bullet = self.y
                    self.speed_bullet_x = 0
                    self.speed_bullet_y = 5

        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_SPACE:
        #         pass
        return [self.x_bullet,self.y_bullet,self.speed_bullet_x,self.speed_bullet_y]


    #Colision for tank
    def colision_Tank(self):
        pass

    #Cho nay cho con AI quyet dinh
    def Automove(self):
        pass




