import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from buttom import Button
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    sw_settings = Settings()
    screen = pygame.display.set_mode((sw_settings.screen_width, sw_settings.screen_height))
    pygame.display.set_caption("Star Wars")
    play_button = Button(sw_settings, screen, "Play")

    ship = Ship(sw_settings, screen)
    bullets = Group()
    aliens = Group()
    stats = GameStats(sw_settings)
    sb = Scoreboard(sw_settings, screen, stats)

    gf.create_fleet(sw_settings, screen, ship, aliens)

    while True:
        gf.check_events(sw_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(sw_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(sw_settings, screen, stats, sb, ship, aliens, bullets)
        gf.update_screen(sw_settings, screen, stats, sb, ship, aliens, bullets, play_button)
        pygame.display.flip()


run_game()
