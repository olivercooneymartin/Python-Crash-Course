# This file contains the Rocket class used by the Rocket Game.

import pygame


class Rocket:
    """A class that represents the player's rocket."""

    def __init__(self, r_game):
        """Initialize the rocket and set its starting position."""

        # Store the screen and settings.
        self.screen = r_game.screen
        self.settings = r_game.settings
        self.screen_rect = r_game.screen.get_rect()

        # Load the rocket image and get its rectangle.
        self.image = pygame.image.load("images/rocket.bmp")
        self.rect = self.image.get_rect()

        # Start the rocket in the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store the rocket's exact position as floats.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the rocket's position based on movement flags."""

        # Move right if the rocket is not at the right edge.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed

        # Move left if the rocket is not at the left edge.
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed

        # Move up if the rocket is not at the top edge.
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Move down if the rocket is not at the bottom edge.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed

        # Update the rocket's rectangle position.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the rocket at its current position."""
        self.screen.blit(self.image, self.rect)
