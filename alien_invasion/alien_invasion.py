#!/usr/bin/env python3
#
# alien_invasion.py

import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
