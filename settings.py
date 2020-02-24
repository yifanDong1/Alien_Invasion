class Settings():
    '''Store settings of alien invasion'''

    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_length = 600
        self.bg_color = (0, 100 ,255)
        
        # Ship settings
        self.ship_speed_factor = 1.5
        
        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
