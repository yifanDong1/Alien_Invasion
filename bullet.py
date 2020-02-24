import pygame
from pygame.sprite import Sprite

class Bullet(sprite):
    '''Manage bullets'''
    
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen
        
        # Create a bullet at 0,0 in screen, then set the location correctly
        self.rect = pygame.rect(0, 0, ai_settings.bullet.width,
            ai_settings.bullet.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the y coordinate of the bullet
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y
        

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
