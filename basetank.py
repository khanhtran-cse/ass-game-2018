
from const import *
from util import *
from bullet import Bullet
import random

class BaseTank(pygame.sprite.Sprite):

	speed = TANK_SPEED
	isVisible = False
	canShot = True
	size_image = (50,30)

	def __init__(self, position, angle, isAlly):
		pygame.sprite.Sprite.__init__(self)

		self.image_sprite = pygame.image.load('./images/tank-sprite-png-2.png')

		self.position = position
		self.isAlly = isAlly
		self.angle = angle
		if isAlly == True:
			self.tank1_image()
		else:
			self.tank2_image()
		self.hp = TANK_HP
		
		self.state = ('Nothing')

		self.timeToReload = pygame.time.get_ticks()
		self.timeToChangeAI = pygame.time.get_ticks()

	def tank1_image(self):
		self.original_image = self.image_sprite.subsurface((182,15,232 - 182,88-15))
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect(center = self.position)

	def tank2_image(self):
		self.original_image = self.image_sprite.subsurface((182,345,232 - 182,415-345))
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect(center = self.position)


	def updateIsVisible(self, isVisible):
		self.isVisible = isVisible

	def move(self, direction):
		if(direction == "head"):
			self.position = newPosition(self.position, self.angle +90 , self.speed)
		elif(direction == 'left'):
			self.angle += TANK_ANGLE_TO_ROTATE
			self.angle %=360
			# self.position = newPosition(self.position, self.angle, self.speed)
		elif(direction == 'right'):
			self.angle -= TANK_ANGLE_TO_ROTATE
			self.angle %=360
			# self.position = newPosition(self.position, self.angle, self.speed)
		elif(direction == 'back'):
			self.position = newPosition(self.position, self.angle + 90, -self.speed)
		x, y = self.position
		if x <= 0:
			x = 0
		elif x >= WINDOW_WIDTH:
			x = WINDOW_WIDTH
		if y <=0:
			y =0
		elif y >= WINDOW_HEIGHT:
			y = WINDOW_HEIGHT
		self.position = (x,y)
		# print(self.angle)
		# print(self.position)

	def shot(self):
		if self.canShot:
			self.canShot = False
			return Bullet(self.angle +90, newPosition(self.position, self.angle + 90, TANK_ALPHA_FOR_BULLET_FIRE))
		else:
			print("Need time to reload")
			return None

	def isShoted(self, hp):
		if hp < self.hp:
			self.hp -= hp
			# animation for shoted
		else:
			# animation for destroyed
			self.kill()

	def perception(self, teamEnemy, flagEnemy, flagAlly, attack_per):
		res = []
		mi = 100000000
		for i in teamEnemy:
			res.append(distance_eulic(self.position, i.position) )
			if(res[-1] < mi):
				temp = i
		res.append(distance_eulic(self.position, flagEnemy.position))
		if (res[-1]<mi):
			temp = flagEnemy
		tmp = min(res)
		if tmp <= BULLET_MAX_DISTANCE**2:
			return ('findEnemy', temp)
		elif flagAlly.hp <= FLAG_HP_WARNING:
			return ('inDefend', flagAlly)
		elif flagEnemy.hp <= FLAG_HP_WARNING:
			return('inAttack', flagEnemy)
		elif random.random() <= attack_per:
			return('inAttack', flagEnemy)
		else:
			return('inDefend', flagEnemy)


	def moveAt(self,target):
		angle = pygame.math.Vector2(target.position[0]- self.position[0], target.position[1]- self.position[1]).angle_to((1,0))
		# print(abs(angle), self.angle +90)
		if( abs(abs(angle)-(self.angle+90)) < ANGLE_PERCENT) :
			self.move('head')
		else:
			self.move('left')
		pass

	def AI(self, teamEnemy, bulletGroup, flagEnemy, flagAlly,attack_per):
		self.tmp = pygame.time.get_ticks()
		if self.tmp - self.timeToChangeAI  >= TIMER:
			# print('in')
			self.timeToReload = self.tmp
			self.state = self.perception(teamEnemy, flagEnemy, flagAlly,attack_per)
		if (self.state[0] == 'findEnemy'):
			# print(self.state[1])
			angle = pygame.math.Vector2(self.state[1].position[0]- self.position[0], self.state[1].position[1]- self.position[1]).angle_to((1,0))
			# print(abs(angle), self.angle +90)
			if( abs(abs(angle)-(self.angle+90)) < ANGLE_PERCENT) and self.canShot  :
				print('shot')
				bulletGroup.add(self.shot())
			else:
				self.move('back')

		elif (self.state[0] == 'inAttack'):
			self.moveAt(self.state[1])
		elif (self.state[0] == 'inDefend'):
			self.moveAt(self.state[1])
		else:
			print('stay')
		return self.state



	def update(self):
		self.tmp = pygame.time.get_ticks()
		if (self.tmp - self.timeToReload > TANK_TIME_RELOAD):
			self.timeToReload = self.tmp
			self.canShot = True
		self.image = pygame.transform.rotate(self.original_image, self.angle)
		self.rect = self.image.get_rect(center = self.position)
		# self.rect = (self.position, (232 - 182,415-345))