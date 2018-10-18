from const import *
from util import *
from health import Health

class Flag(pygame.sprite.Sprite):
	size_image = (25, 50)
	number_image = 7
	hp = FLAG_HP
	lose = False

	def __init__(self, position, isEnemy):
		super().__init__()
		self.images = sprite_sheet(self.size_image, './data/flag_200x100.png')
		self.position = position
		self.isEnemy = isEnemy
		self.index = 0
		self.rect =  self.images[0].get_rect(center = self.position)
		if(isEnemy):
			self.health = Health(FLAG_HP,2)
		else:
			self.health = Health(FLAG_HP,1)

	def isShoted(self, hp):
		if hp < self.hp:
			self.hp -= hp
			# animation for shoted
		else:
			# animation for destroyed
			self.lose = True

	def update(self):
		self.index += 1
		if self.index >= self.number_image:
			self.index = 0
		# print(self.index)
		self.image = self.images[self.isEnemy*7 + self.index]
		self.health.update(self,self.hp)
