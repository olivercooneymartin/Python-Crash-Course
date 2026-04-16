import pygame

import sys

from settings import Settings 

from rain import Rain 

class RaindropsGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rain")

        self.raindrops = pygame.sprite.Group()
        self.create_drops()

    def run_game(self):
        while True:
            self.check_events()
            self.rain.update()
            self.update_screen()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def create_drops(self):
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        
        available_space_x = self.settings.screen_width - drop_width
        number_drops_x = available_space_x // (2 * drop_width)

        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * drop_height)


        for row_number in range(number_rows):
            for drop_number in range(number_drops_x):
                self.create_drop(drop_number, row_number)

    def create_drop(self, drop_number, row_number):
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        drop.rect.x = drop_width + 2 * drop_width * drop_number
        drop.y = 2 * drop.rect.height * row_number
        drop.rect.y = drop.y
        self.raindrops.add(drop)


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()

if __name__ == '__main__':

    rd_game = RaindropsGame()
    rd_game.run_game()


