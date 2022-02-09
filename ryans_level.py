import pygame
from pip._vendor.progress.colors import black
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
fps = 60

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
        self.images_moving = []
        self.index = 0
        self.counter = 0
        for num in range(0, 10):
            img = pygame.image.load(f'images/player/p1_walk{num}.png')
            img = pygame.transform.scale(img, (66, 92))
            self.images_moving.append(img)
        self.img = self.images_moving[self.index]
        self.image = pygame.transform.scale(img, (66, 92))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_velocity = 0
        self.jumped = False

    def update(self):
        dx = 0
        dy = 0
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 5
        elif key[pygame.K_RIGHT]:
            dx += 5
        elif key[pygame.K_SPACE] and self.jumped == False:
            self.y_velocity = -15
            self.jumped = True
        elif key[pygame.K_SPACE]:
            self.jumped = False

        self.index += 1
        self.image = self.images_moving[self.index]
        if self.index >= len(self.images_moving):
            self.index = 0

        self.y_velocity += 1
        if self.y_velocity > 10:
            self.y_velocity = 10
        dy += self.y_velocity

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
player = Player(100, screen_height - 245)
level = Level(level_data)
run = True

while run == True:
    clock.tick(fps)
    screen.blit(background, (0, 0))
    level.draw()
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
