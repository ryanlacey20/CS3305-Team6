import pygame
number = pygame.time.get_ticks()
class Player():
	def __init__(self, game, world, level, x, y, lives):
		self.number = pygame.time.get_ticks()
		self.world = world
		self.game = game
		self.lives = lives

		self.orientation = "Right"
		self.anim_images = []
		self.width = 66
		self.height = 92

		self.index = 0
		self.counter = 0

		img = pygame.image.load(level["player_textures"][0])

		for texture in level["player_textures"]:
			aimg = pygame.image.load(texture)
			aimg = pygame.transform.scale(aimg, (self.width, self.height))
			self.anim_images.append(aimg)

		self.image = pygame.transform.scale(img, (self.width, self.height))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.vely = 0
		self.jumped = False
		self.jumpImage = pygame.image.load(level["player_jump_texture"])

		self.step_counter = 0

	def update(self):
		key = pygame.key.get_pressed()
		dx = 0
		dy = 0

		walk_cooldown = 1


		if key[pygame.K_SPACE] and self.jumped == False:
			self.jump(True)
		if key[pygame.K_LEFT]:
			dx -= 5
			self.counter += 1
			self.orientation = "Left"
		if key[pygame.K_RIGHT]:
			dx += 5
			self.counter += 1
			self.orientation = "Right"
		if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and self.jumped == False:
			# Stopped moving
			self.counter = 0
			self.index = 0
			self.image = self.anim_images[self.index]

		#animation
		if self.counter > walk_cooldown and self.jumped == False:
			self.counter = 0

			# Moving forward
			if dx > 0:
				self.index += 1
			else:
				# Moving backwards
				if self.index == 0:
					self.index = len(self.anim_images)
					self.index -= 1
				else:
					self.index -= 1
			if self.index >= len(self.anim_images):
				self.index = 0

			if self.orientation == "Right":
				self.image = self.anim_images[self.index]
			else:
				self.image = pygame.transform.flip(self.anim_images[self.index], True, False)

			self.step_counter += 1
			if self.jumped == False and self.step_counter > 6:
				pygame.mixer.Sound.play(self.world.footstep_sound)
				self.step_counter = 0

		#gravity
		# Is it the space level, if so drop the gravity
		if self.world.levelid == 1:
			self.vely += 0.5
		else:
			self.vely += 1

		if self.vely > 20:
			self.vely = 10
		dy += self.vely

		#collision
		for block in self.world.block_list:
			#x collision
			if block[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				dx = 0


			#y collision
			if block[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
				#Hit from under the block
				if self.vely < 0:
					dy = block[1].bottom - self.rect.top
					self.vely = 0
				elif self.vely >= 0:
					#Hes colliding with the floor => On the ground
					dy = block[1].top - self.rect.bottom
					self.jumped = False
					self.vely = 0

		for enemy in self.world.enemy_group:
			if enemy.dead:
				continue
			# Collided on the x axis, hurt him
			if enemy.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
				# Checks if a second has passed since the last time damage was taken
				if pygame.time.get_ticks() - self.number > 1000:
					if self.lives.livesCount() > 0:
						self.lives.lose_life()
						self.lives.drawLives()
						self.number = pygame.time.get_ticks()

			# Collided on the y axis, do damage to the enemy
			# Y axis is above the enemy
			# Y axis is only 20 pixels above the enemy
			# x axis is between the x of the enemy and less than the width of the enemy
			if (
					self.rect.y + self.rect.height < enemy.rect.y + enemy.rect.height and 
					self.rect.y + self.rect.height > enemy.rect.y - 20 and
					self.rect.x > enemy.rect.x + -50 and
					self.rect.x < (enemy.rect.x + enemy.rect.width)
				):
				enemy.die()
				self.jump()
					
		if self.rect.bottom > self.game.height:
			self.rect.bottom = self.game.height
			dy = 0

		#self.rect.x += dx
		self.rect.y += dy

		self.world.campos += dx

		self.game.screen.blit(self.image, self.rect)


	def jump(self, sound=False):
		self.vely = -15
		self.jumped = True

		if sound:
			pygame.mixer.Sound.play(self.world.jump_sound)

		if self.orientation == "Right":
			self.image = self.jumpImage
		else:
			self.image = pygame.transform.flip(self.jumpImage, True, False)
