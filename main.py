from Game import *
from World import *
from Player import *
from UI import *
from Functions import *


space_level = readLevel("levels/space.json")
jungle_level = readLevel("levels/jungle.json")

levels = [space_level, jungle_level]

level = 0

game = Game(levels[level]["Title"], 1000, 600, levels[level]["ID"])
world = World(game, levels[level])
player = Player(game, world, 100, game.height - 150, levels[level]["player_textures"], levels[level]["player_jump_texture"])
ui = UI(game)

run = True
clock = pygame.time.Clock()
while run:

    clock.tick(game.fps)

    world.draw()

    player.update()


    ui.draw()

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    # When the camera gets passed 150,000 units then switch to the next level
    if(abs(world.camAbsolutePosition) > 150000):
        if level != len(levels) - 1:
            level += 1
            world = World(game, levels[level])
            player = Player(game, world, 100, game.height - 150, levels[level]["player_textures"], levels[level]["player_jump_texture"])
            game.updateTitle(levels[level]["Title"])
            game.levelid = levels[level]["ID"]