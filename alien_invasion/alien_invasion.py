from hashlib import new
from re import A
from ssl import AlertDescription
import sys
from matplotlib.style import available
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
# Overall class to manage game assets and behavior. 
    def __init__(self):

        # Initialize the game, and create game resources.
        pygame.init()
        pygame.display.set_caption("Alien Invasion")  
        self.settings = Settings() 
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        # set background color
        self.bg_color = (230,230,230)

        # Call ship
        self.ship = Ship(self)
        # Call bullets
        self.bullets = pygame.sprite.Group()
        # Call aliens
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
    # Start the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

            pygame.display.flip()
    def _check_events(self):
        # respond to keypress and mouse events.
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
        # Respond to keypress.
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left
            self.ship.moving_left = True
                
    def _check_keyup_events(self,event):
        # Rcespond to release.
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _update_screen(self):
        # update images on the screen, and flip to the new screen.
        # Redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()
    
    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """ Update position of bullets and get rid of old bullets. """
        # Update bullet positions.
        self.bullets.update()
        # Get rid of bullets that have disappear
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """ Create the fleet of aliens """
        # Create an alien and find the number of aliens in a row
        # Spacing berween each alien is equal to one alien width

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width) + 2

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows - 1):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number,row_number)
            
    def _create_alien(self,alien_number,row_number):
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x - 80

        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
        self.aliens.add(alien)
    
if __name__ == "__main__":
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai = ai.run_game()