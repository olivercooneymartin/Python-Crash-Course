# This program creates a simple Rocket Game where the player can move a rocket.

import sys

import pygame

from rocket_settings import Settings
from rocket import Rocket


class RocketGame:
    """A class to manage the Rocket Game."""

    def __init__(self):
        """Initialize the game and create the rocket."""
        pygame.init()

        # Set up the clock and game settings.
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create the game screen.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Rocket Game")

        # Create the player's rocket.
        self.rocket = Rocket(self)

    def run_game(self):
        """Start the main game loop."""
        while True:
            self.check_events()
            self.rocket.update()
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False

        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip()


if __name__ == "__main__":
    rg = RocketGame()
    rg.run_game()
