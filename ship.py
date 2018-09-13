import pygame


class Ship():
    def __init__(self, ai_settings, screen):
        """initialize ship and it's location"""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """place ship at the bottom mid"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        """restore float in center Attribute"""
        self.center = float(self.rect.centerx)

        """moving marks"""
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """adjust ship's position based on moving marks"""
        # update self.center value
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        # update rect Object based on self.center
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx
