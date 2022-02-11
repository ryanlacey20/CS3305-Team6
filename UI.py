import pygame

class UI():

    def __init__(self, game):
        self.game = game
        self.drawFps()

    def drawFps(self):
        self.fpsFont = pygame.font.Font('img/OpenSans.ttf', 20)
        self.fpsText = self.fpsFont.render("60 FPS", True, (255, 255, 255))
        self.fpsTextRect = self.fpsText.get_rect()
        self.fpsTextRect.center = (self.game.width - 40, 20)

    def draw(self):
        self.game.screen.blit(self.fpsText, self.fpsTextRect)