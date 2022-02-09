import pygame
from pip._vendor.progress.colors import black
from pygame.locals import *

pygame.init()
screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Name TBD')

block_size = 50
background = pygame.image.load('images/jungle_background.jpeg')
grass = pygame.image.load('images/grass.jpeg')
door = pygame.image.load('images/door.png')
monster = pygame.image.load('images/tiger.png')
thorns = pygame.image.load('images/thorns.png')
background = pygame.transform.scale(background, (screen_width, screen_height))


class Level():
    def __init__(self, level_data):
        self.block_list = []
        row_count = 0
        for row in level_data:
            column = 0
            for bit in row:
                if bit == 1:
                    block_skin = pygame.transform.scale(grass, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)
                elif bit == 2:
                    block_skin = pygame.transform.scale(door, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)

                elif bit == 3:
                    block_skin = pygame.transform.scale(monster, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)

                elif bit == 4:
                    block_skin = pygame.transform.scale(thorns, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)
                column += 1
            row_count += 1

    def draw(self):
        for block in self.block_list:
            screen.blit(block[0], block[1])


class Player():
    def __init__(self, x, y):
        img = pygame.image.load('images/player/p1_walk0.png')
        self.image = pygame.transform.scale(img, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 5
        elif key[pygame.K_RIGHT]:
            dx += 5
        elif key[pygame.K_UP]:
            dy -= 5
        elif key[pygame.K_DOWN]:
            dy += 5
        self.rect.x += dx
        self.rect.y += dy

        screen.blit(self.image, self.rect)


level_data = [

    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

]
player = Player(100, 150)
level = Level(level_data)
run = True

while run == True:
    screen.blit(background, (0, 0))
    level.draw()
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
