import pygame
import config

from pygame.locals import *

class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if config.SCORE != self.lastscore:
            self.lastscore = config.SCORE
            msg = "Score: %d" % config.SCORE
            self.image = self.font.render(msg, 0, self.color)
