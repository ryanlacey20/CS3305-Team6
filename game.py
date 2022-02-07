import pygame
from time import sleep

pygame.init()

width = 1000
height = 600

block_size = 50

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Level 1')

background = pygame.image.load('img/bg.jpg')
concrete = pygame.image.load('img/concrete.png')

class World():
	def __init__(self):
		self.block_list = []
		row_count = 0
		for row in level_data:
			column = 0
			for bit in row:
				if bit == 1:
					block_skin = pygame.transform.scale(concrete, (block_size, block_size))
					block_rect = block_skin.get_rect()
					block_rect.x = column * block_size
					block_rect.y = row_count * block_size
					block = (block_skin, block_rect)
					self.block_list.append(block)
				elif bit == 2:
					pass
				column += 1
			row_count += 1

	def draw(self):
		for dirt in self.block_list:
			screen.blit(dirt[0], dirt[1])
			#pygame.draw.rect(screen, (255, 255, 255), dirt[1], 2)

class Player():
	def __init__(self, x, y):
		self.anim_images = []
		self.width = 66
		self.height = 92

		self.index = 0
		self.counter = 0

		img = pygame.image.load('img/player/p1_walk0.png')

		for i in range(0, 10):
			aimg = pygame.image.load(f'img/player/p1_walk{i}.png')
			aimg = pygame.transform.scale(aimg, (self.width, self.height))
			self.anim_images.append(aimg)

		self.image = pygame.transform.scale(img, (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.vely = 0
		self.jumped = False

	def update(self):
		key = pygame.key.get_pressed()
		dx = 0
		dy = 0

		walk_cooldown = 1

		if key[pygame.K_SPACE]:
			self.vely = -10
		if key[pygame.K_LEFT]:
			self.rect.x -= 5
			self.counter += 1
		if key[pygame.K_RIGHT]:
			self.rect.x += 5
			self.counter += 1
		if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
			self.counter = 0
			self.index = 0
			self.image = self.anim_images[self.index]

		self.vely += 1
		if self.vely > 10:
			self.vely = 10
		dy += self.vely

		for tile in world.block_list:
			if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				if self.vely < 0:
					dy = tile[1].bottom - self.rect.top
					self.vely = 0
				if self.vely >= 0:
					dy = tile[1].top - self.rect.bottom
					self.vely = 0

		#animation
		if self.counter > walk_cooldown:
			self.counter = 0
			self.index += 1
			if self.index >= len(self.anim_images):
				self.index = 0
			self.image = self.anim_images[self.index]

		if self.rect.bottom > height:
			self.rect.bottom = height
			dy = 0

		self.rect.y += dy

		screen.blit(self.image, self.rect)




level_data = [
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


world = World()
player = Player(0, height - 150)

run = True
while run:

	clock.tick(fps)

	screen.blit(background, (-300, 0))

	world.draw()

	player.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()


pygame.quit()