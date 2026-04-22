import sys
from random import randint


import pygame



from settings import Settings
from star import Star

class StarsGame:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self.create_stars()

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()
            self.clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()

    def create_stars(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = 2*star_width, 2*star_height
        while current_y < (self.settings.screen_height - 3*star_height):
            while current_x < (self.settings.screen_width - 2*star_width):
                self.create_star(current_x, current_y)
                current_x += 2 * star_width
            
            current_x = 2 * star_width
            current_y += 2 * star_height
        
    def create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.rect.x = x_position + self.get_star_offset()
        new_star.rect.y = y_position + self.get_star_offset()
        self.stars.add(new_star)

    def get_star_offset(self):
        offset_size = 15
        return randint(-1 * offset_size, offset_size)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    sg = StarsGame()
    sg.run_game()







        
