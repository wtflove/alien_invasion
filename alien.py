import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        """initialize aliens, palece alien at position"""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # load bmp image and set up rect positions
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # set the alien at near left top conner
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # set position number of aliens to float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # def blitme(self):
    #     """blit alien at certain location"""
    #     self_left = self.rect.left
    #     print(self_left)

    def update(self):
        """move alien to the right"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x
        
        # print(self.rect.left)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if screen_rect.right <= self.rect.right:
            return True
        elif self.rect.left <= 0:
            return True
