import pygame

class Score:
	SCORE_COLOR = (29, 155, 1)
	FAILURE_COLOR = (244, 66, 66)
	BACKGROUND = pygame.image.load('./images/score-background.png')
	score = 0
	miss = 0
	maxMiss = 10

	def __init__(self, gameDisplay, x,y):
		self.gameDisplay = gameDisplay
		self.x = x
		self.y = y
		self.titleScore = "Score: "
		self.titleMiss = "Blood: "
		self.font = pygame.font.SysFont("helvetica", 18)

	def increaseScore(self):
		self.score += 1

	def decreaseMiss(self):
		self.miss += 1

	def getScore(self):
		return self.score

	def getMiss(self):
		return self.miss

	def setMaxMiss(self, max):
		self.maxMiss = max;

	def resetScore(self):
		self.miss = 0
		self.score = 0

	def draw(self):
		textScore = self.font.render(self.titleScore + str(self.score), True, Score.SCORE_COLOR)
		textMiss = self.font.render(self.titleMiss + str(self.maxMiss- self.miss), True, Score.FAILURE_COLOR)
		self.gameDisplay.blit(Score.BACKGROUND,(self.x - 10, self.y - 5))
		self.gameDisplay.blit(textScore, (self.x, self.y ))
		self.gameDisplay.blit(textMiss, (self.x, self.y+ 18))
