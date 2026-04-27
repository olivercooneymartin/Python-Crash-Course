# This file contains the Bullet class used by the Rocket Game.

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class that represents a bullet fired by the rocket."""

    def __init__(self, rg_game):
        """Create a bullet at the rocket's current position."""
        super().__init__()

        # Store the screen, settings, and bullet color.
        self.screen = rg_game.screen
        self.settings = rg_game.settings
        self.color = self.settings.bullet_color

        # Create the bullet rectangle.
        self.rect = pygame.Rect(
            0, 0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )

        # Place the bullet at the top middle of the rocket.
        self.rect.midtop = rg_game.rocket.rect.midtop

        # Store the bullet's exact vertical position as a float.
        self.y = float(self.rect.y)
