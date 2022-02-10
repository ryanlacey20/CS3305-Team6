import pygame
from time import sleep
import time

pygame.init()

width = 1000
height = 600

block_size = 50

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Level 1')

# Hide the first two blocks
campos = 100


def current_milli_time():
    return round(time.time() * 1000)


curTime = current_milli_time()


class World():
    def __init__(self, level_data, background, bit1_skin, bit2_skin, bit3_skin, bit4_skin, bit5_skin):
        self.block_list = []
        bit1 = pygame.image.load('%s' % bit1_skin)
        bit2 = pygame.image.load('%s' % bit2_skin)
        bit3 = pygame.image.load('%s' % bit3_skin)
        bit4 = pygame.image.load('%s' % bit4_skin)
        bit5 = pygame.image.load('%s' % bit5_skin)
        self.level_data = level_data
        self.bit1_skin = bit1
        self.bit2_skin = bit2
        self.bit3_skin = bit3
        self.bit4_skin = bit4
        self.bit5_skin = bit5
        self.background = pygame.image.load('%s' % background)

        row_count = 0
        for row in self.level_data:
            column = 0
            for bit in row:
                if bit == 1:
                    block_skin = pygame.transform.scale(self.bit1_skin, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)
                elif bit == 2:
                    block_skin = pygame.transform.scale(self.bit2_skin, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)
                elif bit == 3:
                    block_skin = pygame.transform.scale(self.bit3_skin, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)
                elif bit == 4:
                    block_skin = pygame.transform.scale(self.bit4_skin, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)
                elif bit == 5:
                    block_skin = pygame.transform.scale(self.bit5_skin, (block_size, block_size))
                    block_rect = block_skin.get_rect()
                    block_rect.x = column * block_size
                    block_rect.y = row_count * block_size
                    block = (block_skin, block_rect)
                    self.block_list.append(block)
                column += 1
            row_count += 1

    def draw(self):
        for block in self.block_list:
            b = block
            global campos
            b[1].x -= campos

            screen.blit(b[0], b[1])
        # pygame.draw.rect(screen, (255, 255, 255), block[1], 2)
        campos = 0


class Player():
    def __init__(self, x, y, world):
        self.orientation = "Right"
        self.anim_images = []
        self.width = 66
        self.height = 92
        self.world = world
        self.index = 0
        self.counter = 0

        img = pygame.image.load('img/player/p1_walk0.png')

        for i in range(0, 10):
            aimg = pygame.image.load(f'img/player/p1_walk{i}.png')
            aimg = pygame.transform.scale(aimg, (self.width, self.height))
            self.anim_images.append(aimg)

        self.image = pygame.transform.scale(img, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vely = 0
        self.jumped = False
        self.jumpImage = pygame.image.load('img/player/jump.png')

    def update(self):
        global campos
        key = pygame.key.get_pressed()
        dx = 0
        dy = 0

        walk_cooldown = 1

        if key[pygame.K_SPACE] and self.jumped == False:
            self.vely = -15
            self.jumped = True

            if self.orientation == "Right":
                self.image = self.jumpImage
            else:
                self.image = pygame.transform.flip(self.jumpImage, True, False)

        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.orientation = "Left"
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.orientation = "Right"
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and self.jumped == False:
            # Stopped moving
            self.counter = 0
            self.index = 0
            self.image = self.anim_images[self.index]

        # animation
        if self.counter > walk_cooldown and self.jumped == False:
            self.counter = 0

            # Moving forward
            if dx > 0:
                self.index += 1
            else:
                # Moving backwards
                if self.index == 0:
                    self.index = len(self.anim_images)
                    self.index -= 1
                else:
                    self.index -= 1
            if self.index >= len(self.anim_images):
                self.index = 0

            if self.orientation == "Right":
                self.image = self.anim_images[self.index]
            else:
                self.image = pygame.transform.flip(self.anim_images[self.index], True, False)

        # gravity
        self.vely += 1
        if self.vely > 10:
            self.vely = 10
        dy += self.vely

        # collision
        for block in self.world.block_list:
            # x collision
            if block[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            # y collision
            if block[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # Hit from under the block
                if self.vely < 0:
                    dy = block[1].bottom - self.rect.top
                    self.vely = 0
                elif self.vely >= 0:
                    # Hes colliding with the floor => On the ground
                    dy = block[1].top - self.rect.bottom
                    self.jumped = False
                    self.vely = 0

        if self.rect.bottom > height:
            self.rect.bottom = height
            dy = 0

        # self.rect.x += dx
        self.rect.y += dy

        campos += dx

        screen.blit(self.image, self.rect)


class UI():

    def __init__(self):
        self.fpsFont = pygame.font.Font('img/OpenSans.ttf', 20)
        self.fpsText = self.fpsFont.render("60 FPS", True, (255, 255, 255))
        self.fpsTextRect = self.fpsText.get_rect()
        self.fpsTextRect.center = (width - 40, 20)

    def draw(self):
        screen.blit(self.fpsText, self.fpsTextRect)


floor = [2 for i in range(1, 998)]
underFloor = [1 for i in range(1, 998)]
floor.insert(0, 1)
floor.insert(0, 1)
underFloor.insert(0, 1)
underFloor.insert(0, 1)


ui = UI()


def run(world):
    player = Player(100, height - 150, world)
    run = True
    while run:

        clock.tick(fps)

        screen.blit(world.background, (-300, 0))

        world.draw()

        player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        ui.draw()

        pygame.display.update()
    # print( round(1000 / (current_milli_time() - curTime) ))
    # curTime = current_milli_time()

    pygame.quit()
