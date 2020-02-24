import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    
    #Start the game
    pygame.init()

    # Initialize settings
    ai_settings = Settings()
    
    # Set screen size
    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_length))
        
    # Set name of the game
    pygame.display.set_caption("Alien Invasion")

    # Create a ship
    ship = Ship(ai_settings, screen)
    
    #Game Loop
    while True:
        
        # Monitor keyboard and mouse event
        gf.check_events(ship)
        
        # Update ship
        ship.update()
        
        # Redraw the screen in every loop
        gf.update_screen(ai_settings, screen, ship)
        


run_game()
