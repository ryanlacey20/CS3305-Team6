import pygame

img = pygame.image.load('img/Heart.png')
img = pygame.transform.scale(img, (50, 50))

class lives():
    def __init__(self, game):
        self.game = game
        self.lives = 5
    def livesCount(self):
        return int(self.lives)
    def drawLives(self):
        i = 1
        while i <= self.lives:
            self.game.screen.blit(img,(i * 50, 0))
            i += 1

    def lose_life(self):
        if self.lives > 0:
            self.lives = self.lives -1
        return

    def gain_life(self):
        self.lives = self.lives + 1
        return
