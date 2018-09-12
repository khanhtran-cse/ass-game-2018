import pygame


class Score:
	score = 0
	miss = 0

	def __init__(seft, gameDisplay, x,y):
		seft.gameDisplay = gameDisplay
		seft.x = x
		seft.y = y
		seft.titleScore = "Score: "
		seft.titleMiss = "Miss: "
		seft.colorText = (128, 0, 0)
		seft.font = pygame.font.SysFont("helvetica", 30)

	def increaseScore(seft):
		seft.score += 1

	def decreaseMiss(seft):
		seft.miss += 1

	def draw(seft):
		textScore = seft.font.render(seft.titleScore + str(seft.score), True, seft.colorText)
		textMiss = seft.font.render(seft.titleMiss + str(seft.miss), True, seft.colorText)
		seft.gameDisplay.blit(textScore, (seft.x, seft.y ))
		seft.gameDisplay.blit(textMiss, (seft.x, seft.y+ 20))
