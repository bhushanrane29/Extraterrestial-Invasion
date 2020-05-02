import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    # Initialize game and create a screen object.
    pygame.init()

    ai_settings = Settings()

    # Set the background color.
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Making a ship
    ship  = Ship(ai_settings,screen)

    #Making a bullet
    bullets = Group()

    # Make an alien group
    aliens = Group()

    # Creating fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Start the main loop for the game.
    while True:
        # Checkfor keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        # Update ship positions continuously
        ship.update()

        # Update bullet positions
        gf.update_bullets(bullets)

        # Update alien positions
        gf.update_aliens(ai_settings, aliens)

        # Redraw the screen during each while loop pass
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
