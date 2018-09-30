
from const import *

class BaseTank(pygame.sprite.Sprite):

	blood = TANK_BLOOD
	speed = TANK_SPEED
	isDead = False
	isVisible = False

	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([30,50])
		self.image.fill(COLOR_BLUE)
		self.rect = self.image.get_rect()

		self.pos = pos


	def updateBlood(self, blood):
		self.blood = blood

	def updateIsDead(self, isDead):
		self.isDead = isDead

	def updateIsVisible(self, isVisible):
		self.isVisible = isVisible

	def move(self, loc):
		pass

	def shot(self):
		pass

	def isShoted(self, ):
		pass

	def perception(self):
		pass

	def 