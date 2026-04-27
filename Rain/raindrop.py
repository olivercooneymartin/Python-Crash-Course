# This file contains the Raindrop class used by the Raindrops game.

import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    """A class that represents a single raindrop."""

    def __init__(self, rd_game):
        """Initialize the raindrop and set its starting position."""
        super().__init__()

        # Store the screen and settings.
        self.screen = rd_game.screen
        self.settings = rd_game.settings

        # Load the raindrop image and get its rectangle.
        self.image = pygame.image.load("images/raindrop.png")
        self.rect = self.image.get_rect()

        # Start each raindrop near the top-left area of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact vertical position as a float.
        self.y = float(self.rect.y)

    def check_disappeared(self):
        """Check if the raindrop has fallen below the screen."""
        if self.rect.top > self.screen.get_rect().bottom:
            return True
        else:
            return False

    def update(self):
        """Move the raindrop down the screen."""
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
