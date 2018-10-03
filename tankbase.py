
from const import *
from util import *

class BaseTank(pygame.sprite.Sprite):

	speed = TANK_SPEED
	isDestroy = False
	isVisible = False
	size_image = (50,30)

	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)

		self.image_sprite = pygame.image.load('./images/tank-sprite-png-2.png')

		self.pos = pos
		self.hp = TANK_HP

	def tank1_image(self):
		self.image = self.image_sprite.subsurface((182,15,232 - 182,88-15))
		self.rect = (self.pos, (232 - 182,88-15))

	def tank2_image(self):
		self.image = self.image_sprite.subsurface((182,345,232 - 182,415-345))
		self.rect = (self.pos, (232 - 182,415-345))


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
