import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        # Initialize ship and set it's location
        self.screen = screen
        self.setting = ai_settings

        # Load the image and set the size to 50x50
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        
        # Load the rectangular of the screen
        self.screen_rect = screen.get_rect()

        # Put every new ship on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.ship_centerx = float(self.rect.centerx)
        self.ship_bottom = float(self.rect.bottom)
        
        # Moving flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.ship_centerx += self.setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.ship_centerx -= self.setting.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.ship_bottom -= self.setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.ship_bottom += self.setting.ship_speed_factor
        
        '''
        We shouldn't use elif here because if we use elif, when the user
        press, say two keys at the same time, this function will perform
        only the first action, and that is not correct.
        '''
        
        self.rect.centerx = self.ship_centerx
        self.rect.bottom = self.ship_bottom
        
    def blitme(self):
        ''' Draw the ship at designated place'''
        print(self.rect)
        self.screen.blit(self.image, self.rect)
        
