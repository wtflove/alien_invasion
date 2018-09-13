import pygame
import sys

from bullet import Bullet
from alien import Alien
from time import sleep

# def show_bulet_number(bullets):

#     print(len(bullets))


def check_keydown_events(event, ship, ai_settings, screen, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

        # space down to shot bullets
        elif event.key == pygame.K_SPACE:
            if ai_settings.bullet_allowed > len(bullets):
                fire_bullet(ai_settings, screen, ship, bullets)

        # adjust ship's speed
        elif event.key == pygame.K_UP and ai_settings.ship_speed_factor < 5:
            ai_settings.ship_speed_factor += 0.5
            print(ai_settings.ship_speed_factor)
        elif event.key == pygame.K_DOWN and ai_settings.ship_speed_factor > 0.5:
            ai_settings.ship_speed_factor -= 0.5
            print(ai_settings.ship_speed_factor)


def check_keyup_events(event, ship, ai_settings):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False


def check_events(ship, ai_settings, screen, bullets, play_button, stats, aliens):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship, ai_settings)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, stats, mouse_x,
                              mouse_y, bullets, aliens)


def check_play_button(play_button, stats, mouse_x, mouse_y, bullets, aliens):
    """clik button to reset game"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        # hide crusor
        pygame.mouse.set_visible(False)
        stats.game_active = True
        # reset game stats
        stats.reset_stats()
        bullets.empty()
        aliens.empty()


def update_screen(ai_settings, screen, ship, bullets, aliens, play_button, stats, score_board):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    score_board.show_score()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def update_bullets(bullets, aliens, stats, ai_settings, score_board):
    """update bullets' positions, and delete bullets out of the screen"""
    # update bullet
    bullets.update()

    # remove bullets
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    check_alien_bullet_collision(bullets, aliens, stats, ai_settings, score_board)


def fire_bullet(ai_settings, screen, ship, bullets):
    new_bullet = Bullet(ai_settings, screen, ship)
    bullets.add(new_bullet)


def get_alien_number_x(ai_settings, alien):
    alien_width = alien.rect.width
    avaliable_space_x = ai_settings.screen_width - (2 * alien_width)
    number_alien_x = int(avaliable_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(ai_settings, alien):
    number_alien_y = int(ai_settings.screen_height /
                         2 / (alien.rect.height * 2))
    return number_alien_y


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    new_alien = Alien(ai_settings, screen)
    new_alien.x = (1 + alien_number * 2) * new_alien.rect.width
    new_alien.rect.x = new_alien.x
    new_alien.y = (1 + row_number * 2) * new_alien.rect.height
    new_alien.rect.y = new_alien.y
    aliens.add(new_alien)


def create_fleet(ai_settings, screen, aliens):
    """create alien fleet"""
    alien = Alien(ai_settings, screen)
    # alien number each row
    number_alien_x = get_alien_number_x(ai_settings, alien)
    number_rows = get_number_rows(ai_settings, alien)

    # create alien for row 1
    for alien_number in range(number_alien_x):
        for row_number in range(number_rows):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings, screen, aliens, stats, bullets, ship):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    if len(aliens) == 0:
        create_fleet(ai_settings, screen, aliens)

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, bullets, aliens, ai_settings, screen, ship)
        # print(stats.ships_left)


def check_fleet_edges(ai_settings, aliens):
    """behave when the fleet reach the edges"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """
    make fleet dropped & direction changed
    """
    for alien in aliens.sprites():
        alien.y = alien.rect.y
        alien.rect.y = alien.y + ai_settings.alien_drop_speed
    ai_settings.fleet_direction *= -1


def check_alien_bullet_collision(bullets, aliens, stats, ai_settings, score_board):

    # check if any bullet hits an alien, remove alien if it does
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            score_board.pre_score()


def ship_hit(stats, bullets, aliens, ai_settings, screen, ship):

    # condition for game over
    if stats.ships_left > 0:
        stats.ships_left -= 1
        bullets.empty()
        aliens.empty()
        ship.center_ship()
        create_fleet(ai_settings, screen, aliens)
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(stats, bullets, aliens, ai_settings, screen, ship):
    """
    check if aliens at the bottom
    """
    screen_bottom = screen.screen_rect.bottom
    if aliens.rect.bottom >= screen_bottom:
        ship_hit(stats, bullets, aliens, ai_settings, screen, ship)
