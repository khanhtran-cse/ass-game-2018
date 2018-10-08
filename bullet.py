from const import *
from util import *

class Bullet(pygame.sprite.Sprite):

	isStop = False
	speed = BULLET_SPEED
	timeCollionWithWall = BULLET_TIME_REFLECT_WALL

	def __init__(self, angle, position):
		"""type of buttle like laze, ... 
			vect: pygame.math.Vector2
		"""
		super().__init__()

		self.image_sprite = pygame.image.load('./images/bullet_x.jpg').convert_alpha()
		self.original_image = self.image_sprite.subsurface((427,253,468-427,372-253))
		self.original_image = pygame.transform.scale(self.original_image, (5,20))
		self.image = pygame.transform.rotate(self.original_image, angle) 
		self.original_position = position
		self.position = position
		self.rect = self.image.get_rect(center= self.position)
		self.angle = angle
		self.damage = BULLET_DAMAGE

		self.start_time = pygame.time.get_ticks()

	def checkCollisionWithWall(self):
		"""		width
			0---y--->
			|
			|x height
			|
		"""
		(current_x, current_y) = self.position
		if 0 < current_x < WINDOW_WIDTH  and 0 < current_y < WINDOW_HEIGHT:
			return False
		return True

	def update(self):
		self.updatePos()
		if self.checkCollisionWithWall(): 
			if self.timeCollionWithWall ==0 :
				self.kill()
			else:
				self.angle = (180-self.angle)*2+ self.angle
			self.timeCollionWithWall-=1
		# else self.checkCollisionWithTarget():
		# 	pass
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect(center= self.position)

	def updatePos(self):
		if distance_eulic(self.position, self.original_position) >= BULLET_MAX_DISTANCE**2:
			self.kill()
		tmp = pygame.time.get_ticks()
		self.position = newPosition(self.position, self.angle, (tmp - self.start_time)*self.speed)
		self.start_time = tmp

	def render():
		vectX = pygame.math.Vector2(1,0)
		angle = vectX.angle_to(self.vect)
		image = pygame.transform.rotate(self.image, angle)
		self.screen.blit(image, self.pos)

	def checkCollisionWithTarget(self, target):
		""" include collision with tank or enemy's home
		"""

		pass
