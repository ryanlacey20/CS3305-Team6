import pygame
from menu import *

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

		self.running = True
		#self.playing

		self.display = pygame.Surface((self.width, self.height))

		self.main_menu = MainMenu(self)
		self.load_menu = LoadMenu(self)

		self.current_menu = self.main_menu



	def updateTitle(self, title):
		pygame.display.set_caption(title)

	def updateMusic(self, music):
		pygame.mixer.music.unload()
		pygame.mixer.music.load(music)
		pygame.mixer.music.play()
