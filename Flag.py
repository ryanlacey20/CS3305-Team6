import pygame
class Flag(pygame.sprite.Sprite):
	def __init__(self, world, x, y, texture):
		pygame.sprite.Sprite.__init__(self)
		self.world = world

		self.image = pygame.image.load(texture)

		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y + 3




