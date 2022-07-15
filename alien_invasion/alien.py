import pygame
from pygame.sprite import Sprite
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