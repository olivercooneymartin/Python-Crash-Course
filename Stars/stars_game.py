# This program creates a screen filled with randomly offset stars.

import sys
from random import randint

import pygame

from settings import Settings
from star import Star


class StarsGame:
    """A class to manage the Stars game."""

    def __init__(self):
        """Initialize the game and create the stars."""
        pygame.init()

        # Set up the clock and game settings.
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Create the game screen.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Stars")

        # Create a group to store all the stars.
        self.stars = pygame.sprite.Group()
        self.create_stars()

    def run_game(self):
        """Start the main game loop."""
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        """Respond to keyboard and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_q:
            sys.exit()

    def create_stars(self):
        """Create rows of stars across the screen."""
        star = Star(self)
        star_width, star_height = star.rect.size

        # Start placing stars away from the edges of the screen.
        current_x = 2 * star_width
        current_y = 2 * star_height

        # Keep creating rows until there is no more vertical space.
        while current_y < self.settings.screen_height - 3 * star_height:

            # Create one row of stars.
            while current_x < self.settings.screen_width - 2 * star_width:
                self.create_star(current_x, current_y)
                current_x += 2 * star_width

            # Move back to the left side and start the next row.
            current_x = 2 * star_width
            current_y += 2 * star_height

    def create_star(self, x_position, y_position):
        """Create one star and place it on the screen."""
        new_star = Star(self)

        # Add a small random offset so the stars look less uniform.
        new_star.rect.x = x_position + self.get_star_offset()
        new_star.rect.y = y_position + self.get_star_offset()

        self.stars.add(new_star)

    def get_star_offset(self):
        """Return a small random offset for a star's position."""
        offset_size = 15
        return randint(-offset_size, offset_size)

    def update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    sg = StarsGame()
    sg.run_game()
