class Settings:
    # A class to store all settings for Alien Invasion.
    # Screen settings
    def __init__(self):
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,230)

        # Bullet setting
        self.bullet_speed = 1.5
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 15.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction = 1

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game """
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 15.0
        # fleet_direction of 1 represents right; -1 represent left
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50
    
    def increase_speed(self):
        """ Increase speed settings. """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
