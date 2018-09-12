import pygame


class Score:
	score = 0
	miss = 0

	def __init__(self, gameDisplay, x,y):
		self.gameDisplay = gameDisplay
		self.x = x
		self.y = y
		self.titleScore = "Score: "
		self.titleMiss = "Miss: "
		self.colorText = (128, 0, 0)
		self.font = pygame.font.SysFont("helvetica", 30)

	def increaseScore(self):
		self.score += 1

	def decreaseMiss(self):
		self.miss += 1

	def getScore(self):
		return self.score

	def getMiss(self):
		return self.miss

	def draw(self):
		textScore = self.font.render(self.titleScore + str(self.score), True, self.colorText)
		textMiss = self.font.render(self.titleMiss + str(self.miss), True, self.colorText)
		self.gameDisplay.blit(textScore, (self.x, self.y ))
		self.gameDisplay.blit(textMiss, (self.x, self.y+ 20))
