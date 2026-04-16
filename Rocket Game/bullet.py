#bullet module

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, rg_game):
        super().__init__()
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = rg_game.rocket.rect.midtop

        self.y = float(self.rect.y)