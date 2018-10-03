from const import *
from util import *

class Flag(pygame.sprite.Sprite):
	size_image = (25, 50)
	number_image = 7
	hp = FLAG_HP

	def __init__(self, pos, isEnemy):
		super().__init__()
		self.images = sprite_sheet(self.size_image, './images/flag_200x100.png')
		self.pos = pos
		self.isEnemy = isEnemy
		self.index = 0
		self.rect = (pos, self.size_image)

	def update(self):
		self.index += 1
		if self.index >= self.number_image:
			self.index = 0
		# print(self.index)
		self.image = self.images[self.isEnemy*7 + self.index]
