import pygame
import random
import time

pygame.init()

display_Height = 1000
display_Width = 700

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

pygame.mouse.set_visible(False)
gameDisplay = pygame.display.set_mode((display_Height,display_Width))
pygame.display.set_caption('Game1')
clock = pygame.time.Clock()

bua = pygame.image.load('bua.png')
face = pygame.image.load('face.png')


x = (display_Width * 0.3)
y = (display_Height * 0.3)

def Display(face_x,face_y):
    gameDisplay.blit(face,(face_x,face_y))


crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    if event.type == pygame.mouse.get_pos():
        print(event)

    gameDisplay.fill(white)
    pos = pygame.mouse.get_pos()
    gameDisplay.blit(bua, (pos[0], pos[1]))


    rand_x = random.randint(1, 800)
    rand_y = random.randint(1, 600)

    Display(rand_x,rand_y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
