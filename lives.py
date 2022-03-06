import pygame

img = pygame.image.load('img/Heart.png')
img = pygame.transform.scale(img, (25, 25))

class lives():

    def __init__(self, game):
        self.game = game
        self.lives = 5
        self.ouch_sound = pygame.mixer.Sound("music/ouch.mp3")
    def livesCount(self):
        return int(self.lives)

    def drawLives(self):
        i = 1
        while i <= self.lives:
            self.game.screen.blit(img,(((i * 30) + 5) - 25, 10))
            i += 1

    def lose_life(self):
        if self.lives > 0:
            pygame.mixer.Sound.play(self.ouch_sound)
            self.lives = self.lives -1
        return

    def gain_life(self):
        self.lives = self.lives + 1
        return
