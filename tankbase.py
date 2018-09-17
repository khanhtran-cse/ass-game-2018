
from const import *

class BaseTank:

	blood = TANK_BLOOD
	speed = TANK_SPEED
	isDead = False
	isVisible = False

	def __init__(self, pos):
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

	def perception(self):
		pass