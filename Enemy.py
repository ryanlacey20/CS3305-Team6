import pygame
class Enemy(pygame.sprite.Sprite):
	def __init__(self, world, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.world = world

		textures = world.enemy_textures
		self.enemy_death_texture = pygame.image.load(world.enemy_death_texture)
		self.image = pygame.image.load(textures[0])

		self.anim_images = []

		for texture in textures:
			aimg = pygame.image.load(texture)
			aimg = pygame.transform.scale(aimg, (aimg.get_rect().width, aimg.get_rect().height))
			self.anim_images.append(aimg)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0
		self.anim_counter = 0
		self.anim_index = 0
		self.dead = False
		# 120 frames, so fade away in 2 seconds
		self.death_counter = 120

	def update(self):

		for particle in self.world.enemy_particles:
			particle[0][0] -= particle[1][0]
			particle[0][1] -= particle[1][1]
			particle[2] -= 0.1
			pygame.draw.circle(self.world.game.screen, (223, 138, 244), particle[0], particle[2])

			if particle[2] <= 0:
				self.world.enemy_particles.remove(particle)

		if not self.dead:
			if self.move_direction == 1:
				self.rect.x += 1
			else:
				self.rect.x -= 1

			self.move_counter += 1
			if self.move_counter > 150:
				self.move_direction *= -1
				self.move_counter = 0

			# Animation
			self.anim_counter += 1
			if self.anim_counter > 20:
				if self.anim_index == len(self.anim_images) - 1:
					self.anim_index = 0
				else:
					self.anim_index += 1

				self.anim_counter = 0

			if self.move_direction == 1:
				self.image = pygame.transform.flip(self.anim_images[self.anim_index], True, False)
			else:
				self.image = self.anim_images[self.anim_index]

	def die(self):
		self.dead = True
		self.image = self.enemy_death_texture
		self.rect.y = self.rect.y + 17
		pygame.mixer.Sound.play(self.world.enemy_death_sound)

		self.world.enemy_particles.append([[self.rect.x, self.rect.y], [0, 0.5], 5])
		self.world.enemy_particles.append([[self.rect.x + 20, self.rect.y], [0, 1], 5])
		self.world.enemy_particles.append([[self.rect.x + 40, self.rect.y], [0, 0.5], 5])




