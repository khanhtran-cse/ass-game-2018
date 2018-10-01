
from const import *

class BaseTank(pygame.sprite.Sprite):

	speed = TANK_SPEED
	isDestroy = False
	isVisible = False
	size_image = (50,30)

	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)

		self.image = pygame.Surface(self.size_image)
		self.image.fill(COLOR_BLUE)
		self.rect = (pos, self.size_image)

		self.pos = pos
		self.hp = TANK_HP

	def updateIsDestroy(self):
		self.isDestroy = True

	def updateIsVisible(self, isVisible):
		self.isVisible = isVisible

	def move(self, loc):
		pass

	def shot(self):
		pass

	def isShoted(self, hp):
		if hp < self.hp:
			self.hp -= hp
			# animation for shoted
		else:
			self.isDestroy = True
			# animation for destroyed

	def perception(self):
		pass
