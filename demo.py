# import pygame
# import time
# from bullet import *
# from util import *

# pygame.init()

# screen = pygame.display.set_mode(WINDOW_SIZE)

# background = pygame.image.load('./data/background.jpg')
# background = pygame.transform.scale(background, WINDOW_SIZE)
# sprite_flag = sprite_sheet((25,50), './data/flag_200x100.png')

# clock = pygame.time.Clock()
# exit = False
# i =0
# while not exit:
#   for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#           exit = True
#   screen.blit(background, (0,0))

#   screen.blit(sprite_flag[i%7], (50, 100))
#   i +=1
#   pygame.display.flip()
#   clock.tick(4)

# pygame.quit()
# print(newPosition((1,1), 60, -5))

import sys, pygame
from pygame.locals import *

pygame.init()
SCREEN = pygame.display.set_mode((200, 200))
CLOCK  = pygame.time.Clock()

surface = pygame.Surface((50 , 50))
surface.fill((0, 0, 0))
rotated_surface = surface
rect = surface.get_rect()
print(rect)
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill((255, 255, 255))
    angle += 30
    angle %=360
    rotated_surface = pygame.transform.rotate(surface, angle)
    rect = rotated_surface.get_rect(center = (100, 100))
    print(rect)
    SCREEN.blit(rotated_surface, (rect.x, rect.y))

    pygame.display.update()
    CLOCK.tick(3)