# This file contains the Star class used to create star sprites.

import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    """A class that represents a single star."""

    def __init__(self, stars_game):
        """Initialize the star and set its starting position."""
        super().__init__()

        # Store the game screen.
        self.screen = stars_game.screen

        # Load the star image and get its rectangle.
        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()

        # Start each star near the top-left area of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
