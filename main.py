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
candy_level = readLevel("levels/candy.json")
completed = readLevel("levels/completion.json")

levels = [space_level, jungle_level, cave_level, candy_level, completed]

level = 0

enemy_group = pygame.sprite.Group()
finish_flag = pygame.sprite.Group()
text = levels[level]["text"]

game = Game(levels[level]["Title"], 1000, 600, levels[level]["ID"])
lives = lives(game)
world = World(game, levels[level], enemy_group, finish_flag)
player = Player(game, world, levels[level], 100, game.height - 150, lives)
ui = UI(game)

menu = Menu(game)

run = True
clock = pygame.time.Clock()

while run:
    level_reset = False
    game_reset = False
    while game.running:
        game.current_menu.display()
        if game.current_menu.playing:
            game.running = False
        # if exit selected exit run loop
        if not game.current_menu.run:
            run = False

    clock.tick(game.fps)

    world.draw()

    lives.drawLives()
    if player.lives.livesCount() == 0:
        game_reset = True
        for i in range(5):
            player.lives.gain_life()

    enemy_group.update()
    enemy_group.draw(game.screen)

    finish_flag.draw(game.screen)

    player.update()

    ui.draw()

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    if player.rect.y + player.height >= player.game.height - player.game.block_size:
        if pygame.time.get_ticks() - player.number > 1000:
            player.lives.lose_life()
            player.number = pygame.time.get_ticks()
            level_reset = True
    # When the camera gets passed 150,000 units then switch to the next level
    if pygame.sprite.spritecollide(player, finish_flag, False) or level_reset == True or game_reset == True:
        if game_reset == True:
            level = 0
        if level_reset == False and game_reset == False and level != len(levels)-2:
                level += 1
        elif level == len(levels)-2 and level_reset == False:
            level = len(levels)-1
        enemy_group.empty()
        finish_flag.empty()
        world = World(game, levels[level], enemy_group, finish_flag)
        player = Player(game, world, levels[level], 100, game.height - 200, lives)
        game.updateTitle(levels[level]["Title"])
        game.levelid = levels[level]["ID"]
