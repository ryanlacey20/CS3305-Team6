import pygame

'''
'''
class Menu():
    def __init__(self, game):
        self.game = game
        self.middle = [self.game.width / 2, self.game.height /2]
        self.run_menu = True
        self.cursor = pygame.Rect(0, 0, 15, 15)
        self.start_key = False
        #self.back_key = False
        self.up_key = False
        self.down_key = False

        self.playing = True

    '''
    '''
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font('fonts/Oswald.ttf', size)
        t = font.render(text, True, (255, 255, 255))
        t_rect = t.get_rect()
        t_rect.center = (x, y)
        self.game.display.blit(t, t_rect)

    def draw_cursor(self):
        self.draw_text('>', 25, self.cursor.x, self.cursor.y)

    def key_down_check(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # exit game
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.start_key = True

    def reset(self):
        self.game.screen.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.start_key, self.up_key, self.down_key = False, False, False

    def move_cursor(self):
        # when I add more options, check for down/up key action
        return

'''
'''
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Start'
        self.start = [self.middle[0], self.middle[1]]
        self.cursor.midtop = (self.start[0] - 50, self.start[1])

    '''
    '''
    def display(self):
        self.run_menu = True
        while self.run_menu:
            self.key_down_check()
            self.check_input()
            pygame.Surface((self.game.width, self.game.height)).fill((0, 0, 0))
            self.draw_text('Space Hoppers', 20, self.middle[0], self.middle[1] - 80)
            self.draw_text('Start Game', 15, self.start[0], self.start[1])
            self.draw_cursor()
            self.reset()

    def check_input(self):
        self.move_cursor()
        if self.start_key:
            if self.state == 'Start':
                self.playing = True
            self.run_menu = False

class LoadMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

# instruction /tutorial menu

# Settings menu