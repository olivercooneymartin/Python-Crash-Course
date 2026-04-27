# This program creates rows of raindrops that fall down the screen.

import sys

import pygame

from settings import Settings
from raindrop import Raindrop


class RaindropsGame:
    """A class to manage the Raindrops game."""

    def __init__(self):
        """Initialize the game and create the raindrops."""
        pygame.init()

        # Set up the game settings.
        self.settings = Settings()

        # Create the game screen.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Raindrops")

        # Create a group to store all the raindrops.
        self.raindrops = pygame.sprite.Group()
        self._create_drops()

    def run_game(self):
        """Start the main game loop."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_drops(self):
        """Create the starting rows of raindrops."""
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size

        # Figure out how many raindrops fit in one row.
        available_space_x = self.settings.screen_width - drop_width
        self.number_drops_x = available_space_x // (2 * drop_width)

        # Figure out how many rows fit on the screen.
        available_space_y = self.settings.screen_height
        number_rows = available_space_y // (2 * drop_height)

        # Create each row of raindrops.
        for row_number in range(number_rows):
            self._create_row(row_number)

    def _create_row(self, row_number):
        """Create one row of raindrops."""
        for drop_number in range(self.number_drops_x):
            self._create_drop(drop_number, row_number)

    def _create_drop(self, drop_number, row_number):
        """Create one raindrop and place it in a row."""
        drop = Raindrop(self)
        drop_width, drop_height = drop.rect.size

        # Set the raindrop's position.
        drop.rect.x = drop_width + 2 * drop_width * drop_number
        drop.y = 2 * drop_height * row_number
        drop.rect.y = drop.y

        self.raindrops.add(drop)

    def _update_raindrops(self):
        """Update raindrops and replace rows that fall off the screen."""
        self.raindrops.update()

        make_new_drops = False

        # Remove drops that have disappeared below the screen.
        for drop in self.raindrops.copy():
            if drop.check_disappeared():
                self.raindrops.remove(drop)
                make_new_drops = True

        # Add a new row when old drops disappear.
        if make_new_drops:
            self._create_row(0)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    rd_game = RaindropsGame()
    rd_game.run_game()
