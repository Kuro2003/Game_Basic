import pygame
from pygame.sprite import Sprite
from settings import Settings
class Alien(Sprite):
    """ A class to represent a single alien in the feet """
    def __init__(self,ai_game):
        """ Initialize the alien and set its starting posotion. """
        super().__init__()
        self.screen = ai_game.screen
        # Load the alien image annd set its rect atribute. 
        self.image = pygame.image.load('alien_invasion\images\\aliens.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.settings = Settings()
    
    def check_edges(self):
        """ Return True if alien is at the adge of screen. """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """ Move the alien to the right or left """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x