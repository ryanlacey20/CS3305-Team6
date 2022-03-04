import pygame
from Functions import *
from Enemy import *

class World():
	def __init__(self, game, level, enemy_group):
		self.game = game
		self.background = pygame.image.load(level["background"])
		self.enemy_textures = level["enemy_textures"]
		self.enemy_death_texture = level["enemy_death_texture"]
		self.enemy_death_sound = pygame.mixer.Sound(level["enemy_death_sound"])

		self.footstep_sound = pygame.mixer.Sound(level["footstep_sound"])

		self.levelid = level["ID"]

		self.text = level["text"]
		self.texts = []

		pygame.font.init()

		for text in self.text:
			self.font = pygame.font.Font('fonts/Oswald.ttf', text[1])
			t = self.font.render(text[0], True, (255, 255, 255))
			self.texts.append([ t, text[2], text[3] ])

		self.camAbsolutePosition = 100

		self.enemy_group = enemy_group

		self.campos = 100
		self.textures = []

		self.musicUpdater(level["music"])

		for texture in level["textures"]:
			self.textures.append(pygame.image.load(texture))

		self.block_list = []
		row_count = 0
		for row in level["data"]:
			column = 0
			for bit in row:
				if bit == 1:
					block_skin = pygame.transform.scale(self.textures[bit - 1], (game.block_size, game.block_size))
					block_rect = block_skin.get_rect()
					block_rect.x = column * game.block_size
					block_rect.y = row_count * game.block_size
					block = (block_skin, block_rect)
					self.block_list.append(block)
				elif bit == 2:
					block_skin = pygame.transform.scale(self.textures[bit - 1], (game.block_size, game.block_size))
					block_rect = block_skin.get_rect()
					block_rect.x = column * game.block_size
					block_rect.y = row_count * game.block_size
					block = (block_skin, block_rect)
					self.block_list.append(block)
				elif bit == 3:
					block_skin = pygame.transform.scale(self.textures[bit - 1], (game.block_size, game.block_size))
					block_rect = block_skin.get_rect()
					block_rect.x = column * game.block_size
					block_rect.y = row_count * game.block_size
					block = (block_skin, block_rect)
					self.block_list.append(block)
				elif bit == 4:
					block_skin = pygame.transform.scale(self.textures[bit - 1], (game.block_size, game.block_size))
					block_rect = block_skin.get_rect()
					block_rect.x = column * game.block_size
					block_rect.y = row_count * game.block_size
					block = (block_skin, block_rect)
					self.block_list.append(block)
				elif bit == 5:
					block_skin = pygame.transform.scale(self.textures[bit - 1], (game.block_size, game.block_size))
					block_rect = block_skin.get_rect()
					block_rect.x = column * game.block_size
					block_rect.y = row_count * game.block_size
					block = (block_skin, block_rect)
					self.block_list.append(block)
				elif bit == "E":
					enemy = Enemy(self, column * game.block_size, row_count * game.block_size + 22)
					enemy_group.add(enemy)
				elif bit == 6:
					block_skin = pygame.transform.scale(self.textures[bit - 1], (game.block_size, game.block_size))
					block_rect = block_skin.get_rect()
					block_rect.x = column * game.block_size
					block_rect.y = row_count * game.block_size
					block = (block_skin, block_rect)
					self.block_list.append(block)
				column += 1
			row_count += 1

	def draw(self):
		self.game.screen.blit(self.background, (-300, 0))

		for text in self.texts:
			text[1] -= self.campos
			self.game.screen.blit(text[0], (text[1], text[2]))

		for enemy in self.enemy_group:
			enemy.rect.x -= self.campos

		for block in self.block_list:
			b = block
			b[1].x -= self.campos
			self.camAbsolutePosition -= self.campos

			self.game.screen.blit(b[0], b[1])
			#pygame.draw.rect(screen, (255, 255, 255), block[1], 2)
		self.campos = 0

	def musicUpdater(self, music):
		pygame.mixer.music.unload()
		pygame.mixer.music.load(music)
		pygame.mixer.music.play(-1, 100000)
		pygame.mixer.music.set_volume(0.1)
