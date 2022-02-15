import pygame

class Game():
	def __init__(self, title, width, height, levelid):
		pygame.init()
		pygame.mixer.init()

		self.width = width
		self.height = height
		self.block_size = 50

		self.levelid = levelid

		self.fps = 60

		self.screen = pygame.display.set_mode((width, height))

		self.updateTitle(title)



	def updateTitle(self, title):
		pygame.display.set_caption(title)

	def updateMusic(self, music):
		pygame.mixer.music.unload()
		pygame.mixer.music.load(music)
		pygame.mixer.music.play()
