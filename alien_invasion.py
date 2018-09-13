import pygame

from settings import Settings

from ship import Ship
from bullet import Bullet
from alien import Alien

import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from score_board import ScoreBoard


def run_game():

    # 初始化游戏，并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    stats = GameStats(ai_settings)
    play_button = Button(screen, ai_settings, 'PLAY')
    score_board = ScoreBoard(ai_settings, screen, stats)

    # a group for storing bullets
    bullets = Group()

    # a group for aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    # alien = Alien(ai_settings, screen)

    while True:
        gf.check_events(ship, ai_settings, screen, bullets, play_button, stats, aliens)

        # create PLAY button
        
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, screen, aliens, stats, bullets, ship)
            # aliens.update()
            gf.update_bullets(bullets, aliens, stats, ai_settings, score_board)

        gf.update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, score_board)


run_game()
