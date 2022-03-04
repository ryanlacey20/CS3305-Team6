from game import *
from World import *
from Player import *
from UI import *
from Functions import *
from menu import *
from lives import *


space_level = readLevel("levels/space.json")
jungle_level = readLevel("levels/jungle.json")
cave_level = readLevel("levels/cave.json")

levels = [space_level, jungle_level, cave_level]

level = 0

enemy_group = pygame.sprite.Group()
text = levels[level]["text"]

game = Game(levels[level]["Title"], 1000, 600, levels[level]["ID"])
lives = lives(game)
world = World(game, levels[level], levels[level]["music"], enemy_group, levels[level]["enemy_textures"], levels[level]["enemy_death_texture"], levels[level]["enemy_death_sound"], text)
player = Player(game, world, 100, game.height - 150, levels[level]["player_textures"], levels[level]["player_jump_texture"], lives)
ui = UI(game)

menu = Menu(game)

run = True
clock = pygame.time.Clock()
while run:

    while game.running:
        game.current_menu.display()
        game.running = False

    clock.tick(game.fps)

    world.draw()
    lives.drawLives()
    if player.lives.livesCount()==0:
        run = False
    enemy_group.update()
    enemy_group.draw(game.screen)

    player.update()

    ui.draw()

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    # When the camera gets passed 150,000 units then switch to the next level
    if(abs(world.camAbsolutePosition) > 350000):
        if level != len(levels) - 1:
            level += 1
            enemy_group.empty()
            world = World(game, levels[level], levels[level]["music"], enemy_group, levels[level]["enemy_textures"], levels[level]["enemy_death_texture"], levels[level]["enemy_death_sound"], levels[level]["text"])
            player = Player(game, world, 100, game.height - 150, levels[level]["player_textures"], levels[level]["player_jump_texture"], lives)
            game.updateTitle(levels[level]["Title"])
            game.levelid = levels[level]["ID"]