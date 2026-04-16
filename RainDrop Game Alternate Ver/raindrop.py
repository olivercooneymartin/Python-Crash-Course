import pygame
from pygame.sprite import Sprite
 
class Raindrop(Sprite):
    """A class to represent a single raindrop."""

    def __init__(self, rd_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings

       
        self.image = pygame.image.load('images/rain.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
