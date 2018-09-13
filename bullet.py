import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    """the Class managing bullet"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at the ship"""
        super().__init__()
        self.screen = screen

        # create a a bullet at (0,0), then put it at the ship's position
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.midbottom = ship.rect.midtop

        # restore the position of the bullet in float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move bullet upward"""
        # update bullet speed in float
        self.y -= self.speed_factor
        # update bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
