#rain

import pygame

from pygame.sprite import Sprite

class Rain(Sprite):
    def __init__(self, rd_game):
        super().__init__()
        self.screen = rd_game.screen
        
        self.settings = rd_game.settings

        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y 

    