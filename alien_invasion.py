import pygame
import game_functions
from settings import Settings
from ship import Ship

def run_game():
    """Start the game, and create a object to the screen."""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(screen)
    while True:
        game_functions.check_events(ship)
        ship.update()
        game_functions.update_screen(ai_settings, screen, ship)

                
run_game()