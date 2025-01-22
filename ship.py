import pygame

class Ship():
    """"""
    def __init__(self, screen):
        """Starts the aircraft, and define your initial position."""
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = None
        self.moving_left = None

    def update(self):
        """Update the ship position according to the moving_right flag."""
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1

    def blitme(self):
        """Draw the aircraft in your current position."""
        self.screen.blit(self.image, self.rect)