import pygame
import time
from bullet import *
from util import *

pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)

background = pygame.image.load('./images/background.jpg')
background = pygame.transform.scale(background, WINDOW_SIZE)
sprite_flag = sprite_sheet((25,50), './images/flag_200x100.png')

clock = pygame.time.Clock()
exit = False
i =0
while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
	screen.blit(background, (0,0))

	screen.blit(sprite_flag[i%7], (50, 100))
	i +=1
	pygame.display.flip()
	clock.tick(4)

pygame.quit()