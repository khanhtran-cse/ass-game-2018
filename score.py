import pygame

class Score:
	SCORE_COLOR = (29, 155, 1)
	FAILURE_COLOR = (244, 66, 66)
	BACKGROUND = pygame.image.load('./data/score-background.png')
	score = 0
	miss = 0

	def __init__(self, gameDisplay, x,y):
		self.gameDisplay = gameDisplay
		self.x = x
		self.y = y
		self.titleScore = "Score: "
		self.titleMiss = "Failure: "
		self.font = pygame.font.SysFont("helvetica", 30)

	def increaseScore(self):
		self.score += 1

	def decreaseMiss(self):
		self.miss += 1

	def getScore(self):
		return self.score

	def getMiss(self):
		return self.miss

	def resetScore(self):
		self.miss = 0
		self.score = 0

	def draw(self):
		textScore = self.font.render(self.titleScore + str(self.score), True, Score.SCORE_COLOR)
		textMiss = self.font.render(self.titleMiss + str(self.miss), True, Score.FAILURE_COLOR)
		self.gameDisplay.blit(Score.BACKGROUND,(self.x - 10, self.y - 5))
		self.gameDisplay.blit(textScore, (self.x, self.y ))
		self.gameDisplay.blit(textMiss, (self.x, self.y+ 20))