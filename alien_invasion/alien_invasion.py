from hashlib import new
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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

    def run_game(self):
    # Start the main loop for the game
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that have disappear
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                
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
        pygame.display.flip()
    
    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullets group """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


    
if __name__ == "__main__":
    #Make a game instance, and run the game
    ai = AlienInvasion()
    ai = ai.run_game()